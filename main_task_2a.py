import numpy as np

from classes import Orbit
from rkk4 import runge_kutta_4
from grafics import start_plot

# a = (6371 + 410) * 1000 * 3  # Большая полуось


T = 92.899 * 60
e = 0.00021  # Эксцентриситет
i = 51.638  # Наклонение
omega = np.deg2rad(12.867)  # Долгота восходящего узла
w = np.deg2rad(284.400)  # Аргумент перицентра
nu = 0.1 * np.pi  # Истиная аномалия
mu = 3.986 * 10 ** 14  # Гравитационный параметр
a = (mu*T**2/(4*np.pi**2))**(1/3)
orbit = Orbit(a=a, e=e, i=i, omega=omega, w=w, nu=nu, mu=mu)

# Вызов метода Рунге-Кутта 4-го порядка
h = 0.1  # Шаг интегрирования по времени
n = 570000  # Количество шагов
runge_kutta_4(f=orbit.vector_function_right_parts, t0=orbit.t0, y0=orbit.y0, h=h, n=n, orbit=orbit)

# строим графики
start_plot(orbit=orbit)