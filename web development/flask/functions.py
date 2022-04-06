def decorator_function(function):
    def wrapper_function():
        function()
        print("Leonor")
    
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello")

@decorator_function
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

# or

decorated_function = decorator_function(say_greeting)
decorated_function()