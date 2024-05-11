from fastapi import HTTPException, Header
from config import API_KEY


# Extend method to add UM auth based upon keys - Fetch key from Redis based on UserToken
async def validate_key(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key


def return_response(data=None, status_code=200, message=None):
    if message and data:
        return {"message": message, "data": data}, status_code
    elif data:
        return data, status_code
    elif message:
        return {"message": message}, status_code
    else:
        return {}, status_code
