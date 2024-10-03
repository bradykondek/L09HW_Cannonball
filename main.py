from math import sin, cos
from matplotlib import pyplot as plt
import random

# Print Interface class
class PrintInterface:

    # Print function for this class
    def mainPrint(self, x, y):
        
        print("The ball is at (%.1f, %.1f)" % (self.getX(), self.getY()))
        plt.scatter(x, y)
        plt.pause(.01)

## Represent a cannonball, tracking its position and velocity.
#
class Cannonball:
    
    # Establish HAS-A relationship with PrintInterface class
    printInterface_cls = PrintInterface
    
    ## Create a new cannonball at the provided x position.
    #  @param x the x position of the ball
    #
    def __init__(self, x):
        self._x = x
        self._y = 0
        self._vx = 0
        self._vy = 0
        self.printInterface = self.printInterface_cls  # relate class to this class

    ## Move the cannon ball, using its current velocities.
    #  @param sec the amount of time that has elapsed.
    #
    def move(self, sec, grav=9.81):
        dx = self._vx * sec
        dy = self._vy * sec

        self._vy = self._vy - grav * sec

        self._x = self._x + dx
        self._y = self._y + dy

    ## Get the current x position of the ball.
    #  @return the x position of the ball
    #
    def getX(self):
        return self._x

    ## Get the current y position of the ball.
    #  @return the y position of the ball
    #
    def getY(self):
        return self._y

    ## Shoot the canon ball.
    #  @param angle the angle of the cannon
    #  @param velocity the initial velocity of the ball
    #
    def shoot(self, angle, velocity, user_grav):
        self._vx = velocity * cos(angle)
        self._vy = velocity * sin(angle)
        self.move(0.1, user_grav)

        while self.getY() > 1e-14:
            self.printInterface.mainPrint(self._vx, self._vy)
            self.move(0.1, user_grav)

# Crazyball class
class Crazyball(Cannonball):
    
    # Move function (modified for this class)
    def move(self, sec, grav=9.81):
        
        #super().__init__(_x, _y, _vx, _vy)
        
        # Calculate the change in posiiton based on velocity
        dx = self._vx * sec
        dy = self._vy * sec

        # Update the vertical velocity to account for gravity
        self._vy = self._vy - grav * sec

        # Update the object's positon
        self._x = self._x + dx
        self._y = self._y + dy

        # Generate a random value
        self.rand_q = random.randrange(0, 10)

        # Update x with random number
        if(self.getX() < 400):  # if x is less than 400

            # Adjust x by random number
            self._x += self.rand_q

        # Update y with random number
        if(self.getY() < 400):  # if y is less than 400

            # Adjust y by random number
            self._y += self.rand_q

# Main function
def main():
    ##
    #  Demonstrate the cannonball class.
    #
    #from cannonball import Cannonball

    angle = float(input("Enter starting angle:"))
    v = float(input("Enter initial velocity:"))
    c = Cannonball(0)
    c.shoot(angle, v, 9.81)

# Run program
if __name__ == '__main__':
    main()  # run main function