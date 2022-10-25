
def hello():
    return "hello world"

#print(hello())

def user_age_in_secs():
    user_age = int(input("Please enter your age: "))
    age_in_seconds = user_age *365 * 24 * 60 * 60
    user_age_in_secs_var = f"Your age in seconds is {age_in_seconds}"
    return user_age_in_secs_var


friends = ["Dara", "Kushal"]
def add_friend():
    friends.append("Omkar")

add_friend()
print(friends)
