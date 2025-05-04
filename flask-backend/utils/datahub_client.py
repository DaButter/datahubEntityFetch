import logging
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph

log = logging.getLogger(__name__)

class NewDataHubConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            try:
                cls._instance = super().__new__(cls)
                cls._instance.client = DataHubGraph(DatahubClientConfig(server="https://api.datahub.richert.li"))
                log.info("DataHub connection established")
            except Exception as e:
                log.error("Failed to initialize DataHub connection", exc_info=True)
                raise
        return cls._instance
    
    def execute_query(self, query, variables):
        try:
            # log.debug(f"Executing query with variables: {variables}")
            return self.client.execute_graphql(query=query, variables=variables)
        except Exception as e:
            log.error("GraphQL query failed", exc_info=True)
            raise