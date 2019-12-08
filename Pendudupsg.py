from random import randrange
from dessinspendus import *
from fonctions import *
import pickle
import scrapy
import json
import webbrowser
points = 0

create_liste ()
    
               
scores()

def play_pendu():
    global points
    turlu = create_liste ()
    chances = 9
    number = (randrange(len(turlu[0]))-1)
    word = turlu[0][number].upper()
  
    secret_list = list(len(word) *'?')
    

    print(('                       ') + (' '.join(secret_list)))
    word_list = list(word)
    continuer = True
    utilisees = []
    while continuer:
        prints = {9:z,8:a,7:b,6:c,5:d,4:e,3:f,2:g,1:h}
        print(prints[chances])
        
        letter = input('    Choisis une lettre svp:\n').upper()
        
        def lettres_utilisees():        
            if letter not in utilisees:
                utilisees.append(str(letter))
            else:
                print('     !      !       !       !     !')
                print('    Tu a déja joué cette lettre!')
                print('     !      !       !       !     !')
        
        lettres_utilisees()
        
        print('\n Vous avez utilisé:', utilisees, '\n' )
        
        if letter in word_list:
            index = [i for i, x in enumerate(word_list) if x == letter]
            for i in index:
                secret_list[i] = letter
            print(('                       ') + (' '.join(secret_list)))
                        
            if '?' not in secret_list:
                    print('        Gagné!\n')
                    print('------------------------------------------------')
                    print('        Vous avez gagné: ',chances,' points')
                    print('------------------------------------------------')
                    continuer = False
                    information= input ('Si tu veux tu en savoir plus sur ' + word +' presse i \n').lower()
                    if information == 'i':
                        links_liste()
                        toto = (links_liste()[number])
                        url= "https://fr.wikipedia.org"  + (' '.join(toto))
                        webbrowser.open_new_tab(url)
                    with open('scores','rb') as fichier:
                        mon_pickler = pickle.Unpickler(fichier)
                        score_saved = mon_pickler.load()    
                    score_saved[nom] +=  chances
                    with open('scores', 'wb') as fichier:
                        player_score = pickle.Pickler(fichier)
                        player_score.dump(score_saved)
                    jouer = input('Voulez-vous continuer ? o/n \n').lower()
                    if jouer == ('n'):
                       exit()   
               
        elif letter not in word:
            print('      Perdu!  \n')
            print(('                       ') + (' '.join(secret_list)))
            chances -= 1
            if chances < 1:                
                print(y)
                print('      Perdu! C\'était:  ', word.upper(), '\n')
                def get_information ():
                    information= input ('Si tu veux tu en savoir plus sur ' + word  +' presse i \n').lower()
                    if information == 'i':
                        links_liste()
                        toto = (links_liste()[number])
                        url= "https://fr.wikipedia.org" + (' '.join(toto))
                        webbrowser.open_new_tab(url)
                get_information()
                print('------------------------------------------------')
                print('                  Vous avez: ',points,' points')
                continuer = False
                print('------------------------------------------------\n')
                jouer = input('Voulez-vous continuer ? o/n \n').lower()
                if jouer == ('n'):
                   exit()       
    
    play_pendu()
    
   
play_pendu()