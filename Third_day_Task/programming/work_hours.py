def get_work_hours(day):
    # Timetable data (rows = people, columns = days Mon to Sun)
    timetable = [
        [3, 3, 3, 3, 3, 3, 0],
        [2, 2, 2, 2, 2, 1, 0],
        [2, 2, 2, 1, 1, 0, 0]
    ]
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


    if day not in days:
        return "Invalid day input."


    index = days.index(day)
    
    work_hours = [row[index] for row in timetable]

    return work_hours

user_day = input("Enter the day (e.g., Mon, Tue, Wed, Thu,..): ")

result = get_work_hours(user_day)

print("Work hours for", user_day, ":", result)

    