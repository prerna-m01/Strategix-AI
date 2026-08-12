# 🚀 Strategix AI

> **AI Executive Decision Intelligence Platform**
> **Case Study #1:** Global Marketing & Communications Enterprise
> *(Inspired by publicly available information about Publicis Groupe)*

🚧 **Project Status: Under Active Development**

Strategix AI is an enterprise-focused AI platform being developed to demonstrate how **Business Intelligence, Machine Learning, Retrieval-Augmented Generation (RAG), and Multi-Agent AI** can be combined to support executive-level business decision-making.

The platform is being built incrementally, beginning with a modular backend and enterprise business data layer before progressing toward analytics, machine learning, AI agents, RAG, dashboards, and deployment.

All business data used in the project is synthetic and intended for educational and portfolio purposes.

---

# 📌 Overview

Strategix AI aims to transform enterprise business data into actionable intelligence.

The long-term platform will allow executives to:

* Monitor business KPIs
* Analyze companies, employees, clients, projects, and campaigns
* Identify business risks
* Detect opportunities
* Forecast business performance
* Query organizational knowledge
* Receive AI-generated strategic recommendations
* Interact with specialized AI agents

The current implementation focuses on building the **enterprise backend foundation and business data architecture** required for these capabilities.

---

# 🎯 Problem Statement

Large organizations generate data across multiple business functions including:

* Finance
* Marketing
* Operations
* Human Resources
* Client Management
* Projects
* Campaigns

Traditional reporting systems primarily present information through dashboards and reports.

Executives still need to manually connect information across different business areas to understand:

* What is happening?
* Why is it happening?
* What risks exist?
* Where are opportunities?
* What should happen next?

Strategix AI is designed to eventually provide an intelligent layer over this business data.

---

# 💡 Vision

The long-term vision is to build an **Executive Decision Intelligence Platform** capable of combining structured enterprise data with AI reasoning.

The intended flow is:

```text
Enterprise Data
       │
       ▼
Data & Business Intelligence Layer
       │
       ▼
Analytics + Machine Learning
       │
       ▼
Knowledge Retrieval (RAG)
       │
       ▼
Specialized AI Agents
       │
       ▼
Executive Strategy Agent
       │
       ▼
Strategic Recommendations
```

The project is intentionally being developed in stages so that the AI layer is built on top of a reliable enterprise data and software architecture.

---

# 🏗️ Current Architecture

```text
                    Executive / API Client
                            │
                            ▼
                     FastAPI Application
                            │
                     API Router Layer
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
   Authentication      Business APIs       Health APIs
        │                   │
        │        ┌──────────┼──────────┐
        │        │          │          │
        ▼        ▼          ▼          ▼
      Users   Companies   Employees   Departments
                            │
                            ▼
                     Business Entities
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
           Clients       Projects      Campaigns
              │             │             │
              └─────────────┼─────────────┘
                            ▼
                     Service Layer
                            │
                            ▼
                    Repository Layer
                            │
                            ▼
                     SQLAlchemy ORM
                            │
                            ▼
                       PostgreSQL
                            │
                            ▼
                        Alembic
```

The future architecture will extend this foundation with:

```text
PostgreSQL
    │
    ├── Business Intelligence
    ├── Machine Learning
    ├── RAG Knowledge Base
    └── Multi-Agent AI
             │
             ▼
      Executive Intelligence
```

---

# ✨ Planned Capabilities

## Executive Intelligence

* Executive decision support
* Strategic recommendations
* Cross-functional analysis
* KPI monitoring
* Risk detection
* Opportunity identification
* Executive reporting

## Business Intelligence

* Revenue analytics
* Marketing analytics
* Client intelligence
* Project analytics
* Campaign performance
* Workforce analytics
* Department performance
* Financial analytics

## Artificial Intelligence

* Multi-Agent AI
* LangGraph workflows
* Retrieval-Augmented Generation
* Business knowledge retrieval
* AI reasoning
* Executive summarization
* Strategic planning assistance

## Machine Learning

Planned capabilities include:

