

class Graph:
    def __init__(self):
        self.nodes_list = []
        self.adj_list = dict()
        self.graph = []

    def add_node(self, node: str):
        if type(node) != str:
            raise TypeError("Nodes' name should be string")
        if node in self.adj_list:
            return "Such node is already exist"
        else:
            self.nodes_list.append(node)
            self.adj_list.update({node: dict()})
            return self.adj_list

    def add_edge(self, first_node, second_node, weight):
        if not first_node in self.adj_list:
            raise ValueError(f"There is no {first_node} node in graph")
        if not second_node in self.adj_list:
            raise ValueError(f"There is no {second_node} node in graph")
        if first_node == second_node:
            raise ValueError("First node and second node should be different")
        self.adj_list[first_node][second_node] =  weight
        self.adj_list[second_node][first_node] =  weight
        return self.adj_list

    def remove_edge(self, first_node, second_node):
        if not first_node in self.adj_list:
            raise ValueError(f"There is no {first_node} node in graph")
        if not second_node in self.adj_list:
            raise ValueError(f"There is no {second_node} node in graph")
        if first_node == second_node:
            raise ValueError("First node and second node should be different")
        if not second_node in self.adj_list:
            raise ValueError(f"There is no edge between {first_node} and {second_node}")
        del self.adj_list[second_node][first_node]
        del self.adj_list[first_node][second_node]
        return self.adj_list

    def remove_node(self, node):
        if type(node) != str:
            raise TypeError("Nodes' name should be string")
        if not node in self.nodes_list:
            return "Such node isn't exist"
        node_index = self.nodes_list.index(node)
        local_nodes_list = set(self.graph[node_index].keys()).copy()
        for i in local_nodes_list:
            self.remove_edge(node, i)
        del self.graph[node_index]
        del self.nodes_list[node_index]

    def add_nodes(self, *args):
        for node in args:
            self.add_node(node)
        return self.adj_list

    def remove_nodes(self, *args):
        for node in args:
            self.remove_node(node)

    def add_edges(self, *args):
        for first_node, second_node, weight in args:
            self.add_edge(first_node, second_node, weight)
        return self.nodes_list

    def remove_edges(self, *args):
        for first_node, second_node in args:
            self.remove_edge(first_node, second_node)

    def clear(self):
        self.nodes_list = []
        self.graph = []

    def clear_edges(self):
        self.graph = [{} for i in range(len(self.nodes_list))]



    def get_matrix(self):
        nodes = sorted(self.adj_list.keys())
        num_nodes = len(nodes)
        node_to_index = {}
        for i, node in enumerate(nodes):
            node_to_index[node] = i
        adj_matrix = []
        for i in range(num_nodes):
            adj_matrix.append([0] * num_nodes)

        for u, neighbors in self.adj_list.items():
            row_idx = node_to_index[u]
            for v, weight in neighbors.items():
                if v in node_to_index:
                    col_idx = node_to_index[v]

                    adj_matrix[row_idx][col_idx] = weight

        return adj_matrix


g = Graph()
l = g.add_nodes('1', '2', '3')
print(g.add_edge('2', '3', 0.9))
print(g.add_edge('1', '2', 3))
print(g.remove_edge('2', '3'))
print(g.get_matrix())



