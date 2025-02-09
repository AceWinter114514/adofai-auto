import __init__ as ad
import pydirectinput as pd
import time
import keyboard as kb
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
from threading import *

pd.PAUSE = 0

win = tk.Tk()
win.title('adofai自动打谱')
win.geometry('260x160')
file = ''
times = []
def importButtonC():
    global file
    file = askopenfilename(filetypes=[('adofai文件','*.adofai'),])
    importLabel.config(text=file)
def start():
    thread1 = Thread(target=_thread1)
    thread1.start()
    
importButton = ttk.Button(text='导入文件',command=importButtonC)
importButton.place(x=0,y=0)

importLabel = tk.Label(text='未导入文件')
importLabel.place(x=0,y=27)

keyLabel = tk.Label(text='输入按键:')
keyLabel.place(x=0,y=50)

keyEntry = ttk.Entry(width=11)
keyEntry.place(x=58,y=50)

muliterLabel = tk.Label(text='休眠时间倍率:')
muliterLabel.place(x=0,y=78)

muliterEntry = ttk.Entry(width=8)
muliterEntry.place(x=80,y=78)
muliterEntry.insert(0,'0.995')

mouseLabel = tk.Label(text='鼠标灵敏度:')
mouseLabel.place(x=0,y=105)

mouseEntry = ttk.Entry(width=9)
mouseEntry.place(x=74,y=105)
mouseEntry.insert(0,'0.000001')

startButton = ttk.Button(text='开始',command=start)
startButton.place(x=0,y=130)
def sleep(duration):
    start = time.perf_counter()
    while time.perf_counter() - start < duration:
        pass

def _thread1():
    f = ad.adofai(file)
    bpm = f.settings['bpm']
    times = []
    ra = f.absBeats(bpm)
    ra.pop(0)
    for i in ra:
        times.append(i*60/bpm)
    key = keyEntry.get()
    muliter = float(muliterEntry.get())
    mouse = float(mouseEntry.get())
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

win.mainloop()
