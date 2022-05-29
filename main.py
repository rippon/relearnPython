import ExternalCode
from GraphicsButton import *

from Blob import *

window = Tk()
window.title("window title")
frame = Frame(window)
frame.grid()

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
windowWidth = int(screenWidth/2.5)
windowHeight = int(screenHeight/2)
windowPositionAcross = int(screenWidth*0.55)
windowPositionDown = int(screenHeight*0.03)
windowDimensionsString = str(windowWidth) + "x" + str(windowHeight)
windowOffsetString = "+" + str(windowPositionAcross) + "+" + str(windowPositionDown)
window.geometry(windowDimensionsString + windowOffsetString)
canvasWidth = int(0.8*windowWidth)
canvasHeight = int(0.65*windowHeight)
distanceUnit = canvasWidth / 20
rectangleBase = 3
rectangleHeight = 2

def rectangleBaseSelectorClicked(event):
        print('base ' + rectangleBaseSelector.get() + ' is selected')
        myRectangle.base = int(rectangleBaseSelector.get())
def rectangleHeightSelectorClicked(event):
        print('height ' + rectangleHeightSelector.get() + ' is selected')
        myRectangle.height = int(rectangleHeightSelector.get())

def testButtonResponse():
    print("hallo from testButtonResponse() method")

def buttonDrawRectangleResponse():
    myRectangle.draw(canvas)

# btnGraphics = GraphicsButton(frame, window = "five", text = 'graphics').grid(row = 0, column = 0)
btnTest = Button(frame, text = 'test', command = testButtonResponse).\
    grid(row = 0, column = 0, padx = distanceUnit/5, pady = distanceUnit/10)
btnExit = Button(frame, text = 'exit', command = exit).grid(row = 1, column = 0)
#btnBlank = Button(frame, text = 'blankButton')
canvas = Canvas(frame, bg = "yellow", height = canvasHeight, width = canvasWidth)
canvas.grid(row = 0, column = 3, rowspan = 5)

Label(frame, text = "Select base:", font = ("Times New Roman", 10)).grid(column = 1,
                                                                                row = 1, padx = 5, pady = 1)
Label(frame, text = "Select height:", font = ("Times New Roman", 10)).grid(column = 1,
                                                                                row = 3, padx = 5, pady = 1)
rectangleDimensionOptions = ["1", "2", "3", "4", "5", "6", ]
rectangleBaseSelector = ttk.Combobox(frame, width = 5, value = rectangleDimensionOptions)
rectangleBaseSelector.current(2)
rectangleBaseSelector.bind("<<ComboboxSelected>>", rectangleBaseSelectorClicked)
rectangleBaseSelector.grid(row = 2, column = 1)
rectangleHeightSelector = ttk.Combobox(frame, width = 5, value = rectangleDimensionOptions)
rectangleHeightSelector.current(1)
rectangleHeightSelector.bind("<<ComboboxSelected>>", rectangleHeightSelectorClicked)
rectangleHeightSelector.grid(row = 4, column = 1)
buttonDrawRectangle = Button(frame, text = 'draw rectangle', command = buttonDrawRectangleResponse)\
    .grid(row = 0, column = 1)

rectanglePosition = [2, 1]
myRectangle = ExternalCode.Rectangle(distanceUnit, rectanglePosition, rectangleBase, rectangleHeight)
# myRectangle.draw(canvas)

canvas.create_oval(20, 20, 100, 100)


counter = 0
xDisplacement = -canvasWidth/20
yDisplacement = canvasHeight/20
blobs = []
xPos = canvasWidth + xDisplacement
yPos = yDisplacement
blobs.append(
    Blob(xPos, yPos, radius = distanceUnit))
while counter < 3:
    xPos = xPos + xDisplacement
    yPos = yPos + yDisplacement
    blobs.append(
        Blob(xPos, yPos, radius = distanceUnit))
    # blobs[counter].draw(canvas)
    counter = counter + 1

# add to window and show
window.mainloop()
