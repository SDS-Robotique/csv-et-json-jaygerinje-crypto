nouveauFichier = open("00_nouveau.txt", "w")
nouveauFichier.write("Voici du texte que j'ajoute dans ce fichier !")
nouveauFichier.close

modificationFichier = open("00_nouveau.txt", "a")
modificationFichier.write("J'ajoute du texte à la fin du fichier")
modificationFichier.close