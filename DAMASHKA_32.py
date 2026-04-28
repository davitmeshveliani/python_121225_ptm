def make_rounder(num):

    def wrapper(number):
        return round(number, num)
    return wrapper

round2 = make_rounder(2)
round0 = make_rounder(0)
round2(3.14159)
round2(2.71828)
round0(9.999)
####################################
from datetime import datetime

def make_logger():
    events = []
    def logger_event(message=None, event_time=None):
        if message:
            if event_time is None:
                event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_event = f" {message} {event_time}"
            events.append(log_event)
        return events
    return logger_event

log = make_logger()

log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")
##############################################
def frame(func):
    def wrapper(*args, **kwargs):
        texst = func(*args, **kwargs)
        border = "-" * 50
        result = f"{border}\n{texst}\n{border}"
        return result
    return wrapper
@frame
def say_hello():
    return "Привет, игрок!"

@frame
def say_chao():
    return "Пока, игрок!"

say_hello()
say_chao()