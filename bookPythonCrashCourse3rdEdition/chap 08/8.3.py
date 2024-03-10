'''
8-3. T-Shirt: 
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.
'''

def make_shirt(size, text):
    """ This function displays T shirt size and the Text to be printed on it """
    print(f"The selected T-shirt Size is '{size}', and Text to be printed is '{text}'")

make_shirt('medium', 'Python is COOL!!!!')  
make_shirt(size='large', text='I love Programming')