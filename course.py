import sys

if len(sys.argv) == 7:
    learner = sys.argv[1]
    course = sys.argv[2]
    duration = sys.argv[3]
    a1 = int(sys.argv[4])
    a2 = int(sys.argv[5])
    a3 = int(sys.argv[6])
else:
    learner = "Aarav"
    course = "DevOps Fundamentals"
    duration = "12"
    a1, a2, a3 = 82, 88, 90

# Calculate average
average = (a1 + a2 + a3) / 3

if average >= 85:
    status = "Distinction"
elif average >= 70:
    status = "Successfully Completed"
elif average >= 55:
    status = "Completed"
elif average >= 40:
    status = "Partially Completed"
else:
    status = "Not Completed"

# Display details
print("Learner Name:", learner)
print("Course:", course)
print("Duration (weeks):", duration)
print("Assessment Scores:", a1, a2, a3)
print("Average Score:", average)
print("Completion Status:", status)