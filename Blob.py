from tkinter import *


class Blob:
    "'A base class to define a blob.'"
    count = 0

    def __init__(self, xPos = 10, yPos = 10, radius = 20, colour = 'cyan'):
        self.xPos = xPos
        self.yPos = yPos
        self.radius = radius
        self.colour = colour

    def draw(self, canvas):
        topLeftX = self.xPos
        topLeftY = self.yPos
        bottomRightX = topLeftX + 2*self.radius
        bottomRightY = topLeftY + 2*self.radius
        canvas.create_oval(topLeftX, topLeftY, bottomRightX, bottomRightY, fill = self.colour)
