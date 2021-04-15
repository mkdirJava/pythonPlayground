from typing import List, Callable

import abc

class Person:
    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName
        self.detail: str

    def printName(self) -> str:
        return self.firstName + self.lastName

    # abstract method
    @abc.abstractmethod
    def doSomthing(self)-> str:
        pass

    @property
    def detail(self)-> str:
        return self.detail
    @detail.setter
    def detail(self,detail:str) -> str:
        self.detail = detail
        return self.detail
    
        

class Teacher(Person):
    def __init__(self,firstName: str, lastName: str):
        super().__init__(firstName,lastName)

    # This is an override of by the Teacher class of the person abstract method
    def doSomthing(self) -> str:
        return "Teacher doing somthing"
    
class Student(Person):
    def __init__(self, firstName:str, lastName:str):
        super().__init__(firstName,lastName)

    # This is an override of by the Student class of the person abstract method
    def doSomthing(self) -> str:
        return "SLEEP IN UNTIL 12:00"


## private collection of Person in list acting as a repo.
_personCollection :List[Person] = []
def clearRepo():
    _personCollection.clear()
def addToRepo( person: Person):
    _personCollection.append(person)
def getRepo() -> List[Person]:
    return _personCollection.copy()


def findInRepo(predicateFunction: Callable[[Person],bool]) -> List[Person]:
    return [potential for potential in _personCollection if (predicateFunction(potential)) ]


    
def removeFromRepo(person:Person):
    _personCollection.remove(person)

def _doSomthingWithTeacher(teahcer :Teacher):
    print(teahcer.printName())


# This would warn over a type issue but will still work if executed
# _doSomthingWithTeacher(Student("FirstName","LastName"))
