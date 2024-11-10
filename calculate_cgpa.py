def calculate_cgpa():
    total_credit_hours = 0
    total_weighted_points = 0

    num_subjects = int(input("Enter the number of subjects: "))

    for i in range(num_subjects):
        print(f"\nSubject {i+1}:")
        grade_point = float(input("Enter the grade point (e.g., 4.0, 3.7, etc.): "))
        credit_hours = float(input("Enter the credit hours for this subject: "))

        # Update total credit hours and weighted points
        total_credit_hours += credit_hours
        total_weighted_points += grade_point * credit_hours

    # Calculate CGPA
    cgpa = total_weighted_points / total_credit_hours
    return round(cgpa, 2)

# Run the program
cgpa = calculate_cgpa()
print("\nYour CGPA is:", cgpa)
