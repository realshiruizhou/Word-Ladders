import time
from collections import deque
adj_list = {}
w = deque()
words = set()


class Vertex:
    def __init__(self, state, parent, path_length):
        self.state = state
        self.parent = parent
        self.path_length = path_length

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_path_length(self):
        return self.path_length


def adjacent(state):
    adj = []
    ref = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, len(state)):
        for j in range(0, len(ref)):
            if state[i] != ref[j]:
                n = state[:i] + ref[j] + state[i + 1:]
                if n in words:
                    adj.append(n)
    return adj


def print_path(state, goal):
    start = Vertex(state, None, 0)
    fringe = deque()
    fringe.appendleft(start)
    visited = set()
    visited.add(start.get_state())
    while len(fringe) != 0:
        v = fringe.pop()
        if v.get_state() == goal:
            print(v.get_path_length())
            parents = list()
            p = v
            while p is not None:
                parents.append(p)
                p = p.get_parent()
            while parents:
                t = parents.pop()
                print(t.get_state())
            return v.get_path_length()
        c = adj_list[v.get_state()]
        temp = []
        for e in c:
            add = Vertex(e, v, v.get_path_length() + 1)
            temp.append(add)
        for a in temp:
            if a.get_state() not in visited:
                fringe.appendleft(a)
                visited.add(a.get_state())
    print("No solution")


def bfs_winnable(state):
    fringe = deque()
    fringe.appendleft(state)
    visited = set()
    visited.add(state)
    while len(fringe) != 0:
        v = fringe.pop()
        for a in adjacent(v):
            if a not in visited:
                fringe.appendleft(a)
                visited.add(a)
    return visited


def connected():
    count = 0
    visit = set()
    for k in words:
        if k not in visit:
            t = bfs_winnable(k)
            count += 1
            for j in t:
                visit.add(j)
    return count


def path(state):
    start = Vertex(state, None, 0)
    fringe = deque()
    fringe.append(start)
    visited = set()
    visited.add(start.get_state())
    long = 0
    word = ""
    while fringe:
        v = fringe.pop()
        c = adj_list[v.get_state()]
        temp = set()
        for e in c:
            vert = Vertex(e, v, v.get_path_length() + 1)
            temp.add(vert)
        for a in temp:
            if a.get_state() not in visited:
                fringe.appendleft(a)
                visited.add(a.get_state())
                long = a.get_path_length()
                word = a.get_state()
    return long, word


def longest():
    p_l = 0
    s = ""
    e = ""
    for a in words:
        (x, y) = path(a)
        if p_l < x:
            p_l = x
            s = a
            e = y
    return s, e


file = open("words_6.txt", "r")
for line in file:
    k = line.split()
    words.add(k[0])
for n in words:
    adj_list[n] = adjacent(n)
file2 = open("puzzles.txt", "r")
for line2 in file2:
    j = line2.split()
    print_path(j[0], j[1])
print(connected())
print(longest())
