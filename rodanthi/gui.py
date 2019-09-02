import tkinter as tk
import time
import objects

class window:
    def __init__(self, width, height, framerate):
        self.WIDTH = width
        self.HEIGHT = height
        self.FRAMERATE = framerate
        self.ROOT = tk.Tk()
        self.CANVAS = tk.Canvas(self.ROOT, width=self.WIDTH, height=self.HEIGHT)
        self.CANVAS.pack()
        self.CANVAS.bind_all('<Left>', self.key_left)
        self.CANVAS.bind_all('<Right>', self.key_right)
        self.obj = objects.objects(self.WIDTH, self.HEIGHT)
        self.coords = [0, 0, self.WIDTH, self.HEIGHT]
        self.initialise()

    def initialise(self):
        self.CANVAS.create_text(10, 0, width=self.WIDTH - 10, anchor="nw", text=self.obj.display_text, tag="test")

    def remove_object(self, obj_array):
        for tag in obj_array:
            for obj in self.CANVAS.find_withtag(tag):
                self.CANVAS.delete(obj)

    def key_left(self, event):
        self.obj.counter =- self.obj.word_count
        self.obj.update()

    def key_right(self, event):
        self.obj.counter += self.obj.word_count
        self.obj.update()

    def update_frames(self):
        while True:
            time.sleep(self.FRAMERATE)
            self.remove_object(['test'])
            self.CANVAS.create_text(10, 0, width=self.WIDTH - 10, anchor="nw", text=self.obj.display_text, tag="test")
            self.CANVAS.update()
