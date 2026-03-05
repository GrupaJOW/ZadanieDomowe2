from collections import deque

# Wczytanie liczby wierzchołków i krawędzi
n, m = map(int, input().split())

graf = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, waga = map(int, input().split())
    graf[a].append((b, waga))
    
# Wczytanie pary wierzchołków do wyznaczenia ścieżki
v, u = map(int, input().split())

# Wczytanie wierzchołka w do wyznaczenia cyklu
w = int(input())


# --- FUNKCJA GŁÓWNA ALGORYTMU ---
def moore(start):
    d = [float('inf')] * (n+1)
    f = [-1] * (n+1)
    
    # Stany wierzchołka: 0 - nieodwiedzony, 1 - w kolejce, 2 - przetworzony
    stan = [0] * (n+1) 
    
    d[start] = 0
    Q = deque([start])
    stan[start] = 1

    while Q:
        obecny = Q.popleft()
        stan[obecny] = 2  # Oznaczamy jako zdjęty z kolejki
        
        for sasiad, waga in graf[obecny]:
            # Jeśli znajdziemy krótszą ścieżkę (relaksacja)
            if d[sasiad] > d[obecny] + waga:
                d[sasiad] = d[obecny] + waga
                f[sasiad] = obecny
                
                # Zgodnie z pseudokodem: dodajemy na koniec lub początek kolejki
                if stan[sasiad] == 0:
                    Q.append(sasiad)      # Nowy -> na koniec
                    stan[sasiad] = 1
                elif stan[sasiad] == 2:
                    Q.appendleft(sasiad)  # Wypadł wcześniej -> na początek
                    stan[sasiad] = 1
    return d, f


# --- 1. MACIERZ NAJKRÓTSZYCH DRÓG ---
macierz = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    d, _ = moore(i)
    for j in range(1, n+1):
        if i != j:
            macierz[i][j] = d[j] if d[j] != float('inf') else 0
        else:
            # Dla przekątnej (i == j) szukamy najkrótszego cyklu
            min_cykl = float('inf')
            for skad in range(1, n+1):
                for dokad, waga in graf[skad]:
                    if dokad == i and d[skad] != float('inf'):
                        min_cykl = min(min_cykl, d[skad] + waga)
            macierz[i][j] = min_cykl if min_cykl != float('inf') else 0

# Wyświetlenie macierzy (pomijamy zerowy indeks)
for i in range(1, n+1):
    print(" ".join(map(str, macierz[i][1:])))


# --- 2. ŚCIEŻKA MIĘDZY V ORAZ U ---
d_v, f_v = moore(v)
sciezka = []
curr = u

# Cofamy się po poprzednikach od 'u' do 'v'
while curr != -1:
    sciezka.append(curr)
    curr = f_v[curr]
    
sciezka.reverse()  # Odwracamy listę, by szła od początku do końca
print(d_v[u], " ".join(map(str, sciezka)))


# --- 3. NAJKRÓTSZY CYKL PRZEZ W ---
naj_cykl = float('inf')
cykl_sciezka = []

# Szukamy najkrótszej drogi powrotnej od każdego sąsiada 'w' z powrotem do 'w'
for sasiad, waga in graf[w]:
    d_s, f_s = moore(sasiad)
    
    if d_s[w] != float('inf'):
        dlugosc = waga + d_s[w]
        
        # Jeśli znaleźliśmy lepszy cykl, zapisujemy go i odtwarzamy trasę
        if dlugosc < naj_cykl:
            naj_cykl = dlugosc
            
            temp = []
            curr = w
            while curr != -1:
                temp.append(curr)
                if curr == sasiad:
                    break
                curr = f_s[curr]
                
            temp.reverse()
            cykl_sciezka = [w] + temp  # Doklejamy początkowe 'w'

print(naj_cykl, " ".join(map(str, cykl_sciezka)))
