"""Refactored student records system using appropriate data structures."""

from collections import namedtuple

# Fixed field names and immutable student records.
Student = namedtuple("Student", ["name", "age", "grade"])

# Fixed collection of grades. A tuple prevents accidental modification.
VALID_GRADES = ("A", "B", "C", "D", "F")

# Grade order is fixed. Earlier grades are better than later grades.
GRADE_ORDER = ("F", "D", "C", "B", "A")

def audit_structure(name, data, reason):
    """Print a formatted report about a data structure.

    Args:
        name: The name of the data structure.
        data: The data to audit.
        reason: The reason for the audit."""
    print(f"{name:<20} : {type(data).__name__:<12} - {reason}")


def create_student(name, age, grade):
    """Create a new student record.

    Args:
        name: The student's name.
        age: The student's age.
        grade: The student's grade.

    Returns:
        A Student namedtuple if valid, otherwise None."""

    if not isinstance(age, int) or isinstance(age, bool):
        return None

    if age <= 0:
        return None

    if grade not in VALID_GRADES:
        return None

    if not isinstance(name, str) or not name.strip():
        return None
    return Student(name.strip(), age, grade)


def display_all_students(students):
    """Display all student records in an aligned table.

    Args:
        students: A list of Student namedtuples.
    Returns:
        None."""
    if not students:
        print("Student list is empty.")
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
    """Find the student with the highest grade.

    Args:
        students: A list of Student namedtuples.
    Returns:
        The Student namedtuple with the highest grade, or None if the list is empty."""
    
    if not students:
        return None

    return max(
        students,
        key=lambda student: GRADE_ORDER.index(student.grade),
    )



def filter_by_grade(students, minimum_grade):
    """Filter students by a minimum grade.

    Args:
        students: A list of Student namedtuples.
        minimum_grade: The minimum grade to filter by.

    Returns:
        A list of Student namedtuples with grades equal to or better than the minimum_grade."""
    
    if minimum_grade not in VALID_GRADES:
        return []

    minimum_value = GRADE_ORDER.index(minimum_grade)

    return [
        student for student in students
        if GRADE_ORDER.index(student.grade) >= minimum_value
    ]


def  demonstrate_immutability():
    """Demonstrate that student namedtuples are immutable.
    Returns:
        None.
    """
    student = Student("Alice", 20, "A")
    print("\n=== Immutability Demonstration ===")
    print(f"Original student: {student}")

    try:
        student.age = "F"
    except AttributeError as error:
        print(f"Error caught: {error}")
        print(
            "Student records are immutable because they are namedtuples."
        )
        print(
            "This means you cannot change the fields" \
            " of a student record after it has been created."
        )


def compute_grade_distribution(students):
    """Compute the distribution of grades among students.

    Args:
        students: A list of Student namedtuples.
    Returns:
        A dictionary with grades as keys and counts as values."""
    # A dictionary is appropraite because counts change during the execution.
    distribution = {
        grade: 0 for grade in VALID_GRADES
    }

    for student in students:
        distribution[student.grade] += 1

    return distribution


def audit_all_structures(students, student_record, distribution):
    """Display the data structure audit for the program.
    
    Args:
        students: The list of Student namedtuples.
        student_record: A single Student namedtuple.
        distribution: The grade distribution dictionary.
        
        Returns:
        None.
    """
    print("\n=== Data Structure Audit ===")

    audit_structure(
        "students",
        students,
        "ordered collection of student records"
    )
    audit_structure(
        "student_record",
        student_record,
        "fixed-field immutable record accessed by field names",
    )


    audit_structure(
       "VALID_GRADES",
       VALID_GRADES,
       "fixed collection of valid grades",
    )


    audit_structure(
        "GRADE_ORDER",
        GRADE_ORDER,
        "fixed collection of grades in order from worst to best",
    )


    audit_structure(
        "distribution",
        distribution,
        "dictionary of grade counts",
    )

    print()


def main():
    """Create student records and demonstrate the system."""
    students = []

    student_data = [
        ("Alice", 20, "A"),
        ("John", 17, "B"),
        ("Mary", 16, "C"),
        ("David", 18, "B"),
    ]

    for name, age, grade in student_data:
        student = create_student(name, age, grade)

        if student is not None:
            students.append(student)
             # Create an example record for the audit.
    student_record = Student("Ola", 16, "A")

    # The distribution is a dictionary because its counts change.
    distribution = compute_grade_distribution(students)

    # Display the full audit at program startup.
    audit_all_structures(
        students,
        student_record,
        distribution,
    )

    display_all_students(students)

    top_student = find_top_student(students)

    if top_student is not None:
        print(
            f"\nTop student: {top_student.name} "
            f"with grade {top_student.grade}"
        )

    filtered_students = filter_by_grade(students, "B")

    print("\nStudents with grade B or higher:")

    for student in filtered_students:
        print(
            f"{student.name:<20}"
            f"{student.grade:<8}"
        )

    print("\n=== Grade Distribution ===")

    for grade, count in distribution.items():
        print(f"Grade {grade}: {count}")

    demonstrate_immutability()


if __name__ == "__main__":
    main()
