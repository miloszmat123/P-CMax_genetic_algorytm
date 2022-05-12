def data_reading(filename):
    file = open(filename, "r")
    tasks = []
    for line in file.readlines():
        tasks.append(int(line))
    file.close()
    number_of_processors = tasks[0]
    tasks = tasks[2:]
    return number_of_processors, tasks
