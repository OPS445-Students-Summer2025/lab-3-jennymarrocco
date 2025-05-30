def hello():
    print('Hello World')
    print('Inside a Function')
    return 

my_stuff = hello()
print('Stuff return from hello():', my_stuff)
print('The object my_stuff is a type:', type(my_stuff))
