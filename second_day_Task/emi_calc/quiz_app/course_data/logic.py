import csv
from statistics import mean

# Load data from course.csv
def load_data(filename='B:/bhema/Workkspace-python/second_day_Task/emi_calc/quiz_app/course_data/course.csv'):
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    # Convert some fields to appropriate types
    for row in data:
        row['Score'] = float(row['Score'])
    return data

# 1. Get all students by qualification
def by_qualification(data, qualification):
    return [r for r in data if r['Qualification'] == qualification]

# 2. Count students by qualification
def count_by_qualification(data):
    counts = {}
    for r in data:
        q = r['Qualification']
        counts[q] = counts.get(q, 0) + 1
    return counts

# 3. Count students who got placed
def count_placed(data):
    return sum(1 for r in data if r['Placed'] == 'Y')

# 4. Count students who completed but not placed
def count_completed_not_placed(data):
    return sum(1 for r in data if r['Completed'] == 'Y' and r['Placed'] == 'N')

# 5. Count placed vs not placed
def placed_vs_not(data):
    placed = sum(1 for r in data if r['Placed'] == 'Y')
    not_placed = sum(1 for r in data if r['Placed'] == 'N')
    return {'Placed': placed, 'Not Placed': not_placed}

# 6. Search student by name
def search_by_name(data, name):
    name = name.strip().upper()
    return [r for r in data if r['Name'] == name]

# 7. Average success rate of a batch (placed / completed)
def batch_success_rate(data, batch):
    batch_data = [r for r in data if r['Batch'] == batch]
    if not batch_data:
        return None
    completed = sum(1 for r in batch_data if r['Completed'] == 'Y')
    placed = sum(1 for r in batch_data if r['Placed'] == 'Y')
    return (placed / completed * 100) if completed > 0 else 0

# 8. Student(s) with max score
def max_score_students(data):
    max_score = max(r['Score'] for r in data)
    return [r for r in data if r['Score'] == max_score]

# 9. Get all student names
def all_names(data):
    return [r['Name'] for r in data]

# 10. Names, qualification, score
def names_qual_score(data):
    return [(r['Name'], r['Qualification'], r['Score']) for r in data]

def menu():
    print("""
Select an option (1–10):
 1. List students by qualification
 2. Count students by qualification
 3. Count placed students
 4. Count completed but not placed
 5. Count placed vs not placed
 6. Search student by name
 7. Batch success rate
 8. Student(s) with max percentage
 9. All student names
10. Names, qualification, score
 0. Exit
""")

def main():
    data = load_data()
    while True:
        menu()
        choice = input("Enter option: ").strip()
        if choice == '0':
            print("Goodbye!")
            break

        if choice == '1':
            qual = input("Enter qualification (e.g. BE, MCA): ").strip()
            result = by_qualification(data, qual)
            print(f"\nStudents with qualification {qual}:")
            for r in result:
                print(r)
        elif choice == '2':
            counts = count_by_qualification(data)
            print("\nCount by qualification:")
            for q, cnt in counts.items():
                print(f"{q}: {cnt}")
        elif choice == '3':
            print("\nTotal placed students:", count_placed(data))
        elif choice == '4':
            print("\nCompleted but not placed:", count_completed_not_placed(data))
        elif choice == '5':
            counts = placed_vs_not(data)
            print("\nPlaced vs Not Placed:")
            for k, v in counts.items():
                print(f"{k}: {v}")
        elif choice == '6':
            name = input("Enter student name (last name in uppercase): ").strip()
            results = search_by_name(data, name)
            if results:
                print("\nSearch results:")
                for r in results:
                    print(r)
            else:
                print(f"No student named '{name}' found.")
        elif choice == '7':
            batch = input("Enter batch (e.g. BCJ1, BCJ2): ").strip()
            rate = batch_success_rate(data, batch)
            if rate is None:
                print(f"No records for batch '{batch}'.")
            else:
                print(f"\nBatch {batch} success rate: {rate:.2f}%")
        elif choice == '8':
            top = max_score_students(data)
            print("\nStudent(s) with maximum score:")
            for r in top:
                print(r)
        elif choice == '9':
            names = all_names(data)
            print("\nAll student names:")
            print("\n".join(names))
        elif choice == '10':
            info = names_qual_score(data)
            print("\nName | Qualification | Score")
            for name, qual, score in info:
                print(f"{name} | {qual} | {score}")
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
