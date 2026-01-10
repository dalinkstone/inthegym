class Student:
    def __init__(self, name: str):
        self.name = name
        self.next: Student = None


class Students:
    def __init__(self):
        self.students: list[Student] = []
        self.head: Student = None

    def add_student(self, student: Student):
        if self.head is None:
            self.head = student
            self.students.append(self.head)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = student
            self.students.append(current.next)

    def get_students(self) -> list[Student]:
        return self.students

    def size(self) -> int:
        count = 0
        for student in self.students:
            count += 1
        return count


class Solution:
    def __init__(self, students: Students):
        self.students = students

    def get_solution(self) -> Students:
        return self.students.get_students()

    def reorder_students(self, students: Students) -> None:
        if students.size() == 1 or students.size() == 0 or students.size() == 2:
            return

        half = len(students.get_students()) // 2
        count = 0
        current = students.head

        while count != half - 1:
            current = current.next
            count += 1

        end_of_half = current
        previous = None
        current = current.next

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
            count += 1

        end_of_half.next = previous

        self.students = students


def main():
    print("This algorithm should reverse the last half of the list")

    billy = Student("Billy")
    james = Student("James")
    tyler = Student("Tyler")
    susie = Student("Susie")
    lauren = Student("Lauren")
    matt = Student("Matt")
    greg = Student("Greg")
    nate = Student("Nate")
    heather = Student("Heather")
    vika = Student("Vika")

    thomas = Student("Thomas")
    frank = Student("Frank")
    dave = Student("Dave")
    emma = Student("Emma")
    gabby = Student("Gabby")
    sammi = Student("Sammi")
    wallace = Student("Wallace")

    alex = Student("Alex")
    bailey = Student("Bailey")
    caleb = Student("Caleb")
    dalin = Student("Dalin")
    ethan = Student("Ethan")
    george = Student("George")
    haley = Student("Haley")
    izzy = Student("Izzy")
    jess = Student("Jess")
    kate = Student("Kate")
    luke = Student("Luke")

    new_students1 = Students()
    new_students2 = Students()
    new_students3 = Students()

    new_students1.add_student(billy)
    new_students1.add_student(james)
    new_students1.add_student(tyler)
    new_students1.add_student(susie)
    new_students1.add_student(lauren)
    new_students1.add_student(matt)
    new_students1.add_student(greg)
    new_students1.add_student(nate)
    new_students1.add_student(heather)
    new_students1.add_student(vika)

    new_students2.add_student(thomas)
    new_students2.add_student(frank)
    new_students2.add_student(dave)
    new_students2.add_student(emma)
    new_students2.add_student(gabby)
    new_students2.add_student(sammi)
    new_students2.add_student(wallace)

    new_students3.add_student(alex)
    new_students3.add_student(bailey)
    new_students3.add_student(caleb)
    new_students3.add_student(dalin)
    new_students3.add_student(ethan)
    new_students3.add_student(george)
    new_students3.add_student(haley)
    new_students3.add_student(izzy)
    new_students3.add_student(jess)
    new_students3.add_student(kate)
    new_students3.add_student(luke)

    input_students1 = new_students1
    input_students2 = new_students2
    input_students3 = new_students3

    final_solution1 = Solution(input_students1)
    final_solution2 = Solution(input_students2)
    final_solution3 = Solution(input_students3)

    final_solution1.reorder_students(input_students1)
    final_solution2.reorder_students(input_students2)
    final_solution3.reorder_students(input_students3)

    result1 = final_solution1.get_solution()
    result2 = final_solution2.get_solution()
    result3 = final_solution3.get_solution()

    print(
        "\nWe are passing [Billy, James, Tyler, Susie, Lauren, Matt, Greg, Nate, Heather, Vika]"
    )
    print(
        "Which means we expect [Billy, James, Tyler, Susie, Lauren, Vika, Heather, Nate, Greg, Matt]"
    )

    print(*(student.name for student in result1))

    print("\nWe are passing [Thomas, Frank, Dave, Emma, Gabby, Sammi, Wallace]")
    print("Which means we expect [Thomas, Frank, Dave, Wallace, Sammi, Gabby, Emma]")

    print(*(student.name for student in result2))

    print(
        "\nWe are passing [Alex, Bailey, Caleb, Dalin, Ethan, Haley, Izzy, Jess, Kate, Luke]"
    )
    print(
        "Which means we expect [Alex, Bailey, Caleb, Dalin, Ethan, Luke, Kate, Jess, Izzy, Haley, George]"
    )

    print(*(student.name for student in result3))


if __name__ == "__main__":
    main()
