import json
total = 0
Average = 0
with open("people.json" , "r") as f:
    data = json.load(f)

print(data["Class"])
print(len(data["Students"]))
print(data["Students"][0]["Name"])

for student in data["Students"]:
    print(student["Name"] ," Scored " ,student["Marks"] )
    total += student["Marks"]

Average = total/len(data["Students"])

print(round(Average,2))