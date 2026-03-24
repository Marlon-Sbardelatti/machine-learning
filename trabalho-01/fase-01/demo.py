from typing import List
import matplotlib.pyplot as plt
import math

"""
    Equipe: Cristina Siewert Jansen, Marlon Sbardelatti, Sofia Sousa Lindner
    Professora: Andreza Sartori
    As respostas das questões 3) e 4) da Fase 1 estão no README.md.
"""

def scatter_dispersion_graph(x_axis: List[float], y_axis: List[float]):
    plt.scatter(x_axis, y_axis)
    plt.xlabel("X")
    plt.ylabel("Y")


def average(axis: List[float]) -> float:
    total_sum = sum([el for el in axis])
    return total_sum / len(axis) 


def deviation(points: List[tuple[float, float]], x_avg: float, y_avg: float) -> float:
    deviation = 0
    for p in points:
        deviation += (p[0] - x_avg) * (p[1] - y_avg)
    return deviation


def variance(
    x_axis: List[float], y_axis: List[float], x_avg: float, y_avg: float
) -> float:
    x = sum([math.pow(x - x_avg, 2) for x in x_axis])
    y = sum([math.pow(y - y_avg, 2) for y in y_axis])
    return math.sqrt(x * y)


def correlation(x_axis: List[float], y_axis: List[float]) -> float:
    x_avg = average(x_axis)
    y_avg = average(y_axis)

    points = list(zip(x_axis, y_axis))
    
    dev = deviation(points, x_avg, y_avg)
    var = variance(x_axis, y_axis, x_avg, y_avg)

    return dev / var


def regression(x_axis: List[float], y_axis: List[float]):
    x_avg = average(x_axis)
    y_avg = average(y_axis)

    points = list(zip(x_axis, y_axis))

    sum_dev = deviation(points, x_avg, y_avg)
    sqr_dev_x = sum_squared_deviation_x(x_axis, x_avg)
    
    b1 = sum_dev / sqr_dev_x
    b0 = y_avg - (b1 * x_avg)
    
    def unknown_function(x: float):
        return b0 + b1 * x
    
    return b0, b1, [unknown_function(xi) for xi in x_axis]


def sum_squared_deviation_x(x_axis: List[float], x_avg: float) -> float:
    return sum([math.pow(x - x_avg, 2) for x in x_axis])


def main():
    datasets = [
        {
            "x": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5.0],
            "y": [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68],
        },
        {
            "x": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5.0],
            "y": [9.14, 8.14, 8.47, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74],
        },
        {
            "x": [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19.0],
            "y": [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56, 7.91, 6.89, 12.50],
        },
        {
            "x": [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
            "y": [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73],
        },
        {
            "x": [10.0, 8.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0], # Sem x do outlier
            "y": [7.46, 6.77, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73], # Sem y do outlier
        },
    ]

    graph_index = 0
    for dt in datasets:
        x = dt["x"]
        y = dt["y"]
        
        # Correlação
        r = correlation(x, y)
        
        # Regressão
        b0, b1, y_model = regression(x, y)
        
        # Gráfico
        scatter_dispersion_graph(x, y)
        
        plt.plot(x, y_model)
        
        plt.title(f"r = {r:.4f} | β0 = {b0:.4f} | β1 = {b1:.4f}")
        
        plt.savefig(f"dataset-{graph_index + 1}.png")
        
        graph_index += 1
        plt.close()


if __name__ == "__main__":
    main()
