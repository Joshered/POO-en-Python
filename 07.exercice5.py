fruits={
    "pomme":"rouge",
    "banane":"jaune",
    "orange":"orange" 
}
fruits["kiwi"]="vert"
couleurBanane=fruits["banane"]
fruits["pomme"]="vert"
del fruits["banane"]
print(fruits)