"""Week 4 local and global variables"""

my_variable = "I am global"


def test_scope():
    my_variable = "I am local"
    print(my_variable)
    
test_scope()
print(my_variable)

"""One prints the global variable and ignores the function test scope outputing I am global.
The other prints the my variable in the function outputting I am local"""