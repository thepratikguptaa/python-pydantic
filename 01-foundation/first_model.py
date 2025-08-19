from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id': 101, 'name': "John Doe", 'is_active': True}
# input_data = {'id': 101, 'name': "John Doe", 'is_active': "True"} // notice how this will not fail... pydantic will convert it to boolean
# input_data = {'id': 101, 'name': "John Doe", 'is_active': "sahi"} // but here it won't
# input_data = {'id': "101", 'name': "John Doe", 'is_active': "sahi"} // pydantic will automatically convert where possible... to save you from errors

user = User(**input_data)
print(user)
print("Type of user.is_active:", type(user.is_active))