classes = {
    "object oriented programming": 82,
    "modern physics": 50,
    "linear algebra": 86,
    "discreate mathematics": 82,
    "User Interface Design": 66,
    "manufacturing Practice": 54,
    "Glimpses of glorious India": 50
}

def main():
    print("Available subjects:")
    for subject in classes:
        print(f"- {subject}")
    subject = input("Enter the subject: ")
    
    if subject not in classes:
        print("Invalid subject. Please try again.")
        return
    
    try:
        current_total_happened = int(input("Enter total classes that have happened so far: "))
        classes_attended = int(input("Enter classes you have attended so far: "))
        future_absences = int(input("Enter classes you will be absent for in the future: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return
    
    end_of_course_total = classes[subject]
    remaining_classes = end_of_course_total - current_total_happened
    total_attended_end = classes_attended + (remaining_classes - future_absences)
    final_attendance_percentage = (total_attended_end / end_of_course_total) * 100
    print(f"\nSuggestion 1: Your attendance at the end of the course will be {final_attendance_percentage:.2f}%.")
    
    total_absences = (current_total_happened - classes_attended) + future_absences
    required_attended_75 = 3 * total_absences
    additional_classes_needed = max(0, required_attended_75 - classes_attended)
    print(f"Suggestion 2: To achieve 75% attendance attend {additional_classes_needed:.1f} more classes.")

if __name__ == "__main__":
    main() 
    