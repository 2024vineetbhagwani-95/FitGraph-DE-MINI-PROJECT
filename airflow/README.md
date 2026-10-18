# Optional Airflow orchestration

The DAG is `dags/fitgraph_etl_dag.py`. It has three stages:
1. `extract_transform`: validates source records and creates cleaned activity records.
2. `graph_analytics`: creates participant profiles, similarity edges and centrality/community metrics.
3. `warehouse_load`: loads fact/dimension/aggregate tables into PostgreSQL.

For a real Airflow installation, configure `AIRFLOW_HOME` and install the requirements in `pipeline/requirements.txt` in the scheduler/worker environment. Set `FITGRAPH_ROOT` to the project root and `DATABASE_URL` to the PostgreSQL URL. The DAG intentionally runs on demand (`schedule=None`) so a large source file is not reprocessed unexpectedly.
