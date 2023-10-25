import random
class Person:
    def __init__(self, name) -> None:
        self.name  = name
    
class Teacher(Person):
    def __init__(self, name, subject) -> None:
        self.subject = subject
        super().__init__(name)
    
    def teach(self):
        pass

    def take_exam(self, subject, students):
        for student in students:
            marks = random.randint(0,100)
            #TODO set marks for the subjects for each student

    def __repr__(self) -> str:
        return f"{self.name} subject: {self.subject}"



class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.__id = None
        self.classroom = classroom
        self.marks  = {} #dictionary of subjects and mark
        self.grade = None
    @property # getter
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id

    def __repr__(self) -> str:
        return self.name
    

    


