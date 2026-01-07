def process_course_data(learner_name, course, duration, scores):
    average = sum(scores) / len(scores)

    if average >= 85:
        status = "Distinction"
    elif average >= 60:
        status = "Pass"
    else:
        status = "Fail"

    return {
        "learner_name": learner_name,
        "course": course,
        "duration": duration,
        "scores": scores,
        "average": average,
        "status": status
    }


if __name__ == "__main__":
    data = process_course_data(
        "Aarav",
        "DevOps Fundamentals",
        12,
        [82, 88, 90]
    )

    print("Learner Name:", data["learner_name"])
    print("Course:", data["course"])
    print("Duration (weeks):", data["duration"])
    print("Assessment Scores:", *data["scores"])
    print("Average Score:", data["average"])
    print("Completion Status:", data["status"])
