class Student:
    "Common base class for all students"

    def __init__(self, name=None, score=None):
        self.name = name
        self.score = score

    def getStudent(self, parameterType):
        if parameterType == "Name":
            return self.name
        elif parameterType == "Score":
            return self.score
        else:
            return "Data Not Found"

    def setStudent(self, name, score):
        self.name = name
        self.score = score


student1 = Student()

while True:
    print("\n===== OOP Program =====")
    print("1. Declare Object")
    print("2. Display Object")
    print("3. Change Object Value")
    print("4. Delete Object")
    print("5. Exit Program")

    choice = input("Enter Your Choice (1/2/3/4/5): ")

    if choice == "1":
        name = input("Enter Your Name: ")
        score = input("Enter Your Score: ")

        student1.setStudent(name, score)
        print("Data Successfully Added")

    elif choice == "2":
        studentName = student1.getStudent("Name")
        studentScore = student1.getStudent("Score")

        print("Name:", studentName)
        print("Score:", studentScore)

    elif choice == "3":
        change = input("What would you like to change (Name/Score): ")

        if change == "Name":
            newName = input("Enter New Name: ")

            student1.setStudent(newName,student1.getStudent("Score"))

            print("Name Data Successfully Changed")

        elif change == "Score":
            newScore = input("Enter New Score: ")

            student1.setStudent(tudent1.getStudent("Name"),newScore)

            print("Score Data Successfully Changed")

        else:
            print("Data Not Found")

    elif choice == "4":
        student1.setStudent(None, None)
        print("Data Successfully Deleted")

    elif choice == "5":
        print("Thank you for using my program.")
        break

    else:
        print("Invalid Choice")