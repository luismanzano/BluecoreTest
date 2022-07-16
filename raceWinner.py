from datetime import timedelta

def race_winner(input):
    best_time = float("inf")
    second_time = float("inf")
    winner_name = ""

    for element in input:

        if element["time"] != 'dnf':
            time = get_seconds(element["time"])
            if time < best_time:
                second_time = best_time
                best_time = time
                winner_name = element["name"]
            elif time < second_time:
                second_time = time

    if best_time == "inf":
        return "There is no winner"

    if second_time == "inf":
        return f'{winner_name} won by no contest'

    mins, secs = divmod(second_time-best_time, 60)

    hours, mins = divmod(mins, 60)

    return f'{winner_name} won by {hours} hours, {mins}, minutes, {secs} seconds'






def get_seconds(string):
    h, m, s = string.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


if __name__ == '__main__':

    example_input = [
        {
            'name': 'Samuel',
            'time': '5:42:14'
        },
        {
            'name': 'Fred',
            'time': '5:12:53'
        },
        {
            'name': 'Cynthia',
            'time': 'dnf'
        }
    ]

    print(race_winner(example_input))
