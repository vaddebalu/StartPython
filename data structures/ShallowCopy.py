"""
This program demonstrates the use of the deep copy in Python programming language
"""
import copy
default_config={"Name":"Balu","EMPNO":123,"DESIGNATION":"PM"}
print(default_config)
user_config=copy.copy(default_config)
user_config["DESIGNATION"]="VP"
user_config["LOCATION"]="HYDERABAD"

print("default configuration ",default_config)
print("User configuration ",user_config)