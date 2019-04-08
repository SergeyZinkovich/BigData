from tkinter import Tk, Canvas, Frame, BOTH, Button
import time


class Example(Canvas):

    def __init__(self, parent):
        Canvas.__init__(self, width=500, height=500,
                        background="white", highlightthickness=0)
        self.parent = parent
        self.initUI()

    def click_button(self):
        self.after(100, self.change)

    def initUI(self):
        self.parent.title("Animation")
        self.pack(fill=BOTH, expand=1)

        self.pack(fill=BOTH, expand=1)


        closeButton = Button(self, text="Start", command=self.click_button)
        closeButton.pack()

        self.file = open("lab1.json", "r")
        self.file.read(1)



    def change(self):
        self.delete("all")
        a = self.file.read(1)
        if (a == ''):
            self.reopen()
        for i in range(3):
            for j in range(3):
                self.file.read(1)
                s = ""
                c = self.file.read(1)
                while (c != ']'):
                    s += c
                    c = self.file.read(1)
                s = s.split(',')
                c1 = int(s[0])
                c2 = int(s[1])
                c3 = int(s[2])
                self.file.read(1)
                self.create_rectangle(i+50*i, j+50*j, i+50*i+50, j+50*j+50, outline='#%02x%02x%02x' % (c1, c2, c3), fill='#%02x%02x%02x' % (c1, c2, c3))
        self.file.read(1)
        self.after(100, self.change)

    def reopen(self):
        self.file.close()
        self.file = open("lab1.json", "r")
        self.file.read(2)


def main():
    root = Tk()
    ex = Example(root)
    root.geometry("400x250")
    root.mainloop()


if __name__ == '__main__':
    main()