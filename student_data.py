from student import Student

# Function to load student details from a file (CSV/JSON) and return a list of Student objects
def load_student_details(file_path):
    students = []
    # Code to load student details from the file and populate the 'students' list
    # You can use libraries like csv or json to handle file operations

    # Example:
    with open(file_path, 'r') as file:
        # Assuming CSV format with 'id', 'name', and 'total_marks' columns
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            total_marks = int(row['total_marks'])
            student = Student(id, name, total_marks)
            students.append(student)

    return students
