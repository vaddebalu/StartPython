def track(func):
   # print("start ...")
    def inner(*args):
        print("start ...")
        out=func(*args)
        print("stop ...")
        return out
    return inner
@track
def add(x,y):
    return x+y

print(add(2,3))
