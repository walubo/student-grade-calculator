"""
Student Grade Calculator
Author: Aries R. Magto
Description: A console application to compute student course grades, GPA equivalents,
             and evaluation remarks with robust input validation.
"""

from typing import List, Tuple


def get_valid_score(prompt: str) -> float:
    """Prompt the user for a numeric score between 0 and 100 with validation."""
    while True:
        user_input = input(prompt).strip()
        try:
            score = float(user_input)
            if 0.0 <= score <= 100.0:
                return score
            print("  [Error] Score must be between 0.0 and 100.0. Please try again.")
        except ValueError:
            print("  [Error] Invalid input. Please enter a numerical score.")


def calculate_average(scores: List[float]) -> float:
    """Calculate the arithmetic mean of given scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def determine_grade_and_status(average: float) -> Tuple[str, str, float]:
    """
    Determine letter grade, passing status, and college GPA equivalent.
    
    Grading Scale:
    - 90 - 100 : A | GPA 4.0 | Passed (Excellent / President's List)
    - 85 - 89.9: B+ | GPA 3.5 | Passed (Very Satisfactory / Dean's List)
    - 80 - 84.9: B  | GPA 3.0 | Passed (Good)
    - 75 - 79.9: C  | GPA 2.5 | Passed (Fair / Satisfactory)
    - 70 - 74.9: D  | GPA 2.0 | Passed (Conditional / Remediable)
    - Below 70 : F  | GPA 0.0 | Failed
    """
    if average >= 90.0:
        return "A", "Passed (Excellent - President's List)", 4.0
    elif average >= 85.0:
        return "B+", "Passed (Very Satisfactory - Dean's List)", 3.5
    elif average >= 80.0:
        return "B", "Passed (Good)", 3.0
    elif average >= 75.0:
        return "C", "Passed (Fair / Satisfactory)", 2.5
    elif average >= 70.0:
        return "D", "Passed (Conditional)", 2.0
    else:
        return "F", "Failed", 0.0


def display_report(student_name: str, subject_scores: List[Tuple[str, float]]) -> None:
    """Print a formatted grade summary card."""
    print("\n" + "=" * 65)
    print("                     STUDENT GRADE REPORT")
    print("=" * 65)
    print(f" Student Name : {student_name}")
    print(f" Total Courses: {len(subject_scores)}")
    print("-" * 65)
    print(f" {'Course / Subject':<40} {'Score':>12} {'Status':>8}")
    print("-" * 65)

    for subject, score in subject_scores:
        status_tag = "PASS" if score >= 75.0 else "FAIL"
        print(f" {subject:<40} {score:>12.2f} {status_tag:>8}")

    scores_only = [score for _, score in subject_scores]
    avg = calculate_average(scores_only)
    letter, remark, gpa = determine_grade_and_status(avg)

    print("-" * 65)
    print(f" {'Overall Average':<40} {avg:>12.2f}")
    print(f" {'Letter Grade':<40} {letter:>12}")
    print(f" {'Grade Point Average (GPA)':<40} {gpa:>12.1f}")
    print(f" {'Academic Standing':<40} {remark:>12}")
    print("=" * 65)


def main() -> None:
    print("=" * 65)
    print("          WELCOME TO STUDENT GRADE CALCULATOR")
    print("=" * 65)
    student_name = input("Enter student full name: ").strip()
    if not student_name:
        student_name = "Anonymous Student"

    default_subjects = [
        "Programming 1 (Python)",
        "Data Structures & Algorithms",
        "Discrete Mathematics",
        "Information Management",
        "Technical Communication",
    ]

    print(f"\nEvaluating grades for {student_name}:")
    print("Enter the score (0-100) for each course below.\n")

    records: List[Tuple[str, float]] = []
    for subj in default_subjects:
        score = get_valid_score(f"Enter score for [{subj}]: ")
        records.append((subj, score))

    display_report(student_name, records)


if __name__ == "__main__":
    main()
