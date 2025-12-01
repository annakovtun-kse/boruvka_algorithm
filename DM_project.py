class Graph:
    def __init__(self):
        self.nodes_list = []
        self.graph = []

    def add_node(self, node: str):
        if type(node) != str:
            raise TypeError("Nodes' name should be string")
        if node in self.nodes_list:
            return "Such node is already exist"
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
            return "Such node isn't exist"
        node_index = self.nodes_list.index(node)
        local_nodes_list = set(self.graph[node_index].keys()).copy()
        for i in local_nodes_list:
            self.remove_edge(node, i)
        del self.graph[node_index]
        del self.nodes_list[node_index]