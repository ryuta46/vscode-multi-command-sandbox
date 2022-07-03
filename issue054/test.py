
import time

f = open('output.txt', 'w')
f.write('start.\n')
f.close()
print("doing something...")

time.sleep(5)

f = open('output.txt', 'a')
f.write('end.\n')
f.close()

