# https://stackoverflow.com/questions/2049582/how-to-determine-if-a-point-is-in-a-2d-triangle


# Basic idea -- get area of triangle ABC, then get areas of ABD, BCD, and ACD and add them.  If their sum is the same is ABC, the D must be inside of ABC.

def area(a, b, c):
    return abs(0.5*(a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1])))


def solve_area(d,a,b,c):
    orig_area = area(a,b,c)

    t1 = area(d,a,b)
    t2 = area(d,a,c)
    t3 = area(d,b,c)

    return round(orig_area,3) == round(t1+t2+t3,3)



def solve_puzzle():
    contains = 0
    with open('triangles.txt') as f:
        for line in f:
            points = line.strip().split(",")
            a = [int(x) for x in points[:2]]
            b = [int(x) for x in points[2:4]]
            c = [int(x) for x in points[4:6]]
            d = [int(x) for x in points[6:]]
            if solve_area(d,a,b,c):
                contains += 1
                print(line)
    print(contains)

from random import randint

def generate_points():
    this_line = ""
    for i in range(7):
        this_line += str(randint(-1000,1000)) +","
    this_line += str(randint(-1000,1000))
    return this_line

def create_data():
    with open("triangles.txt","w") as f:
        for i in range(10000):
            f.write(generate_points() + "\n")

#create_data()
solve_puzzle()
# ANSWER 786