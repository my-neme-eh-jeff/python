class Employee:
    _id:int
    name:str
    desig:str
    def __init__(self,_id,name,desig):
        self._id=_id
        self.name=name
        self.desig=desig

class Developer(Employee):
    def __init__(self,_id,name):
        super().__init__(_id,name,desig="Developer")

class Tester(Employee):
    def __init__(self,_id,name):
        super().__init__(_id,name,desig="Tester")

class Manager(Employee):
    def __init__(self,_id,name):
        super().__init__(_id,name,desig="Manager")
    _developers=[]

    def add_dev(self,developer:Developer):
        self._developers.append(developer)

    def rem_dev(self,_id):
        for dev in self._developers:
            if _id==dev._id:
                self._developers.remove(dev)
                return True
        return False
    
    def myDevs(self):
        print("Devs under me")
        for dev in self._developers:
            print(dev.name)
        return
def main():
    manager=Manager(1,'Virat')
    developer=Developer(2,'Rohit')
    developer2=Developer(3,'Shikhar')
    developer3=Developer(4,'Bhuvi')
    tester=Tester(5,'Dhoni')
    manager.add_dev(developer=developer)
    manager.add_dev(developer=developer2)
    manager.add_dev(developer=developer3)
    manager.myDevs()
    manager.rem_dev(3)
    manager.myDevs()
main() 