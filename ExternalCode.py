
class Rectangle:
    def __init__(self, distanceUnit, position, base, height):
        self.distanceUnit = distanceUnit
        self.position = position
        self.base = base
        self.height = height
    def draw(self, canvas):
        canvas.delete('all')
        unit = self.distanceUnit
        canvas.create_rectangle(self.position[0] * unit, self.position[1] * unit,
                                (self.position[0] + self.base) * unit,
                                (self.position[1] + self.height) * unit)
        for i in range(1, self.base):
            canvas.create_line((self.position[0] + i) * unit, self.position[1] * unit, (self.position[0] + i) * unit, (self.position[1] + self.height) * unit)
        for i in range(1, self.height):
            canvas.create_line(self.position[0] * unit, (self.position[1] + i) * unit, (self.position[0] + self.base) * unit, (self.position[1] + i) * unit)


def draw_line_from_external_code(canvas):
    print('hallo from draw_line_from_external_code(canvas) method')
    canvas.create_line(20, 50, 70, 130)

def drawRectangle(canvas):
    pass

def constructRectangle(canvas, distanceUnit, position, dimensions):
    print("dimensions are: %d4, %d4" % (dimensions[0], dimensions[1]))
    canvas.create_rectangle(position[0] * distanceUnit, position[1] * distanceUnit,
                            (position[0] + dimensions[0]) * distanceUnit, (position[1] + dimensions[1]) * distanceUnit)
    # canvas.create_rectangle(position[0], position[1], position[0] + dimensions[0], position[1] + dimensions[1],
    #                         outline = "#f11", fill = "#1f1", width = 2)
    # canvas.create_rectangle(230, 10, 290, 60,
    #                         outline = "#f11", fill = "#1f1", width = 2)
    # canvas.create_oval(10, 10, 80, 80, outline = "#f11",
    #                    fill = "#1f1", width = 2)
    # canvas.create_oval(110, 10, 210, 80, outline = "#f11",
    #                    fill = "#1f1", width = 2)
    # canvas.create_arc(30, 200, 90, 100, start = 0,
    #                   extent = 210, outline = "#f11", fill = "#1f1", width = 2)



