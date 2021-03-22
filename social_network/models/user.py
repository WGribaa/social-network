"""
Defines a User class for our database
"""

from typing import Optional, List

from pydantic import BaseModel, Field, EmailStr

from .object_id import PyObjectId


class User(BaseModel):
    user_id: Optional[PyObjectId] = Field(
        alias="_id", description="Unique identifier for users"
    )
    username: str = Field(..., description="Username for the user")
    friends: List[PyObjectId] = Field([], description="List of friends ids")
    skills: List[PyObjectId] = Field([], description="List of skills ids")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: str}

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.username == other.username
        return NotImplemented
