classroom_schedules={
    '101': {
        'monday': {'0900': 0, '1100': 0, '1300': 1, '1500': 0, '1600': 1},
        'tuesday': {'0900': 1, '1200': 1, '1300': 1, '1500': 1, '1600': 0},
        'wednesday': {'0900': 0, '1100': 1, '1400': 0, '1500': 1, '1600': 1},
        'thursday': {'0900': 1, '1100': 0, '1300': 1, '1500': 0, '1600': 0},
        'friday': {'0900': 0, '1100': 1, '1300': 0, '1500': 1, '1600': 1},
        'saturday': {'0900': 1, '1100': 1, '1300': 0, '1500': 0, '1600': 1}
    },
    '102': {
        'monday': {'0900': 1, '1100': 0, '1300': 1, '1500': 0, '1600': 0},
        'tuesday': {'0900': 1, '1100': 1, '1300': 0, '1600': 1, '1600': 1},
        'wednesday': {'0900': 0, '1200': 1, '1300': 1, '1500': 0, '1600': 1},
        'thursday': {'1200': 1, '1300': 0, '1500': 0},
        'friday': {'0900': 1, '1700': 1, '1100': 1},
        'saturday': {'0900': 0, '1200': 1, '1300': 1, '1600': 1, '1600': 1}
    },
    '201': {
        'monday': {'0900': 0, '1100': 0, '1300': 1, '1500': 1, '1600': 0},
        'tuesday': {'0900': 1, '1100': 0, '1300': 0, '1500': 1, '1600': 1},
        'wednesday': {'0900': 0, '1100': 1, '1400': 0, '1500': 0, '1600': 1},
        'thursday': {'0900': 1, '1100': 0, '1300': 1, '1500': 0, '1600': 1},
        'friday': {'0900': 0, '1100': 1, '1300': 0, '1500': 1, '1600': 0},
        'saturday': {'0900': 1, '1100': 0, '1300': 1, '1500': 0, '1600': 1}
    },
    '202': {
        'monday': {'0900': 1, '1100': 0, '1300': 0, '1500': 1, '1600': 1},
        'tuesday': {'0900': 0, '1100': 1, '1300': 1, '1500': 0, '1600': 0},
        'wednesday': {'0900': 1, '1100': 0, '1400': 1, '1500': 1, '1600': 0},
        'thursday': {'0900': 0, '1100': 1, '1300': 0, '1500': 1, '1600': 0},
        'friday': {'0900': 1, '1100': 0, '1300': 1, '1500': 0, '1600': 1},
        'saturday': {'0900': 0, '1100': 1, '1300': 0, '1500': 1, '1600': 0}
    },
    '205': {
        'monday': {'0900': 1, '1100': 0, '1300': 1, '1500': 0, '1600': 1},
        'tuesday': {'0900': 0, '1100': 1, '1300': 0, '1500': 1, '1600': 0},
        'wednesday': {'0900': 1, '1100': 0, '1400': 1, '1500': 0, '1600': 0},
        'thursday': {'0900': 0, '1100': 1, '1300': 1, '1500': 0, '1600': 1},
        'friday': {'0900': 1, '1100': 0, '1300': 0, '1500': 1, '1600': 0},
        'saturday': {'0900': 0, '1100': 1, '1300': 1, '1500': 0, '1600': 1}
    }
}



def fetch_classrooms_with_value_zero(schedules, day, time_slot):
    classrooms_with_zero = []
    for classroom, days in schedules.items():
        for day_key, times in days.items():
            if day_key == day:
                for time, value in times.items():
                    if time == time_slot and value == 0 and classroom not in classrooms_with_zero:
                        classrooms_with_zero.append(classroom)
    return classrooms_with_zero

# Ask for day and time slot from the user
day = input("Enter the day: ")
time_slot = input("Enter the time slot: ")

# Fetch and print the classroom numbers with value 0 for the given day and time slot
classrooms = fetch_classrooms_with_value_zero(classroom_schedules, day, time_slot)
print(f"Classroom numbers with value 0 on {day} at {time_slot}: {classrooms}")


