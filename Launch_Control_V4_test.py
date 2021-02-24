# import the library
from appJar import gui
from gpiozero import LED, Button
from time import sleep, time


#-------------------------------------------------------------------
#definition des E/S
#-------------------------------------------------------------------
# Avertisseurs lumineux & sonores
LP1_r = LED(4)
LP2_r = LED(17)
LP3_r = LED(27)
LP4_r = LED(22)
LP1_b = LED(23)
LP2_b = LED(24)
LP3_b = LED(25)
LP4_b = LED(12)
BUZ_r = LED(5)
BUZ_b = LED(20)
SP = LED(6)

# Signaux Chrono
SC_r = LED(26)
SC_b = LED(21)

# Sorties de puissance
EA_r = LED(13)
EA_b = LED(18)
RP_r = LED(19)
RP_b = LED(16)


#-------------------------------------------------------------------
# Fonction de gestion du départ
#-------------------------------------------------------------------
def Launch():
#     ----------------------------------------------------------    
    # Globals variables
#     ----------------------------------------------------------
    global couleur
    global delay_s
    global Nbr_departs
    global tea_rouge
    global tea_bleu
    global filename
    global qualif
    
    #definition des E/S
    # Avertisseurs lumineux & sonores
    global LP1_r
    global LP2_r
    global LP3_r
    global LP4_r
    global LP1_b
    global LP2_b
    global LP3_b
    global LP4_b
    global BUZ_r
    global BUZ_b
    global SP

    # Signaux Chrono
    global SC_r
    global SC_b

    # Sorties de puissance
    global EA_r
    global EA_b
    global RP_r
    global RP_b
    
#     ----------------------------------------------------------    
    # Locals variables
#     ----------------------------------------------------------
    # Definition des flags pour validé que l'étape à été effectuée     
    r0=0; r1=0; r2=0; r3=0; r4=0; r5=0; r6=0; r8=0
    b0=0; b1=0; b2=0; b3=0; b4=0; b5=0; b6=0; b8=0
    end = 0 # si end == 1 alors la séquence est terminée
    i = 0 # nombre de tour de la boucle
    time_base = 0.5 # temps le plus court entre deux étapes
    redard_bleu = 0
    retard_rouge = 0
    init_time=time()
    
#     ----------------------------------------------------------    
    # Calcul des délais pour chaqune des étapes de la séquence
