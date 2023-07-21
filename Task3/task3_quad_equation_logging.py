import os
import sys

# Перехожу в дирикторию Task2 для импорта logger из модуля task2
task3_path = os.path.dirname(__file__)
dir_task_3 = os.path.split(task3_path)[0]
task2_path = os.path.join(dir_task_3, 'Task2')
sys.path.append(task2_path)
os.chdir(task2_path)
from task2 import logger
os.chdir(task3_path) # Возвращаюсь в дирикторию Task2

def quad_equation_solution():
    path = 'task3_log_quad_equation.log'
    if os.path.exists(path):
        os.remove(path)

    @logger(path)
    def discriminant(a, b, c):
        """
        функция для нахождения дискриминанта
        """
        return b ** 2 - 4 * a *c

    @logger(path)
    def solution(a, b, c):
        """
        функция для нахождения корней уравнения
        """
        d = discriminant(a, b, c)
        if d > 0:
            x1 = (-b + d ** (1 / 2)) / 2 / a
            x2 = (-b - d ** (1 / 2)) / 2 / a
            return (x1, x2)
        elif d == 0:
            x = -b / 2 / a
            return x
        else:
            return 'корней нет'

    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)


if __name__ == '__main__':
    quad_equation_solution()