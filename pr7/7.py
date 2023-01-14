import numpy as np
import matplotlib.pyplot as plt
from sympy import *


def main():
    x = np.arange(0.01, 5, 0.1)

    # График функции
    k = Symbol('k')
    y = cos(3 * k) * log(k ** 2)
    plt.subplot(3, 2, 1)
    plt.plot(x, lambdify(k, y, 'numpy')(x), color='b')

    # Точки минимума и максимума
    xmax = x[np.argmax(lambdify(k, y, 'numpy')(x))]
    ymax = lambdify(k, y, 'numpy')(x).max()
    xmin = x[np.argmin(lambdify(k, y, 'numpy')(x))]
    ymin = lambdify(k, y, 'numpy')(x).min()
    plt.scatter(xmax, ymax, color='m')
    plt.scatter(xmin, ymin, color='m')

    # Построение касательной и нормаль
    x0 = 1
    plt.subplot(3, 2, 1)
    plt.title("Касательные и нормаль")
    y0 = np.cos(3 * x0) * np.log(x0 ** 2)
    y00 = -3*np.sin(3 * x0) * np.log(x0 ** 2) + (2*x0/(x0 ** 2)) * np.cos(3 * x0)
    yk = y0 + y00 * (x - x0)
    plt.plot(x, yk, linestyle='dashed', color = 'g')
    yn = y0 - (1/y00) * (x-x0)
    plt.plot(x, yn, linestyle='dashed', color = 'r')

    # Первая производная
    yf = y.diff(k)
    plt.subplot(3, 2, 2)
    plt.title("График  y'")
    plt.plot(x, lambdify(k, yf, 'numpy')(x), color='b')
    print('Первая производная =', yf)

    # Вторая производная
    yff = yf.diff(k)
    plt.subplot(3, 2, 5)
    plt.title("График  y'"+"'")
    plt.plot(x, lambdify(k, yff, 'numpy')(x), color='b')
    print('Вторая производная =', yff)

    #Касательное расслоение
    plt.subplot(3, 2, 6)
    plt.title("Касательное расслоение")
    plt.plot(x, lambdify(k, y, 'numpy')(x), color='b')
    for x0 in range(1, 5, 1):
        yk = lambdify(k, y, 'numpy')(x0) + lambdify(k, yf, 'numpy')(x0) * (x - x0)
        plt.plot(x, yk, linestyle='dashed', color='g')

    #Длина кривой через интеграл
    arclength = np.trapz(np.sqrt(1 + np.gradient(lambdify(k, y, 'numpy')(x), x) ** 2))
    print(f'Длина кривой: {arclength:.5e}')
    plt.show()


if __name__ == "__main__":
    main()
