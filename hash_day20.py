# key   >   value 

student = {
    "Name " : "Anas",
    "City" : "Multan",
    "Semester" : 2
 }
print(student["Name "])
print(student["City"])
print(student["Semester"])


# adding a key

student["GPA"] = "3.2"
print(student["GPA"])

# updating the key 
student["City"] = "Lahore"
print(student["City"])

#deleting the key 
del student["GPA"]
print(student)

#  Loop over keys only (Default Behaiviour)
for key in student:
    print(key)
# Name
# City
# Semester 

# Loop over value
for value in student.values():
    print(value)
# Anas
# Lahore
# 2nd 

# loop over both key and value
for key, value in student.items():
    print(key ,"→" , value )


# loop over only string keys
for key , value in student.items():
    if type(value) == str:
        print(key , "→", value)