* Revenue forecasting
* Customer segmentation
* Campaign prediction
* Risk prediction
* Trend forecasting
* Time-series analysis

---

# 🧩 Current Business Domain Model

The current backend is being developed around the following business entities:

```text
Company
   │
   ├── Departments
   ├── Employees
   ├── Clients
   │      │
   │      └── Projects
   │             │
   │             └── Campaigns
   │
   └── Business KPIs
```

Current core entities include:

| Entity       | Purpose                                  |
| ------------ | ---------------------------------------- |
| User         | Authentication and authorization         |
| Company      | Enterprise/company information           |
| Department   | Organizational departments               |
| Employee     | Workforce information                    |
| Client       | Client/business relationship information |
| Project      | Client/company project information       |
| Campaign     | Marketing/campaign information           |
| Business KPI | Business performance metrics             |

---

# 🛠️ Technology Stack

## Backend

* Python 3.11+
* FastAPI
* SQLAlchemy 2.0
* PostgreSQL
* Alembic
* Pydantic Settings
* Uvicorn
* psycopg v3

## Authentication & Security

* JWT
* Password hashing
* FastAPI dependency injection
* Protected API routes

## Testing

* Pytest
* FastAPI TestClient
* SQLAlchemy model validation
* API integration testing

## Planned AI Stack

* LangChain
* LangGraph
* Google Gemini
* ChromaDB
* FAISS
* LangSmith

## Planned Machine Learning Stack

* Scikit-learn
* XGBoost
* Prophet
* Pandas
* NumPy

## Planned Frontend

* React
* TypeScript
* Tailwind CSS

## Planned Visualization

* Power BI

## Planned Deployment

* Docker
* Railway
* GitHub Actions

---

# 📂 Project Structure

```text
Strategix-AI/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── auth/
│   │   ├── config/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   └── alembic/
│       └── versions/
│
├── tests/
│
├── frontend/
├── agents/
├── ml/
├── datasets/
├── powerbi/
├── deployment/
├── docs/
│
├── pyproject.toml
├── pytest.ini
├── uv.lock
└── README.md
```

---

# 🔄 Development Progress

| Phase                                        | Status      |
| -------------------------------------------- | ----------- |
| Sprint 1 — Backend Foundation                | ✅ Completed |
| Sprint 2 — Core Business Models              | ✅ Completed |
| Sprint 3.1 — Employee Module                 | ✅ Completed |
| Sprint 3.2 — Employee Repository/Service/API | ✅ Completed |
| Sprint 3.3 — Client Module                   | ✅ Completed |
| Sprint 3.4 — Project & Campaign Module       | ✅ Completed |
| ETL & Data Engineering                       | ⏳ Planned   |
| Business Intelligence                        | ⏳ Planned   |
| Machine Learning                             | ⏳ Planned   |
| RAG Knowledge Base                           | ⏳ Planned   |
| Multi-Agent AI                               | ⏳ Planned   |
| Frontend Dashboard                           | ⏳ Planned   |
| Production Deployment                        | ⏳ Planned   |

### Current Backend Validation

The current backend test suite contains **22 tests**, all passing.

```text
22 passed
```

Database migrations are also synchronized:

```text
Alembic Head:
016f6679189b

Alembic Check:
No new upgrade operations detected.
```

This means the current SQLAlchemy models and PostgreSQL schema are synchronized at the current migration head.

---

# 🧪 Development Validation

Run the test suite:

```bash
uv run pytest -v
```

Check the current Alembic revision:

```bash
uv run alembic current
```

Verify that the database schema matches the SQLAlchemy models:

```bash
uv run alembic check
```

Run the FastAPI application:

```bash
uv run uvicorn backend.app.main:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# ⚙️ Local Development

## Clone

```bash
git clone https://github.com/prerna-m01/Strategix-AI.git
cd Strategix-AI
```

## Create Virtual Environment

```bash
uv venv
```

### Windows

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
uv sync
```

## Environment Configuration

Create a `.env` file in the project root.

