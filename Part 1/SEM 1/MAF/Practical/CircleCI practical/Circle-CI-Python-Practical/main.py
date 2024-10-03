def to_upper(str):
    return str.upper()

def say_hello(str):
    print("Hello ", str)

if __name__ == '__main__':
    name ="shivam"
    up = to_upper(name)
    say_hello(up)
    say_hello(name)