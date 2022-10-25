numbers = [1,3,5]
result = []

for num in numbers:
   result.append(num**2)

#print(result)

result = [num**2 for num in numbers]
#print(result)

#strings 

friends = ["Omkar", "Dara", "Kushal"]
startsWith_D = []
for friend in friends:
    if friend.startswith('D'):
        startsWith_D.append(friend)

#print(startsWith_D)

startsWith_D = [friend for friend in friends if friend.startswith('D')]
print(startsWith_D)


