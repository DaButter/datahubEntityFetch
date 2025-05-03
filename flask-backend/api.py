import logging
import os

from flask import Flask, jsonify
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph
# from fetchDatasets import fetch_datasets

app = Flask(__name__)
log = logging.getLogger(__name__)
logging.basicConfig(level=os.getenv("LOG_LEVEL") or "INFO")

client = DataHubGraph(DatahubClientConfig(server="https://api.datahub.richert.li"))

@app.route("/api")
def get_data():
    log.info("Handling GET request for /api")

    query = """
    {
      search(input: { type: DATASET, query: "*", start: 0, count: 15 }) {
        searchResults {
          entity {
            urn
            type
            ... on Dataset {
              name
              properties {
                description
              }
            }
          }
        }
      }
    }
    """
    result = client.execute_graphql(query=query)
    return jsonify(result)

# TODO
    # '''
    
    # Use the DataHubGraph client to fetch all entities of type "dataset" from DataHub
    # https://datahubproject.io/docs/python-sdk/clients/#datahub.ingestion.graph.client.DataHubGraph
    # The required dependency is listed in the requirements.txt file
    # Use https://api.datahub.richert.li as the DataHub server (no authentication required) 
    
    # '''