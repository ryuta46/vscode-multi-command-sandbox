
import time
import datetime

f = open('output.txt', 'w')
f.write(f'start. {datetime.datetime.now()} \n')
f.close()
print("doing something...")

time.sleep(5)

f = open('output.txt', 'a')
f.write(f'end. {datetime.datetime.now()}\n')
f.close()

