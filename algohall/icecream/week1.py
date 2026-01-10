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
            while current is not None:
                current = current.next
            current = student
            self.students.append(current)

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
        half = len(students.get_students()) // 2
        size = students.size()

        print(half)
        print(f"\n{size}")

        self.students = students


def main():
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

    new_students = Students()

    new_students.add_student(billy)
    new_students.add_student(james)
    new_students.add_student(tyler)
    new_students.add_student(susie)
    new_students.add_student(lauren)
    new_students.add_student(matt)
    new_students.add_student(greg)
    new_students.add_student(nate)
    new_students.add_student(heather)
    new_students.add_student(vika)

    input_students = new_students

    final_solution = Solution(input_students)

    final_solution.reorder_students(input_students)

    result = final_solution.get_solution()

    print("This algorithm should reverse the last half of the list")
    print(
        "\nWe are passing [Billy, James, Tyler, Susie, Lauren, Matt, Greg, Nate, Heather, Vika]"
    )
    print(
        "Which means we expect [Billy, James, Tyler, Susie, Lauren, Vika, Heather, Nate, Greg, Matt]"
    )

    print(*(student.name for student in result))


if __name__ == "__main__":
    main()
