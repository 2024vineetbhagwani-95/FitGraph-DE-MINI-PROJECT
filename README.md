# FitGraph — Fitness Activity & Workout Network Analytics Platform

FitGraph is a Data Engineering + graph analytics project built from the supplied `health_fitness_dataset.csv` Kaggle archive.

## What is included
- **687,701 activity records**, **3,000 participants**, 10 activity types, dates from 2024-01-01 to 2024-12-25.
- Python/Pandas ETL: extraction, validation, cleaning, deduplication, feature engineering and analytics generation.
- PostgreSQL warehouse loader with raw/staging, activity fact, participant dimension, and daily aggregate tables.
- Apache Airflow DAG for orchestrating the ETL and warehouse load.
- FastAPI REST API serving the processed analytics and graph data.
- React + Vite dashboard with overview charts, participant similarity network, participant explorer, and pipeline monitor.
- NetworkX graph analysis: degree/betweenness centrality and community detection where installed.
- Docker Compose for local API, PostgreSQL and frontend.

## Important data note
The CSV contains activity/health measurements, not explicit follow/friend relationships. FitGraph therefore creates an **inferred fitness-similarity graph** from participant workout preferences and activity metrics. These edges are analytical estimates, not real social connections. Fitness and health fields are for coursework/demo analysis only, not medical advice. The dataset has many missing values in `health_condition`; these are treated as unknown rather than as a negative health condition.

## Quick start (dashboard demo)
Requirements: Python 3.10+ and Node.js 18+.

1. Unzip this project.
2. In terminal 1:
   ```bash
   cd backend
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload --port 8000
   ```
3. In terminal 2:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
4. Open the Vite URL shown in terminal (usually http://localhost:5173). API docs: http://localhost:8000/docs.

The dashboard uses precomputed outputs under `data/processed/` so it opens quickly. Re-run the ETL to regenerate those outputs from the raw CSV.

## Run the ETL locally
From the project root:
```bash
python -m pip install -r pipeline/requirements.txt
python -m pipeline.run_pipeline --input data/raw/health_fitness_dataset.csv --output data/processed
```
This validates and transforms the full CSV, regenerates analytics/graph outputs, and writes a quality report. If `DATABASE_URL` is set, it also loads the warehouse tables into PostgreSQL.

## PostgreSQL with Docker
```bash
docker compose up --build
```
- Frontend: http://localhost:5173
- API: http://localhost:8000
- PostgreSQL: localhost:5432 (database `fitgraph`, user `fitgraph`, password `fitgraph_dev`)

The API uses precomputed analytics JSON in this demo build; the ETL independently loads the warehouse tables. This separation makes the UI fast and makes the pipeline repeatable. For a production version, API reads can be switched to query materialized warehouse tables.

## Airflow
The DAG is `airflow/dags/fitgraph_etl_dag.py`. It runs extract/transform, graph analytics, then warehouse loading. Airflow is provided as an optional setup because it has higher memory requirements than the dashboard. See `airflow/README.md`.

## Core concepts to explain in a viva
- ETL/ELT, schema validation and data quality
- Incremental/idempotent loads and unique constraints
- Data warehouse star schema (fact + dimensions)
- Workflow orchestration, DAG dependencies, retries
- Graph nodes/edges, centrality, similarity and communities
- REST APIs and dashboard visualization
- Reproducible local environment with Docker

## Data-quality observations
- Source file has no fully duplicated rows and no missing critical fields among participant/date/activity/duration.
- `health_condition` is missing in a large portion of records; it is preserved as nullable/unknown.
- Validate units and interpretation before treating every field as clinically meaningful; this project does not provide medical recommendations.

## Premium UI and Fitness Trends refresh

The frontend has a restrained dark-navy/purple visual system, a welcome hero, cleaner cards and spacing. The former participant-similarity network page has been replaced with a dedicated Fitness Trends workspace: interactive monthly time-series charts (workout sessions, recorded calories, average duration, or active participants), 3/6/12-month range selection, area/line modes, weekday activity patterns, and category-volume comparisons. These visualizations use the processed monthly, weekday, and activity aggregates already served by the API.

### Run the refreshed UI

1. Start the FastAPI backend in one terminal from the project root:
   `cd backend` then `python -m venv .venv` (only if needed), activate it, `pip install -r requirements.txt`, and `uvicorn app.main:app --reload --port 8000`.
2. In a second terminal: `cd frontend`, `npm install`, then `npm run dev`.
3. Open the local URL printed by Vite (usually `http://localhost:5173`).

The dashboard continues to use the existing processed dataset and API; no analytics values or source records were intentionally changed as part of the visual refresh.
