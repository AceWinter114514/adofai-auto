import tkinter as tk
import tkinter.ttk as ttk




def writeSettingsFile():
    key = keyEntry.get()
    muliter = float(muliterEntry.get())
    mouse = float(mouseEntry.get())
    fileName = fileNameEntry.get()

    settings = {
        'key': key,
        'muliter': muliter,
        'mouse': mouse
    }

    with open(fileName, 'w') as f:
        f.write(str(settings))

    print(f'设置文件已保存为 {fileName}')

window = tk.Tk()
window.title('设置文件生成器')
window.geometry('250x150')
window.resizable(False, False)
keyLabel = tk.Label(text='输入按键:')
keyLabel.place(x=0,y=0)

keyEntry = ttk.Entry(width=11)
keyEntry.place(x=58,y=0)

muliterLabel = tk.Label(text='休眠时间倍率:')
muliterLabel.place(x=0,y=28)

muliterEntry = ttk.Entry(width=8)
muliterEntry.place(x=80,y=28)
muliterEntry.insert(0,'0.995')

mouseLabel = tk.Label(text='鼠标灵敏度:')
mouseLabel.place(x=0,y=55)

mouseEntry = ttk.Entry(width=9)
mouseEntry.place(x=74,y=55)
mouseEntry.insert(0,'0.0000008')

fileNameLabel = tk.Label(text='设置文件名:')
fileNameLabel.place(x=0,y=80)

fileNameEntry = ttk.Entry(width=10)
fileNameEntry.place(x=70,y=80)

startButton = ttk.Button(text='写入设置文件',command=writeSettingsFile)
startButton.place(x=0,y=105)

window.mainloop()