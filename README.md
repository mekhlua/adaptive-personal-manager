# Adaptive Personal Manager

Personalized productivity & behavioral-analytics system. See `docs/` for the SRS.

## Setup

    cd backend
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt -r requirements-dev.txt
    uvicorn app.main:app --reload

## Branching
- `main`: stable
- `develop`: integration branch
- `feature/<name>`: work branches, PR into `develop`
