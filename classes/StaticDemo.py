class StaticDemo:
    name=''
    def __init__(self):
        self.name='There'
    @staticmethod
    def display(name):
        print('Hi ',name)
if(__name__=='__main__'):
    StaticDemo.display('Balu')