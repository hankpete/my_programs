# Gravitating Objects 2D
# old program from 1/12/14 that I redid with physics and calc knowledge
# Henry Peterson 2/26/16

print("Loading...")

import matplotlib.pyplot as plt
import numpy as np

G = 6.673848e-11    # grav const
t = .1             # time interval 

def run_through():
    
    """ main loop """ 
    
    ## object 1 specs
    #print("\nObject 1 begins at the origin.")
    #x1 = 0
    #y1 = 0
    #m1 = float(input("Mass of object 1 (kg): "))
    #vx1 = float(input("Initial x-component of velocity of object 1 (m/s): "))
    #vy1 = float(input("Initial y-component of velocity of object 1 (m/s): "))

    ##object 2 specs
    #m2 = float(input("\nMass of object 2 (kg): "))
    #x2 = float(input("Starting x-coordinate of object 2 (m): "))
    #y2 = float(input("Starting y-coordinate of object 2 (m): "))
    #vx2 = float(input("Initial x-component of velocity of object 2 (m/s): "))
    #vy2 = float(input("Initial y-component of velocity of object 2 (m/s): "))

    #its = int(input("Number of iterations (s): "))
 
    # debugging
    x1, y1, m1, vx1, vy1, m2, x2, y2, vx2, vy2, its = -10.0, 0.0, 10000000000.0, 0.0, -0.1155, 10000000000.0, 90.0, 0.0, 0.0, 0.1155, 100

    # object 1 lists
    x1_list = [x1]
    y1_list = [y1]
    vx1_list = [vx1]
    vy1_list = [vy1]
    ax1_list = []
    ay1_list = []

    # object 2 lists
    x2_list = [x2]
    y2_list = [y2]
    vx2_list = [vx2]
    vy2_list = [vy2]
    ax2_list = []
    ay2_list = []
    
    while its > 0:
        
        # current situation
        d = np.sqrt((x2-x1)**2 + (y2-y1)**2)
        angle = np.arccos(np.absolute((x2-x1)/d))

        # object 1 changes
        a1 = G*m2/d**2
        
        if x1 > x2:
            ax1_list.append(-(a1)*np.cos(angle))
        elif x1 < x2:
            ax1_list.append(a1*np.cos(angle))
        else:
            ax1_list.append(0.0)

        if y1 > y2:
            ay1_list.append(-(a1)*np.sin(angle))
        elif y1 < y2:
            ay1_list.append(a1*np.sin(angle))
        else:
            ay1_list.append(0.0)
        
        vx1_list.append(vx1_list[0] + np.sum(ax1_list)*t)
        vy1_list.append(vy1_list[0] + np.sum(ay1_list)*t)

        x1 = x1_list[0] + np.sum(vx1_list)*t
        y1 = y1_list[0] + np.sum(vy1_list)*t
        x1_list.append(x1)
        y1_list.append(y1)

        # object 2 changes
        a2 = G*m1/d**2
        
        if x2 > x1:
            ax2_list.append(-(a2)*np.cos(angle))
        elif x2 < x2:
            ax2_list.append(a2*np.cos(angle))
        else:
            ax2_list.append(0.0)

        if y2 > y1:
            ay2_list.append(-(a2)*np.sin(angle))
        elif y2 < y1:
            ay2_list.append(a2*np.sin(angle))
        else:
            ay2_list.append(0.0)

        vx2_list.append(vx2_list[0] + np.sum(ax2_list)*t)
        vy2_list.append(vy2_list[0] + np.sum(ay2_list)*t)

        x2 = x2_list[0] + np.sum(vx2_list)*t
        y2 = y2_list[0] + np.sum(vy2_list)*t
        x2_list.append(x2)
        y2_list.append(y2)

        its -= 1

    plt.title("Gravitating Objects 2D")
    plt.plot(x1_list, y1_list, "ro")
    plt.plot(x2_list, y2_list, "bo")
    plt.show() 

def main():

    """ loops program to try over """
    
    run_through()

    #again = None
    #while again != "n":
    #    run_through()
    #    again = input("\nAgain? ").lower()
    #input("\nPress enter to exit.")

# run it
main()
