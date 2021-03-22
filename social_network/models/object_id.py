"""
Defines a PyObjectId to make conversion between BSON ObjectId and Pydantic.
Adds Validation to ObjectId to be compliant with Pydantic and FastAPI's usage.
"""

from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, oid):
        if not ObjectId.is_valid(oid):
            raise ValueError("Invalid ObjectId")
        return ObjectId(oid)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
