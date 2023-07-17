import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

# link: dictionary containing links between nodes
# Each entry in the dictionary is of the form {index: [node1, node2]}
link = {}
for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    link[i] = [n1, n2]

# sommetsNonTraités: list of gateway nodes that haven't been treated yet
sommetsNonTraités = []
for i in range(e):
    ei = int(input())
    sommetsNonTraités.append(ei)  

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    cle_to_remove = []
    # Iterate over each gateway node that hasn't been treated yet

    for sommet in sommetsNonTraités:            
        for cle, valeurs in link.items():
            if si in valeurs and '''ei, verifier que c'est le bon''' in valeurs:
                print(str(valeurs[0]) + " " + str(valeurs[1])) 'verifier que les valeur sont bien les valeurs si et ei'
                cle_to_remove.append(cle)
                del link[cle]
                break

            elif  sommet in valeurs:
                print(str(valeurs[0]) + " " + str(valeurs[1]))
                cle_to_remove.append(cle)
                del link[cle]
                break

                        

    
    

    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # Example: 0 1 are the indices of the nodes you wish to sever the link between