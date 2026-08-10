import math
import heapq


# ---------- Heuristic Function ----------
def heuristic(node, goal):
    x1, y1 = coords[node]
    x2, y2 = coords[goal]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# ---------- Node State ----------
class State:
    def __init__(self, node, g, f, parent):
        self.node = node
        self.g = g
        self.f = f
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f


# ---------- A* Search ----------
def astar(start, goal):
    pq = []

    start_state = State(start, 0, heuristic(start, goal), None)
    heapq.heappush(pq, start_state)

    while pq:
        current = heapq.heappop(pq)

        if current.node == goal:
            path = []
            temp = current

            while temp:
                path.append(temp.node)
                temp = temp.parent

            path.reverse()

            print("Solution Path:", " - ".join(path))
            print("Solution Cost:", current.g)
            return

        for neighbor, cost in adjlist[current.node]:
            g = current.g + cost
            h = heuristic(neighbor, goal)
            f = g + h

            new_state = State(neighbor, g, f, current)
            heapq.heappush(pq, new_state)

    print("No Path Found")


# ---------- Read Input ----------
coords = {}
adjlist = {}

with open("input.txt", "r") as file:

    V = int(file.readline())

    for _ in range(V):
        node, x, y = file.readline().split()
        coords[node] = (float(x), float(y))
        adjlist[node] = []

    E = int(file.readline())

    for _ in range(E):
        u, v, cost = file.readline().split()
        adjlist[u].append((v, int(cost)))

    start = file.readline().strip()
    goal = file.readline().strip()

astar(start, goal)
