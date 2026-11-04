
def calculate_grade(marks):
    """Calculate grade based on student marks."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def get_valid_name():
    """Get a valid student name."""
    while True:
        name = input("Enter student name: ").strip()

        if not name:
            print("Error: Name cannot be empty.")
        elif not any(char.isalpha() for char in name):
            print("Error: Name must contain letters.")
        else:
            return name


def get_valid_marks():
    """Get marks between 0 and 100."""
    while True:
        try:
            marks_input = input("Enter marks (0-100): ").strip()
            marks = float(marks_input)

            if not 0 <= marks <= 100:
                print("Error: Marks must be between 0 and 100.")
            else:
                return marks

        except ValueError:
            print("Error: Please enter a valid number.")


def add_student(students):
    """Add a student to the records."""
    name = get_valid_name()

    if name.casefold() in (student["name"].casefold()
                           for student in students):
        print("Error: This student already exists.")
        return

    marks = get_valid_marks()

    student = {
        "name": name,
        "marks": marks,
        "grade": calculate_grade(marks)
    }

    students.append(student)
    print(f"Successfully added {name}!")


def display_results(students):
    """Display all student results."""
    if not students:
        print("\nNo student records available.")
        return

    print("\n" + "=" * 55)
    print(f"{'STUDENT RESULTS':^55}")
    print("=" * 55)

    print(f"{'Name':<25}{'Marks':<15}{'Grade':<10}")
    print("-" * 55)

    for student in students:
        print(
            f"{student['name']:<25}"
            f"{student['marks']:<15.2f}"
            f"{student['grade']:<10}"
        )

    print("=" * 55)

    average = sum(s["marks"] for s in students) / len(students)
    print(f"Total Students: {len(students)}")
    print(f"Class Average:  {average:.2f}")

    topper = max(students, key=lambda s: s["marks"])
    print(f"Top Student:    {topper['name']} ({topper['marks']:.2f})")


def main():
    students = []

    while True:
        print("\n===== STUDENT MARKS MANAGEMENT =====")
        print("1. Add Student")
        print("2. Display Results")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_results(students)

        elif choice == "3":
            print("Thank you! Exiting program.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
