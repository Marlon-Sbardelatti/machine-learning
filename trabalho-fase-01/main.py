from typing import List
import matplotlib.pyplot as plt
import math


def scatter_dispersion_graph(x_axis: List[float], y_axis: List[float]):
    plt.scatter(x_axis, y_axis)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def average(axis: List[float]) -> float:
    sum = 0
    for element in axis:
        sum += element

    return sum / len(axis)


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

    b0_dev = deviation(points, x_avg, y_avg)
    b1_sum_sqr_dev = sum_squared_deviation_x(x_axis, x_avg)
    b1 = b0_dev / b1_sum_sqr_dev
    b0 = y_avg - (b1 * x_avg)
    print(b0)
    print(b1)
    print()

    def unknown_function(x):
        return b0 + b1 * x

    return unknown_function


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
    ]

    count = 1
    for dt in datasets:
        x = dt["x"]
        y = dt["y"]
        scatter_dispersion_graph(x, y)
        r = correlation(x, y)
        print(r)
        unknown_function = regression(x, y)
        model = list(map(unknown_function, x))
        plt.plot(x, model)
        plt.savefig(f"dataset-{count}.png")
        count += 1
        plt.close()


if __name__ == "__main__":
    main()
