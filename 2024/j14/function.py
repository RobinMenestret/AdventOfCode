import re

inputs = open('2024/j14/input.txt').readlines()

width = 101
height = 103
def p1():
    seconds = 6771
    count = [0, 0, 0, 0]
    for robot in inputs :
        (px, py, vx, vy) = [int(x) for x in re.findall("-?[0-9]+", robot)]
        (np_x, np_y) = ((px+vx*seconds)%width, (py+vy*seconds)%height)
        
        if np_x < width//2 :
            if np_y < height//2 :
                count[0]+=1
            elif np_y > height//2 :
                count[1]+=1
        elif np_x > width//2 :
            if np_y < height//2  :
                count[2]+=1
            elif np_y > height//2 :
                count[3]+=1
        #print("x : {}, y : {}, count = {}".format(np_x,np_y, count))
    print(count)
    print(count[0]*count[1]*count[2]*count[3])

def p2():
    for seconds in range(10000):
        room = [['.'] * width for _ in range(height)]
        count = [0, 0, 0, 0]
        for robot in inputs :
            (px, py, vx, vy) = [int(x) for x in re.findall("-?[0-9]+", robot)]
            (np_x, np_y) = ((px+vx*seconds)%width, (py+vy*seconds)%height)
            room[np_y][np_x] = 'O'
            if np_x < width//2 :
                if np_y < height//2 :
                    count[0]+=1
                elif np_y > height//2 :
                    count[1]+=1
            elif np_x > width//2 :
                if np_y < height//2  :
                    count[2]+=1
                elif np_y > height//2 :
                    count[3]+=1
        viz = False
        for i in range(width) :
            count = 0
            for j in range(height) :
                if room[j][i] == "O" :
                    count +=1
            if count > 30 :
                viz = True
        if viz :
            viz_room = '\n'.join([''.join(x) for x in room])
            print(viz_room)
            a = input("ok?")
            if a == 'done':
                print(count)
                print("seconds : {}".format(seconds))
                return

p2()