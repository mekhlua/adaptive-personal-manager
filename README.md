# Adaptive Personal Manager

Personalized productivity & behavioral-analytics system. Full spec in `docs/`.

## Quick Start (new teammate — 3 commands)

    git clone https://github.com/mekhlua/adaptive-personal-manager.git
    cd adaptive-personal-manager
    make setup && make up

App runs at http://localhost:8000/docs (FastAPI auto docs).

## Everyday commands

    make up      # start backend + db
    make down    # stop everything
    make test    # run tests
    make lint    # run ruff

## Branching
- `main`: stable, protected
- `develop`: integration branch, protected
- `feature/<name>`: your work, PR into `develop`

## Project structure
See `docs/architecture.md`
