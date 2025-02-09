import __init__ as ad
import os
import json
import pydirectinput as pd
import time
import keyboard as kb
import tkinter as tk
from tkinter.filedialog import askopenfilename

pd.PAUSE = 0
file = ''
times = []
def sleep(duration):
    start = time.perf_counter()
    while time.perf_counter() - start < duration:
        pass
print('读取设置文件...')
with open('settings.txt','r') as f:
    dic = json.loads(f.read())
    
muliter = dic['muliter']
mouse = dic['mouse']
key = dic['key']
print('导入文件')
os.system('pause')
tk = tk.Tk()
file = askopenfilename(filetypes=[('adofai文件','adofai'),])
tk.destroy()
f = ad.adofai(file)
bpm = f.settings['bpm']
times = []
ra = f.absBeats(bpm)
ra.pop(0)
for i in ra:
    times.append(i*60/bpm)
kb.wait(key)
for i in times:
    s1 = pd.position()[0]-pd.size()[0]/2
    s=(i*muliter)/2+s1*mouse
    pd.keyDown(key)
    sleep(s)
    pd.keyUp(key)
    sleep(s)
pd.keyDown(key)
pd.keyUp(key)
