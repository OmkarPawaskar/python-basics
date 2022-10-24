# # While

# number = 7

# play = input("Would you like to play ? y/n ")

# while play != 'n' :
#     user_input = int(input("Guess the number : "))
#     if user_input == number:
#         print("You guessed it correctly!")
#     elif abs(number - user_input) == 1:
#         print("You missed guessing by 1!")
#     else:
#         print("Sorry its wrong!")

#     play = input("Would you like to play ? y/n ")


# # while True:
# #     print("you are hacked")



# while True :
#     play = input("Would you like to play ? y/n ")

#     if play == 'n':
#         break  
    
#     user_input = int(input("Guess the number : "))
#     if user_input == number:
#         print("You guessed it correctly!")
#     elif abs(number - user_input) == 1:
#         print("You missed guessing by 1!")
#     else:
#         print("Sorry its wrong!")
    

# For loop

l = ["Omkar", "Dara", "Kushal"]

for i in l:
    print(f"{i} is part of this class.")

grades =  [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade # total = total + grade

print(total)


# range(start index, number of elements, step_size)
for i in range(len(grades)): #range(0, len(grades))
    print(i)







