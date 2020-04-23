import time

def time_this(NUM_RUNS=10):
    def decorator(f):
        def func():
            avg = 0
            for _ in range(NUM_RUNS):
                t0 = time.time()
                f()
                t1 = time.time()
                avg += (t1 - t0)
            avg /= NUM_RUNS
            print("Среднее время выполнения функции за %s запусков: %.5f секунд" % (NUM_RUNS, avg))
        return func

    return decorator

@time_this()
def f():
    for j in range(1000000):
        pass
f()