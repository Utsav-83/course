from course import process_course_data

def test_default_course_data():
    result = process_course_data(["course.py"])
    assert result["learner"] == "Aarav"
    assert result["status"] == "Distinction"

def test_custom_course_data():
    args = [
        "course.py",
        "Meera",
        "Cloud Computing",
        "10",
        "60",
        "58",
        "55"
    ]
    result = process_course_data(args)
    assert result["average"] == 57.666666666666664
    assert result["status"] == "Completed"
