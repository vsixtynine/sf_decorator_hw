import functools
import time


class ContextDecorator(object):
    ''' класс менеджера контекста и декоратора '''

    def __init__(self, name="def", runs=3):
        self._name = name
        self._runs = runs

    def __enter__(self):
        return self._name.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._name.__exit__()

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ''' запускаем контекстный менеджер класса TimeCalc '''
            with self:
                print(f"\nЗапускаю {self._name} {self._runs} раз")

                ''' цикл по количеству итераций '''
                for n in range(1, self._runs + 1):
                    print("Инерация:", n)

                    ''' сохраняем результат выполнения фунции'''
                    result = func(*args, **kwargs)
                return result

        return wrapper


class TimeCalc(ContextDecorator):
    ''' калькулятор выполнения функции '''

    def __enter__(self):
        '''Фиксируем время запуска декорируемой функции'''
        
        self.start = time.time()
        return self

    def __exit__(self, ex_ty, ex_va, ex_tb):
        '''Фиксируем время окончания после всех итераций'''
        
        self.end = time.time()
        self.time_delta = self.end - self.start
        
        
        '''делим общее время работы на количество итераций'''
        self.time = self.time_delta / num_runs

        print("\nСреднее время исполнения: %.6f с." % self.time)

        return self


def ask_runs():

    while True:
        try:
            answer = int(input("\nВведите количество запусков функции: "))
        except ValueError:
            print("(!) Ошибка: Необходимо ввести число.")
        else:
            return answer


def ask_sequence_num():

    while True:
        try:
            answer = int(
                input("\nВведите порядковый номер элемента в последовательности: "))
        except ValueError:
            print("(!) Ошибка: Необходимо ввести число.")
        else:
            return answer

''' Запрашиваем данные для расчета '''
num_runs = ask_runs()
seq_num = ask_sequence_num()


''' функция расчета последовательности фибоначчи декорируемая классом '''
@TimeCalc(name="таймер функции фибоначчи", runs=num_runs)
def fibo(num):
    n1, n2 = 0, 1
    if num == 0:
        return n1
    if num == 1:
        return n2

    for _ in range(1, num):
        n1, n2 = n2, n1 + n2

    return n2


print("\nЧисло фибоначчи:", fibo(seq_num))
