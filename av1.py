
from Library.Grafo import GrafoListaAdj
from Library.CentroArvore import CentroArvore

G = GrafoListaAdj(orientado = False)


G.DefinirN(4, VizinhancaDuplamenteLigada = True)


e = G.AdicionarAresta(1, 2)
e = G.AdicionarAresta(1, 3)
e = G.AdicionarAresta(1, 4)
#e = G.AdicionarAresta(3, 2)


C = CentroArvore(G)


print("centro da arvore é aresta",C)
