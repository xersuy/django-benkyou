from ninja import Schema, Field


class UserSchema(Schema):
    id: int
    first_name: str
    last_name: str


class LoginSchema(Schema):
    username: str
    password: str


class UserInfo(Schema):
    data: str
