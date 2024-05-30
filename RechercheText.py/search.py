def contientMot(texte, mot):
    return mot in texte.split(" ")

def compterOccurrences(texte, mot):
    return texte.split(" ").count(mot)
  
