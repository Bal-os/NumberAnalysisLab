from abc import abstractmethod
from inspect import signature

main_f = lambda x: x ** 4 + x ** 3 - 6 * (x ** 2) + 20 * x - 16


def _answer_start() -> float:
    return float(input('Enter Guess: '))


class Methods:

    def __init__(self):
        pass

    def _get_eps_by_precision(self, precision: int = 5) -> object:
        return 1 / (10 ** precision)

    def _iterations(self, f, x0: float, eps: float = _get_eps_by_precision(7), n: int = 100):
        """
        special f(x) for solves with current method
        :param f: f
        :param x0: starting point
        :param eps: precision wanted
        :param n: number of mandatory iterations
        :return: root of f(x) = 0
        """

        is_secant = len((signature(f)).parameters) - 1

        x = x0
        x_prev = x0 + 2 * eps
        i = 0
        flag = True

        while flag and i < n:

            print('x%d = %0.6f and f(x%d) = %0.6f' % (i, x, i, main_f(x)))

            if is_secant == 1:
                x, x_prev = f(x, x_prev)
            elif is_secant == 0:
                x, x_prev = f(x), x
            else:
                break

            i += 1
            flag = abs(x - x_prev) >= eps

        if not flag:
            print('\nRequired root is: %0.8f' % x)
        else:
            print('\nNot Convergent.')

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def run_with_params(self, x0: float, eps: float = _get_eps_by_precision(7), n: int = 100):
        pass

    @abstractmethod
    def __funk(self):
        pass


class Iter_Method(Methods):
    __iter_const: int = 689

    def __funk(self, x: float):
        return x + 2 * (main_f(x)) / self.__iter_const

    def run(self):
        self._iterations(self.__funk, _answer_start())


class Relax_Method(Methods):

    def __funk(self, x: float):
        return x - (main_f(x)) / main_f(-3)

    def run(self):
        self._iterations(self.__funk, _answer_start())


class Secant_Method(Methods):

    def __funk(self, x: float, x_prev: float):
        return x - main_f(x) * (x - x_prev) / (main_f(x) - main_f(x_prev)), x

    def run(self):
        self._iterations(self.__funk, _answer_start())


def main():
    relax_man = Relax_Method()
    relax_man.run()

    iter_ = Iter_Method()
    iter_.run()

    secant_ = Secant_Method()
    secant_.run()


if __name__ == '__main__':
    main()
