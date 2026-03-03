import sys, math

def floyd_warshall_with_path(n, edges):
    dist = [[math.inf] * n for _ in range(n)]
    nxt = [[None] * n for _ in range(n)]

    for a, b, w in edges:
        a -= 1
        b -= 1
        if w < dist[a][b]:
            dist[a][b] = w
            nxt[a][b] = b

    for k in range(n):
        for i in range(n):
            if dist[i][k] >= math.inf:
                continue
            dik = dist[i][k]
            for j in range(n):
                if dist[k][j] >= math.inf:
                    continue
                nd = dik + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd
                    nxt[i][j] = nxt[i][k]

    return dist, nxt

def reconstruct_path(nxt, u, v):
    u -= 1
    v -= 1
    if nxt[u][v] is None:
        return None
    path = [u]
    while u != v:
        u = nxt[u][v]
        if u is None:
            return None
        path.append(u)
        if len(path) > 10_000:
            return None
    return [x + 1 for x in path]

def reconstruct_cycle_through_w(n, nxt, w):
    w0 = w - 1
    if nxt[w0][w0] is None:
        return None
    cycle = [w0]
    cur = w0
    for _ in range(n + 1):
        cur = nxt[cur][w0]
        if cur is None:
            return None
        cycle.append(cur)
        if cur == w0:
            return [x + 1 for x in cycle]
    return None

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    edges = []
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        w = int(next(it))
        edges.append((a, b, w))

    u = int(next(it))
    v = int(next(it))
    w_vertex = int(next(it))

    dist, nxt = floyd_warshall_with_path(n, edges)

    for i in range(n):
        row = []
        for j in range(n):
            if dist[i][j] >= math.inf // 2:
                row.append("INF")
            else:
                row.append(str(dist[i][j]))
        print(" ".join(row))

    if dist[u - 1][v - 1] >= math.inf // 2:
        print("INF")
    else:
        p = reconstruct_path(nxt, u, v)
        print(dist[u - 1][v - 1], *p)

    if dist[w_vertex - 1][w_vertex - 1] >= math.inf // 2:
        print("INF")
    else:
        cyc = reconstruct_cycle_through_w(n, nxt, w_vertex)
        if cyc is None:
            print("INF")
        else:
            print(dist[w_vertex - 1][w_vertex - 1], *cyc)

if __name__ == "__main__":
    main()