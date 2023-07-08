import pyautogui as st
import time
import random
limit = ("Enter your limit : ")
msg = ("Enter your msg ")

i = 0
time.sleep(20)
while i < int(limit):
    st.typewrite(msg)
    st.press("Enter ")
    i = i + 1
