import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

speed = "100"
num_loop = 0
# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # print(f"x = {x}, y = {y}", file=sys.stderr, flush=True)
    # print(f"check x = {next_checkpoint_x}, check y = {next_checkpoint_y}", file=sys.stderr, flush=True)
    # print(f"angel = {next_checkpoint_angle}", file=sys.stderr, flush=True)
    # print(f"loop: {num_loop}", file=sys.stderr, flush=True)

    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        speed = 0
    else:
        if int(next_checkpoint_dist) > 10000 and num_loop > 130:
            speed = 'BOOST'
        else:
            speed = 100

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + f" {speed} {next_checkpoint_dist} {num_loop}")
    num_loop+=1
