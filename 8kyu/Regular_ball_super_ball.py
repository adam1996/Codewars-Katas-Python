"""

Regular Ball Super Ball (8Kyu)
https://www.codewars.com/kata/53f0f358b9cb376eca001079

Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"
"""

class Ball(object):
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type
    
