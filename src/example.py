def read_file():
    file_path = ""
    with open(file_path, 'r') as read_file:
        for line in read_file.readlines():
            pass


def write_file():
    data = [[1, 2, 3, 4], [5, 6, 7, 8]]
    file_path = ""
    with open(file_path, 'w') as write_file:
        for row in data:
            pass

