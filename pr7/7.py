import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.arange(0.01, 5, 0.1)
    # График функции
    y = np.cos(3 * x) * np.log(x ** 2)
    plt.subplot(2, 2, 1)
    plt.plot(x, y, color='b')
    # Точки минимума и максимума
    xmax = x[np.argmax(y)]
    ymax = y.max()
    xmin = x[np.argmin(y)]
    ymin = y.min()
    plt.scatter(xmax, ymax, color='m')
    plt.scatter(xmin, ymin, color='m')
    # Построение касательной и нормаль
    x0 = 1
    plt.subplot(2, 2, 1)
    y0 = np.cos(3 * x0) * np.log(x0 ** 2)
    y00 = -3*np.sin(3 * x0) * np.log(x0 ** 2) + (2*x0/(x0 ** 2)) * np.cos(3 * x0)
    yk = y0 + y00 * (x - x0)
    plt.plot(x, yk, linestyle='dashed', color = 'g')
    yn = y0 - (1/y00) * (x-x0)
    plt.plot(x, yn, linestyle='dashed', color = 'r')

    # Первая производная
    y = -3*np.sin(3 * x) * np.log(x ** 2) + (2*x/(x ** 2)) * np.cos(3 * x)
    plt.subplot(2, 2, 2)
    plt.plot(x, y, color='b')
    print('Первая производная = -3*np.sin(3 * x) * np.log(x ** 2) + (2*x/(x ** 2)) * np.cos(3 * x)')

    # Вторая производная
    y = ((-9*np.cos(3 * x) * np.log(x ** 2)) + ((-3)*np.sin(3 * x) * 2*x/(x ** 2))+
         (((-2)*x**2/(x ** 4)) * np.cos(3 * x))+((-3)*np.sin(3 * x)*2*x/(x ** 2)))
    plt.subplot(2, 2, 3)
    plt.plot(x, y, color='b')
    print('Вторая производная = ((-9*np.cos(3 * x) * np.log(x ** 2)) + ((-3)*np.sin(3 * x) * 2*x/(x ** 2))+(((-2)*x**2/(x ** 4)) * np.cos(3 * x))+((-3)*np.sin(3 * x)*2*x/(x ** 2)))')

    #Касательное расслоение
    y = np.cos(3 * x) * np.log(x ** 2)
    plt.subplot(2, 2, 4)
    plt.plot(x, y, color='b')
    for x0 in range(1, 5, 1):
        y0 = np.cos(3 * x0) * np.log(x0 ** 2)
        y00 = -3 * np.sin(3 * x0) * np.log(x0 ** 2) + (2 * x0 / (x0 ** 2)) * np.cos(3 * x0)
        yk = y0 + y00 * (x - x0)
        plt.plot(x, yk, linestyle='dashed', color='g')

    plt.show()
if __name__ == "__main__":
    main()