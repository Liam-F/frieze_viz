# Frieze groups
# Marielle Foster for Abstract Algebra, Winter 2016

def find_furthest_x(side, vertices):
    if side == "l":
        x = 1000
        for i in vertices:
            if i.x < x:
                x = i.x

        return x

    if side == "r":
        x = 0
        for i in vertices:
            if i.x > x:
                x = i.x
        return x

def is_possible(vertices):
    for v in vertices:
        if v.x > 1000:
            return False
    return True

def draw_frieze(win, vertices, frieze, trans):

    #shift over to left
    x_left = find_furthest_x("l", vertices)

    for i in vertices:
        i.x = i.x - x_left

    possible = True
    alt = False

    mod4 = 1

    while possible:
        pattern = Polygon(vertices)
        pattern.setFill('gray')
        pattern.setOutline('black')
        pattern.setWidth(4)  # width of boundary line
        pattern.draw(win)

        if frieze == 1:
            for v in vertices:
                v.x = v.x + trans

        if frieze == 2:
            for v in vertices:
                v.x = v.x + trans
                v.y = 600 - v.y
            
        if frieze > 2:
            r = find_furthest_x("r", vertices)

        if frieze == 3:
            for v in vertices:
                v.x = 2*r - v.x + 5
            
        
        if frieze == 4:
            for v in vertices:
                v.x = 2*r - v.x + 5
                v.y = 600 - v.y
        
        if frieze == 5:
            for v in vertices:
                v.x = 2*r - v.x + 5 

                if alt == True:
                    v.y = 600 - v.y
        
        if frieze == 6:
            for v in vertices:
                v.y = 600 - v.y    

                if alt == True:
                        v.x = 2*r - v.x + trans
        
        if frieze == 7:
            for v in vertices:
                if alt == True:
                    v.x = 2*r - v.x + 5
                    if mod4 % 4 == 0:
                        v.x = v.x + trans
                else:
                    v.y = 600 - v.y
                    
                    
            mod4 += 1



        if alt == True:
            alt = False
        else:
            alt = True

        possible = is_possible(vertices)


#   7:
#       1st: y = -y
#       2nd: x = 2f - x



from graphics import *

def main():
    num_points = input("How many points do you want for your polygon? ")
    num_points = int(num_points)

    win = GraphWin('Frieze Patterns', 1000, 600)

    win.setBackground('white')
    

    square = Rectangle(Point(425, 275), Point(575, 125))
    square.draw(win)

    message = Text(Point(win.getWidth()/2, 30), 'Click on %i points inside the box' % num_points) 
    message.setTextColor('black')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)

    # Get and draw vertices of polygon
    vertices = []
    for i in range(num_points):
        pt = win.getMouse()
        pt.draw(win)
        vertices.append(pt)


    # Use Polygon object to draw the triangle
    pattern = Polygon(vertices)
    pattern.setFill('gray')
    pattern.setOutline('black')
    pattern.setWidth(4)  # width of boundary line
    pattern.draw(win)

    message.setText('Please type in the terminal which frieze group and translation you want')

    frieze = input("Which frieze group do you want (any number 1-7)? ")
    frieze = int(frieze)


    while frieze < 1 and frieze > 7:
        frieze = input("That was wrong. Which frieze group do you want (any number 1-7)? ")
        frieze = int(frieze)

    trans = input("How big do you want the translation factor to be? (under 100 recommended) ")

    pattern.undraw()
    square.undraw()
    for pt in vertices:
        pt.undraw()

    draw_frieze(win, vertices, frieze, int(trans))

    message.setText('Click anywhere to quit') # change text message
    win.getMouse()
    win.close() 

main()