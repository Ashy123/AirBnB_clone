#!/usr/bin/env python3
from models.base_model import BaseModel

my_model_dict = {
    'id': 'd5b33c1e-6c0e-4077-aa07-853d87fcf6e7',
    'created_at': '2022-03-10T14:00:00.000000',
    'updated_at': '2022-03-10T14:00:00.000000',
    'name': 'My First Model',
    'my_number': 89,
    '__class__': 'BaseModel'
}

my_model = BaseModel(**my_model_dict)
print(my_model)
