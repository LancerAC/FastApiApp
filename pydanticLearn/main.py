from pydantic import BaseModel, Field, EmailStr, ConfigDict


data = {
    "email": "abc@mail.ru",
    "bio": "Some biography",
    "age": 12,
    "gender": "male",
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=1000)
    age: int = Field(ge=0, le=130)

    model_config = ConfigDict(extra='forbid')


user = UserSchema(**data)
print(repr(user))