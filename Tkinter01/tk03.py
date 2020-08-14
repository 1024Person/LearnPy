import tkinter as tk
class APP:
    def __init__(self,master):
        self.frame = tk.Frame(master)
        self.frame.pack(side=tk.LEFT,padx=10,pady=100)

        self.button = tk.Button(self.frame,command = self.say,text="hello world.",bg='black',fg='red')
        self.button.pack()
    def say(self):
        print('hello world!')
root = tk.Tk()
root.title('FishC Dome')
app = APP(root)

tk.mainloop()
