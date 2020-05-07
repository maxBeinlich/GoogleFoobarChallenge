"""
========================================================
Google Foobar challenge - Level 4, Challenge 2
========================================================

Bringing a Gun to a Guard Fight
===============================

Uh-oh - you've been cornered by one of Commander Lambdas elite guards! Fortunately, 
you grabbed a beam weapon from an abandoned guard post while you were running 
through the station, so you have a chance to fight your way out. But the beam weapon 
is potentially dangerous to you as well as to the elite guard: its beams reflect off 
walls, meaning you'll have to be very careful where you shoot to avoid bouncing a 
shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too 
weak to cause damage. You also know that if a beam hits a corner, it will bounce 
back in exactly the same direction. And of course, if the beam hits either you or 
the guard, it will stop immediately (albeit painfully). 

Write a function solution(dimensions, your_position, guard_position, distance) that 
gives an array of 2 integers of the width and height of the room, an array of 2 
integers of your x and y coordinates in the room, an array of 2 integers of the 
guard's x and y coordinates in the room, and returns an integer of the number of 
distinct directions that you can fire to hit the elite guard, given the maximum 
distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the 
elite guard are both positioned on the integer lattice at different distinct 
positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim]. Finally, 
the maximum distance that the beam can travel before becoming harmless will be 
given as an integer 1 < distance <= 10000.

For example, if you and the elite guard were positioned in a room with dimensions 
[3, 2], your_position [1, 1], guard_position [2, 1], and a maximum shot distance 
of 4, you could shoot in seven different directions to hit the elite guard (given as 
vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], 
and [-3, -2]. As specific examples, the shot at bearing [1, 0] is the straight line 
horizontal shot of distance 1, the shot at bearing [-3, -2] bounces off the left wall 
and then the bottom wall before hitting the elite guard with a total shot distance of 
sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting 
the elite guard with a total shot distance of sqrt(5).

Input:
solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9
"""

import math
from fractions import Fraction as frac

def solution(dimensions, your_position, guard_position, distance):
    res, b = {}, {}
    h = int(round(distance / dimensions[1]))+1 # reflections in each vertical direction
    w = int(round(distance / dimensions[0]))+1 # reflections in each horizontal direction

    for i in range(-1*h, h+1, 1):
        for j in range(-1*w, w+1, 1):
            # generating reflected you
            reflected_you = generate_reflection(dimensions, your_position, [j, i])
            yBeam = get_beam(your_position, reflected_you)
            b[yBeam[0]] = min(yBeam[1], b.get(yBeam[0], float('Inf')))
            if res.get(yBeam[0], -1) > yBeam[1]:
                del res[yBeam[0]]

            # generating reflected guard, validating dist to your_position less than given distance
            reflected_guard = generate_reflection(dimensions, guard_position, [j, i])
            gBeam = get_beam(your_position, reflected_guard)
            if gBeam[1] <= distance**2 and (gBeam[0] not in b or b[gBeam[0]] > gBeam[1]):
                res[gBeam[0]] = min(gBeam[1], res.get(gBeam[0], float('Inf')))

            # cr.update(generate_corners(dimensions, your_position, [j, i]))
    return len(res)


def generate_reflection(dimensions, position, reflection):
    # calculate x position of reflection
    x = reflection[0] * dimensions[0] 
    if reflection[0] % 2 == 0:
        x = x + position[0]
    else:
        x = x + dimensions[0] - position[0]
    
    # calculate y position of reflection
    y = reflection[1] * dimensions[1] 
    if reflection[1] % 2 == 0:
        y = y + position[1]
    else:
        y = y + dimensions[1] - position[1]
    return (x, y)

def get_beam(p1, p2):
    deltaX, deltaY = p2[0]-p1[0], p2[1]-p1[1]
    dist_sq = deltaX**2 + deltaY**2
    angle = frac(math.atan2(deltaX, deltaY)*180/math.pi)
    return (angle, dist_sq)

print(solution([3,2], [1,1], [2,1], 4))



