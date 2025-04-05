#Q4
def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return 1+hailstone(n//2)

def odd(n):
    "*** YOUR CODE HERE ***"
    if(n==1):
        return 1
    else:
        return 1+hailstone(3*n+1)

#Q5
def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)
    
def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        print(f"Player {who} says {i}")
        if i == n:
            return who
        #"*** YOUR CODE HERE ***"
        if (has_seven(i) or i%7==0):
            direction=-direction
        who=(who+direction+k)%k
        if who<1:
            who=k
        return f(i+1,who,direction)
            
        
        
    return f(1, 1, 1)

