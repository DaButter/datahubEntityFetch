import logging
import os

from flask import Flask, jsonify
from flask_cors import CORS
from utils.entities_service import fetch_datasets

app = Flask(__name__)
CORS(app)

log = logging.getLogger(__name__)
logging.basicConfig(level=os.getenv("LOG_LEVEL") or "INFO")

@app.route("/api/fetch_entities")
def get_entities():
    log.info("Handling GET request for /api/fetch_entities")
    try:
        entities = fetch_datasets()
        log.info(f"Successfully fetched {len(entities)} entities")
        return jsonify(entities)
    except Exception as e:
        log.error("Failed to fetch entities", exc_info=True)
        return jsonify({
            "error": "Failed to fetch entity data",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

'''
    Use the DataHubGraph client to fetch all entities of type "dataset" from DataHub
    https://datahubproject.io/docs/python-sdk/clients/#datahub.ingestion.graph.client.DataHubGraph
    The required dependency is listed in the requirements.txt file
    Use https://api.datahub.richert.li as the DataHub server (no authentication required)
'''