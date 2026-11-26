def pack_result(function):
    def wrapper(*args):
        result = function(*args)
        return {
            'result': result,
            'status': 'success'
        }
    return wrapper

@pack_result
def add(a, b):
    return a + b

@pack_result
def greeting(name):
    return f'Hello, {name}!'

@pack_result
def multiply(a, b):
    return a * b

print(add(1, 2))
print(greeting('John'))
print(multiply(2, 3))