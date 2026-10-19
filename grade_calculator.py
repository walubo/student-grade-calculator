"""
Student Grade Calculator
Author: Aries R. Magto
Description: A console application to compute student course grades and evaluation remarks.
"""

from typing import List, Tuple


def calculate_average(scores: List[float]) -> float:
    """Calculate the arithmetic mean of given scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def determine_grade_and_status(average: float) -> Tuple[str, str]:
    """
    Determine letter grade and passing status based on standard academic scale.
    
    Grading Scale:
    - 90 - 100 : A (Excellent)
    - 80 - 89.9: B (Good)
    - 75 - 79.9: C (Satisfactory)
    - 70 - 74.9: D (Conditional / Needs Improvement)
    - Below 70 : F (Failed)
    """
    if average >= 90.0:
        return "A", "Passed (Excellent)"
    elif average >= 80.0:
        return "B", "Passed (Good)"
    elif average >= 75.0:
        return "C", "Passed (Satisfactory)"
    elif average >= 70.0:
        return "D", "Passed (Conditional)"
    else:
        return "F", "Failed"


def display_report(student_name: str, subject_scores: List[Tuple[str, float]]) -> None:
    """Print a formatted grade summary card."""
    print("\n" + "=" * 50)
    print("             STUDENT GRADE REPORT")
    print("=" * 50)
    print(f"Student Name: {student_name}")
    print("-" * 50)
    print(f"{'Subject':<30} {'Score':>15}")
    print("-" * 50)

    for subject, score in subject_scores:
        print(f"{subject:<30} {score:>15.2f}")

    scores_only = [score for _, score in subject_scores]
    avg = calculate_average(scores_only)
    letter, remark = determine_grade_and_status(avg)

    print("-" * 50)
    print(f"{'Overall Average:':<30} {avg:>15.2f}")
    print(f"{'Letter Grade:':<30} {letter:>15}")
    print(f"{'Academic Remark:':<30} {remark:>15}")
    print("=" * 50)


def main() -> None:
    print("Welcome to the Student Grade Calculator!\n")
    student_name = input("Enter student name: ").strip()
    if not student_name:
        student_name = "Anonymous Student"

    subjects = ["Programming 1", "Data Structures", "Discrete Mathematics", "Technical Writing"]
    records: List[Tuple[str, float]] = []

    for subj in subjects:
        raw_val = input(f"Enter grade for {subj} (0-100): ")
        try:
            score = float(raw_val)
        except ValueError:
            score = 0.0
        records.append((subj, score))

    display_report(student_name, records)


if __name__ == "__main__":
    main()
