friend_ages = {"Omkar" : 26, "Kushal" : 25, "Dara" : 25}

print(friend_ages)
print(friend_ages["Omkar"])

for key,value in friend_ages.items():
    print(key)

friends = [
    {"name" : "Omkar", "age": 26, "last" : "pawaskar"},
    {"name" : "Kushal", "age": 25 },
    {"name" : "Dara", "age": 26 }
]


#print(friends)

# result = []
# for dict in friends:
#     for key,values in dict.items():
#         result.append(values)

#print(result)

result = [values for dict in friends for key,values in dict.items()]

print(result)