# Zestaw 2 (Grafy i ich zastosowania)

## Tasks
- [x] 1. Napisać program do sprawdzania, czy dana sekwencja liczb naturalnych jest ciągiem graficznym, i do konstruowania grafu prostego o stopniach wierzchołków zadanych przez ciąg graficzny.
- [x] 2. Napisać program do randomizacji grafów prostych o zadanych stopniach wierzchołków. Do tego celu wielokrotnie powtórzyć operację zamieniającą losowo wybraną parę krawędzi: ab i cd na parę ad i bc.
- [x] 3. Napisać program do znajdowania największej spójnej składowej na grafie.
- [x] 4. Używając powyższych programów napisać program do tworzenia losowego grafu eulerowskiego i znajdowania na nim cyklu Eulera.
- [x] 5. Napisać program do generowania losowych grafów k-regularnych.
- [x] 6. Napisać program do sprawdzania (dla małych grafów), czy graf jest hamiltonowski.

Uruchomienie:
Opcje -r, -H i -c działają tylko razem z opcją -f. np. python main.py -r 3 -f  "g.dat"
Opcje -s, -e, -kr należy używać bez opcji -f.
 
python main.py [OPTIONS]

Options:
  -s, --sequence TEXT        Check if sequence consisting of ints separated by
                             commas is graphic, if true generates a graph.

  -f, --filename TEXT        Read adjacency matrix representing graph from
                             file

  -r, --randomize INTEGER    Randomize edges n (int) times
  -e, --euler INTEGER        Create a randomized Euler graph with given n
                             (int) nodes or random n if n=0

  -kr, --regular INTEGER...  Make k-regular graph with n nodes where n(int) is
                             first parameter and k(int) the second one

  -H, --hamilton             Check if Hamilton cycle exists in given graph. If
                             true prints it

  -c, --components           Find all connected  components in given graph and
                             mark the greatest

  --help                     Show this message and exit.