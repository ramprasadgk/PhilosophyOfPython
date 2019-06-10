from functools import wraps

def make_blinks(function):
   
    def decorator():
        ret= function()
        return "blink" + ret + "<blink>"
    return decorator
    
@make_blinks        
def hello_world():
    
    return 'Hello World!'

print (hello_world())