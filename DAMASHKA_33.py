from datetime import datetime

def measure_time(repeats=5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            result = None

            for _ in range(repeats):
                start = datetime.now()
                result = func(*args, **kwargs)
                end = datetime.now()

                total_time += (end - start).total_seconds()

            avg_time = total_time / repeats
            status_message = (f"Среднее время выполнения для {repeats} вызовов: {avg_time:.2f} секунд\n"
                      f"Результат: {result}")

            return status_message
        return wrapper
    return decorator

@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total
compute()