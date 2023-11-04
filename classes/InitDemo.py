class InitDemo:
    name=''
    def __init__(self):
        self.name='There'
    def setName(self,name):
        self.name=name
    def display(self):
        print('Hi ',self.name)
if __name__=='__main__':
    print('In Main')
    init=InitDemo()
    init.display()
    init.setName('Balu')
    init.display()