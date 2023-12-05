#!/usr/bin/env python3

"""
module for Base model that defines all common attributes/methods
for other classes
"""
import uuid
import datetime


class BaseModel:
    """
    defines all common attributes/methods for other classes

    attr:
    id - assign with an uuid when an instance is created
    created_at - assign with the current datetime on creation of an instance
    updated_at - assign with the current datetime on update if instance

    methods:
    save - updates the public instance attr updated_at with the current datetime
    to_dict(self): returns a dict containing all keys/values of the instance
    """

    def __init__(self, **kwargs):

        for key, value in kwargs.items():
            self[key] = value
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ returns  [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dict_copy = self.__dict__.copy()

        dict_copy['__class__'] = self.__class__.__name__
        for key, value in dict_copy.items():
            if (key == "created_at" or key == "updated_at"):
                dict_copy[key] = value.isoformat()
        return dict_copy
