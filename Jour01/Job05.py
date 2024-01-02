class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print (f"Les coordonnées sont : {self.x}, {self.y}")

    def afficherX (self):
        print (f"Le point x est : {self.x}")

    def afficherY (self):
        print (f"Le point y est : {self.y}")
    
    def ChangerX (self, new_x):
        self.x = new_x

    def ChangerY (self, new_y):
        self.y = new_y

point = Point (12, 2)

point.afficherLesPoints()

point.afficherX()
point.afficherY()

point.ChangerX(3)
point.ChangerY(8)

point.afficherLesPoints()