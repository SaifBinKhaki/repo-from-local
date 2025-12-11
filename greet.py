def greet(name):
    print("Inside greet function")
    return f"Hello, {name}!"


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
