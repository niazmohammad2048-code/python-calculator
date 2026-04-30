# simple_cgpa_calculator.py

def calculate_cgpa():
    print("--- BUET CGPA Calculator ---")
    num_courses = int(input("How many course's result?: "))
    
    total_points = 0
    total_credits = 0
    
    for i in range(num_courses):
        print(f"\n course {i+1}:")
        credit = float(input("credit (ex: 3.0, 1.5): "))
        grade_point = float(input("grade point(ex: 4.0, 3.75): "))
        
        total_points += (credit * grade_point)
        total_credits += credit
        
    if total_credits == 0:
        print("credit can't be zero")
    else:
        cgpa = total_points / total_credits
        print(f"\n Total credit: {total_credits}")
        print(f"Your CGPA: {cgpa:.2f}")

if __name__ == "__main__":
    calculate_cgpa()