# Project-Cache
Python 3.9
FASTAPI Server Acts as ASGI BE

Kindly use the below API_KEY for all transactions - Mentioned here for marking purposes.
API_KEY - 'TEST'

POST /collections/:

1.Creates a new collection with a specified capacity.
Endpoint: /collections/
Method: POST
Parameters:
capacity: The capacity of the new collection (optional, default is 10).
Returns:
JSON response containing the collection_id of the newly created collection.
HTTP status code 201 (Created) if successful.


PUT /collections/{collection_id}/capacity/:

2.Updates the capacity of an existing collection.
Endpoint: /collections/{collection_id}/capacity/
Method: PUT
Parameters:
collection_id: The ID of the collection to update.
new_capacity: The new capacity for the collection.
Returns:
JSON response is returned.
HTTP status code 204 (No Content) if successful.


POST /collections/{collection_id}/data/:

3.Adds or updates data in a collection.
Endpoint: /collections/{collection_id}/data/
Method: POST
Parameters:
collection_id: The ID of the collection to add data to.
key: The key of the data.
value: The value of the data.
Returns:
JSON response is returned.
HTTP status code 204 (No Content) if successful.


GET /collections/{collection_id}/data/{key}/:

4.Retrieves data from a collection based on a given key.
Endpoint: /collections/{collection_id}/data/{key}/
Method: GET
Parameters:
collection_id: The ID of the collection to retrieve data from.
key: The key of the data to retrieve.
Returns:
JSON response containing the value of the requested data.
HTTP status code 200 (OK) if successful.
HTTP status code 404 (Not Found) if the collection or key is not found.