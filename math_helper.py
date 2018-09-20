import math 

''' Welcome to the math helper.
'''

    
    
def pythag_theo(a,b):
    ''' This function calculates the pythagorean theorem for the user
        while also checking for impossible inputs
        
        >>> pythag_theo(3,4)
        5.0
    
        >>> pythag_theo(0,5)
        Traceback (most recent call last):
        ...
        ValueError: a or b must be positive
         
        >>> pythag_theo(-5,5)
        Traceback (most recent call last):
        ...
        ValueError: a or b must be positive
    
    '''
    if a<= 0 or b <= 0:
        raise ValueError("a or b must be positive")
    c = ((a**2)+(b**2))
    return math.sqrt(c)


def mid_point(x1,y1,x2,y2):
    ''' This function finds the midpoint between two points
    
        >>> mid_point(1,1,10,1)
        (4.5, 0.0)
        
        >>> mid_point(32,16,64,32)
        (16.0, 8.0)
        
        >>> mid_point(50,20,50,20)
        Traceback (most recent call last):
            ...
        ValueError: x1,x2 and y1,y2 cannot be equal
    
    
    '''
    if x1 == x2 and y1==y2:
        raise ValueError('x1,x2 and y1,y2 cannot be equal')
    return(x2-x1)/2,(y2-y1)/2

def distance_formula(x1,x2,y1,y2):
    ''' This function finds the distance between two points.

        >>> distance_formula(0,10,0,0)
        10.0
        
        
        >>> distance_formula(0,0,0,0)
        Traceback (most recent call last):
            ...
        ValueError: x1,x2 and y1,y2 cannot be equal
        
        
    '''
    if x1 == x2 and y1==y2:
        raise ValueError('x1,x2 and y1,y2 cannot be equal')
    return math.sqrt((x2-x1)**2)+((y2-y1)**2)
    
    
def quadratic_equation(a,b,c):
    ''' This formula utilizes the qaudratic equation to
        find the zeros
        
        >>> quadratic_equation(2,-14,24)
        '4.0 and 3.0'
        
        >>> quadratic_equation(1,2,1)
        '-1.0'
        
    '''
    if a==0:
        print('No real answer')
    ans = (-1*b + math.sqrt(b**2-4*a*c))/(2*a), (-1*b - math.sqrt(b**2-4*a*c))/(2*a)
    if ans[0]==ans[1]:
        return f'{ans[0]}'
    else:
        return f'{ans[0]} and {ans[1]}'

def main():
    #pythag_theo
    pass

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #main()
    
    
    

    