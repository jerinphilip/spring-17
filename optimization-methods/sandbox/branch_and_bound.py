from math import ceil, floor
from pprint import pprint
from copy import deepcopy

global_max = -1 
count = 0
tree = {}

fx1 = lambda x: min(6-x, (45-5*x)/9)
fx2 = lambda x: min(6-x, (45-9*x)/5)

visited = []

feasible = lambda x, y: x + y <= 6.0 and 5*x + 9*y <= 45 and x >=0 and y >=0
integers = lambda x, y: int(x) == x and int(y) == y

z = lambda x, y: 5*x + 8*y
def branch(x1, x2, parent):
    global global_max
    global count
    if ((x1, x2) in visited):
        return 

    visited.append((x1, x2))

    count += 1
    proper_count = deepcopy(count)

    tree[parent]["children"].append(proper_count)
    tree[proper_count] = {}
    tree[proper_count]["children"] = []
    tree[proper_count]["state"] = (x1, x2, z(x1, x2), feasible(x1, x2))

    #print("x1 = %lf, x2 = %lf, z = %lf"%(x1, x2, z(x1, x2)))


    if ( not feasible(x1, x2)):
        return

    if ( z(x1, x2) <= global_max ):
        return

    if integers(x1, x2):
        global_max = z(x1, x2)

    if int(x1) != x1:
        #x1 = min(6-x2, (45-9*x2)/5)
        #x1 = fx2(x2)
        ux1 = ceil(x1)
        lx1 = floor(x1)

        # Case ux2
        #ux2 = min(6-ux1, (45-5*ux1)/9)
        ux2 = fx1(ux1)
        branch(ux1, ux2, proper_count)

        # Case lx2
        #lx2 = min(6-lx1, (45-5*ux2)/9)
        lx2 = fx1(lx1)
        branch(lx1, lx2, proper_count)
        
    if int(x2) != x2:
        #x2 = min(6-x1, (45-5*x1)/9)
        #print("Branching at x1")
        #x2 = fx1(x1)
        ux2 = ceil(x2)
        lx2 = floor(x2)

        # Case ux2
        #ux1 = min(6-ux2, (45-9*ux2)/5)
        ux1 = fx2(ux2)
        #print("Trying %lf %lf"%(ux1, ux2))
        branch(ux1, ux2, proper_count)

        # Case lx2
        #lx1 = min(6-lx2, (45-9*lx2)/5)
        lx1 = fx2(lx2)
        #print("Trying %lf %lf"%(lx1, lx2))
        branch(lx1, lx2, proper_count)




#print(integers(1, 2))
#print(integers(1, 2.3))
#exit()
tree[0] = {}
tree[0]["children"] = []
branch(9/4, 15/4, 0)
#pprint(tree, indent=4)

def gen_dot(tree):
    s = "digraph{\n"
    for u in tree:
        edges = tree[u]["children"]
        for v in edges:
            s += "%d -> %d;\n"%(u, v)
    for u in tree:
        if "state" in tree[u]:
            x1, x2, z, feasible = tree[u]["state"]
            node_str = "x1 = %.6lf, x2 = %.6lf\\n z = %.6lf\\n feasible=%s"%(x1, x2, z, feasible)
            dot_str = "%d [label=\"%s\"]\n"%(u, node_str)
            s += dot_str
    s += "}"
    return s

    


print(gen_dot(tree))
        
