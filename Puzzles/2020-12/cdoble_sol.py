# Submitted by Carlos Doble 12/14/2020

import math
def cleanup(directions):
    clean_directions = ""
    acceptable = "NESW;"
    for char in directions:
        if char in acceptable:
            clean_directions += char
    return clean_directions

def yards_to_miles(distance):
    miles = distance * 0.00056818
    return round(miles,1)

def direct_distance(direction):
    distx = 0
    disty = 0
    for char in direction:
        if char == "N":
            disty += 100
        elif char == "S":
            disty -= 100
        elif char == "E":
            distx += 100
        else:
            distx -= 100
    return math.sqrt(distx**2 + disty**2)

def dist_total_house(direction):
    return direct_distance(direction) + len(direction)*100

def longest_distance(distances):
    distances_list = []
    for direction in distances:
        distances_list.append(yards_to_miles(direct_distance(direction)))
    return max(distances_list)

def main():
    corpus = open("corpus.txt", "r").read()
    #corpus = "N;NNE;EESNW;EWSWSSE"

    corpus = cleanup(corpus)
    new_corpus = ""
    for char in corpus:
        if char == ";":
            new_corpus += " "
        else:
            new_corpus += char
    new_list = new_corpus.split()
    total_distance = 0
    for direction in new_list:
        total_distance += dist_total_house(direction)
    total_distance = yards_to_miles(total_distance)
    long = longest_distance(new_list)
    print(round(total_distance + long,1))
    
if __name__ == "__main__":
    main()



