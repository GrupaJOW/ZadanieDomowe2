import heapq

print("""Przykladowe Dane:
4 4
1 2 1
2 4 1
1 3 5
3 4 1
1 4
1""")

n,m = map(int ,input().split()) #wczytanie liczb wierzcholkow n i krawedzmi m

graf= [[] for _ in range(n+1)] #tworzymy pusty graf (l.wierzh)

for _ in range(m):
    p,k,waga = map(int ,input().split()) # wczytanie krawedzi (poczatek,koniec,waga)
    graf[p].append((k,waga))

x,y = map(int ,input().split())
w= int(input())

def dijkstra(start):
    odl = [float('inf')]*(n+1) #zalozenie ze na poczatku odleglosc jest nieskonczonosc wszedzie
    pop = (n+1)*[-1] #zapisanie poprzednika w drodze (-1 dla braku poprzednika)
    odl[start] = 0 #par. startowy
    kol=[(0,start)] #kolejka prioretytowa (dys., wierzcholek)

    while kol:
        ob_dys, obecny = heapq.heappop(kol) #pozyskanie najb. wierzcholka

        if ob_dys > odl[obecny]: #sprawdzenie drogi
            continue
        for sasiad, waga in graf[obecny]: #sprawdzenie wszystkich sasiadow wierzcholka
            n_dys = ob_dys + waga
            if n_dys < odl[sasiad]: #jesli znajdziemy nowa krotsza droge
                odl[sasiad] = n_dys #zapamietanie nowej lepszej
                pop[sasiad] = obecny #zapisanie poprzednika
                heapq.heappush(kol,(n_dys,sasiad)) #wrzucenie sasiada do drogi
    return odl, pop

odl_x, pop_x = dijkstra(x) #uruchomienie funkcji z punktu x
trasa=[] #pusta lista na trase
ob_punkt=y #rozpoczecie z y

while ob_punkt != -1: #wykonujemy dopoki nie bedzie poczatku (-1)
    trasa.append(ob_punkt) #dodanie punktu do trasy
    ob_punkt = pop_x[ob_punkt] #cofniecie sie do ostatniego punktu
trasa.reverse() #odwracamy poniewaz zaczynalismy od y a nie od x

print(f"Wynik: Calk.dystans={odl_x[y]}, punkty w trasie: {' '.join(map(str, trasa))}") #wypisanie calk. dystansu oraz kolejne punkty w trasie
