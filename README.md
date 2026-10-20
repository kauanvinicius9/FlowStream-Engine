## FlowStream-Engine Project Documentation

## Overview

**FlowStream-Engine** is a full-stack application developed for managing and executing manuals and process steps. The system has a robust backend built on **Django / Django REST Framework** and a modern reactive frontend built on **React**, **TypeScript** and **Vite**.

---

## Architecture and Components

### Backend (`Django REST Framework`)

- **`flow_stream/`**: Django core settings module (`settings.py`, `urls.py`, WSGI/ASGI support).
- **`manuals/`**: Application responsible for managing manuals and workflow steps:
  - **`models.py`**: Domain data models (Manuals, Process Steps/`ProcessStep`).
  - **`serializers.py`**: Serialization of models for consumption via JSON API.
  - **`services.py`**: Business logic layer for executing and controlling flows.
  - **`views.py`**: REST endpoints to manipulate manual resources.
  - **`management/commands/seed_db.py`**: Custom command to populate the initial database (`python manage.py seed_db`).

### Frontend (React + TypeScript + Vite)

- **`src/services/api.ts`**: HTTP client for communicating with the Django REST API.
- **`src/types.ts`**: TypeScript type definitions for application data contracts.
- **`src/App.tsx`**: Core UI component.

---

## Execution Instructions

### Backend Configuration

1. Navigate to the backend folder:

   ```bash
   cd FlowStream-Engine-main/backend
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply the migrations to the database:

   ```bash
   python manage.py migrate
   ```

4. (Optional) Populate the database with initial data:

   ```bash
   python manage.py seed_db
   ```

5. Start the Django server:

   ```bash
   python manage.py runserver
   ```

### Frontend Configuration

1. In a new terminal, navigate to the frontend folder:

   ```bash
   cd FlowStream-Engine-main/frontend
   ```

2. Install Node.js dependencies:

   ```bash
   npm install
   ```

3. Start the Vite development server:

   ```bash
   npm run dev
   ```
