from display import *
from matrix import *
from math import *

def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point(points,x0,y0,z0)
    add_point(points,x1,y1,z1)
    add_point(points,x2,y2,z2)
    
def normal(x, y, z, x1, y1, z1, x2, y2, z2):
    a = [x1-x, y1-y, z1-z]
    b = [x2-x, y2-y, z2-z]

    l=[]

    l.append((a[1]*b[2])-(a[2]*b[1]))
    l.append((a[2]*b[0])-(a[0]*b[2]))
    l.append((a[0]*b[1])-(a[1]*b[0]))

    return l

def draw_polygons( points, screen, color ):
   # print points
    if len(points) < 3:
        print 'Need at least 3 points to draw'
        return

    i = 0
    while i < len(points) - 2:
    # print i
        x = points[i][0]
        y = points[i][1]
        z = points[i][2]

        x1 = points[i+1][0]
        y1 = points[i+1][1]
        z1 = points[i+1][2]

        x2 = points[i+2][0]
        y2 = points[i+2][1]
        z2 = points[i+2][2]

        v = normal(x, y, z, x1 , y1, z1, x2, y2, z2)

        if (v[2]> 0):
            draw_line(int(x), int(y), int(x1), int(y1), screen, color)
            draw_line(int(x1), int(y1), int(x2), int(y2), screen, color)
            draw_line(int(x), int(y), int(x2),int(y2), screen, color)
        i += 3
                
def add_box( points, x, y, z, width, height, depth ):
    w = x + width
    h = y - height
    d = z - depth

    add_polygon(points, x, y, d, x, h, z, x, y, z)
    add_polygon(points, x, y, d, x, h, d, x, h, z)
    add_polygon(points, x, h, z, x, h, d, w, h, z)
    add_polygon(points, w, h, z, x, h, d, w, h, d)
    add_polygon(points, w, y, z, w, h, d, w, y, d)
    add_polygon(points, w, y, z, w, h, z, w, h, d)
    add_polygon(points, x, y, z, w, y, z, x, y, d)
    add_polygon(points, x, y, d, w, y, z, w, y, d)
    add_polygon(points, x, y, d, w, y, d, x, h, d)
    add_polygon(points, x, h, d, w, y, d, w, h, d)
    add_polygon(points, x, y, z, x, h, z, w, h, z)
    add_polygon(points, x, y, z, w, h, z, w, y, z)

def add_sphere( edges, cx, cy, cz, r, step ):
    points = generate_sphere(cx, cy, cz, r, step)
    counter = int(1/step + 0.1)
    
    lat_start = 0
    lat_stop = counter
    longt_start = 0
    longt_stop = counter
    
    counter +=1

    for lat in range(lat_start,lat_stop):
        for longt in range(longt_start, longt_stop+1):
            i = lat * counter + longt
            
            # 4 points are i, i+1, i+counter, i+(counter+1)

            #i
            x = points[i][0]
            y = points[i][1]
            z = points[i][2]
            
            #i+1
            x1 = points[(i + 1) % len(points)][0]
            y1 = points[(i + 1) % len(points)][1]
            z1 = points[(i + 1) % len(points)][2]

            #i+counter
            x2 = points[(i + counter) % len(points)][0]
            y2 = points[(i + counter) % len(points)][1]
            z2 = points[(i + counter) % len(points)][2]

            #i+(counter+1)
            x3 = points[(i + counter + 1) % len(points)][0]
            y3 = points[(i + counter + 1) % len(points)][1]
            z3 = points[(i + counter + 1) % len(points)][2]

            add_polygon(edges, x, y, z, x1, y1, z1, x3, y3, z3)
            add_polygon(edges, x, y, z, x3, y3, z3, x2, y2, z2)
    
       
def generate_sphere( cx, cy, cz, r, step ):
    points = []
    num_steps = int(1/step+0.1)
    
    rot_start = 0
    rot_stop = num_steps
    circ_start = 0
    circ_stop = num_steps
            
    for rotation in range(rot_start, rot_stop):
        rot = step * rotation
        for circle in range(circ_start, circ_stop+1):
            circ = step * circle

            x = r * math.cos(math.pi * circ) + cx
            y = r * math.sin(math.pi * circ) * math.cos(2*math.pi * rot) + cy
            z = r * math.sin(math.pi * circ) * math.sin(2*math.pi * rot) + cz

            points.append([x, y, z])
            #print 'rotation: %d\tcircle%d'%(rotation, circle)
    return points
        
def add_torus( edges, cx, cy, cz, r0, r1, step ):
    points = generate_torus(cx, cy, cz, r0, r1, step)
    counter = int(1/step+0.1)
    
    lat_start = 0
    lat_stop = counter
    longt_start = 0
    longt_stop = counter

    for lat in range(lat_start, lat_stop):
        for longt in range(longt_start, longt_stop):
            i = lat * counter + longt

            # 4 points are i, i+1, i+counter, i+(counter+1)

            #i
            x = points[i][0]
            y = points[i][1]
            z = points[i][2]
            
            #i+1
            x1 = points[(i+1) % len(points)][0]
            y1 = points[(i+1) % len(points)][1]
            z1 = points[(i+1) % len(points)][2]

            #i+counter
            x2 = points[(i + counter) % len(points)][0]
            y2 = points[(i + counter) % len(points)][1]
            z2 = points[(i + counter) % len(points)][2]

            #i+(counter+1)
            x3 = points[(i + counter + 1) % len(points)][0]
            y3 = points[(i + counter + 1) % len(points)][1]
            z3 = points[(i + counter + 1) % len(points)][2]

            add_polygon(edges, x, y, z, x1, y1, z1, x2, y2, z2)
            add_polygon(edges, x1, y1, z1, x3, y3, z3, x2, y2, z2)

def generate_torus( cx, cy, cz, r0, r1, step ):
    points = []
    num_steps = int(1/step+0.1)
    
    rot_start = 0
    rot_stop = num_steps
    circ_start = 0
    circ_stop = num_steps

    print num_steps
    
    for rotation in range(rot_start, rot_stop):
        rot = step * rotation
        for circle in range(circ_start, circ_stop):
            circ = step * circle

            x = math.cos(2*math.pi * rot) * (r0 * math.cos(2*math.pi * circ) + r1) + cx;
            y = r0 * math.sin(2*math.pi * circ) + cy;
            z = -1*math.sin(2*math.pi * rot) * (r0 * math.cos(2*math.pi * circ) + r1) + cz;

            points.append([x, y, z])
    return points

def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy
    t = step

    while t <= 1.00001:
        x1 = r * math.cos(2*math.pi * t) + cx;
        y1 = r * math.sin(2*math.pi * t) + cy;

        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        t+= step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    t = step
    while t <= 1.00001:
        x = xcoefs[0] * t*t*t + xcoefs[1] * t*t + xcoefs[2] * t + xcoefs[3]
        y = ycoefs[0] * t*t*t + ycoefs[1] * t*t + ycoefs[2] * t + ycoefs[3]
                
        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t+= step

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return
    
    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)    
        point+= 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    
def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )
    



def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
