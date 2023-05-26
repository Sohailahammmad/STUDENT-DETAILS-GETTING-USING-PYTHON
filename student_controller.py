from flask import Flask, request, jsonify
from student_data import load_student_details

app = Flask(__name__)

# Load student details from the file (assuming 'students.csv' as the file path)
students = load_student_details('students.csv')

@app.route('/api/students', methods=['GET'])
def get_students():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))

    start_index = (page - 1) * page_size
    end_index = min(start_index + page_size, len(students))

    paginated_students = students[start_index:end_index]

    return jsonify(paginated_students)

@app.route('/api/students/filter', methods=['POST'])
def filter_students():
    filter_criteria = request.json

    filtered_students = []
    for student in students:
        if meets_filter_criteria(student, filter_criteria):
            filtered_students.append(student)

    return jsonify(filtered_students)

def meets_filter_criteria(student, criteria):
    if 'id' in criteria and student.id != criteria['id']:
        return False

    if 'name' in criteria and criteria['name'] not in student.name:
        return False

    if 'min_total_marks' in criteria and student.total_marks < criteria['min_total_marks']:
        return False

    if 'max_total_marks' in criteria and student.total_marks > criteria['max_total_marks']:
        return False

    return True

if __name__ == '__main__':
    app.run()