```env
APP_NAME=Strategix AI
APP_VERSION=0.1.0

HOST=127.0.0.1
PORT=8000

DB_HOST=localhost
DB_PORT=5432
DB_NAME=strategix_ai
DB_USER=postgres
DB_PASSWORD=your_password

SECRET_KEY=your_secret_key

DEBUG=True
ENVIRONMENT=development
```

---

# 🗄️ Database Architecture

Strategix AI uses PostgreSQL as its primary relational database.

SQLAlchemy provides the ORM layer while Alembic manages database schema versioning.

```text
FastAPI
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
SQLAlchemy
   │
   ▼
PostgreSQL
   │
   ▲
   │
Alembic Migrations
```

Current database entities include:

```text
users
companies
departments
employees
business_kpis
clients
projects
campaigns
```

---

# 🧱 Engineering Architecture

Strategix AI follows a layered backend architecture.

```text
API Layer
    │
    ▼
Schema / Validation Layer
    │
    ▼
Service Layer
    │
    ▼
Repository Layer
    │
    ▼
SQLAlchemy Models
    │
    ▼
PostgreSQL
```

### API Layer

Responsible for:

* HTTP endpoints
* Authentication dependencies
* Request handling
* Response serialization

### Schema Layer

Responsible for:

* Request validation
* Response validation
* Data contracts

### Service Layer

Responsible for:

* Business logic
* Workflow coordination
* Business rules

### Repository Layer

Responsible for:

* Database queries
* CRUD operations
* Persistence

### Model Layer

Responsible for:

* Database tables
* Relationships
* Constraints

---

# 🧠 Planned AI Architecture

The AI architecture will be introduced after the underlying business data platform is sufficiently developed.

The intended multi-agent system includes:

| Agent                        | Responsibility                            |
| ---------------------------- | ----------------------------------------- |
| CEO Strategy Agent           | Executive-level strategic recommendations |
| Finance Agent                | Financial analysis                        |
| Marketing Intelligence Agent | Marketing and campaign analysis           |
| Operations Agent             | Operational analysis                      |
| Client Success Agent         | Client intelligence                       |
| Forecast Agent               | Predictive insights                       |
| Risk Assessment Agent        | Risk analysis                             |
| AI Innovation Agent          | AI opportunity discovery                  |

These agents are part of the **planned architecture** and are not represented as fully implemented capabilities in the current backend.

---

# 📖 Case Study

Strategix AI uses a synthetic enterprise case study inspired by the marketing and communications industry.

The project references publicly available information about **Publicis Groupe** only as inspiration for the business scenario and architecture.

No proprietary Publicis Groupe data or systems are used.

All operational datasets created for Strategix AI are synthetic.

---

# 🛣️ Future Roadmap

```text
Backend Foundation
       │
       ▼
Business Data Platform
       │
       ▼
ETL & Data Engineering
       │
       ▼
Business Intelligence
       │
       ▼
Machine Learning
       │
       ▼
RAG Knowledge Base
       │
       ▼
Multi-Agent AI
       │
       ▼
Executive Intelligence
       │
       ▼
Dashboard & Deployment
```

The objective is to evolve Strategix AI from a structured enterprise backend into an integrated **AI-powered Executive Decision Intelligence Platform**.

---

# 🌍 Future Industry Applications

The architecture is intended to be adaptable to multiple industries, including:

* Marketing & Communications
* Retail
* Banking
* Healthcare
* Manufacturing
* Supply Chain
* Consulting
* Telecommunications

---

# 👩‍💻 Author

**Prerna Mishra**

GitHub:
https://github.com/prerna-m01

LinkedIn:
https://linkedin.com/in/prernamishra01

---

# 📜 License

Strategix AI is licensed under the **MIT License**.

See the `LICENSE` file for the complete license text.

---

# ⭐ Project Status

🚧 **Strategix AI is currently under active development.**

The backend foundation and core enterprise business data layer are currently being implemented and validated through automated testing and database migrations.

The analytics, machine learning, RAG, multi-agent AI, dashboard, and deployment layers are planned for subsequent development phases.
