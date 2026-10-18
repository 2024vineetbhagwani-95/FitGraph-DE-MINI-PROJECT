# FitGraph — Fitness Activity & Workout Network Analytics

FitGraph is a **Data Engineering mini project** built using a Kaggle health and fitness dataset. It processes fitness activity records through an ETL pipeline and generates analytical insights using data transformation, PostgreSQL, graph analytics, and an interactive dashboard.

### Key Features

- **ETL Pipeline:** Extracts, validates, cleans, deduplicates, and transforms source data.
- **Data Quality Checks:** Detects missing critical values, invalid ranges, and duplicate records.
- **Fitness Analytics:** Analyzes workout frequency, duration, calories, activity types, and weekday/monthly trends.
- **Participant Profiles:** Summarizes participant activity and fitness-related metrics.
- **Graph Analytics:** Builds a participant similarity network using NetworkX.
- **Interactive Dashboard:** Displays fitness insights through a React and Vite web interface.
- **Workflow Orchestration:** Includes an Apache Airflow DAG for coordinating pipeline stages.
-
## Dataset

The project uses the Kaggle dataset included in `data/raw/health_fitness_dataset.csv`.

The bundled dataset contains approximately **687,701 activity records across 3,000 participants**, covering multiple activity types and fitness-related measurements.

The pipeline processes fields such as:

- Participant ID and date
- Age, gender, height, and weight
- Activity type, duration, and intensity
- Calories burned and average heart rate
- Sleep duration, stress, daily steps, and hydration
- BMI, resting heart rate, blood pressure, and fitness-related fields

Dataset statistics describe the bundled source file; they may differ if the dataset is replaced or updated.

## Technology Stack

| Component | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Graph Analytics | NetworkX |
| Backend API | FastAPI |
| Frontend | React, Vite, JavaScript |
| Database | PostgreSQL |
| Workflow Orchestration | Apache Airflow |
| Containerization | Docker, Docker Compose |


## System Architecture

```text
Kaggle Fitness Dataset (CSV)
            |
            v
     Extract & Validate
            |
            v
    Clean & Transform Data
            |
            v
      Feature Engineering
            |
            +---------------------+
            |                     |
            v                     v
    Fitness Analytics       Graph Analytics
            |                     |
            +----------+----------+
                       |
                       v
             Processed JSON / CSV
                       |
             +---------+---------+
             |                   |
             v                   v
       FastAPI Backend     PostgreSQL Warehouse
             |
             v
       React Dashboard

     Apache Airflow orchestrates
     pipeline stages (optional)
```

## Project Structure

```text
fgwork/
├── airflow/
│   └── dags/             # Airflow pipeline DAG
├── backend/
│   └── app/              # FastAPI application
├── data/
│   ├── raw/              # Kaggle source dataset
│   └── processed/        # Generated analytics outputs
├── frontend/             # React dashboard
├── pipeline/
│   ├── run_pipeline.py   # Main ETL pipeline
│   ├── transform.py      # Cleaning and transformation
│   ├── graph.py          # Similarity graph analytics
│   └── load_postgres.py  # Warehouse loading
├── sql/                  # Database schema documentation
├── .env.example
├── docker-compose.yml
└── README.md
```

## Installation and Setup

### Prerequisites

- Python 3.10 or later
- Node.js and npm
- Git
- PostgreSQL for warehouse loading
- Docker Desktop for containerized execution

### 1. Clone the Repository

```bash
git clone https://github.com/2024vineetbhagwani-95/FitGraph-DE-MINI-PROJECT.git
cd FitGraph-DE-MINI-PROJECT
```

### 2. Install Pipeline Dependencies

Run from the project root:

```powershell
python -m pip install -r pipeline/requirements.txt
```

### 3. Run the ETL Pipeline

```powershell
python -m pipeline.run_pipeline --input data/raw/health_fitness_dataset.csv --output data/processed --skip-postgres
```

This command reads the Kaggle CSV, validates and transforms records, generates participant profiles and graph analytics, and writes processed JSON/CSV outputs. The `--skip-postgres` flag skips database loading.

To load the data into PostgreSQL instead, configure the required `DATABASE_URL` connection string and run the pipeline without `--skip-postgres`.

### 4. Start the Backend

Open a terminal at the project root:

```powershell
cd backend
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API documentation is available at:

`http://localhost:8000/docs`

### 5. Start the Frontend

Open a second terminal at the project root:

```powershell
cd frontend
npm install
npm run dev
```

Open the local URL displayed by Vite, usually:

`http://localhost:5173`
```

Review `docker-compose.yml` and `.env.example` for the configured services and environment variables.



