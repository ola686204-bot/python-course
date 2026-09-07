"""Student records system using namedtuples."""

from collections import namedtuple


Student = namedtuple("Student", ["name", "age", "grade"])


def create_student(name, age, grade):
    """Create and validate a Student namedtuple.

    Args:
        name: The student's name.
        age: The student's age.
        grade: The student's grade.

    Returns:
        A Student namedtuple if valid, otherwise None.
    """
    valid_grades = ["A", "B", "C", "D", "F"]

    if not isinstance(age, int) or isinstance(age, bool):
        return None

    if age <= 0:
        return None

    if grade not in valid_grades:
        return None

    if not name.strip():
        return None

    return Student(name, age, grade)


def display_all_students(students):
    """Display all student records in an aligned table.

    Args:
        students: A list of Student namedtuples.

    Returns:
        None.
    """
    if not students:
        print(f"Student list is empty.")
        return

    print(f"\n{'=' * 40}")
    print(f"{'STUDENT RECORDS':^40}")
    print(f"{'=' * 40}")

    print(
        f"{'Name':<20}"
        f"{'Age':<8}"
        f"{'Grade':<8}"
    )

    print(f"{'-' * 36}")

    for student in students:
        print(
            f"{student.name:<20}"
            f"{student.age:<8}"
            f"{student.grade:<8}"
        )


def find_top_student(students):
    """Return the student with the highest grade.

    Args:
        students: A list of Student namedtuples.

    Returns:
        The Student with the highest grade, or None.
    """
    if not students:
        return None

    grade_order = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2,
        "F": 1,
    }

    return max(
        students,
        key=lambda student: grade_order[student.grade],
    )


def filter_by_grade(students, minimum_grade):
    """Return students at or above the minimum grade.

    Args:
        students: A list of Student namedtuples.
        minimum_grade: The minimum acceptable grade.

    Returns:
        A list of students meeting the grade requirement.
    """
    grade_order = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2,
        "F": 1,
    }

    if minimum_grade not in grade_order:
        return []

    minimum_value = grade_order[minimum_grade]

    return [
        student
        for student in students
        if grade_order[student.grade] >= minimum_value
    ]


def demonstrate_immutability():
    """Demonstrate that Student namedtuples are immutable.

    Returns:
        None.
    """
    student = Student("Ola", 16, "A")

    print(f"\n=== Immutability Demonstration ===")
    print(f"Original student: {student}")

    try:
        student.grade = "F"
    except TypeError as error:
        print(f"Error caught: {error}")
        print(
            f"Student records are immutable because "
            f"namedtuples cannot be changed after creation."
        )
        print(
            f"This is useful because important student "
            f"records should not be changed accidentally."
        )


def compute_grade_distribution(students):
    """Calculate how many students received each grade.

    Args:
        students: A list of Student namedtuples.

    Returns:
        A dictionary containing the count for each grade.
    """
    distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0,
    }

    for student in students:
        distribution[student.grade] += 1

    return distribution


def main():
    """Create student records and demonstrate the system."""
    students = []

    student_data = [
        ("Ola", 16, "A"),
        ("John", 17, "B"),
        ("Mary", 16, "A"),
        ("David", 18, "C"),
        ("Sarah", 17, "B"),
    ]

    for name, age, grade in student_data:
        student = create_student(name, age, grade)

        if student is not None:
            students.append(student)

    display_all_students(students)

    top_student = find_top_student(students)

    if top_student is not None:
        print(
            f"\nTop student: {top_student.name} "
            f"with grade {top_student.grade}"
        )

    filtered_students = filter_by_grade(
        students,
        "B",
    )

    print(f"\nStudents with grade B or higher:")

    for student in filtered_students:
        print(
            f"{student.name:<20}"
            f"{student.grade:<8}"
        )

    distribution = compute_grade_distribution(students)

    print(f"\n=== Grade Distribution ===")

    for grade, count in distribution.items():
        print(f"Grade {grade}: {count}")

    demonstrate_immutability()


if __name__ == "__main__":
    main()
