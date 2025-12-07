import random
from DM_project import Graph


def generate_erdos_renyi(num_vertices, density, weighted=True):

    graph = Graph()
    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            if random.random() <= density:

                if weighted:
                    weight = random.randint(1, 100)
                else:
                    weight = 1

                graph.add_edge(f'{u}', f'{v}', weight)



    return graph

graph = generate_erdos_renyi(5, 0.7)
print(graph.get_matrix())