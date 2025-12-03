class Graph:
    def __init__(self, weighted=False):
        self.weighted = weighted
        self.adj_list = dict()
        self.adj_matrix = [[]]
