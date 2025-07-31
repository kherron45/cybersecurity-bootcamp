users = {"Keith": 25, "bob" : 30}

print(users["Keith"])

#Safety get value for "charlie"
print(users.get("charlie", "Not found"))

#Add a new user
users["charlie"] = 28
print(users)

