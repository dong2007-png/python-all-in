import tkinter as tk
import random
import threading
import time


def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('你的电脑正在被攻击')
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window, text='你的电脑正在被攻击', bg='red',
    font=('宋体', 17), width=20, height=4).pack()
    window.mainloop()


threads = []
for i in range(100):
    t = threading.Thread(target=boom)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()
