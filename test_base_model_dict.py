#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89

print("Initial state of my_model:")
print("my_model.id: ", my_model.id)
print("my_model:")
print(my_model)
print("type(my_model.created_at): ", type(my_model.created_at))
print("--")

my_model_json = my_model.to_dict()

print("Dictionary representation of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("\nJSON representation of my_model:")
print(my_model_json)

print("--")
my_new_model = BaseModel(**my_model_json)

print("State of my_new_model after creating a new instance from the dictionary representation of my_model:")
print("my_new_model.id: ", my_new_model.id)
print("my_new_model:")
print(my_new_model)
print("type(my_new_model.created_at): ", type(my_new_model.created_at))

print("--")
print("Is my_model the same instance as my_new_model?")
print(my_model is my_new_model)

print(my_model.id == my_new_model.id)
