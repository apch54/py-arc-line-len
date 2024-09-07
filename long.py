# Calculating the length of an func function arc

from math import pi 
# import other methods if necessary

def func (x):return x 
# func must be define, here it is func(x) = x    

# a, b is the calculation interval
# nb : number iterations

def len_arc (a, b, nb = 100):
    lg = 0 # initialating len of arc
    dx = (b - a) / nb # value of incrementation on x axe
    x0, y0 = a, func(a) # x0,y0 initialisation
    for i in range(nb): 
        x1, y1 = a +(i+1)*dx,func(a +(i+1)*dx)
        dl = ( dx**2 + (y1-y0)**2)**.5
        lg += dl # len arc increentation
        x0, y0 = x1, y1 # and again to nb value
    return lg


if __name__ == "__main__":

    # test the method len_arc
    # l = len_arc(0,2*mt.pi, 200)
    # l = len_arc(0, 2*mt.pi) # 100 iteration

    l = len_arc(0, 1, 50)
    print(l,50, l-pow(2,.5) ) 

    l = len_arc(0, 1, 100)
    print(l,100,l-pow(2,.5) )  

  