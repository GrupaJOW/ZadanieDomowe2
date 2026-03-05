import heapq

n, m = map(int, input().split()) #wczytanie liczb wierzcholkow n i krawedzi m
graf = [[] for _ in range(n + 1)] #tworzymy pusty graf (l.wierzh)

for _ in range(m):
    p, k, waga = map(int, input().split()) #poczatek, koniec, waga drogi
    graf[p].append((k, waga)) #dodanie krawedzi do grafu

x, y = map(int, input().split()) #wczytanie wierzcholkow x i y do szukania trasy
w = int(input()) #wczytanie wierzcholka w do szukania cyklu

def dijkstra(start):
    odl = [float('inf')] * (n + 1) #tablica dlugosci (na poczatku nieskonczonosc)
    pop = [-1] * (n + 1) #zapisanie poprzednika w drodze (-1 dla braku pop.)
    odl[start] = 0 #pkt. startowy
    kol = [(0, start)] #kolejka priorytetowa (dys., wierzcholek)

    while kol: #wykonujemy dopoki kolejka ma elementy
        ob_dys, obecny = heapq.heappop(kol) #pozyskanie najblizszego wierzcholka

        if ob_dys > odl[obecny]: #sprawdzenie drogi (ignorujemy gorsze trasy)
            continue
        for sasiad, waga in graf[obecny]: #sprawdzenie wszystkich sasiadow wierzcholka
            n_dys = ob_dys + waga
            if n_dys < odl[sasiad]: #jesli znajdziemy nowa krotsza droge
                odl[sasiad] = n_dys #zapamietanie nowej lepszej
                pop[sasiad] = obecny #zapisanie poprzednika
                heapq.heappush(kol, (n_dys, sasiad)) #wrzucenie sasiada do kolejki
    return odl, pop #zwrocenie odleglosci i poprzednikow

macierz = [[0] * (n + 1) for _ in range(n + 1)] #tworzymy pusta macierz najkrotszych drog

for i in range(1, n + 1):
    odl_i, _ = dijkstra(i) #uruchomienie dla kazdego wierzcholka

    for j in range(1, n + 1):
        if i != j: #jesli sa rozne punkty
            macierz[i][j] = odl_i[j] if odl_i[j] != float('inf') else 0 #wpisujemy dystans lub 0
        else:
            min_cykl = float('inf')
            for skad in range(1, n + 1): #sprawdzamy wszystkie krawedzie wchodzace
                for dokad, waga in graf[skad]:
                    if dokad == i and odl_i[skad] != float('inf'):
                        if odl_i[skad] + waga < min_cykl: #szukanie najkrotszego powrotu
                            min_cykl = odl_i[skad] + waga
            macierz[i][j] = min_cykl if min_cykl != float('inf') else 0 #zapisanie cyklu do macierzy

for i in range(1, n + 1):
    print(" ".join(map(str, macierz[i][1:])))

odl_x, pop_x = dijkstra(x) #uruchomienie z punktu x
trasa = [] #pusta lista na trase
ob_punkt = y #rozpoczecie z y (od konca)

while ob_punkt != -1: #wykonujemy dopoki nie trafimy na start (-1)
    trasa.append(ob_punkt) #dodanie punktu do trasy
    ob_punkt = pop_x[ob_punkt] #cofniecie sie do poprzedniego punktu

trasa.reverse() #odwracamy liste poniewaz szlismy od tylu
print(odl_x[y], " ".join(map(str, trasa))) #wypisanie calk. dystansu oraz trasy

naj_cykl = float('inf') #najkrotszy cykl to na poczatku nieskonczonosc
trasa_cyklu = [] #pusta lista na trase cyklu

for sasiad, waga in graf[w]: #sprawdzenie wszystkich sasiadow wierzcholka w
    odl_s, pop_s = dijkstra(sasiad) #uruchomienie funkcji z sasiada

    if odl_s[w] != float('inf'): #jesli da sie wrocic z sasiada do w
        dlugosc = waga + odl_s[w] #calkowity dystans cyklu

        if dlugosc < naj_cykl: #jesli znalezlismy krotszy cykl
            naj_cykl = dlugosc #zapamietanie nowej dlugosci

            temp = [] #tymczasowa lista na odtwarzanie drogi
            ob_punkt = w

            while ob_punkt != -1: #odtwarzanie drogi powrotnej
                temp.append(ob_punkt)
                if ob_punkt == sasiad: #przerywamy gdy dojdziemy do sasiada
                    break
                ob_punkt = pop_s[ob_punkt] #cofniecie sie

            temp.reverse() #odwracamy liste
            trasa_cyklu = [w] + temp #dodajemy punkt startowy w na poczatek listy

print(naj_cykl, " ".join(map(str, trasa_cyklu))) #wypisanie dlugosci cyklu i trasy