#     ----------------------------------------------------------
    if couleur==1:
        retard_rouge=delay_s
        redard_bleu=0
    elif couleur==-1:
        redard_bleu=delay_s
        retard_rouge=0
    else:
        redard_bleu=0
        retard_rouge=0
    
    tr0 = init_time + retard_rouge + (time_base*0)
    tb0 = init_time + redard_bleu + (time_base*0)
    tr1 = init_time + retard_rouge + (time_base*1)
    tb1 = init_time + redard_bleu + (time_base*1)
    tr2 = init_time + retard_rouge + (time_base*2)
    tb2 = init_time + redard_bleu + (time_base*2)
    tr3 = init_time + retard_rouge + (time_base*3)
    tb3 = init_time + redard_bleu + (time_base*3)
    tr4 = init_time + retard_rouge + (time_base*4)
    tb4 = init_time + redard_bleu + (time_base*4)
    tr5 = init_time + retard_rouge + (time_base*5)
    tb5 = init_time + redard_bleu + (time_base*5)
    tr6 = init_time + retard_rouge + (time_base*6)
    tb6 = init_time + redard_bleu + (time_base*6)
    tr8 = init_time + retard_rouge + (time_base*8)
    tb8 = init_time + redard_bleu + (time_base*8)
    
    #SP.on()
    Nbr_departs=Nbr_departs+1
    print("Départ",Nbr_departs,"en cours...")
    
    while end==0:
        i=i+1
        temps_actuel=time()
        # gestion des Electro-aimants
        #-------------------------------------------------------------------
        
        #After 6 delay for red
        if (tr6<temps_actuel) and (r6==0):
            LP4_r.on()
            BUZ_r.on()
            EA_r.on()
            SC_r.on()
            r6=1
            tea_rouge=time()-init_time
            #print("Electro-aimants Rouge ouverts après : ", time()-init_time)
            
            
        #After 6 delay for blue
        if (tb6<temps_actuel) and (b6==0):
            LP4_b.on()
            BUZ_b.on()
            EA_b.on()
            SC_b.on()
            b6=1
            tea_bleu=time()-init_time
            #print("Electro-aimants Bleu ouverts après  : ", time()-init_time)
            continue
        
        # gestion des GPIOs du coté rouge
        #-------------------------------------------------------------------
        #After 0 delay for red
        if (tr0<temps_actuel)and(r0==0):
            LP1_r.on()
            BUZ_r.on()
            r0=1
            #print("r0 : ", time()-init_time)
            continue #return at the begining of the while loop
            
        #After 1 delay for red
        if (tr1<temps_actuel)and(r1==0):
            BUZ_r.off()
            r1=1
            #print("r1 : ", time()-init_time)
            continue
            
        #After 2 delay for red
        if (tr2<temps_actuel)and(r2==0):
            LP2_r.on()
            BUZ_r.on()
            r2=1
            #print("r2 : ", time()-init_time)
            continue
            
        #After 3 delay for red
        if (tr3<temps_actuel)and(r3==0):
            BUZ_r.off()
            r3=1
            #print("r3 : ", time()-init_time)
            continue
            
        #After 4 delay for red
        if (tr4<temps_actuel)and(r4==0):
            LP3_r.on()
            BUZ_r.on()
            r4=1
            #print("r4 : ", time()-init_time)
            continue
            
        #After 5 delay for red
        if (tr5<temps_actuel)and(r5==0):
            BUZ_r.off()
            r5=1
            #print("r5 : ", time()-init_time)
            continue
            

            
        #After 8 delay for red
        if (tr8<temps_actuel)and(r8==0):
            BUZ_r.off()
            r8=1
            continue
            
        # gestion des GPIOs du coté bleu
        #-------------------------------------------------------------------
        #After 0 delay for blue
        if (tb0<temps_actuel)and(b0==0):
            LP1_b.on()
            BUZ_b.on()
            b0=1
            #print("b0 : ", time()-init_time)
            continue
            
        #After 1 delay for blue
        if (tb1<temps_actuel)and(b1==0):
            BUZ_b.off()
            b1=1
            #print("b1 : ", time()-init_time)
            continue
            
        #After 2 delay for blue
        if (tb2<temps_actuel)and(b2==0):
            LP2_b.on()
            BUZ_b.on()
            b2=1
            #print("b2 : ", time()-init_time)
            continue
            
        #After 3 delay for blue
        if (tb3<temps_actuel)and(b3==0):
            BUZ_b.off()
            b3=1
            #print("b3 : ", time()-init_time)
            continue
            
        #After 4 delay for blue
        if (tb4<temps_actuel)and(b4==0):
            LP3_b.on()
            BUZ_b.on()
            b4=1
            #print("b4 : ", time()-init_time)
            continue
            
        #After 5 delay for blue
        if (tb5<temps_actuel)and(b5==0):
            BUZ_b.off()
            b5=1
            #print("b5 : ", time()-init_time)
            continue
            

            
        #After 8 delay for blue
        if (tb8<temps_actuel)and(b8==0):
            BUZ_b.off()
            b8=1
            continue
            
        # condition de sortie de la boucle
        #-------------------------------------------------------------------
        if (r8==1)and(b8==1):
            end=1
            EA_b.off()
            EA_r.off()
            #SP.off()
            continue
        
        # FIN DE LA BOUCLE DE SEQUANCE
    
    # initialise GPIO
    # Avertisseurs lumineux & sonores
    LP1_r.off()
    LP2_r.off()
    LP3_r.off()
    LP4_r.off()
    LP1_b.off()
    LP2_b.off()
    LP3_b.off()
    LP4_b.off()
    BUZ_r.off()
    BUZ_b.off()
    #SP.off()
    
    # Signaux Chrono
    SC_r.off()
    SC_b.off()
    
    # Sorties de puissance
    EA_r.off()
    EA_b.off()
    RP_r.off()
    RP_b.off()
    
    print("Electro-aimants Rouge ouverts après : ", round(tea_rouge,3))
    print("Electro-aimants Bleu ouverts après  : ", round(tea_bleu,3))
    print("...")
    print("L'écart d'ouverture en seconde est de : ", round(abs(tea_bleu-tea_rouge),3))
    
    if(couleur==1):
        clr="rouge"
    elif(couleur==-1):
        clr="bleu"
    else:
        clr="-"
        
    if(not(bool(qualif))):
        depart_effectif=open(filename,"a")
        depart_effectif.write("%d) " %Nbr_departs)# nombre de départ
        depart_effectif.write("Le dossard numéro %d" %(dossard))# nombre de départ
        depart_effectif.write(" a un retard de %.2f seconde " %(delay_s))
        depart_effectif.write("du coté %s.\r\n" %(clr))
        depart_effectif.write("     Le retard software est de %.5f\r\n" % (abs(tea_bleu-tea_rouge)))# Difference is:
        depart_effectif.close()
    
    #print("Temps d'execution du départ = ", time()-init_time)
    #print("Nombre de tours de boucle   = ", i)
    return 0


