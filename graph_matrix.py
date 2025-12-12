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
    target_graph.nodes_list = []
    target_graph.parent = []
    target_graph.rank = []
    for i in range(num_vertices):
        target_graph.matrix.append([float('inf')] * num_vertices)
        target_graph.parent.append(i)
        target_graph.rank.append(0)
        target_graph.nodes_list.append(i)
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
        self.rank = []
        self.parent = []


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
            self.parent.append(new_size - 1)
            self.rank.append(0)
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
            column_index_in_row = row.index(column)
            del row[column_index_in_row]

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

    def find_component(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find_component(self.parent[i])
        return self.parent[i]

    def union_sets(self, i, j):
        root_i = self.find_component(i)
        root_j = self.find_component(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

    def reset_dsu(self):
        num_vertices = len(self.matrix)
        self.parent = list(range(num_vertices))
        self.rank = [0] * num_vertices

def boruvka_mst(graph_obj):
    num_vertices = len(graph_obj.matrix)
    mst_result = MatrixGraph()

    for node in graph_obj.nodes_list:
        mst_result.add_node(node)

    graph_obj.reset_dsu()

    num_components = num_vertices
    total_weight = 0

    while num_components > 1:
        cheapest = [None] * num_vertices

        for u in range(num_vertices):
            for v in range(u + 1, num_vertices):
                w = graph_obj.matrix[u][v]
                if w != float('inf'):
                    set_u = graph_obj.find_component(u)
                    set_v = graph_obj.find_component(v)

                    if set_u != set_v:
                        if cheapest[set_u] is None or cheapest[set_u][2] > w:
                            cheapest[set_u] = [u, v, w]
                        if cheapest[set_v] is None or cheapest[set_v][2] > w:
                            cheapest[set_v] = [u, v, w]

        edges_added = 0
        for i in range(num_vertices):
            if cheapest[i] is not None:
                u, v, w = cheapest[i]
                if graph_obj.union_sets(u, v):

                    name_u = graph_obj.nodes_list[u]
                    name_v = graph_obj.nodes_list[v]
                    mst_result.add_edge(name_u, name_v, w)

                    total_weight += w
                    num_components -= 1
                    edges_added += 1


        if edges_added == 0:
            break


    return mst_result.matrix, total_weight




m = MatrixGraph()
generate_erdos_renyi_matrix(m, 4, 0.8)

boruvka_mst(m)




