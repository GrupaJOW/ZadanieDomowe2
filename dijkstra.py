# wczytanie liczby wierzchołków i krawędzi
n, m = map(int, input().split())

# wczytanie krawędzi
krawedzie = []
for _ in range(m):
    a, b, waga = map(int, input().split())
    krawedzie.append((a, b, waga))

# wczytanie pary wierzchołków
v, u = map(int, input().split())

# wczytanie wierzchołka w
w = int(input())