#-------------------------------------------------------------------
# definition des Fonctions de calcul et d'affichage
#-------------------------------------------------------------------

# fonction sleep maison
def MySleep(delay, T_init):
    i=0
    while ((T_init+delay)>time()):
        i=i+1
#     print(time())
#     print(time()-T_init)
#     print(T_init)
#     print(delay)
    return i

# test si l'entrée numérique est valide
def validfloatEntry(c,n):
    global error
    try:
        r = float(c)
        return round(r,n)
    except ValueError:
        error=1
        return 0
    
def validintEntry(c):
    global error
    try:
        r = int(c)
        return abs(r)
    except ValueError:
        error=1
        return 0
    
    
# affiche les variables dans la console   
def PrintVar():
    global qualif
    global couleur
    global delay_s
    global var_set
    global ready
    global error
    print(" ")
    print("Check variables")
    print("-couleur   = ",couleur)
    print("-qualif    = ",qualif)
    print("-delay [s]= ",delay_s)
    print("-var_set   = ",var_set)
    print("-ready     = ",ready)
    print("-Error     = ",error)
    
def maxmin_delay():
    global delay_s
    global error
    max_s = 10 #secondes
    min_s = 0 #secondes
    if delay_s>max_s:
        delay_s=max_s
        error=1
    elif delay_s<min_s:
        delay_s=min_s
        error=1
        
#-------------------------------------------------------------------
# definition des Fonctions de callback de l'interface graphique
#-------------------------------------------------------------------

def Select_str_entry(): #app_Select_filename
    global filename
    txt = str(app_Select_filename.getEntry("fichier"))
    if bool(txt):
        if (".txt" in txt):
            filename=txt
        else:
            filename=txt+".txt"
    app_Select_filename.stop()

# gestion du bouton "Qualifications"
def Qualif():
    global qualif
    global delay_s
    delay_s=0
    qualif=1
    app_Welcome.stop()
    
# gestion du bouton "Exit"
def stop_Welcome():
    global stop_GUI
    global qualif
    qualif = 1
    stop_GUI=1
    app_Welcome.stop()

# gestion des boutons "Rouge" & "Bleu"
def Colour(button):
    global couleur
    if button == "Rouge":
        couleur=1
        app_Welcome.stop()
    else:
        couleur=-1
        app_Welcome.stop()
        
