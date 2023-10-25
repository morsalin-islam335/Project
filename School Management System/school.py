class School:
    def __init__(self, name, address,email) -> None:
        self.name = name
        self.teachers = {} # key subject, value teacher object
        self.address = address
        self.email = email
        self.classrooms = dict() # key class_room name, value classroom object

    def add_teacher(self,teacher):
        
        self.teachers[teacher.subject] = teacher
        

    def add_classroom(self,classroom):# classroom will be objects
        self.classrooms[classroom.name] = classroom
    

    def student_admission(self, student):
        if student.classroom.name in self.classrooms:
            self.classrooms[student.classroom.name].add_students(student)
        
        else:
            print(f"No classroom name as {student.classroom.name}")


    def __repr__(self) -> str:
        print("________________All Classrooms__________")
        for key, value in self.classrooms.items():
            print(key)

        print("_____________STUDENTS_________\n")
        # ten = self.classrooms['Ten']
        # print(ten)  #TODO print class ten all students
        i = 6
        for classroom in self.classrooms.values():
            print(f"class {i} students is/are: ", end = "")
            print(classroom.students)
            i += 1

        print("__________OUR TEACHERS________\n")
        for teacher in self.teachers.values():
            print(teacher)

        return ""

class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        self.students = []
        self.subjects = ["Physics", 'Chemistry', 'Math', 'Higher Math', 'Bangla', 'English', "Religion"]



    def add_students(self, student):
        serial_id = f"{self.name} --{len(self.students)}"
        student.id = serial_id
        self.students.append(student)
        

    
    def __str__(self) -> str:
        # return f"{self.name} -- {len(self.students)}"
        print(f"Total students of class {self.name} is {len(self.students)}")
        print(f"class {self.name} students is/are: \n {self.students} ")
        return ""
    
    # TODO sort students by grade
    def get_top_students(self):
        pass
