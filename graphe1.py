import networkx as nx
import matplotlib.pyplot as plt
def creer_graphe():
    print("=== Creation dun graphe pour un domaine universitaire ===")
    G = nx.DiGraph()
    couleurs_noeuds = {}
    # Etape 1 : Creation des noeuds
    print("\nEtape 1 : Creation des noeuds")
    while True:
        nom_noeud = input("Entrez le nom du noeud (ou '0' pour terminer) : ")
        if nom_noeud == '0':
            break
        couleur = input(f"Entrez une couleur pour le noeud '{nom_noeud}' : ")
        G.add_node(nom_noeud)
        couleurs_noeuds[nom_noeud] = couleur