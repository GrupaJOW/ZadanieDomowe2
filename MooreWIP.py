from collections import deque

# Wczytanie liczby wierzchołków i krawędzi
n, m = map(int, input().split())

# Tworzymy listę sąsiedztwa grafu: (sąsiad, waga)
graf = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, waga = map(int, input().split())
    graf[a].append((b, waga))

# Wczytanie pary wierzchołków do wyznaczenia ścieżki
v, u = map(int, input().split())
# Wczytanie wierzchołka w do wyznaczenia cyklu
w = int(input())



# Funkcja Moore'a  
def moore(s):
    d = [float('inf')] * (n+1)
    f = [-1] * (n+1)
    in_queue = [False] * (n+1)
    d[s] = 0
    Q = deque()
    Q.append(s)
    in_queue[s] = True

    while Q:
        u0 = Q.popleft()
        in_queue[u0] = False
        for v0, waga in graf[u0]:
            if d[v0] > d[u0] + waga:
                d[v0] = d[u0] + waga
                f[v0] = u0
                if not in_queue[v0]:
                    Q.append(v0)
                    in_queue[v0] = True
    return d, f

# Macierz najkrótszych dróg
macierz = [[0]*(n+1) for _ in range(n+1)]
for s in range(1, n+1):
    d, _ = moore(s)
    for t in range(1, n+1):
        macierz[s][t] = d[t] if d[t] != float('inf') else 0

# Wyświetlenie macierzy najkrótszych dróg
for i in range(1, n+1):
    print(" ".join(str(macierz[i][j]) for j in range(1, n+1)))

# Wyznaczenie ścieżki między v i u
_, f = moore(v)
sciezka = []
curr = u
while curr != -1:
    sciezka.append(curr)
    curr = f[curr]
sciezka = sciezka[::-1]
print(macierz[v][u], " ".join(map(str, sciezka)))

# Wyznaczenie najkrótszego cyklu przechodzącego przez w
najkrotszy_cykl = float('inf')
cykl_sciezka = []

# Sprawdzamy wszystkie sąsiednie krawędzie wierzchołka w
for sasiad, waga_sasiad in graf[w]:
    d, f = moore(sasiad)  # droga powrotna do w
    if d[w] != float('inf'):
        dl = waga_sasiad + d[w]
        if dl < najkrotszy_cykl:
            najkrotszy_cykl = dl
            # odbudowanie ścieżki cyklu
            temp = []
            curr = w
            while curr != -1 and curr != sasiad:
                temp.append(curr)
                curr = f[curr]
            temp.append(sasiad)
            cykl_sciezka = [w] + temp

print(najkrotszy_cykl, " ".join(map(str, cykl_sciezka)))