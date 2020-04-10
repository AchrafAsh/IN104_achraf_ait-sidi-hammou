class Person:
    def __init__(self, firstName, lastName, age, mood):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__age = age
        self.mood = mood

    def __str__(self):
        return self.introduce()

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getAge(self):
        return self.__age

    def setAge(self, newAge):
        if(newAge > self.getAge()):
            print("Growing older...")
        elif(newAge < self.getAge()):
            print("Getting younger ?")
        else:
            print('This person is already ', newAge)

        self.__age = newAge

    def introduce(self):
        return "Hello I'm " + self.getFirstName() + "! I'm " + str(self.getAge()) + " and I'm feeling " + self.mood


class Student(Person):
    def __init__(self, firstName, lastName, age, mood, grade, school):
        Person.__init__(self, firstName, lastName, age, mood)
        self.grade = grade
        self.school = school

    def __str__(self):
        self.introduce()
        return "Hi! I'm a " + self.grade + " studying at " + self.school


class Teacher(Person):
    def __init__(self, firstName, lastName, age, mood, courses, researchTopic):
        Person.__init__(self, firstName, lastName, age, mood)
        self.courses = courses
        self.researchTopic = researchTopic

    def __str__(self):
        self.introduce()
        introduction = "Hey! I teach "
        for course in self.courses:
            introduction += course + ","
        if(self.researchTopic):
            introduction += " I also work on " + self.researchTopic
        return introduction


if __name__ == "__main__":
    Achraf = Person('Achraf', 'ASH', 22, "bored")
    print(Achraf.introduce())
    Achraf.mood = "sick"
    print(Achraf)

    Achraf = Student("Achraf", "ASH", 22, "bored", "Graduate", "MIT")

    AnonymousTeacher = Teacher("Anonymous", "Teacher", 34, "curious", [
                               "Computer Science", "Data Visualization"], "Machine Learning CI/CD")
    print(Achraf)
    print(AnonymousTeacher)
