import time
import threading

def sleepTime(wait , name):
    print("Вывдим текст: {}".format(name))
    time.sleep(wait)
    print("Выводим текст повторно: {}".format(name))

start = time.time()
t_list = []

for i in range(5):
    name = 'SleepTime: ' + str(i)
    print("{} был запущен".format(name))

    td = threading.Thread(target = sleepTime,
                          name = name,
                          args = (3, name))
    td.start()
    t_list.append(td)

for t in t_list:
    t.join()

end = time.time()


print("{}: total time spent".format(end-start))
print("Hiii")

