"""
This program demonstrates how to use * and ** unpacking operators in Python
"""
def displayCountries(ctry1,ctry2,ctry3):
    print("countries",ctry1,ctry2,ctry3)
countries=("India","America","Singapore")
#display list with unpacking operators
displayCountries(*countries)

countrynames={'ctry1':'India','ctry2':'Singapore','ctry3':'America'}

#display dictionary keys with unpacking operator
displayCountries(*countrynames)
#display dictionary values with unpacking operator
print(type(countrynames))
displayCountries(**countrynames)