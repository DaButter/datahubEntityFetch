import logging
import os

from flask import Flask, jsonify
from flask_cors import CORS
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph

app = Flask(__name__)
CORS(app)
log = logging.getLogger(__name__)
logging.basicConfig(level=os.getenv("LOG_LEVEL") or "INFO")

client = DataHubGraph(DatahubClientConfig(server="https://api.datahub.richert.li"))

@app.route("/api/fetch_entities")
def get_data():
    log.info("Handling GET request for /api/fetch_entities")
    search_results = []
    scroll_id = None

    # grapql allows up to 10 000 entry returns per request, but for better development purposes,
    # added a paginator to demonstrate scrollID usage
    while True:
        query = """
        query($input: ScrollAcrossEntitiesInput!) {
          scrollAcrossEntities(input: $input) {
            searchResults {
              entity {
                urn
                type
                ... on Dataset {
                  name
                  description
                  platform {
                    name
                  }
                }
              }
            }
            nextScrollId
          }
        }
        """
        variables = {
            "input": {
                "types": ["DATASET"],
                "query": "*",
                "count": 4
            }
        }
        if scroll_id:
            variables["input"]["scrollId"] = scroll_id

        result = client.execute_graphql(query=query, variables=variables)

        search_results.extend(result["scrollAcrossEntities"]["searchResults"])
        scroll_id = result["scrollAcrossEntities"].get("nextScrollId")
        if not scroll_id:
            break

    # format entity list
    entities = []
    for entity_wrapper in search_results:
        entity = entity_wrapper["entity"]
        log.info(f"Unwrapped entity: {entity}")

        entities.append({
            "name"        : entity["name"],
            "type"        : entity["type"],
            "urn"         : entity["urn"],
            "platform"    : entity["platform"]["name"].upper(),
            "description" : entity["description"] if entity["description"] else "No description"
        })

    log.info(f"Formed entities list: {entities}")
    return jsonify(entities)

# temporary, this will be added in docker config
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# TODO
    # '''
    
    # Use the DataHubGraph client to fetch all entities of type "dataset" from DataHub
    # https://datahubproject.io/docs/python-sdk/clients/#datahub.ingestion.graph.client.DataHubGraph
    # The required dependency is listed in the requirements.txt file
    # Use https://api.datahub.richert.li as the DataHub server (no authentication required) 
    
    # '''