import json

text = '{"Name" : "Anas" , "age ": "20", "is_true": true , "Courses" : ["DSA" , "Python"] , "Address": {"city" : "Multan" } }'

data = json.loads(text)

print(type(text))
print(type(data))
print(data["Name"])
print(data["Courses"][0])
print(data["Address"]["city"])