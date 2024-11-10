from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate CGPA
def calculate_cgpa(grades):
    total_credit_hours = 0
    total_weighted_points = 0

    for grade in grades:
        grade_point = float(grade['grade_point'])
        credit_hours = float(grade['credit_hours'])

        total_credit_hours += credit_hours
        total_weighted_points += grade_point * credit_hours

    cgpa = total_weighted_points / total_credit_hours if total_credit_hours > 0 else 0
    return round(cgpa, 2)

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for CGPA calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    subjects = request.form.getlist('subject')
    grade_points = request.form.getlist('grade_point')
    credit_hours = request.form.getlist('credit_hours')

    # Prepare grades data
    grades = [
        {'subject': subjects[i], 'grade_point': grade_points[i], 'credit_hours': credit_hours[i]}
        for i in range(len(subjects))
    ]

    # Calculate CGPA
    cgpa = calculate_cgpa(grades)
    return render_template('index.html', cgpa=cgpa, grades=grades)

if __name__ == '__main__':
    app.run(debug=True)
