city_plan = {}
streets = {}
car_path = {}

simulacion = {}

def read_file(file_path):
    with open(file_path, 'r') as read_file:
        plan = read_file.readline().strip().split(' ')
        city_plan['D'] = int(plan[0])
        city_plan['I'] = int(plan[1])
        city_plan['S'] = int(plan[2])
        city_plan['V'] = int(plan[3])
        city_plan['F'] = int(plan[4])

        for _ in range(city_plan['S']):
            street = read_file.readline().strip().split(' ')
            aux = {
                'B': int(street[0]),
                'E': int(street[1]),
                'L': int(street[3])
            }
            streets[street[2]] = aux
        
        for i in range(city_plan['V']):
            path = read_file.readline().strip().split(' ')
            car_path[i] = {
                'P': int(path[0]),
                'streets': path[1:]
            }

def la_logica():
    pass

'''
simulacion = {
    'n_traffic_lights': 3,
    'intersections': [
        {
            'id': 1,
            'n_streets': 2,
            'strets': [('rue-d-athenes', 2), ('rue-d-amsterdam', 1)]
        },
        {
            'id': 0,
            'n_streets': 1,
            'strets': [('rue-de-londres', 2)]
        },
        {
            'id': 2,
            'n_streets': 1,
            'strets': [('rue-de-moscou', 1)]
        }
    ]
}
'''

def write_file():
    with open('res.txt', 'w') as write_file:
        write_file.write(str(simulacion['n_traffic_lights']) + '\n')
        for intersection in simulacion['intersections']:
            write_file.write(str(intersection['id']) + '\n')
            write_file.write(str(intersection['n_streets']) + '\n')
            for street in intersection['strets']:
                write_file.write(str(street[0]) + ' ' + str(street[1]) + '\n')

    
if __name__ == "__main__":
    data_file = 'b.txt'
    read_file(r'C:\Users\Mario\Documents\GitHub\Hash-Code-2021\data\\' + data_file)
    la_logica()
    write_file()