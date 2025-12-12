import time
import matplotlib.pyplot as plt
from graph_matrix import MatrixGraph, generate_erdos_renyi_matrix, boruvka_mst

def run_full_experiment():

    vertex_sizes = [50, 75, 100, 125, 150, 175, 200, 225, 250]
    densities = [0.65, 0.7, 0.75, 0.8, 0.85, 0.9]
    iterations = 25

    results = {}
    for density in densities:
        results[density] = []
        for v in vertex_sizes:
            curr_times = []
            for i in range(iterations):
                g = MatrixGraph()
                generate_erdos_renyi_matrix(g, v, density)

                s = time.perf_counter()
                boruvka_mst(g)
                e = time.perf_counter()
                curr_times.append(e - s)

                with open('matrix_experiment.csv', 'a') as f:
                    f.write(f'{v},{density},{e-s}\n')

            avg = sum(curr_times) / len(curr_times)
            results[density].append(avg)

    plt.figure(figsize=(10, 6))
    for d, times in results.items():
        plt.plot(vertex_sizes, times, marker='o', label=f'Щільність {d}')

    plt.title('Залежність часу виконання від кількості вершин')
    plt.xlabel('Кількість вершин')
    plt.ylabel('Час (в секундах)')
    plt.legend()
    plt.grid(True)

    filename = 'experiment_results.png'
    plt.savefig(filename)
    plt.show()

print(run_full_experiment())