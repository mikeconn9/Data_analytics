text = input()

# When writting a decorator with parameters:
# 1. return func(parm)
# 2. return wrapper
def uppercase_decorator(func):
    def wrapper(text):
        return func(text.upper())
    return wrapper

@uppercase_decorator
def display_text(text):
    return(text)

print(display_text(text))