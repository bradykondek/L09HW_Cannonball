# Import libraries
from math import sin, cos
from matplotlib import pyplot as plt
import random

# Print Interface class
class Print_Iface:

    # Print function for this class
    def plotCannonball(self, x, y):
        
        print("The ball is at (%.1f, %.1f)" % (x, y))
        plt.scatter(x, y)
        plt.pause(.01)

## Represent a cannonball, tracking its position and velocity.
#
class Cannonball:
    
    # Establish HAS-A relationship with Print_Iface class
    print_iface_cls = Print_Iface
    
    ## Create a new cannonball at the provided x position.
    #  @param x the x position of the ball
    #
    def __init__(self, x):
        self._x = x
        self._y = 0
        self._vx = 0
        self._vy = 0
        self.Print_Iface = self.print_iface_cls()  # create an instance of the class

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
        
        # Return value of x instance variable
        return self._x

    ## Get the current y position of the ball.
    #  @return the y position of the ball
    #
    def getY(self):

        # Return value of y instance variable
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

            # Call plotCannonball function within Print_Iface class to plot on graph
            self.Print_Iface.plotCannonball(self.getX(), self.getY())
            self.move(0.1, user_grav)

# Crazyball class
class Crazyball(Cannonball):
    
    # Move function (modified for this class)
    def move(self, sec, grav=9.81):
        
        # Generate a random value
        self.rand_q = random.randrange(0, 10)

        # If x coordinate is less than 400
        if self.getX() < 400:
            
            # Update x instance variable with random number
            self._x = self._x + self.rand_q

        # If x coordinate is greater than/equal to 400
        if self.getX() >= 400:
            
            # Update x instance variable with random number
            self._x = self._x - self.rand_q

# Get option from user
def getOption():

    while True:

        # Declare list of possible options
        validOptions = [1, 2, 3, 4]
        
        # Prompt user with choices
        print("1: Earth Gravity")
        print("2: Moon Gravity")
        print("3: Crazy Trajectory")
        print("4: Quit")

        # Verify option is valid, otherwise inform the user
        try:  # attempt to do
            
            # Prompt user for option
            userOption = int(input("Select an option: "))

            # Verify option is within range
            if(userOption in validOptions):  # if choice is in list of valid options
                
                # Return user choice
                return userOption
            
            else:  # if choice is not in list of valid options

                # Print error message
                print("Invalid option, must be a value in range 1-4.\n")

        except ValueError:  # if ValueError arises from not being an integer
            
            # Print error message
            print("Input must be of integer data type.\n")

# Get angle and velocity information
def getStartInfo():

    # Prompt user for starting angle
    angle = float(input("Enter starting angle: "))

    # Prompt user for initial velocity
    v = float(input("Enter initial velocity: "))

    # Return starting angle and initial velocity
    return angle, v 

# Shoot cannonball
def shoot(cannonball, angle, v, option):

    # Shoot cannonball depending on user-selected option
    if(option == 1):  # if user selected option 1, earth gravity
        
        # Shoot cannonball using earth gravity
        cannonball.shoot(angle, v, 9.81)

    elif(option == 2):  # if user selected option 2, moon gravity
        
        # Shoot cannonball using moon gravity
        cannonball.shoot(angle, v, 1.625)

    elif(option == 3):  # if user selected option 3, crazy trajectory
        
        # Create Crazyball object
        cannonball = Crazyball(0)
        
        # Shoot cannonball using crazy trajectory
        cannonball.shoot(angle, v, 9.81)

# Main function
def main():
    ##
    #  Demonstrate the cannonball class.
    #
    #from cannonball import Cannonball

    # Loop program until user chooses to quit
    while True:

        # Get angle and velocity information
        angle, v = getStartInfo()

        # Declare Cannonball object
        c = Cannonball(0)

        # Get option from user
        userOption = getOption()
        
        # If user chooses option to quit, break out of while loop
        if(userOption == 4):

            # Break from while loop
            break
        
        # Shoot cannonball
        shoot(c, angle, v, userOption)

# Run program
if __name__ == '__main__':

    # Run main function
    main()