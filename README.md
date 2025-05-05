# DataHub Frontend-Backend Integration

A Vue.js + Flask application that displays dataset entities from DataHub.

## Architecture

![System Architecture](sys_arch.png)

## Features

- Fetches dataset entities from DataHub API
- Displays entities in responsive card view
- Modular backend with singleton connection pattern

## Backend Structure

```
flask-backend/
├── app.py
├── utils/
│ ├── datahub_client.py   # DataHub connection manager
│ └── entities_service.py # fetching dataset entities
```

## Frontend Structure and Components

```
vue-frontend/
├── vite.config.js
├── src/
│ ├── App.vues
```

- SDX components for UI (cards, tags, buttons)
- Vue.js for state management
- Axios for API communication

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run Flask backend: `python app.py`
3. Start Vue frontend: `npm run serve`

## API Endpoints
`GET /api/fetch_entities` - Returns formatted dataset entities
