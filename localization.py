colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []
X = len(colors[0])
Y = len(colors)
# maximum confusion
p = [[1.0/(X*Y) for x in range(X)] for y in range(Y)]

def sense(p, Z):
    # p[x,y] = p[x,y]*(sr if p[x,y]==Z else 1-sr)
    q = [[a*b for a,b in zip(p[y], [sensor_right if c==Z else 1-sensor_right
                                    for c in colors[y]])]
         for y in xrange(len(colors))]
    s = sum([sum(row) for row in q])
    return [[r/s for r in row] for row in q]

def move(p, U):
    # convolution - p[x,y] = p_move*p[x-U(x),y-U(y)]+(1-p_move)*p[x,y]
    dy, dx = U
    return [[p[(y-dy)%Y][(x-dx)%X]*p_move+p[y][x]*(1-p_move)
             for x in xrange(X)]
            for y in xrange(Y)]

for U, Z in zip(motions, measurements):
    p = sense(move(p, U), Z)

#Your probability array must be printed
#with the following code.

show(p)
