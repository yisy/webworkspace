def log(func):
    def wrap(*args, **kvgs):
        print("before")
        print("args",args)
        func(*args, **kvgs)
        print("after")
        print("kvgs",kvgs)
    return wrap

@log
def a(*args, **kvgs):
    print "hello world"

if __name__ == '__main__':
    a(name='dd',age='b')

