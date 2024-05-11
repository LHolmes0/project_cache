import json

from typing import Dict, Any

from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response

from log import logger
from models.models import Collection
from config import API_KEY
from models.apiUtils import validate_key, return_response


app = FastAPI(
    title="Project-Cache",
    version="1.0.0",
    contact={
        "name": "LHolmes",
        # "url": "127.0.0.1:8000",  # Hosting URL To Be Mapped
        "email": "lholmes2017@gmail.com",
    },
)


# app.middleware('http')(catch_exceptions_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # try to restrict  access to the service from unwanted calls
    allow_headers=["*"],
)

# endpoint = "/api/v1"

# Dictionary to store collections
collections: Dict[int, Collection] = {}


@app.get("/", include_in_schema=False)
async def root():
    """
    To check if server is up
    Parameters
    ----------
    None
    Returns
    -------
    JSON response is returned.
    """
    return {"message": "Project-Cache Backend is Healthy"}


@app.post("/collections/", dependencies=[Depends(validate_key)])
async def create_collection(capacity: int = 10):
    """
    To create a collection
    The capacity of the new collection (optional, default is 10).
    Parameters
    ----------
    capacity: The capacity of the new collection (optional, default is 10).
    Returns
    -------
    JSON response containing the collection_id of the newly created collection.
    """
    collection_id = len(collections) + 1
    collections[collection_id] = Collection(capacity)
    logger.info(f"Added ID: {collection_id} to collection")
    return return_response({"collection_id": collection_id}, message="Collection created successfully", status_code=201)


@app.put("/collections/{collection_id}/capacity/", dependencies=[Depends(validate_key)])
async def update_capacity(collection_id: int, new_capacity: int):
    """
    To update capacity of a collection
    Parameters
    ----------
    collection_id: The ID of the collection to update.
    new_capacity: The new capacity for the collection.
    Returns
    -------
    JSON response is returned.
    """
    if collection_id not in collections:
        raise HTTPException(status_code=404, detail="Collection not found")
    collections[collection_id].update_capacity(new_capacity)
    logger.info(f"Updated capacity of ID: {collection_id} to {new_capacity}")
    return return_response(message=f"Updated capacity of ID: {collection_id} to {new_capacity}")


@app.post("/collections/{collection_id}/data/", dependencies=[Depends(validate_key)])
async def put_data(collection_id: int, key: str, value: Any):
    """
    Add data to a collection
    Parameters
    ----------
    collection_id: The ID of the collection to add data to.
    key: The key of the data.
    value: The value of the data.
    Returns
    -------
    JSON response is returned.
    """
    if collection_id not in collections:
        raise HTTPException(status_code=404, detail="Collection not found")
    collections[collection_id].put(key, value)
    logger.info(f"Added Data to ID: {collection_id}")
    return return_response(message="Data added to collection successfully")


@app.get("/collections/{collection_id}/data/{key}/", dependencies=[Depends(validate_key)])
async def get_data(collection_id: int, key: str):
    """
    Get data from a collection
    Parameters
    ----------
    collection_id: The ID of the collection to retrieve data from.
    key: The key of the data to retrieve.
    Returns
    -------
    JSON response containing the value of the requested data.
    """
    if collection_id not in collections:
        raise HTTPException(status_code=404, detail="Collection not found")
    value = collections[collection_id].get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    logger.info(f"Got data from collection ID: {collection_id} for key: {key}")
    return return_response({"value": value})


# start server locally in debug mod
# it will be available here http://127.0.0.1:8000/docs#/
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
