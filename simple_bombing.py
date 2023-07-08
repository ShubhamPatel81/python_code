import random
import pyautogui as pg
import time

a = int(input('How many times u want to sent msg: '))
msg = input("Enter ur msg: ")
gli = ('df,sac,efwef,qwr,we,qw,rwe,daf,rg,awfd')

time.sleep(10)

for i in range(a):
    a = random.choice(gli)
    pg.write('you are a ' + a)

    pg.write(msg)
    pg.press('enter')
