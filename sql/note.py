class Emp:
    name = ''
    gschool = ''
    def __init__(self,school):
        print('생성자 = ', school)
        self.gschool = school
        #self.name=name
        #print('__init__(self, name) ',name)

    def insert(self):
        print('insert함수 9:25')
        print(self.gschool)

    def printAll(self):
        print('printAll 9:25')
        print(self.gschool)
    
if __name__ == "__main__":
    print()
    my = Emp('안동대학교')
    my.insert()
    my.printAll()
    print()
