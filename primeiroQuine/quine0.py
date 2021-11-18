
import random
import shutil
import subprocess
import time

randomNumber = str(random.randint(1, 15))
print("hello world" , randomNumber)
new_file_name = "quine" + randomNumber + ".py"
shutil.copy(__file__, new_file_name)
time.sleep(1)

code = __file__
if code[51:] == 'quine0.py':
    print('First')

subprocess.Popen(['python', new_file_name])

for num in range(10):
    time.sleep(0.3)
    print(num, "code", randomNumber)
