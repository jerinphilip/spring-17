import numpy as np
from operator import add
from functools import reduce

np.random.seed(42)

uw_adj = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: [1]
}

fillcolor = {
        1: "yellow",
        2: "green",
        3: "skyblue",
        4: "orange"
}

def gendot(uw_adj):
    s = 'digraph G {\n'
    s += '   rankdir = LR; \n'
    for v in uw_adj:
        for u in uw_adj[v]:
            s += '   %d -> %d;\n'%(v, u)
    for v in uw_adj:
        s += '   %d [style="filled", fillcolor="%s", shape="circle"];\n'%(v, fillcolor[v])
    s += '}'
    return s

def genfdot(uw_adj):
    f = lambda x: np.random.randint(1, 10)
    s = 'digraph G {\n'
    s += '   rankdir = LR; \n'
    for v in uw_adj:
        for u in uw_adj[v]:
            s += '   %d -> %d;\n'%(v, u)
    for v in uw_adj:
        s += '   %d [label = "%d \nf(%d) = %d", style="filled", fillcolor="%s", shape="circle"];\n'%(v, v, v, f(v), fillcolor[v])
    s += '}'
    return s



def list2adjmat(uw_adj, n):
    A = np.zeros((n, n), dtype=np.int)
    for u in uw_adj:
        for v in uw_adj[u]:
            x, y = u-1, v-1
            A[x][y] = 1
    return A

def list2incmat(uw_adj, n):
    edges = [ (u, v) for u in uw_adj for v in uw_adj[u]]
    A = np.zeros((n, len(edges)), dtype=np.int)
    print(edges)
    for i in range(1, n+1):
        for j in range(len(edges)):
            ii, jj = i-1, j
            if edges[j][0] == i:
                A[ii][jj] = 1
            elif edges[j][1] == i:
                A[ii][jj] = -1
    return A

wrap_env = lambda x, s: "\\begin{%s}\n%s \\end{%s}\n"%(x, s, x)

def mat2tex(B):
    matstr = '\\\\\n'.join(list(map(lambda row: '&'.join(list(map(str, row))), B)))
    return wrap_env("bmatrix", matstr)


A = list2adjmat(uw_adj, len(uw_adj))
E = list2incmat(uw_adj, len(uw_adj))

n = len(uw_adj)
D = np.zeros((n, n), dtype=np.int)
for u in uw_adj:
    for v in uw_adj[u]:
        x, y = u-1, v-1
        D[x][x] += 1
        D[y][y] += 1

EtE = E.dot(E.T)
L = D - A


with open("adj.mat", "w+") as adjf:
    adjf.write(mat2tex(A))

with open("inc.mat", "w+") as incf:
    incf.write(mat2tex(E))
            
with open("lap.mat", "w+") as lapf:
    lapf.write(mat2tex(EtE))

with open("uw.graph", "w+") as adjf:
    adjf.write(gendot(uw_adj))

with open("uwf.graph", "w+") as adjf:
    adjf.write(genfdot(uw_adj))

with open("deg.mat", "w+") as degf:
    degf.write(mat2tex(D))

with open("degadj.mat", "w+") as dadjf:
    dadjf.write(mat2tex(L))
