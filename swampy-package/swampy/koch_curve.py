# Jackie Gushue

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()

def koch(turtle, len):
    """Draw a Koch curve."""
    pd(turtle)
    if len < 3:
    	fd(turtle, len)   # draw a straight line
    	return
    div_len = len/3.0
    koch(turtle, div_len)
    lt(turtle, 60)
    koch(turtle, div_len)
    rt(turtle, 120)
    koch(turtle, div_len)
    lt(turtle, 60)
    koch(turtle, div_len)

koch(bob, 75)


        