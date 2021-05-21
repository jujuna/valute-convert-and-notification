import sched
import time
from plyer import notification
from calculator import Convert
import api

event_schedule = sched.scheduler(time.time, time.sleep)

valute='ევრო'

current = 0
def valute_notification():
    global current
    user_valute=valute
    valute_current=Convert.money_find(name=user_valute)


    if valute_current>current:
        notification.notify(title='მოიმატა', message="მოიმატა და გახდა {}".format(valute_current), timeout=5,)
        current=valute_current

    if valute_current<current:
        notification.notify(title='დაიკლო', message="დაიკლო და გახდა {}".format(valute_current),timeout=5, )
        current = valute_current

    print(current)

    event_schedule.enter(5, 1, valute_notification,)


event_schedule.enter(1, 1, valute_notification,)
event_schedule.run()








