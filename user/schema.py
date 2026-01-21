from pydantic import BaseModel,constr
class Create_user(BaseModel):
    name: str
    email: str
    password:constr(min_length=8, max_length=72)
    role: str
  
class User_login(BaseModel):
    password:str
    email:str