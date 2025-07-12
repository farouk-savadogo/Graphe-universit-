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