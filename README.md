# FertiliCare – Fertility Health Tracker & Lifestyle Optimizer

## Quick Start

### Step 1 – Django
```bash
cd django_backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Step 2 – Open browser
```
http://127.0.0.1:8000
```

## Render Deploy

This repo is set up to deploy as a single Django service on Render.

1. Push the repo to GitHub.
2. In Render, create a new Blueprint and point it to `render.yaml`.
3. Render will create the web service from `django_backend`.
4. If you use custom domain names, set `DJANGO_ALLOWED_HOSTS` and `DJANGO_CSRF_TRUSTED_ORIGINS` in the service environment.

The chatbot now uses the local Django fallback logic, so the app does not need a separate FastAPI deployment for basic operation.
