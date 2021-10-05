# Genrative Recursion: Fractals/Math Art

# HtDF Recipie is a little bit different:
    # - Signatre
    # - Purpose
    # - Test Examples: start with BaseCase then gradually from simple to complex
    # - Template: has Three Pieces of critical Question must be pre-prepared
         # "isTrivial(d)" if it is what is the "trivial_answer(d)",
         # it it is Not, How you will reduce to (next-problem(reduced-d)),
         # Did you avoid recursion re computation or you let your running time explode!?


# # Generative Recursion Template..
# def genrec_fn(d):
#     if isTrivial(d):
#         return trivial_answer(d)
#     else:
#         return ... d
#                    genrec_fn(next_problem(d))
# PERFORMANE NOTE: Fractal uses often the recusrion multiple time simultaniously to get same result, Avoid Re_Computation using a local


# Sierpinski Trinagle:

# Analysis:
# Three Way Analysis Algorithm

# BaseCase? Base 'fractal degree': 0!!
CUTOFF = 296
# Degree? 100
DEGREE = 300

import turtle

def draw_trinagle(points, color, myturtle):
    myturtle.fillcolor(color)
    myturtle.up()
    myturtle.goto(points[0][0], points[0][1])
    myturtle.down()
    myturtle.begin_fill()
    myturtle.goto(points[1][0], points[1][1])
    myturtle.goto(points[2][0], points[2][1])
    myturtle.goto(points[0][0], points[0][1])
    myturtle.end_fill()



def getMid(p1, p2):
    return (  (p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2  )



# Number  ->  Image

# given a degree, draw a Sierpinski Trinagle

# def Sierpinski_tri(d, points, myturtle):
#     return draw_trinagle(points, 'black', myturtle)

# I can not provide Test Examples here because i do not know how is th return of turtle
# but i Can draw the Base Case Example from the stub!


## Generative Recursion Template..
# def genrec_fn(d):
#     if isTrivial(d):
#         return trivial_answer(d)
#     else:
#         return ... d
#                    genrec_fn(next_problem(d))


# def Sierpinski_tri(d, points, myturtle):
#     colormap = ['blue','red','green','white','yellow','violet','orange']
#     if d == CUTOFF:
#         draw_trinagle(points, colormap[d%len(colormap)], myturtle)
#     else:
#         draw_trinagle(points, colormap[d%len(colormap)], myturtle)
#         Sierpinski_tri(d-1, [points[0], getMid(points[0], points[1]), getMid(points[0], points[2])],myturtle)
#         Sierpinski_tri(d-1, [points[1], getMid(points[0], points[1]), getMid(points[1], points[2])],myturtle)
#         Sierpinski_tri(d-1, [points[2], getMid(points[2], points[1]), getMid(points[0], points[2])],myturtle)


# def main():
#     myturtle = turtle.Turtle()
#     mywindow = turtle.Screen()
#     triange_points = [[-DEGREE, -DEGREE/2], [0, DEGREE], [DEGREE, -DEGREE/2]]
#     square_points  = [[-DEGREE/2, -DEGREE/2], [-DEGREE/2, DEGREE/2], [DEGREE/2, DEGREE/2], [DEGREE/2, -DEGREE/2]]
#     Sierpinski_tri(DEGREE, triange_points, myturtle)
#
#     mywindow.exitonclick()
#
# if __name__=='__main__':
#     main()

# ==
# ==================================================================================================================
def s(d, l):

    if d == 0: # stop conditions

        # draw filled rectangle

        turtle.color('black')
        turtle.begin_fill()
        for _ in range (4):
            turtle.forward(l)
            turtle.left(90)
        turtle.end_fill()

    else: # recursion

        # around center point create 8 smalles rectangles.
        # create two rectangles on every side
        # so you have to repeat it four times

        for _ in range(4):
            # first rectangle
            s(d-1, l/3)
            turtle.forward(l/3)

            # second rectangle
            s(d-1, l/3)
            turtle.forward(l/3)

            # go to next corner
            turtle.forward(l/3)
            turtle.left(90)

        # update screen
        turtle.update()

# --- main ---

# stop updating screen (to make it faster)
# turtle.tracer(0)

# start
s(4, 400)

# event loop
turtle.done()
