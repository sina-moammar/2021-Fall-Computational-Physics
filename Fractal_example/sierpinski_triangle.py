#importing modules:
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import numpy as np

'''A list of triangles ---> each triangle transform to 3 new triangles ---> A list of triangles ---> ...'''

'''Triagle class:'''
class Triangle:
    def __init__(self,Pos0=np.array([0,0]), Pos1=np.array([50,50*3**0.5]) , Pos2=np.array([100,0]) ):
        self.Pos = np.array([Pos0 , Pos1, Pos2]) #Defines the coordinates vortices of a triangles
    '''
            O->point2

        o       o->midpoint1
        ->midpoint0

    O-      o       O-.point1
    >point0  ->midpoint2  
    '''
    '''A method will generate the 3 new triangles from the input triange:'''
    def newTriangle(self): 
        newTriangles=[] # new triangles will be saved in a list and in the main program add to a the total list
        line21=(self.Pos[2][:]-self.Pos[1][:])/2    #half of vector pointing from point2 to point1 
        line10=(self.Pos[1][:]-self.Pos[0][:])/2    #half of vector pointing from point1 to point0
        line20=(self.Pos[2][:]-self.Pos[0][:])/2    #half of vector pointing from point2 to point0 
        newTriangles.append(Triangle(self.Pos[0][:]+line20 , self.Pos[1][:]+line21 , self.Pos[2][:]))   #midpoint2, midpoint1 , point2
        newTriangles.append(Triangle(self.Pos[0][:] , self.Pos[0][:]+line10 , self.Pos[0][:]+line20))   #point0, midpoint2, midpoint0
        newTriangles.append(Triangle( self.Pos[0][:]+line10 , self.Pos[1][:] , self.Pos[1][:]+line21))  #midpoint2,point1,midpoint1
        return newTriangles

    ''' A method to display a triangle:'''
    def Display(self):
        tr = Polygon(self.Pos)
        return tr



def DisplaySierpienski(n):
    Triangels= [Triangle()]
    for i in range(n):
        NEWTriangels = []
        for tr in Triangels:
            NEWTriangels = NEWTriangels + tr.newTriangle()
        Triangels = NEWTriangels
    plt.rcParams["figure.figsize"] = (50,50)
    ax = plt.axes()
    plt.ylim(0,100)
    plt.xlim(0,100)
    for t in Triangels:
        ax.add_patch(t.Display())

DisplaySierpienski(7)

'''CHANGE IT,AND FILL IT AS YOU DESIRE.'''
class Sierspinski_random_fractal:
    def __init__():

        self.triangle   = None    #input _vertices coordinates_
        self.N_points   = None    #input _number of points_
        self.N_iteration= None    #input _number of times the MidPoint function applies to each point_
        self.points     = None    #generating random coordinates
        
    def plot():
        #plotting the coordinates
        pass

    def Function_MidPint(): 
        #This function should Find the midPoint between an arbitarary point and a random vortix
        #As explained, (N_iteration)
        #in order to obtain Sierpinski Fractal one would apply this function several times, 
        #the more the better!
        pass

    def Sierspinky(self):
        #By calling this function the Fractal (or Fractals!) will be displayed.
        for _ in range(self.N_iteration):
            #calling Function_MidPint
            pass
        pass

s=Sierspinsk_random_fractal()
s.Sierspinky()
