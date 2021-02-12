from decorators import log_decorator

if __name__ == '__main__':
    @log_decorator
    def sum(a, b):
        return a + b

    @log_decorator
    def multy(a, b):
        return a * b

    sum(0, 0)
    sum(1, 10)
    multy(1, 10)