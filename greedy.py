def pc_max_greedy_algorithm(number_of_processors, tasks):
    schedule = [0 for _ in range(number_of_processors)]

    for task in tasks:
        schedule[0] += task
        schedule = insert_sort_first_element(schedule)
        # print(schedule)

    return schedule[-1]


def insert_sort_first_element(schedule):
    for i in range(0, len(schedule) - 1):
        if schedule[i] <= schedule[0] <= schedule[i + 1]:
            schedule.insert(i + 1, schedule[0])
            break
    else:
        schedule.append(schedule[0])
    schedule = schedule[1:]
    return schedule


def main():
    number_of_processors = int(input("Number of processors: "))
    tasks = [int(x) for x in input("Tasks: ").strip().split(" ")]
    print(pc_max_greedy_algorithm(number_of_processors, tasks))


if __name__ == '__main__':
    main()
