import random

class DSU:                                            #Клас для операцій з непересічними множинами був згенерований за допомогою ШІ
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1

class Graph:
    def __init__(self):
        self.graph = dict()

    def add_node(self, node):
        if type(node) != str:
            raise TypeError("Nodes' name should be string")
        if node in self.graph:
            raise ValueError("Such node is already exist")
        self.graph[node] = dict()

    def add_edge(self, first_node, second_node, weight):
        if not first_node in self.graph:
            self.add_node(first_node)
        if not second_node in self.graph:
            self.add_node(second_node)
        if first_node == second_node:
            raise ValueError("First node and second node should be different")
        self.graph[first_node][second_node] = weight
        self.graph[second_node][first_node] = weight

    def remove_edge(self, first_node, second_node):
        if not first_node in self.graph:
            raise ValueError(f"There is no {first_node} node in graph")
        if not second_node in self.graph:
            raise ValueError(f"There is no {second_node} node in graph")
        if first_node == second_node:
            raise ValueError("First node and second node should be different")
        if not second_node in self.graph[first_node]:
            raise ValueError(f"There is no edge between {first_node} and {second_node}")
        del self.graph[first_node][second_node]
        del self.graph[second_node][first_node]

    def remove_node(self, node):
        if type(node) != str:
            raise TypeError("Nodes' name should be string")
        if not node in self.graph:
            raise ValueError("Such node doesn't exist")
        del self.graph[node]

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def remove_nodes(self, nodes):
        for node in nodes:
            self.remove_node(node)

    def add_edges(self, edges):
        for first_node, second_node, weight in edges:
            self.add_edge(first_node, second_node, weight)

    def remove_edges(self, edges):
        for first_node, second_node, weight in edges:
            self.remove_edge(first_node, second_node)

    def clear(self):
        self.graph = {}

    def clear_edges(self):
        for node in self.graph:
            self.graph[node] = {}

    def get_weight(self, first_node, second_node):
        if not first_node in self.graph:
            raise ValueError(f"There is no {first_node} node in graph")
        if not second_node in self.graph:
            raise ValueError(f"There is no {second_node} node in graph")
        if first_node == second_node:
            raise ValueError("First node and second node should be different")
        if not second_node in self.graph[first_node]:
            raise ValueError(f"There is no edge between {first_node} and {second_node}")
        weight = self.graph[first_node][second_node]
        return weight

    def get_size(self):
        size = 0
        for node in self.graph:
            size += len(self.graph[node])
        size /= 2
        size = int(size)
        return size

    def get_min_edge(self, connected_component):
        for node in connected_component:
            if type(node) != str:
                raise TypeError("Nodes' name should be string")
            if not node in self.graph:
                raise ValueError("Such node doesn't exist")
        min_connected_edge = ("error", "error", float("inf"))
        for node in connected_component:
            edges = self.graph[node].items()
            if not edges:
                continue
            min_weight = tuple([node]) + min(edges, key=lambda x: x[1])
            if min_weight[2] < min_connected_edge[2]:
                min_connected_edge = min_weight
        return min_connected_edge

    def get_connected_component(self, node, connected_dict=None):
        if connected_dict is None:
            connected_dict = {}
            if type(node) != str:
                raise TypeError("Nodes' name should be string")
            if not node in self.graph:
                raise ValueError("Such node doesn't exist")
            connected_dict[node] = True
        for node in self.graph[node]:
            if not node in connected_dict:
                connected_dict[node] = False
        connected_nodes = list(connected_dict.keys()).copy()
        for node in connected_nodes:
            if node in connected_dict:
                continue
            self.get_connected_component(node, connected_dict)
        connected_nodes = tuple(connected_dict.keys())
        return connected_nodes


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


def boruvka_algorythm(graph_object: Graph):
    mst = Graph()
    mst.add_nodes(graph_object.graph.keys())
    nodes_num = len(graph_object.graph)
    connected_component = DSU(graph_object.graph.keys())
    while mst.get_size() < nodes_num - 1:
        min_edge_per_comp = {}
        for node in mst.graph.keys():
            node_comp = connected_component.find(node)
            if not node_comp in min_edge_per_comp:
                min_edge_per_comp[node_comp] = ("error", "error", float("inf"))
            for neighbour in graph_object.graph[node]:
                nb_comp = connected_component.find(neighbour)
                if not nb_comp in min_edge_per_comp:
                    min_edge_per_comp[nb_comp] = ("error", "error", float("inf"))
                if nb_comp == node_comp:
                    continue
                if graph_object.graph[node][neighbour] < min_edge_per_comp[node_comp][2]:
                    min_edge_per_comp[node_comp] = (min(node, neighbour), max(node, neighbour), graph_object.graph[node][neighbour])
                if graph_object.graph[node][neighbour] < min_edge_per_comp[nb_comp][2]:
                    min_edge_per_comp[nb_comp] = (min(node, neighbour), max(node, neighbour), graph_object.graph[node][neighbour])
        for first_node, second_node, weight in min_edge_per_comp.values():
            if connected_component.find(first_node) != connected_component.find(second_node):
                connected_component.union(first_node, second_node)
                mst.add_edges([(first_node, second_node, weight)])
    return mst
