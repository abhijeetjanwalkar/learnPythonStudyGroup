'''
8-4. Large Shirts:
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
'''

def make_shirt(size='large', text='I love Python'):
    """ This function displays T shirt size and the Text to be printed on it """
    print(f"The selected T-shirt Size is '{size}', and Text to be printed is '{text}'")

make_shirt('medium')  
make_shirt(size='large')
make_shirt( text='I like programming')