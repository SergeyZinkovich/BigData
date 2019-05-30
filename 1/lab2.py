from tkinter import Tk, Canvas, Frame, BOTH, Button, Label
from PIL import ImageTk, Image, ImageDraw
import time


class Example(Canvas):

    def __init__(self, parent):
        Canvas.__init__(self, width=500, height=500,
                        background="white")
        self.parent = parent
        self.initUI()

    def click_button(self):
        self.after(100, self.change)

    def initUI(self):
        self.parent.title("Animation")
        self.pack(fill=BOTH, expand=1)

        closeButton = Button(self, text="Start", command=self.click_button)
        closeButton.pack()
        self.openFile()
        self.imag = Image.new("RGB", (self.w, self.h), color="white")
        self.draw = ImageDraw.Draw(self.imag)



    def change(self):
        self.delete("all")
        a = self.file.read(1)
        if (a == ''):
            self.reopen()
        for i in range(self.w):
            for j in range(self.h):
                self.file.read(1)
                s = ""
                c = self.file.read(1)
                while (c != ']'):
                    s += c
                    c = self.file.read(1)
                #s.replace(" ", "")
                c1, c2, c3 = map(int, s.split(','))
                self.file.read(2)
                self.draw.point((i, j), (c1, c2, c3))
        print("done")
        #del draw
        self.image = ImageTk.PhotoImage(self.imag)
        self.create_image(0, 0, image=self.image, anchor="nw")
        self.update()
        self.file.read(1)
        self.after(1, self.change)

    def openFile(self):
        self.file = open("file3_1000_563.json", "r")
        self.file.read(10)
        s = ""
        c = self.file.read(1)
        while (c != ','):
            s += c
            c = self.file.read(1)
        self.w = int(s)
        self.file.read(11)
        s = ""
        c = self.file.read(1)
        while (c != ','):
            s += c
            c = self.file.read(1)
        self.h = int(s)
        self.file.read(12)
        s = ""
        c = self.file.read(1)
        while (c != ','):
            s += c
            c = self.file.read(1)
        self.c = int(s)
        self.file.read(15)

    def reopen(self):
        self.file.close()
        self.openFile()
        self.file.read(1)


def main():
    root = Tk()
    ex = Example(root)
    root.geometry("1000x1000")
    root.mainloop()


if __name__ == '__main__':
    main()