# gestion du bouton "Select" lorsque "Rouge" à été sélectionné
def Select_red_delay():
    global delay_s
    global var_set
    global dossard
    dossard = validintEntry(app_Select_red_delay.getEntry("dossard"))
    delay_s = validfloatEntry(app_Select_red_delay.getEntry("délai"),2)
    var_set=1
    print("-dossard = ",dossard)
    print("-délai [s]= ",delay_s)
    app_Select_red_delay.stop()
    
# gestion du bouton "Select" lorsque "Bleu" à été sélectionné
def Select_blue_delay():
    global delay_s
    global var_set
    global dossard
    dossard = validintEntry(app_Select_blue_delay.getEntry("dossard"))
    delay_s = validfloatEntry(app_Select_blue_delay.getEntry("délai"),2)
    var_set=1
    print("-dossard = ",dossard)
    print("-délai [s]= ",delay_s)
    app_Select_blue_delay.stop()
    
# gestion du bouton "Chg. de côté" lorsque "Rouge" à été sélectionné
def Chg_red_delay():
    global couleur
    couleur=-1
    app_Select_red_delay.stop()
    
# gestion du bouton "Chg. de côté" lorsque "Bleu" à été sélectionné
def Chg_blue_delay():
    global couleur
    couleur=1
    app_Select_blue_delay.stop()
    
# gestion du bouton "Start"
def Start_Q():
    global ready
    ready = 1
    app_Qualif.stop()
    
def Start_red():
    global ready
    ready = 1
    app_Start_red.stop()
    
def Start_blue():
    global ready
    ready = 1
    app_Start_blue.stop()

# gestion du bouton "Exit"
def Exit_qualif():
    global qualif
    qualif = 0
    app_Qualif.stop()
    
def Exit_red():
    global couleur
    couleur = 0
    app_Select_red_delay.stop()
    
def Exit_blue():
    global couleur
    couleur = 0
    app_Select_blue_delay.stop()
    
#-------------------------------------------------------------------
# Programme principale
#-------------------------------------------------------------------

# initialise les varibles de la boucle principale (#b: 0=>FALSE / 1=>TRUE)
var_set=0
dossard=0
delay_s=0
ready=0#b
error=0#b
qualif=0#b
stop_GUI=0#b
couleur=0
Nbr_departs=0
test=1 # !!! est toujours à 0 sauf en cas de test (=1) !!!
tea_rouge=0.0
tea_bleu=0.0
filename="nouvelle_feuille_de_temps.txt"

# initialise GPIO
# Avertisseurs lumineux & sonores
LP1_r.off()
LP2_r.off()
LP3_r.off()
LP4_r.off()
LP1_b.off()
LP2_b.off()
LP3_b.off()
LP4_b.off()
BUZ_r.off()
BUZ_b.off()
SP.off()

# Signaux Chrono
SC_r.off()
SC_b.off()

# Sorties de puissance
EA_r.off()
EA_b.off()
RP_r.off()
RP_b.off()

#-------------------------------------------------------------------
# Création du fichier de sauvegarde des délais  
#-------------------------------------------------------------------

print("Bienvenue !")

# with gui("Nom du fichier de sauvegarde", "800x300", bg='Gold', font={'size':22}) as app_Select_filename:
#     app_Select_filename.label("Definissez le nom du fichier de sauvegarde des temps", bg='LightYellow', fg='black')
#     app_Select_filename.entry("fichier", label=True, focus=True)
#     app_Select_filename.buttons(["Select"], [Select_str_entry])
#     app_Select_filename.enableEnter(Select_str_entry)
# 
# depart_effectif=open(filename,"w+")
# depart_effectif.write(filename+"\r\n")
# depart_effectif.close()
# print("fichier créer avec le nom:",filename)

#-------------------------------------------------------------------
# script de test (seulement si test = 1) 
#-------------------------------------------------------------------

if test==1:
    print("Test !")
#     mesure= open("Mesures_de_temps.txt","w+")
#     mesure.close()
    #while 1:
