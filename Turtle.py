import turtle
turtle.bgcolor("black")
turtle.speed(1000)
for i in range(90):
    for colors in ["red","magenta","blue","cyan","yellow","white"]:
        turtle.color(colors)
        turtle.pensize(5)
        turtle.left(12)
        a = 1
        while a <= 5:  #a ko value ley chai euta loop saiye paxi kun point bata suru garney determine garxa
            turtle.forward(150) #forward ley chai side ko length determine garxa
            turtle.left(90) #left ley chai figure kun banxa determine garxa 360/90 =4 so square/rectangle banxa
            a += 1
