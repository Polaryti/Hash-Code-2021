city_plan = {}
streets = {}
car_path = {}

#simulacion = {}

mapa = {}

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


'''
    key: nodo del que sale
    value: tupla
        (nombre_calle, nodo_final, duración)

    Ej.: {2: [('rue-de-londres', 0, 1), ('rue-de-rome', 3, 2)], 0: [('rue-d-amsterdam', 1, 1)], 3: [('rue-d-athenes', 1, 1)], 1: [('rue-de-moscou', 2, 3)]}
'''
def hacer_mapa():
    for street in streets.items():
        if street[1]['B'] not in mapa:
            mapa[street[1]['B']] = [(street[0], street[1]['E'], street[1]['L'])]
        else:
            mapa[street[1]['B']].append((street[0], street[1]['E'], street[1]['L']))


'''
    key: id
    value: pos
'''
coches = {}
def posicionar_coches():
    for path in car_path.items():
        coches[path[0]] = streets[path[1]['streets'][0]]['E']
    

traffic_ligths = []
def realizar_simulación():
    # calles = set()
    # for path in car_path.values():
    #     for st in path['streets']:
    #         calles.add(st)
    

    
    # Por que intersecciones pasa el coche
    intersections = set()

    # algo = car_path.values()
    # print(algo.
    # for i in range(len(algo)):
    #     print(algo[i])

    for street in car_path.values():
        for i in street['streets']:
            for v in mapa.values():
                for k in v:
                    print(k)
                    if i == k[0]:
                        
                        #print(k[1])
                        intersections.add(k[1])
        
        #print(len(intersections))
        

    # inicios = set()
    # pasos = set()
    # for coche in coches.values():
    #     inicios.add(coche)
    
    # print(car_path)
    # for path in car_path.values():
    #     pasos.add(path['P'])
    # # print(len(coches.values()))
    # # print(len(aux))


simulacion = {
    'n_traffic_lights': 3,
    'intersections': [
        {
            'id': 1,
            'n_streets': 2,
            'strets': [('rue-d-athenes', 1), ('rue-d-amsterdam', 2)]
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


def write_file():
    with open('res.txt', 'w') as write_file:
        write_file.write(str(simulacion['n_traffic_lights']) + '\n')
        for intersection in simulacion['intersections']:
            write_file.write(str(intersection['id']) + '\n')
            write_file.write(str(intersection['n_streets']) + '\n')
            for street in intersection['strets']:
                write_file.write(str(street[0]) + ' ' + str(street[1]) + '\n')


    
if __name__ == "__main__":
    data_file = 'a.txt'
    read_file(r'C:\Users\Mario\Documents\GitHub\Hash-Code-2021\data\\' + data_file)
    hacer_mapa()
    posicionar_coches()
    realizar_simulación()
    write_file()