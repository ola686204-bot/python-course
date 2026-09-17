"""Data reload system for student records."""


def load_students(filename):
    """Load valid student records from a CSV file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of valid student dictionaries.
    """
    students = []
    skipped_lines = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            next(file, None)  # Skip the header row

            for line_number, line in enumerate(file, start=2):
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) != 4:
                    print(
                        f"Warning: Skipping malformed line "
                        f"{line_number}: {line}"
                    )
                    skipped_lines += 1
                    continue

                name, age, city, score = parts

                try:
                    student = {
                        "name": name.strip(),
                        "age": int(age.strip()),
                        "city": city.strip(),
                        "score": float(score.strip()),
                    }
                except ValueError:
                    print(
                        f"Warning: Skipping invalid line "
                        f"{line_number}: {line}"
                    )
                    skipped_lines += 1
                    continue

                students.append(student)

    except FileNotFoundError:
        print(f"Warning: {filename} was not found.")
        return []

    except OSError as error:
        print(f"Error reading {filename}: {error}")
        return []

    print(f"Skipped {skipped_lines} malformed line(s).")
    return students

def save_students(students, filename):
    """Save student records to a CSV file.

    Args:
        students (list): A list of student dictionaries.
        filename (str): The name of the file to write.

    Returns:
        bool: True if saving succeeds, otherwise False.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            # The header must always be written first.
            file.write("name,age,city,score\n")

            for student in students:
                file.write(
                    f"{student['name']},"
                    f"{student['age']},"
                    f"{student['city']},"
                    f"{student['score']}\n"
                )

        return True

    except OSError as error:
        print(f"Error saving {filename}: {error}")
        return False

def display_students(students):
    """Display student records in an aligned table.

    Args:
        students (list): A list of student dictionaries.

    Returns:
        None: This function only prints the records.
    """
    if not students:
        print("No records available.")
        return

    print(
        f"{'Name':<15}"
        f"{'Age':<8}"
        f"{'City':<18}"
        f"{'Score':<10}"
        f"{'Grade':<8}"
    )

    print("-" * 59)

    for student in students:
        print(
            f"{student['name']:<15}"
            f"{student['age']:<8}"
            f"{student['city']:<18}"
            f"{student['score']:<10.2f}"
            f"{student['grade']:<8}"
        )


def filter_by_city(students, city):
    """Return students from a specified city.

    Args:
        students (list): A list of student dictionaries.
        city (str): The city to search for.

    Returns:
        list: Students from the specified city.
    """
    matching_students = []

    for student in students:
        if student["city"].lower() == city.lower():
            matching_students.append(student)

    return matching_students

def filter_by_min_score(students, min_score):
    """Return students with scores at least the minimum score.

    Args:
        students (list): A list of student dictionaries.
        min_score (float): The minimum acceptable score.

    Returns:
        list: Students whose scores are greater than or equal to min_score.
    """
    matching_students = []

    for student in students:
        if student["score"] >= min_score:
            matching_students.append(student)

    return matching_students

def compute_summary(students):
    """Compute statistics about student records.

    Args:
        students (list): A list of student dictionaries.

    Returns:
        dict: Summary statistics for the student records.
    """
    if not students:
        return {
            "total": 0,
            "passing": 0,
            "average_score": 0,
            "highest_score": 0,
            "lowest_score": 0,
            "grade_distribution": {},
        }

    total = len(students)
    passing = 0
    scores = []
    grade_distribution = {}

    for student in students:
        score = student["score"]
        grade = student["grade"]

        scores.append(score)

        if score >= 60:
            passing += 1

        if grade not in grade_distribution:
            grade_distribution[grade] = 0

        grade_distribution[grade] += 1

    return {
        "total": total,
        "passing": passing,
        "average_score": sum(scores) / len(scores),
        "highest_score": max(scores),
        "lowest_score": min(scores),
        "grade_distribution": grade_distribution,
    }


def assign_grades(students):
    """Assign a grade to each student based on the score.

    Args:
        students (list): A list of student dictionaries.

    Returns:
        list: The updated list of student dictionaries.
    """
    for student in students:
        score = student["score"]

        if score >= 70:
            student["grade"] = "A"
        elif score >= 60:
            student["grade"] = "B"
        elif score >= 50:
            student["grade"] = "C"
        elif score >= 45:
            student["grade"] = "D"
        elif score >= 40:
            student["grade"] = "E"
        else:
            student["grade"] = "F"

    return students


def run_session(students, filename):
    """Run the student-record menu until the user quits.

    Args:
        students (list): A list of student dictionaries.
        filename (str): The file used to save the records.

    Returns:
        None: The function runs the interactive menu.
    """
    while True:
        print("\nStudent Record Menu")
        print("1. View all students")
        print("2. Filter by city")
        print("3. Filter by minimum score")
        print("4. View summary")
        print("5. Save and quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_students(students)

        elif choice == "2":
            city = input("Enter city: ").strip()
            matching_students = filter_by_city(students, city)
            display_students(matching_students)

        elif choice == "3":
            try:
                min_score = float(
                    input("Enter minimum score: ").strip()
                )
                matching_students = filter_by_min_score(
                    students,
                    min_score,
                )
                display_students(matching_students)

            except ValueError:
                print("Invalid score. Please enter a number.")

        elif choice == "4":
            summary = compute_summary(students)

            print(f"\nTotal students: {summary['total']}")
            print(f"Passing students: {summary['passing']}")
            print(f"Average score: {summary['average_score']:.2f}")
            print(f"Highest score: {summary['highest_score']}")
            print(f"Lowest score: {summary['lowest_score']}")
            print(
                "Grade distribution: "
                f"{summary['grade_distribution']}"
            )

        elif choice == "5":
            if save_students(students, filename):
                print("Student records saved successfully.")
            else:
                print("Student records could not be saved.")

            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1–5.")


def main():
    """Load student records and start the session."""
    filename = "students.txt"

    students = load_students(filename)
    students = assign_grades(students)

    print(f"{len(students)} student record(s) loaded.")

    run_session(students, filename)


if __name__ == "__main__":
    main()
