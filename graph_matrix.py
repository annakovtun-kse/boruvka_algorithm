import random

def generate_erdos_renyi(target_graph, num_vertices, density, weighted=True):
    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            if random.random() <= density:

                if weighted:
                    weight = random.randint(1, 100)
                else:
                    weight = 1

                target_graph.add_edge(f'{u}', f'{v}', weight)
    return target_graph

def generate_erdos_renyi_matrix(target_graph, num_vertices, density, weighted=True):
    target_graph.matrix = []
    for i in range(num_vertices):
        target_graph.matrix.append([float('inf')] * num_vertices)
    weight = 1
    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            if random.random() <= density:
                if weighted:
                    weight = random.randint(1, 100)
                target_graph.matrix[v][u] = weight
                target_graph.matrix[u][v] = weight

    return target_graph.matrix

class MatrixGraph:
    def __init__(self):
        self.matrix = []
        self.nodes_list = []

    def add_node(self, node):
        new_size = len(self.nodes_list) + 1
        if type(node) != str and type(node) != int:
            raise ValueError('Name of the node should be an str or int')
        if node in self.nodes_list:
            return self.matrix
        else:
            self.nodes_list.append(node)
            for row in self.matrix:
                row.append(float('inf'))

            new_row = [float('inf')] * new_size
            self.matrix.append(new_row)
            return self.matrix

    def add_edge(self, node_1, node_2, weight=1):
        if type(node_1) != str and type(node_1) != int:
            raise ValueError('Name of the first node should be an str or int')
        if type(node_2) != str and type(node_2) != int:
            raise ValueError('Name of the second node should be an str or int')

        if node_1 not in self.nodes_list:
            self.add_node(node_1)
        if node_2 not in self.nodes_list:
            self.add_node(node_2)
            
        node_1_id = self.nodes_list.index(node_1)
        node_2_id = self.nodes_list.index(node_2)
        if weight != 1:
            self.matrix[node_1_id][node_2_id] = weight
            self.matrix[node_2_id][node_1_id] = weight
        else:
            self.matrix[node_1_id][node_2_id] = 1
            self.matrix[node_2_id][node_1_id] = 1

        return self.matrix

    def remove_node(self, node):
        if type(node) != str and type(node) != int:
            raise ValueError('Name of the node should be an str or int')

        if node not in self.nodes_list:
            return self.matrix

        node_index = self.nodes_list.index(node)
        for row in self.matrix:
            column = row[node_index]
            row.remove(column)

        self.nodes_list.remove(node)
        self.matrix.remove(self.matrix[node_index])
        return self.matrix


    def remove_edge(self, node_1, node_2):
        if type(node_1) != str and type(node_1) != int:
            raise ValueError('Name of the first node should be an str or int')
        if type(node_2) != str and type(node_2) != int:
            raise ValueError('Name of the second node should be an str or int')

        if node_1 not in self.nodes_list or node_2 not in self.nodes_list:
            raise ValueError('Node does not exist')

        node_1_index = self.nodes_list.index(node_1)
        node_2_index = self.nodes_list.index(node_2)
        self.matrix[node_1_index][node_2_index] = float('inf')
        self.matrix[node_2_index][node_1_index] = float('inf')
        return self.matrix

m = MatrixGraph()

m.add_edge('1', '2', 3)
m.add_edge('3', '4', 8)
for row_0 in m.matrix:
    print(row_0)

m.remove_node('1')

print('\n' * 3)

for row_0 in m.matrix:
    print(row_0)

m.remove_edge('3', '4')

print('\n' * 3)

for row_0 in m.matrix:
    print(row_0)

generate_erdos_renyi_matrix(m, 3, 1)

print('\n' * 3)
for row_0 in m.matrix:
    print(row_0)