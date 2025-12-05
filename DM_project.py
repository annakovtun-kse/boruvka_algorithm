import timeit
class Graph:
    def __init__(self):
        self.nodes_list = []
        self.graph = []

    def add_node(self, node: str):
        if type(node) != str:
            raise TypeError("Nodes' name should be string")
        if node in self.nodes_list:
            raise ValueError("Such node is already exist")
        self.nodes_list.append(node)
        self.graph.append(dict())

    def add_edge(self, first_node, second_node, weight):
        if not first_node in self.nodes_list:
            raise ValueError(f"There is no {first_node} node in graph")
        if not second_node in self.nodes_list:
            raise ValueError(f"There is no {second_node} node in graph")
        if first_node == second_node:
            raise ValueError("First node and second node should be different")
        first_node_index = self.nodes_list.index(first_node)
        second_node_index = self.nodes_list.index(second_node)
        self.graph[first_node_index].update({second_node: weight})
        self.graph[second_node_index].update({first_node: weight})

    def remove_edge(self, first_node, second_node):
        if not first_node in self.nodes_list:
            raise ValueError(f"There is no {first_node} node in graph")
        if not second_node in self.nodes_list:
            raise ValueError(f"There is no {second_node} node in graph")
        if first_node == second_node:
            raise ValueError("First node and second node should be different")
        first_node_index = self.nodes_list.index(first_node)
        second_node_index = self.nodes_list.index(second_node)
        if not second_node in self.graph[first_node_index].keys():
            raise ValueError(f"There is no edge between {first_node} and {second_node}")
        del self.graph[first_node_index][second_node]
        del self.graph[second_node_index][first_node]

    def remove_node(self, node):
        if type(node) != str:
            raise TypeError("Nodes' name should be string")
        if not node in self.nodes_list:
            raise ValueError("Such node doesn't exist")
        node_index = self.nodes_list.index(node)
        local_nodes_list = set(self.graph[node_index].keys()).copy()
        for i in local_nodes_list:
            self.remove_edge(node, i)
        del self.graph[node_index]
        del self.nodes_list[node_index]

    def add_nodes(self, *args):
        for node in args:
            self.add_node(node)

    def remove_nodes(self, *args):
        for node in args:
            self.remove_node(node)

    def add_edges(self, *args):
        for first_node, second_node, weight in args:
            self.add_edge(first_node, second_node, weight)

    def remove_edges(self, *args):
        for first_node, second_node in args:
            self.remove_edge(first_node, second_node)

    def clear(self):
        self.nodes_list = []
        self.graph = []

    def clear_edges(self):
        self.graph = [{} for i in range(len(self.nodes_list))]

    def get_matrix(self):
        _ = float("inf")
        matrix = []
        nodes_number = len(self.nodes_list)
        for i in self.nodes_list:
            matrix.append([_] * nodes_number)
        for row_index, i in enumerate(self.graph):
            for k in i.keys():
                col_index = self.nodes_list.index(k)
                matrix[row_index][col_index] = i[k]
        return matrix

    def get_weight(self, first_node, second_node):
        if not first_node in self.nodes_list:
            raise ValueError(f"There is no {first_node} node in graph")
        if not second_node in self.nodes_list:
            raise ValueError(f"There is no {second_node} node in graph")
        if first_node == second_node:
            raise ValueError("First node and second node should be different")
        first_node_index = self.nodes_list.index(first_node)
        second_node_index = self.nodes_list.index(second_node)
        if not second_node in self.graph[first_node_index].keys():
            raise ValueError(f"There is no edge between {first_node} and {second_node}")
        weight = self.graph[first_node_index][second_node]
        return weight

    def get_size(self):
        size = 0
        for i in self.graph:
            size += len(i)
        size /= 2
        size = int(size)
        return size

    def get_min_edge(self, node):
        if type(node) != str:
            raise TypeError("Nodes' name should be string")
        if not node in self.nodes_list:
            raise ValueError("Such node doesn't exist")
        node_index = self.nodes_list.index(node)
        if len(self.graph[node_index]) == 0:
            raise ValueError("This node hasn't any edges")
        min_weight = min(self.graph[node_index].items(), key=lambda x: x[1])
        return min_weight

#     def get_connected_component(self, node, connection_dict=None):
#         if type(node) != str:
#             raise TypeError("Nodes' name should be string")
#         if not node in self.nodes_list:
#             raise ValueError("Such node doesn't exist")
#         connected_component = {node: True}
#         node_index = self.nodes_list.index(node)
#         for i in self.graph[node_index]:
#             connected_component[i] = False
#         for i in connected_component:
#             if connected_component[i]:
#                 continue
#             self.get_connected_component(i, connected_component)
#         return connected_component
#
#
#
# def boruvka_algorythm(graph_object: Graph, nodes_num, tough):
#     mst = Graph()
#     mst.add_nodes(graph_object.nodes_list)
#     while mst.get_size() < nodes_num - 1:
#         for i in graph_object.nodes_list:
#             mst.add_edge(graph_object.get_min_edge(i))
#
#
#
# a = Graph()
# a.add_nodes("a", "b", "c", "h")
# a.add_edges(("a", "b", 3), ("b", "c", 4), ("h", "c", 4))
# print(dict(zip(a.nodes_list, a.graph)), a.get_connected_component("b"))