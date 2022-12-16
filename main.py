import logging
import student
import group


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")

console = logging.StreamHandler()
console.setLevel(logging.WARNING)
console.setFormatter(formatter)

filehandler = logging.FileHandler("logger.log")
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(filehandler)


if __name__ == "__main__":

    logger.info("Started logging")

    try:
        student_1 = student.StudentPerson("Petrenko", "Petro", "Petrovych", {"year": 1990, "month": 1, "date": 11})
        student_2 = student.StudentPerson("Vasylenko", "Vasylyna", "Vasylivna", {"year": 1990, "month": 2, "date": 12})
        student_3 = student.StudentPerson("Andrienko", "Andriy", "Andrievych", {"year": 1990, "month": 3, "date": 13})
        student_4 = student.StudentPerson("Kuzmenko", "Maria", "Petrivna", {"year": 1990, "month": 4, "date": 14})
        student_5 = student.StudentPerson("Stetsenko", "Stephan", "Andrievych", {"year": 1990, "month": 5, "date": 20})
        student_6 = student.StudentPerson("Shevchenko", "Ivan", "Oleksievych", {"year": 1991, "month": 11, "date": 5})
        student_7 = student.StudentPerson("Sergienko", "Olga", "Sergievna", {"year": 1990, "month": 9, "date": 21})
        student_8 = student.StudentPerson("Petrenko", "Victor", "Andrievych", {"year": 1990, "month": 8, "date": 22})
        student_9 = student.StudentPerson("Ivanenko", "Hanna", "Ivanivna", {"year": 1990, "month": 7, "date": 23})
        student_10 = student.StudentPerson("Bondarenko", "Mykola", "Mykolayovych", {"year": 1990, "month": 6, "date": 24})
        student_11 = student.StudentPerson("Bondarenko", "Mykola", "Vasyliovych", {"year": 1992, "month": 1, "date": 10})

        group_1 = group.Group("Python", 2022)

        logger.warning("Started logging to console and log")

        group_1.add_student(student_1)
        group_1.add_student(student_2)
        group_1.add_student(student_3)
        group_1.add_student(student_4)
        group_1.add_student(student_5)
        group_1.add_student(student_6)
        group_1.add_student(student_7)
        group_1.add_student(student_8)
        group_1.add_student(student_9)
        group_1.add_student(student_10)
        group_1.remove_student(student_5)
        group_1.add_student(student_5)
        group_1.add_student(student_5)
        group_1.add_student(student_11)


    except Exception as error:
        print(error)

    logger.info("Finished logging")

    print(group_1, "\n")
    print(group_1.find_student("Stetsenko"))







