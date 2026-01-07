def process_course_data(args):
    # Defaults
    learner_name = "Aarav"
    course = "DevOps Fundamentals"
    duration = 12
    scores = [82, 88, 90]

    # Custom CLI args
    if len(args) > 1:
        learner_name = args[1]
        course = args[2]
        duration = int(args[3])
        scores = list(map(int, args[4:]))

    average = sum(scores) / len(scores)

    if average >= 85:
        status = "Distinction"
    elif average >= 60:
        status = "Pass"
    else:
        status = "Fail"

    return {
        "learner": learner_name,
        "course": course,
        "duration": duration,
        "scores": scores,
        "average": average,
        "status": status
    }


if __name__ == "__main__":
    import sys
    data = process_course_data(sys.argv)

    print("Learner Name:", data["learner"])
    print("Course:", data["course"])
    print("Duration (weeks):", data["duration"])
    print("Assessment Scores:", *data["scores"])
    print("Average Score:", data["average"])
    print("Completion Status:", data["status"])
