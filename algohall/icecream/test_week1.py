from week1 import Student, Students, Solution


def create_student_list(names):
    students_obj = Students()
    for name in names:
        students_obj.add_student(Student(name))
    return students_obj


def get_linked_list_names(students_obj):
    """
    Helper function to traverse the Linked List via pointers
    to verify the actual structure.
    """
    names = []
    current = students_obj.head
    while current is not None:
        names.append(current.name)
        current = current.next
    return names


def test_reorder_even_number_of_students():
    input_names = [
        "Billy",
        "James",
        "Tyler",
        "Susie",
        "Lauren",
        "Matt",
        "Greg",
        "Nate",
        "Heather",
        "Vika",
    ]
    expected_names = [
        "Billy",
        "James",
        "Tyler",
        "Susie",
        "Lauren",
        "Vika",
        "Heather",
        "Nate",
        "Greg",
        "Matt",
    ]

    students_list = create_student_list(input_names)
    solver = Solution(students_list)
    solver.reorder_students(students_list)

    result_names = get_linked_list_names(students_list)

    assert result_names == expected_names


def test_reorder_odd_number_of_students():
    input_names = ["Thomas", "Frank", "Dave", "Emma", "Gabby", "Sammi", "Wallace"]

    expected_names = ["Thomas", "Frank", "Dave", "Wallace", "Sammi", "Gabby", "Emma"]

    students_list = create_student_list(input_names)
    solver = Solution(students_list)
    solver.reorder_students(students_list)

    result_names = get_linked_list_names(students_list)

    assert result_names == expected_names


def test_reorder_mixed_large_list():
    input_names = [
        "James",
        "Thomas",
        "Susie",
        "Emma",
        "Heather",
        "Gabby",
        "Lauren",
        "Sammi",
        "Nate",
        "Wallace",
        "Greg",
    ]
    expected_names = [
        "James",
        "Thomas",
        "Susie",
        "Emma",
        "Heather",
        "Greg",
        "Wallace",
        "Nate",
        "Sammi",
        "Lauren",
        "Gabby",
    ]

    students_list = create_student_list(input_names)
    solver = Solution(students_list)
    solver.reorder_students(students_list)

    result_names = get_linked_list_names(students_list)

    assert result_names == expected_names
