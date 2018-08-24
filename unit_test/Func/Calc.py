class Calc(object):
    def add(self, a, b):
        return a + b

    def sub(self, a, c):
        return a - c


if __name__ == '__main__':
    print(Calc().add(10, 3))
    print(Calc().sub(10, 5))
