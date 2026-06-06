"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    student_scores = {}
    for record in records:
        name = record['name']
        score = record['score']
        if name not in student_scores:
            student_scores[name] = []
        student_scores[name].append(score)
    averages = {}
    for name, scores in student_scores.items():
        avg = sum(scores) / len(scores)
        averages[name] = round(avg, 2)
    return averages


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    return {record['subject'] for record in records}


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    averages = average_per_student(records)
    name, avg = max(averages.items(), key=lambda item: item[1])
    return name, avg


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    averages = average_per_student(records)
    passing = [name for name, avg in averages.items() if avg >= threshold]
    return sorted(passing)

