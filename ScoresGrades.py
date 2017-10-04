# Score: 90 - 100; Grade - A
# Score: 80 - 89; Grade - B
# Score: 70 - 79; Grade - C
# Score: 60 - 69; Grade - D

def Scores_Grades(y):
    grade = []          #created so that the new data points can be stored.
    for x in range(0,y):
        import random
        points = random.randint(60,100)
        grade.append(points)
    for points in grade:            # "points" used instead of "i" because points index is established from random.randint
        if points in range(90, 101):
            print "Score: ", points, "your grade is A"    # "," lets you mix data types when concatenate(adding elements)
        elif points in range(80, 89):
            print "Score: ", points, "your grade is B"
        elif points in range(70,79):
            print "Score: ", points, "your grade is C"
        else:
            print "Score: ", points, "your grade is D"

Scores_Grades(10)