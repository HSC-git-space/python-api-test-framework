from pydantic import BaseModel
from typing import Optional


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class UserModel(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company


class CreateUserModel(BaseModel):
    name: str
    username: str
    email: str