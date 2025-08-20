from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []
    
    model_config = ConfigDict(
        json_encoders = {
            datetime: lambda dt: dt.strftime("%Y-%m-%d %H:%M:%S %Z")
        }
    )

# create a user instance
user = User(
    id = 1,
    name = "John Doe",
    email = "5oEj8@example.com",
    created_at = datetime(2024, 3, 15, 14, 30),
    address = Address(
        street = "123 Main St",
        city = "Anytown",
        zip_code = "12345"
    ),
    tags = ["premium", "admin"]
)

# using model_dump() to convert the user instance to a dictionary
user_dict = user.model_dump()
print(user_dict)

print("="*120)

# using model_dump_json() to convert the user instance to a JSON string
user_json = user.model_dump_json()
print(user_json) # notice the difference between model_dump() and model_dump_json()