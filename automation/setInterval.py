import threading

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec) 
        print(func)  
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

# def hey(name):
#     print(name)

set_interval(100, 1)
# def printit():
#   threading.Timer(1.0, printit).start()
#   print( "Hello, World!")


# printit()