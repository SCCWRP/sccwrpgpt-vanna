from abc import ABC, abstractmethod
import uuid

# Define classes
class Cache(ABC):
    @abstractmethod
    def generate_id(self, *args, **kwargs):
        pass

    @abstractmethod
    def get(self, id, field):
        pass

    @abstractmethod
    def get_all(self, field_list) -> list:
        pass

    @abstractmethod
    def set(self, id, field, value):
        pass

    @abstractmethod
    def delete(self, id):
        pass


class MemoryCache(Cache):
    def __init__(self):
        self.cache = {}

    def generate_id(self, *args, **kwargs):
        return str(uuid.uuid4())

    def set(self, id, field, value):
        if id not in self.cache:
            self.cache[id] = {}

        self.cache[id][field] = value

    def get(self, id, field):
        if id not in self.cache:
            return None

        if field not in self.cache[id]:
            return None

        return self.cache[id][field]

    def get_all(self, field_list) -> list:
        return [
            {
                "id": id,
                **{
                    field: self.get(id=id, field=field)
                    for field in field_list
                }
            }
            for id in self.cache
        ]

    def delete(self, id):
        if id in self.cache:
            del self.cache[id]




# requires cache decorator
from functools import wraps
from flask import request

cache = MemoryCache()

# NO NEED TO CHANGE ANYTHING BELOW THIS LINE
def requires_cache(fields):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            
            # id is a reserved word in python, which is a function that gets the location of an objectin memory or something like that
            # so we'll be calling in id_
            id_ = request.args.get('id')

            if id_ is None:
                return jsonify({"type": "error", "error": "No id provided"})
            
            for field in fields:
                if cache.get(id=id_, field=field) is None:
                    return jsonify({"type": "error", "error": f"No {field} found"})
            
            field_values = {field: cache.get(id=id_, field=field) for field in fields}
            
            # Add the id to the field_values
            field_values['id'] = id_

            return f(*args, **field_values, **kwargs)
        return decorated
    return decorator