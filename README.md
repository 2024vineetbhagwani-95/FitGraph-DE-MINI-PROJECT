# FitGraph — Fitness Activity & Workout Network Analytics

FitGraph is a data engineering and analytics project that processes fitness activity data to uncover workout trends, participant consistency, recovery patterns, and relationships between participants. It combines an ETL pipeline, data quality validation, a data warehouse, graph analytics, and an interactive web dashboard.

## Key Features

- **ETL Pipeline:** Extracts, validates, cleans, and transforms raw fitness data.
- **Fitness Trend Analysis:** Analyzes workout frequency, duration, activity levels, and monthly trends.
- **Consistency Analysis:** Groups participants according to their workout patterns.
- **Recovery Analysis:** Examines recovery-related patterns using available activity data.
- **Graph Analytics:** Represents participants as nodes and inferred activity-pattern relationships as edges.
- **Interactive Dashboard:** Presents fitness trends and analytics through a web interface.
- **Workflow Orchestration:** Includes Apache Airflow components for data pipeline orchestration.

## Technology Stack

| Component | Technologies |
|---|---|
| Frontend | React, Vite, JavaScript |
| Backend | Python, FastAPI |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Graph Analytics | NetworkX |
| Database | PostgreSQL |
| Data Engineering | ETL, data validation, data quality checks |
| Workflow Orchestration | Apache Airflow |
| Containerization | Docker, Docker Compose |
| Visualization | Interactive fitness analytics dashboard |

## Project Architecture

```text
Raw Fitness Activity Data
          |
          v
   Data Generation / Input
          |
          v
      ETL Pipeline
          |
          v
 Data Validation & Cleaning
          |
          v
 Feature Engineering & Aggregation
          |
          +--------------------+
          |                    |
          v                    v
   Fitness Analytics      Graph Analytics
          |                    |
          +---------+----------+
                    |
                    v
         Processed Analytics Data
                    |
                    v
             FastAPI Backend
                    |
                    v
           React Web Dashboard
```

## Project Structure

```text
fgwork/
├── airflow/          # Workflow orchestration
├── backend/          # FastAPI backend
├── data/             # Raw and processed datasets
├── frontend/         # React dashboard
├── pipeline/         # ETL and analytics scripts
├── sql/              # Database schema and SQL files
├── .env.example      # Example environment configuration
├── .gitignore
├── docker-compose.yml
└── README.md
```

## Getting Started

### Prerequisites

Install the following tools:

- Python 3.10 or later
- Node.js and npm
- Git
- PostgreSQL, if using the database integration
- Docker Desktop, if using the containerized setup

### 1. Clone the Repository

```bash
git clone https://github.com/2024vineetbhagwani-95/FitGraph-DE-MINI-PROJECT.git
cd FitGraph-DE-MINI-PROJECT
```

### 2. Set Up the Python Environment

Run these commands from the project root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r pipeline/requirements.txt
```

### 3. Prepare the Data and Run the Pipeline

Use the input dataset and pipeline commands provided by the project. For example, if the repository includes the synthetic data generator:

```powershell
python -m pipeline.generate_synthetic --output data/raw/synthetic_fitness_dataset.csv --participants 800 --year 2025 --seed 123
```

Then run the ETL pipeline:

```powershell
python -m pipeline.run_pipeline --input data/raw/synthetic_fitness_dataset.csv --output data/processed --skip-postgres
```

These example commands are intended for a version that includes `pipeline.generate_synthetic`. If your Kaggle version uses a different input filename or does not include this module, use the dataset and instructions specific to that version.

### 4. Start the Backend

Open a terminal at the project root:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

If the backend entry point or dependency file differs in your version, follow the actual files in the `backend` directory.

### 5. Start the Frontend

Open another terminal at the project root:

```powershell
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite in your browser.





---

**Developed as a Data Engineering mini project.**
