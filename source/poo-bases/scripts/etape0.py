

class Point(object):
    """Définition d'un point mathématique"""

    def __init__(self, x=0, y=0):
        self.x =  x
        self.y =  y

    def __str__(self):
        return "({};{})".format(self.x, self.y)


class Rectangle(object):
    """Définition d'un rectangle horizontal"""

    def __init__(self, corner, width, height):
        self.coin = coin
        self.width = width
        self.height = height

    def get_center(self):
        xc =  self.coin.x + self.width/2
        yc =  self.coin.y + self.height/2
        return Point(xc, yc)

    def area(self):
        return self.width * self.height


class Carre(Rectangle):
    """Définition d'un carré horizontal"""

    def __init__(self, coin, cote):
        Rectangle.__init__(self, coin, side, side)
        self.side =  side

    def area(self):
        return self.side**2
