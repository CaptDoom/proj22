from flask import Flask, render_template, request

app = Flask(__name__)

#dictionary storing data of classrooms and schedule
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

#Logic defining empty class
def empty_classes(schedules, day, time_slot):
    null_classrooms = []
    for classroom, days in schedules.items():
        for day_key, times in days.items():
            if day_key == day:
                for time, value in times.items():
                    if time == time_slot and value == 0 and classroom not in null_classrooms:
                        null_classrooms.append(classroom)
    return null_classrooms

#Logic defining ongoing classes
def ongoing_classes(schedules, day, time_slot):
    ongoing_classrooms = []
    for classroom, days in schedules.items():
        for day_key, times in days.items():
            if day_key == day:
                for time, value in times.items():
                    if time == time_slot and value == 1 and classroom not in ongoing_classrooms:
                        ongoing_classrooms.append(classroom)
    return ongoing_classrooms

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        day = request.form['day']
        time_slot = request.form['time_slot']
        classrooms = empty_classes(classroom_schedules, day, time_slot)
        ongoing = ongoing_classes(classroom_schedules, day, time_slot)
        return render_template('index.html', day=day, time_slot=time_slot, classrooms=classrooms, ongoing=ongoing)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    