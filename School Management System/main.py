from school import School, ClassRoom
from persons import Student, Teacher

def main():
    school = School("Nautara Abunessa B.L high School", 'Nautara, Dimla, Nilphamari', 'nautaraabiunnessa@yahoo.com')
    six = ClassRoom('Six')
    school.add_classroom(six)

    seven = ClassRoom('Seven')
    school.add_classroom(seven)

    eight = ClassRoom('Eight')
    school.add_classroom(eight)

    nine = ClassRoom('Nine')
    school.add_classroom(nine)

    ten = ClassRoom('Ten')
    school.add_classroom(ten)

    Morsalin = Student("Morsalin Islam", ten)
    school.student_admission(Morsalin)

    Motiur = Student("Motiur Rahman", ten)
    school.student_admission(Motiur)

    Rukunuzzaman = Student("Rukunuzzaman", ten)
    school.student_admission(Rukunuzzaman)

    Abu_taher = Student("Abu-Taher", nine)
    school.student_admission(Abu_taher)

    G_Rabby = Student("Golam Rabby", eight)
    school.student_admission(G_Rabby)


    Nibir = Student("Sakibuzzaman Nibir", seven)
    school.student_admission(Nibir)

    Ariful = Student("Arifuzzaman Arif", six)
    school.student_admission(Ariful)

    Pulin_Bihari = Teacher("Pulin Bihari Odhikari", "Bangla-2")
    school.add_teacher(Pulin_Bihari)

    Monjuara_Begum= Teacher("Monjuara Begum", "ICT")
    school.add_teacher(Monjuara_Begum)

    Jahangir_Alam = Teacher("Jahangir Alam", "Social Science")
    school.add_teacher(Jahangir_Alam)

    



    print(school)


if __name__ == "__main__":
    main()
    