import unittest
from PersonService.PersonRepo import addToRepo,findInRepo,getRepo,findInRepo,removeFromRepo,clearRepo, Teacher,Person,Student,_doSomthingWithTeacher,_personCollection

class PersonRepoTest(unittest.TestCase):
    def setUp(self):
        clearRepo()
        
    def test_canAddToTheRepo(self):
        self.assertEqual(0,len(getRepo()))
        teacher = createTeacher()
        addToRepo(teacher)
        self.assertEqual(1,len(getRepo()))

    def test_canRemoveFromRepo(self):
        self.assertEqual(0,len(getRepo()))
        teacher = createTeacher()
        addToRepo(teacher)
        self.assertEqual(1,len(getRepo()))
        removeFromRepo(teacher)
        self.assertEqual(0,len(getRepo()))

    def test_canGetCopyOfRepoContents(self):
        teacher = createTeacher()
        addToRepo(teacher)
        self.assertEqual(_personCollection,getRepo())
        
    def test_canSearchinRepo(self):
        teacher = createTeacher()
        addToRepo(teacher)
        found = findInRepo(lambda person:  (isinstance(person,Person) and person.firstName == "TOM"))
        self.assertEqual(1,len(found))

    def test_canCallMethodWithEitherStudentOrTeacher(self):
        _doSomthingWithTeacher(Teacher("HOMER","SIMPSON"))
        ## linting issue here
        # _doSomthingWithTeacher(Student("HOMER","SIMPSON"))


def createTeacher():
    teacherFirstName= "TOM"
    teacherLastName="HOBO"
    return Teacher(teacherFirstName,teacherLastName)
    
if __name__ == '__main__':
    unittest.main()



# addToRepo(Student("Tim","BUTTER"))
# found = findInRepo(lambda person:  (isinstance(person,Person) and person.firstName == "Tom"))
# for x in found:
#     print(x.printName())
