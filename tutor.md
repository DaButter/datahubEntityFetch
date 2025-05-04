**Setup requirements:**

Create python virtual environment: ```python -m venv venv```

Activate it ```venv\Scripts\activate```

Install requirements ```pip install -r requirements.txt```

**Run locally for testing**

Run from `flask-backend` directory: ```flask --app api run --debug```

Run from `vue-frontend` directory: ```npm install``` and ```npm run dev```

**Examples**

Server connection + query: https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/dataset_query_entity_v2.py

Dataset entity type: https://docs.datahub.com/docs/graphql/objects#dataset

Front-end desing references taken from here: https://sdx.swisscom.com/

***What did i do***:

Using this I could get a list of all entities with "dataset" type:
```graph.list_all_entity_urns("dataset", 0, 15)```

Using the list of URIs, I wanted to get the necessary aspects of dataset entities:
```get_entities_v2(), get_entity_semityped```
But the return type of get_entity_semityped() was loose.
It was a dictionary that would still need some pre-processing/formating to be parsed to front-end later.

Also tried to use get aspects functions, e.g. ```get_aspects_for_entity, get_aspect```, but the main flaw of this idea was that
I could provide only 1 URN at a time.
To get aspects for all entities, I would need to loop around and spam requests, which is inefficient.

So searching the API description, and finding some examples, decided this data fetch can be beautifuly combined into 1 graphql query using ```execute_graphql```.
Not to hardcode the count (with max number of 10 000), I implemented scroll ID usage.

