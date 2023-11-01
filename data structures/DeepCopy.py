"""
This program demonstrates the use of the deep copy in Python programming language
"""
import copy
first_config={"Name":"Balu","EMPNO":123,"DESIGNATION":"PM"}
print(first_config)
loc_config=copy.deepcopy(first_config)
loc_config["DESIGNATION"]="VP"
loc_config["LOCATION"]="HYDERABAD"

print("location configuration ",loc_config)
print("first configuration ",first_config)

salary_config=copy.deepcopy(first_config)
salary_config['salary']='20LPA'

print("salary configuration ",salary_config)
print("first configuration ",first_config)