#     for x in range(200):
#         delay_s=0
#         couleur=0
#         Launch()
#         mesure= open("Mesures_de_temps.txt","a")
#         mesure.write("%f_" %delay_s)# nombre de départ
#         mesure.write("%f\r\n" % (abs(tea_bleu-tea_rouge)))# Difference is: 
#         mesure.close() 
#         print(" ")
    
    for x in range(50):
        delay_s=0#0.01*x
        couleur=1
        dossard=2*x
        Launch()
        sleep(15)
#         mesure= open("Mesures_de_temps.txt","a")
#         mesure.write("%f_" %(delay_s*couleur))# nombre de départ
#         mesure.write("%f\r\n" % (abs(tea_bleu-tea_rouge)))# Difference is: 
#         mesure.close() 
        print(" ")
    
    for x in range(200):
        delay_s=0#0.01*x
        couleur=-1
        dossard=2*x+1
        Launch()
#         mesure= open("Mesures_de_temps.txt","a")
#         mesure.write("%f_" %(delay_s*couleur))# nombre de départ
#         mesure.write("%f\r\n" % (abs(tea_bleu-tea_rouge)))# Difference is: 
#         mesure.close() 
        print(" ")


# # while not(bool(stop_GUI)):
# #     # réinitialise les varibles (#b: 0=>FALSE / 1=>TRUE)
# #     var_set=bool(0)#b
# #     delay_s=0
# #     dossard=0
# #     ready=bool(0)#b
# #     error=bool(0)#b
# #         
# #     if (not(bool(qualif)))and(not(bool(couleur))):
# #         # Création de la fenêtre
# #         with gui("Menu Principale", "600x400", bg='LightYellow', font={'size':22}) as app_Welcome:
# #             app_Welcome.label("Pour un départ simultané", bg='Yellow', fg='black')
# #             app_Welcome.buttons(["Qualifications"], [Qualif])
# #             app_Welcome.label("Pour un départ avec un retard du côté :", bg='Gold', fg='black')
# #             app_Welcome.buttons(["Rouge", "Bleu"], [Colour, Colour])
# #             app_Welcome.label("Pour fermer l'application", bg='OrangeRed', fg='black')
# #             app_Welcome.buttons(["Exit"], [stop_Welcome])
# #             app_Welcome.enableEnter(Qualif)
# #      
# #     # Check variables
# #     #PrintVar()
# #     
# #     if bool(qualif)and not(bool(stop_GUI)):
# #         # Création de la fenêtre
# #         with gui("Qualifications", "500x200", bg='LightYellow', font={'size':22}) as app_Qualif:
# #             app_Qualif.label("Pressez start pour donner le départ", bg='lime', fg='black')
# #             app_Qualif.buttons(["Start", "Menu"], [Start_Q, Exit_qualif])
# #             app_Qualif.enableEnter(Start_Q)
# #             
# #     elif couleur==1:
# #         # Création de la fenêtre
# #         with gui("Retard pour la piste rouge", "600x300", bg='red', font={'size':22}) as app_Select_red_delay:
# #             app_Select_red_delay.label("Definissez le retard pour le côté rouge", bg='tomato', fg='black')
# #             app_Select_red_delay.entry("dossard", label=True, focus=True)
# #             app_Select_red_delay.entry("délai", label=True, focus=True)
# #             app_Select_red_delay.buttons(["Select", "Menu", "Chg. de côté"], [Select_red_delay, Exit_red, Chg_red_delay])
# #             app_Select_red_delay.enableEnter(Select_red_delay)
# #             
# #     elif couleur==-1:
# #         # Création de la fenêtre
# #         with gui("Retard pour la piste bleu", "600x300", bg='blue', font={'size':22}) as app_Select_blue_delay:
# #             app_Select_blue_delay.label("Definissez le retard pour le côté bleu", bg='deepskyblue', fg='black')
# #             app_Select_blue_delay.entry("dossard", label=True, focus=True)
# #             app_Select_blue_delay.entry("délai", label=True, focus=True)
# #             app_Select_blue_delay.buttons(["Select", "Menu", "Chg. de côté"], [Select_blue_delay, Exit_blue, Chg_blue_delay])
# #             app_Select_blue_delay.enableEnter(Select_blue_delay)
# #             #app_Select_blue_delay.bindKey("<Escape>", Exit_blue)
# #             
# #     elif bool(stop_GUI):
# #         print("Exit !!!")
# #             
# #     else:
# #         error=bool(1)
# #     
# #     #check the validity of delay_s
# #     maxmin_delay()
# #     
# #     # Check variables
# #     #PrintVar()
# #     
# #     if (not(bool(error)))and(not(bool(ready)))and(not(bool(qualif)))and(bool(var_set)):
# #         if couleur==1:
# #             # Création de la fenêtre
# #             with gui("Confirmation du délais", "600x300", bg='red', font={'size':22}) as app_Start_red:
# #                 app_Start_red.label("Le dossard numéro :", bg='coral', fg='black')
# #                 app_Start_red.label(dossard, bg='Yellow', fg='black')
# #                 app_Start_red.label("a un retard du côté rouge (en secondes):", bg='coral', fg='black')
# #                 app_Start_red.label(delay_s, bg='Yellow', fg='black')
# #                 app_Start_red.buttons(["Start", "Cancel"], [Start_red,app_Start_red.stop])
# #                 app_Start_red.enableEnter(Start_red)
# #                 
# #         elif couleur==-1:
# #             # Création de la fenêtre
# #             with gui("Confirmation du délais", "600x300", bg='blue', font={'size':22}) as app_Start_blue:
# #                 app_Start_blue.label("Le dossard numéro :", bg='Lightskyblue', fg='black')
# #                 app_Start_blue.label(dossard, bg='Yellow', fg='black')
# #                 app_Start_blue.label("a un retard du côté bleu (en secondes):", bg='Lightskyblue', fg='black')
# #                 app_Start_blue.label(delay_s, bg='Yellow', fg='black')
# #                 app_Start_blue.buttons(["Start", "Cancel"], [Start_blue,app_Start_blue.stop])
# #                 app_Start_blue.enableEnter(Start_blue)
# #                 
# #     else:
# #         delay_s=0
# #     
# #         # Check variables
# #     #PrintVar()
# #     
# #     if (not(bool(error)))and(bool(ready))and not(bool(stop_GUI)):
# #         Launch()
# #         print(" ")
# # #         depart_effectif=open(filename,"a")
# # #         depart_effectif.write("%d) " %Nbr_departs)# nombre de départ
# # #         depart_effectif.write("le dossard numéro %d a un retard en seconde de :" %(dossard))# nombre de départ
# # #         depart_effectif.write("%f\r\n" %(delay_s))
# # #         depart_effectif.write("     Le retard software est de %f\r\n" % (round(abs(tea_bleu-tea_rouge),6)))# Difference is:
# # #         depart_effectif.close()
# # #         # Création de la fenêtre
# # #         with gui("done", "600x300", bg='snow', font={'size':22}) as app_Launch:
# # #             app_Launch.label("Le départ à été donné...", bg='snow', fg='black')
# # #             app_Launch.buttons(["OK"], [app_Launch.stop])
# # #         #print("FIN de boucle")
# #     elif (bool(error)):
# #         # Création de la fenêtre
# #         with gui("error", "700x400", bg='snow', font={'size':22}) as app_Error:
# #             app_Error.label("Un problème est survenu,", bg='snow', fg='black')
# #             app_Error.label("aucun départ n'est donné...", bg='snow', fg='black')
# #             app_Error.label("Merci de n'écrire que des valeures numériques !!!", bg='snow', fg='black')
# #             app_Error.buttons(["OK"], [app_Error.stop])
# #             app_Error.enableEnter(app_Error.stop)
# #         print("Une erreur est survenue...")
# #         couleur=0
# #         qualif=0
# #     elif (not(bool(ready)))and(bool(var_set))and not(bool(stop_GUI)):
# #         couleur=0
# #         qualif=0
# #         print("La touche cancel a été pressée...")
# #     else:
# #         print(" ")
        #print("END !!!")

    