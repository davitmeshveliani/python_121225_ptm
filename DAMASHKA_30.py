import json
from datetime import datetime
from collections import Counter

try:
    with open('student_courses.json', 'r') as f:
        students = json.load(f)
        ages = []
    all_courses = []
    for s in students:
        birth = datetime.strptime(s['birth_date'], '%d.%m.%Y')
        enroll = datetime.strptime(s['enrollment_date'], '%d.%m.%Y')
        age = enroll.year - birth.year
        if (enroll.month, enroll.day) < (birth.month, birth.day):
            age -= 1
        ages.append(age)
        all_courses = [course for s in students for course in s['courses']]

    report = {
        "total_students": len(students),
        "average_enrollment_age": round(sum(ages) / len(ages), 1) if ages else 0,
         "students_per_course": dict(sorted(Counter(all_courses).items()))
    }

except FileNotFoundError:
    raise FileNotFoundError("file_no_found_student_courses.json")
except Exception as e:
    raise Exception(e)
with open('student_courses_report.json', 'w') as f:
    json.dump(report, f, indent=4)
print(f"(student_courses_report.json):\n{json.dumps(report, indent=4)}")
