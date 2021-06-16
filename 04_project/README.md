# Zestaw 4 (Grafy i ich zastosowania)

- [x] Napisać program do kodowania grafów skierowanych (digrafów) i do generowania losowych digrafów z zespołu G(n, p).
- [x] Zaimplementować algorytm Kosaraju do szukania silnie spójnych składowych na digrafie i zastosować go do digrafu losowego.
- [x] Wykorzystując algorytmy z powyższych punktów wygenerować losowy silnie spójny digraf. Łukom tego digrafu przypisać losowe wagi będące liczbami całkowitymi z zakresu [−5, 10]. Zaimplementować algorytm Bellmana-Forda do znajdowania najkrótszych ścieżek od danego wierzchołka.
- [x] Zaimplementować algorytm Johnsona do szukania odegłości pomiędzy wszystkimi parami wierzchołków na ważonym grafie skierowanym.

##Sposób użycia
#Instalcja
pip insatall -r requirements.txt

#Wywołanie
Program wykonuje wszystkie kroki automatycznie. Podczas wywołąnia możemy podac wartosci paramaetrów n i p

python main.py [n] [p]

n liczba wierzchołków typ: int
p prawdopodobieństwo na występienie krawędzi typ: float zakres [0.0-1.0]

przykładowe wywołanie:

python main.py 6 0.4


