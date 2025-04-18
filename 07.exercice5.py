#cree dictionaire
fruits={
    "pomme":"rouge",
    "banane":"jaune",
    "orange":"orange" 
}

#ajouter 
fruits["kiwi"]="vert"

#stocker dans une autre variable
couleurBanane=fruits["banane"]

#modifier
fruits["pomme"]="vert"

#dupprimer
del fruits["banane"]

#afficher
print(fruits)