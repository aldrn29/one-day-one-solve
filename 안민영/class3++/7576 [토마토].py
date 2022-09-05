from sys import stdin
from collections import deque
input = stdin.readline

col, row = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]

queue = deque()
visited = [[0]*col for _ in range(row)]
count = 0
start = []

for i in range(row) :
    for j in range(col) :
        if matrix[i][j] == 0 : count += 1
        if matrix[i][j] == 1 :
            start.append((i, j))

def bfs(start) :
    for x, y in start :
        queue.append((x, y))
        visited[x][y] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col :
                if visited[nx][ny] == 0 and matrix[nx][ny] == 0 :
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    if count == 0 :
        return 0
    else : 
        for i in range(row) :
            for j in range(col) :
                if visited[i][j] : continue 
                if matrix[i][j] == 0 : return -1

        max_day = 0
        for i in visited :
            for j in i :
                max_day = max(max_day, j)
        return max_day

print(bfs(start))