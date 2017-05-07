from operator import mul, add, or_, and_
from functools import reduce, partial

def dot(c, x):
    return sum(map(mul, c, x))

def find_min_unset(unset_v, zc):
    assert(zc)
    tuples = zip(unset_v, list(map(lambda x: zc[x], unset_v)))
    min_entry = min(tuples, key=lambda x: x[1])
    return min_entry[0]

def violated(state, C, b):
    violation = lambda i: dot(C[i], state) < b[i]
    vls = list(map(violation, range(len(b))))
    return vls

def impossible_violation(unset, state, c, b_j):
    mstate = list(state)
    for i in unset:
        if c[i] > 0: mstate[i] = 1
        else: mstate[i] = 0
    return (dot(c, mstate) < b_j)


tree = {}
hashmap = {}
count = 0
        

def branch(unset, state, zc, C, b):
    global count
    parent = hashmap[state]
    
    if not unset:
        return

    infeasible = reduce(or_, violated(state, C, b))
    if infeasible:
        tree[parent]["feasible"] = "infeasible"
        # Check if possible to maximize further.
        f = partial(impossible_violation, unset, state)
        impossible = reduce(or_, map(f, C, b))

        if not impossible:
            mstate = list(state)
            munset = list(unset)
            ei = find_min_unset(unset, zc)

            munset.remove(ei)
            unset = tuple(munset)

            # Set to 1, branch
            mstate[ei] = 1
            cstate = tuple(mstate)
            count = count + 1
            hashmap[cstate] = count
            tree[parent]["children"].append(count)
            tree[count] = {
                    "children" : [],
                    "state" : cstate
            }
            branch(unset, cstate, zc, C, b)


            # Set to 0, branch
            mstate[ei] = 0
            cstate = tuple(mstate)
            count = count + 1
            hashmap[cstate] = count
            tree[parent]["children"].append(count)
            tree[count] = {
                    "children" : [],
                    "state" : cstate
            }
            branch(unset, cstate, zc, C, b)
            tree[parent]["possible"] = "possible"
        else:
            tree[parent]["possible"] = "impossible"
    else:
        tree[parent]["possible"] = "impossible"
        tree[parent]["feasible"] = "feasible"
        tree[parent]["z"] = dot(zc, state)
        #print(state, ": z = %lf"%(dot(zc, state)))



state = (0, 0, 0, 0, 0, 0)
unset = (0, 1, 2, 3, 4, 5)
coeff = (3, 5, 6, 9, 10, 10)

C = [
        [-2, 6, -3, 4, 1, -2],
        [-5, -3, 1, 3, -2, 1],
        [5, -1, 4, -2, 2, -1]
    ]

b = [ 2, -2, 3 ]



hashmap[state] = count
tree[count] = {}
tree[count]["children"] = []
tree[count]["state"] = state

def pretty_print(state, C, b):
    s = ""
    for i in range(len(b)):
        lhs = dot(C[i], state)
        flag = lhs >= b[i]
        s += "%.3lf >= %.3lf, %s\\n"%(lhs, b[i], flag)
    return s


def gen_dot(tree):
    s = "digraph{\n"
    for u in tree:
        edges = tree[u]["children"]
        for v in edges:
            s += "%d -> %d;\n"%(u, v)
    for u in tree:
        if "state" in tree[u]:
            node_str = str(tree[u]["state"])
            c_str = pretty_print(tree[u]["state"], C, b)
            status_str = "%s, %s "%(tree[u]["feasible"], tree[u]["possible"])
            z_str = ""
            if "z" in tree[u]:
                z_str = tree[u]["z"]
            dot_str = "%d [label=\"%s\\n%s\\n%s\\n%s\"]\n"%(u, node_str, status_str, z_str, c_str)
            s += dot_str
    s += "}"
    return s

#print(violated(state, C, b))
branch(unset, state, coeff, C, b)
print(gen_dot(tree))
    
