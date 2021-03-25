import math
import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius


    def randPoint(self) -> List[float]:
        # angle between 0 and 2pi radians
        randAngle = random.uniform(0, 2*math.pi)
        # r**2 because (x-a)^2 + (y-b)^2 = r^2
        # so we find a random float number between 0 and r**2
        # and sqrt that number
        randRadius = math.sqrt(random.uniform(0, self.r**2))

        # offset r cos (ϴ) with the x_center
        # offset r sin (ϴ) with the x_center
        randX = self.x + (randRadius * math.cos(randAngle))
        randY = self.y + (randRadius * math.sin(randAngle))
        return [randX,randY]



# online optimized solution
# class Solution:

#     def __init__(self, radius: float, x_center: float, y_center: float):
#         self.radius = radius
#         self.x_center = x_center
#         self.y_center = y_center

#     def randPoint(self) -> List[float]:
#         radius = self.radius*sqrt(random.random()) # sample radius as r*sqrt(x)
#         theta = 2*pi*random.random() # sample angle as unif [0, 2*pi)
#         return self.x_center + radius*cos(theta), self.y_center + radius*sin(theta)