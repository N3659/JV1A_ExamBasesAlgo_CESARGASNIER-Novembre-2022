barreSup = [0, 1, 2]
barreMid = [3, 4, 5] #on met en place le plateau
barreBot = [6, 7, 8]
touche = '' #on crée la variable touche 
places = 9 #on indique au programme le nombre de places sur le plateau

while (True):
    for i in range (9): #9 places donc 9 tours
       
   #TOUR DE X

        print (barreSup)
        print (barreMid) #on montre le "plateau" de jeu
        print (barreBot)
        print ("Au tour de X")
        print ("Quel coup faire ?") #puis à qui est-ce le tour et demande l'emplacement a jouer
        print ("Numéro")
        touche = input ()

#le joueur choisi la touche a jouer, le programme met un X à l'emplacement et retire 1 de la variable places

        if (touche == '0'): 
            barreSup[0]= ("X")
        places = places - 1

        if (touche == '1'):
            barreSup[1]= ("X")
            places = places - 1
        
        if (touche == '2'):
            barreSup[2]= ("X")
            places = places - 1
        
        if (touche == '3'):
            barreMid[0]= ("X")
            places = places - 1
        
        if (touche == '4'):
            barreMid[1]= ("X")
            places = places - 1
        
        if (touche == '5'):
            barreMid[2]= ("X")
            places = places - 1
        
    
        if (touche == '6'):
            barreBot[0]= ("X")
            places = places - 1
        
        if (touche == '7'):
            barreBot[1]= ("X")
            places = places - 1
        
        if (touche == '8'):
            barreBot[2]= ("X")
            places = places - 1
        
#Victoire du X

        if (barreSup[0] and barreMid[0] and barreBot[0] == "X"): #si la ligne verticale 1 est remplie par X alors victoire de X
            print ("Tu as gagné X")
            
        if (barreSup[1] and barreMid[1] and barreBot[1] == "X"):#si la ligne verticale 2 est remplie par X alors victoire de X
            print ("Tu as gagné X")
            
        if (barreSup[2] and barreMid[2] and barreBot[2] == "X"): #si la ligne verticale 3 est remplie par X alors victoire de X
            print ("Tu as gagné X")
            
        if (barreSup[0] and barreSup[1] and barreSup[2] == "X"): #si la ligne horizontale 1 est remplie par X alors victoire de X
            print ("Tu as gagné X")
            
        if (barreMid[0] and barreMid[1] and barreMid[2] == "X"): #si la ligne horizontale 1 est remplie par X alors victoire de X
            print ("Tu as gagné X")
            
        if (barreBot[0] and barreBot[1] and barreBot[2] == "X"): #si la ligne horizontale 1 est remplie par X alors victoire de X
            print ("Tu as gagné X")     

        if (barreSup[0] and barreMid[1] and barreBot[2] == "X"): #si la ligne diagonale 1 est remplie par X alors victoire de X
            print ("Tu as gagné X")

        if (barreSup[2] and barreMid[1] and barreBot[0] == "X"): #si la ligne diagonale 2 est remplie par X alors victoire de X
            print ("Tu as gagné X")
        
    #Fin des victoires X

        #TOUR DE O
        
        print (barreSup)
        print (barreMid) #on montre le "plateau" de jeu
        print (barreBot)
        print ("Au tour de O")
        print ("Quel coup faire ?") #puis à qui est-ce le tour et demande l'emplacement a jouer
        print ("Numéro")
        touche = input ()

    #le joueur choisi la touche a jouer, le programme met un X à l'emplacement et retire 1 de la variable places

        if (touche == '0'):
            barreSup[0]= ("O")
            places = places - 1
        
        if (touche == '1'):
            barreSup[1]= ("O")
            places = places - 1
        
        if (touche == '2'):
            barreSup[2]= ("O")
            places = places - 1
        
        if (touche == '3'):
            barreMid[0]= ("O")
            places = places - 1
        
        if (touche == '4'):
            barreMid[1]= ("O")
            places = places - 1
        
        if (touche == '5'):
            barreMid[2]= ("O")
            places = places - 1
        
        if (touche == '6'):
            barreBot[0]= ("O")
            places = places - 1
        
        if (touche == '7'):
            barreBot[1]= ("O")
            places = places - 1
        
        if (touche == '8'):
            barreBot[2]= ("O")
            places = places - 1
        
 #Victoire du O

        if (barreSup[0] and barreMid[0] and barreBot[0] == "O"): #si la ligne verticale 1 est remplie par 0 alors victoire de O
            print ("Tu as gagné O")
            
        if (barreSup[1] and barreMid[1] and barreBot[1] == "O"): #si la ligne verticale 2 est remplie par 0 alors victoire de O
            print ("Tu as gagné O")
                        
        if (barreSup[2] and barreMid[2] and barreBot[2] == "O"): #si la ligne verticale 3 est remplie par 0 alors victoire de O
            print ("Tu as gagné O")
            
        if (barreSup[0] and barreSup[1] and barreSup[2] == "O"): #si la ligne horizontale 1 est remplie par 0 alors victoire de O
            print ("Tu as gagné O")
            
        if (barreMid[0] and barreMid[1] and barreMid[2] == "O"): #si la ligne horizontale 2 est remplie par 0 alors victoire de O
            print ("Tu as gagné O")
            
        if (barreBot[0] and barreBot[1] and barreBot[2] == "O"): #si la ligne horizontale 3 est remplie par 0 alors victoire de O
            print ("Tu as gagné O")
            
        if (barreSup[0] and barreMid[1] and barreBot[2] == "O"): #si la ligne diagonale 1 est remplie par 0 alors victoire de O
            print ("Tu as gagné O")
            
        if (barreSup[2] and barreMid[1] and barreBot[0] == "O"): #si la ligne diagonale 2 est remplie par 0 alors victoire de O
            print ("Tu as gagné O")
            
        #Fin des victoires O

        #Égalités
    if (places == 0): #si la var places arrive à 0 (toutes les cases jouées), le jeu indique une égalité
        print ("Égalité !")



#Si on veut jouer au puissance 4 on devrais faire en sorte que les jetons tombent à l'emplacement
#le plus bas possible et ensuite verifier si il n'y en à pas 4 d'affilées.