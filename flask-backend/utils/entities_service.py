import logging
from .datahub_client import NewDataHubConnection

log = logging.getLogger(__name__)

def fetch_datasets():
    try:
        conn = NewDataHubConnection()
        search_results = []
        scroll_id = None
        page_count = 0

        while True:
            page_count += 1
            # log.debug(f"Fetching page {page_count} (scroll_id: {scroll_id})")

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

            result = conn.execute_query(query, variables)
            search_results.extend(result["scrollAcrossEntities"]["searchResults"])
            scroll_id = result["scrollAcrossEntities"].get("nextScrollId")
            if not scroll_id:
                break

        return [
            {
                "name": entity["entity"]["name"],
                "type": entity["entity"]["type"],
                "urn": entity["entity"]["urn"],
                "platform": entity["entity"]["platform"]["name"].upper(),
                "description": entity["entity"]["description"] or "No description"
            }
            for entity in search_results
        ]
    except Exception as e:
        log.error("Failed to fetch datasets", exc_info=True)
        raise