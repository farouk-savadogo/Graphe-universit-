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
    # Etape 2 : Creation des relations
    print("\nEtape 2 : Creation des relations entre les noeuds")
    while True:
        print("Definir une relation (ou tapez '0' pour terminer) :")
        source = input("  - Noeud source : ")
        if source == '0':
            break
        destination = input("  - Noeud destination : ")
        if destination == '0':
            break
        relation = input("  - Type ou nom de la relation : ")
        G.add_edge(source, destination, label=relation)
    # Etape 3 : Affichage du graphe
    print("\nAffichage du graphe...")
    couleurs = [couleurs_noeuds.get(node, 'gray') for node in G.nodes()]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=couleurs, node_size=1500, font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Graphe du domaine universitaire")
    plt.show()
# Boucle principale
while True:
    creer_graphe()
    continuer = input("\nVoulez-vous creer un graphe pour un autre domaine ? (oui/non) : ")
    if continuer.lower() not in ['oui', 'o', 'yes', 'y']:
        print("Fin du programme. Merci !")
        break
