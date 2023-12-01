# Looping Through a Dictionary:
# Iterating Through Keys in a Dictionary:
# Iterating Through Values in a Dictionary:
# Iterating Through Key-Value Pairs in a Dictionary:
# Checking If a Key Exists in a Dictionary:
# Modifying Dictionary Values Using a Loop:
# Adding Key-Value Pairs Using a Loop:
# Removing Key-Value Pairs Using a Loop:
# person = {"name": "John", "age": 30, "city": "New York"}


person = {"name": "John", "age": 30, "city": "New York"}

for  key in person:
    print(key)
    for value in person:
     print(value)


# Iterating through keys

for key in person:
    print(key)



# Iterating through values
for value in person.values():
    print(value)


for key, value in person.items():
    print(key, value)

key_to_check = "age"
exists = False
for key in person:
    if key == key_to_check:
        exists = True
        break
if exists:
     print(f"{key_to_check} exists in the dictionary")



for key in person:
    if key == "age":
        person[key] *= 2
        print(person)

A = {"Name":"Karthik","Age":23,"ph":9515}
# # print(A["Name"])
# print(A.keys())
A.update({"FirstName":"gunda"})
# print(A)
# print(A.values())
print(A.items())


person = {"name": "John", "age": 30, "city": "New York"}
# Adding a key-value pair: ages['David'] = 28
person["Age"]= 28
person["phone_no"]= 9515767950


# person = set()
person.add(("l.name","kishore"))
# print(person)
print(person)

