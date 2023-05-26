# STUDENT-DETAILS-GETTING-USING-PYTHON

The load_student_details function in student_data.py loads the student details from a file (e.g., CSV) and returns a list of Student objects. You can modify this function based on the file format you're using.
The get_students API in student_controller.py retrieves the paginated student details based on the provided page and page_size parameters.
The filter_students API in student_controller.py filters the student details based on the filter criteria sent from the UI.
The meets_filter_criteria function is a helper function that checks if a student object satisfies the given filter criteria.
You'll need to install the Flask framework (pip install flask) and the required dependencies. Then you can run the Python script, and the API endpoints will be available at http://localhost:5000/api/students and `http://localhost:5000/api
