import heapq
import sys


def rozwiazanie_dijkstra():
    # Wczytanie pierwszej linii
    pierwsza_linia = input().split()
    n = int(pierwsza_linia[0])
    m = int(pierwsza_linia[1])

    # Lista sąsiedztwa
    graf = {i: [] for i in range(1, n + 1)}

    # Wczytywanie m krawędzi (każda krawędź to nowa linia)
    for _ in range(m):
        krawedz = input().split()
        u = int(krawedz[0])
        v = int(krawedz[1])
        waga = int(krawedz[2])
        graf[u].append((v, waga))

    # Wczytanie wierzchołków startowego i końcowego
    przedostatnia = input().split()
    start_v = int(przedostatnia[0])
    koniec_u = int(przedostatnia[1])

    # Wczytanie ostatniej linii (wierzchołek w)
    # Robimy to, aby program nie "zgłupiał", gdy wkleisz całe dane z polecenia
    _ = input()

    # --- Algorytm Dijkstry ---
    odleglosci = {i: float('inf') for i in range(1, n + 1)}
    poprzednicy = {i: None for i in range(1, n + 1)}
    odleglosci[start_v] = 0

    # Kolejka priorytetowa (odleglosc, wierzcholek)
    kolejka = [(0, start_v)]

    while kolejka:
        obecna_odleglosc, obecny_wierzcholek = heapq.heappop(kolejka)

        # Optymalizacja - jeśli mamy już lepszą ścieżkę, pomijamy
        if obecna_odleglosc > odleglosci[obecny_wierzcholek]:
            continue

        # Sprawdzanie sąsiadów
        for sasiad, waga in graf[obecny_wierzcholek]:
            nowa_odleglosc = obecna_odleglosc + waga

            # Jeśli znajdziemy krótszą drogę, aktualizujemy
            if nowa_odleglosc < odleglosci[sasiad]:
                odleglosci[sasiad] = nowa_odleglosc
                poprzednicy[sasiad] = obecny_wierzcholek
                heapq.heappush(kolejka, (nowa_odleglosc, sasiad))

    # --- Odtwarzanie ścieżki ---
    sciezka = []
    aktualny = koniec_u

    if odleglosci[koniec_u] != float('inf'):
        while aktualny is not None:
            sciezka.append(aktualny)
            aktualny = poprzednicy[aktualny]
        sciezka.reverse()

        print(f"{odleglosci[koniec_u]} " + " ".join(map(str, sciezka)))
    else:
        print("Brak drogi")


if __name__ == "__main__":
    rozwiazanie_dijkstra()
