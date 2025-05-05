import logging
import os
import time

from flask import Flask, jsonify
# from flask_cors import CORS
from utils.entities_service import fetch_datasets

app = Flask(__name__)
# actually, we dont need CORS anymore beacuse of nginx, but left it for dev test purposes (curl, postman etc.)
# CORS(app)

log = logging.getLogger(__name__)
logging.basicConfig(level=os.getenv("LOG_LEVEL") or "INFO")

@app.route("/api/fetch_entities")
def get_entities():
    start_time = time.time()
    log.info("Handling GET request for /api/fetch_entities")

    try:
        entities = fetch_datasets()
        log.info(f"Fetched {len(entities)} entities, request completed in {time.time() - start_time:.2f}sec")
        return jsonify(entities)
    except Exception as e:
        log.error("Failed to fetch entities", exc_info=True)
        return jsonify({
            "error": "Failed to fetch entity data",
            "details": str(e)
        }), 500

'''
    Use the DataHubGraph client to fetch all entities of type "dataset" from DataHub
    https://datahubproject.io/docs/python-sdk/clients/#datahub.ingestion.graph.client.DataHubGraph
    The required dependency is listed in the requirements.txt file
    Use https://api.datahub.richert.li as the DataHub server (no authentication required)
'''

# left this for test purposes
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)