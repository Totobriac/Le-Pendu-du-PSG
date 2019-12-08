import json
import pickle


def create_liste ():
    liste = []
    with open('joueur.json') as json_data:
        liste_joueurs = json.load(json_data)
    for i in liste_joueurs:
        for jojo in i.values():
            liste.append(jojo) 
    return (list(zip(*liste)))



nom = input("Quel est ton nom?\n").lower()
    
def links_liste ():
    liste_links = []
    with open('URL.json') as f:
        links_joueurs = json.load(f)
    for i in links_joueurs:
        liste_links.append(list(i.values()))
    return liste_links


def scores():
    
    with open('scores','rb') as fichier:
        mon_pickler = pickle.Unpickler(fichier)
        score_saved = mon_pickler.load()
    if nom in score_saved:
        print('Heureux de te revoir' , nom.capitalize() , 'Tu as', score_saved[nom],' points \n')
    else:
        print('Bonjour', nom.capitalize(),', bienvenue dans mon premier programme :)\n')
        score_saved[nom] = 0
        with open('scores', 'wb') as fichier:
            player_score = pickle.Pickler(fichier)
            player_score.dump(score_saved)

def get_information ():
    information= input ('Si tu veux tu en savoir plus sur ' + word  +' presse i \n').lower()
    if information == 'i':
        links_liste()
        toto = (links_liste()[number])
        url= "https://fr.wikipedia.org" + (' '.join(toto))
        webbrowser.open_new_tab(url)
        
