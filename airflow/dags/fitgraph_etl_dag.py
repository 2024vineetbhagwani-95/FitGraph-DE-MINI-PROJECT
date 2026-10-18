from datetime import datetime, timedelta
import os
from pathlib import Path
from airflow import DAG
from airflow.operators.python import PythonOperator

ROOT = Path(os.getenv("FITGRAPH_ROOT", "/opt/fitgraph"))
INPUT = ROOT / "data" / "raw" / "health_fitness_dataset.csv"
OUTPUT = ROOT / "data" / "processed"

def run_etl():
    import sys
    sys.path.insert(0, str(ROOT))
    from pipeline.transform import transform, build_profiles
    import pandas as pd, json
    OUTPUT.mkdir(parents=True, exist_ok=True)
    raw = pd.read_csv(INPUT)
    cleaned, quality = transform(raw)
    cleaned.to_parquet(OUTPUT / "cleaned_activities.parquet", index=False)
    (OUTPUT / "airflow_quality_report.json").write_text(json.dumps(quality, indent=2))

def run_graph():
    import sys
    sys.path.insert(0, str(ROOT))
    from pipeline.transform import build_profiles
    from pipeline.graph import build_similarity_graph
    import pandas as pd
    cleaned = pd.read_parquet(OUTPUT / "cleaned_activities.parquet")
    profiles = build_profiles(cleaned)
    edges, metrics, _ = build_similarity_graph(profiles)
    profiles.merge(metrics, on="participant_id", how="left").to_csv(OUTPUT / "airflow_participant_profiles.csv", index=False)
    edges.to_csv(OUTPUT / "airflow_graph_edges.csv", index=False)
    metrics.to_csv(OUTPUT / "airflow_graph_metrics.csv", index=False)

def run_load():
    import sys
    sys.path.insert(0, str(ROOT))
    from pipeline.load_postgres import load_warehouse
    from pipeline.transform import build_profiles
    from pipeline.graph import build_similarity_graph
    import pandas as pd
    cleaned = pd.read_parquet(OUTPUT / "cleaned_activities.parquet")
    profiles = build_profiles(cleaned)
    edges, metrics, _ = build_similarity_graph(profiles)
    load_warehouse(cleaned, profiles, metrics)

with DAG(
    dag_id="fitgraph_fitness_etl",
    description="ETL, fitness similarity graph analytics and PostgreSQL warehouse load",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    default_args={"owner":"fitgraph", "retries":1, "retry_delay":timedelta(minutes=2)},
    tags=["fitgraph", "etl", "graph-analytics"],
) as dag:
    extract_transform = PythonOperator(task_id="extract_transform", python_callable=run_etl)
    graph_analytics = PythonOperator(task_id="graph_analytics", python_callable=run_graph)
    warehouse_load = PythonOperator(task_id="warehouse_load", python_callable=run_load)
    extract_transform >> graph_analytics >> warehouse_load
