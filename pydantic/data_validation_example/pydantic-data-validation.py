from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str

# Simulate an incoming API request payload
payload = {
    "id": 123,
    "username": "john_doe",
    "email": "john@example.com"
}

# Validate the payload against the User model
try:
    user = User(**payload)
    print("Payload is valid.")
    print("Parsed User object:", user)
except ValueError as e:
    print("Payload is invalid:", e)
