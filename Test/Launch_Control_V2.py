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
# definition des Fonctions
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
        

# gestion du bouton "Qualifications"
def Qualif():
    global qualif
    global delay_s
    delay_s=0
    qualif=1
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
    delay_s = validNumEntry(app_Select_red_delay.getEntry("delay"))
    var_set=1
    print("-delay [s]= ",delay_s)
    app_Select_red_delay.stop()
    
# gestion du bouton "Select" lorsque "Bleu" à été sélectionné
def Select_blue_delay():
    global delay_s
    global var_set
    delay_s = validNumEntry(app_Select_blue_delay.getEntry("delay"))
    var_set=1
    print("-delay [s]= ",delay_s)
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
    

# test si l'entrée numérique est valide
def validNumEntry(c):
    global error
    try:
        r = float(c)
        return r
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
# gestion du départ
#-------------------------------------------------------------------
def Launch():
#     ----------------------------------------------------------    
    # Globals variables
#     ----------------------------------------------------------
    global qualif
    global couleur
    global delay_s
    global ready
    global error
    
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
    
    SP.on()
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
            continue
            
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
            SP.off()
            continue
        
        # FIN DE LA BOUCLE DE SEQUANCE
    print("Electro-aimants Rouge ouverts après : ", tea_rouge)
    print("Electro-aimants Bleu ouverts après  : ", tea_bleu)
    print("L'écart d'ouverture en seconde est  : ", abs(tea_bleu-tea_rouge))
    print("Temps d'execution du départ = ", time()-init_time)
    print("Nombre de tours de boucle   = ", i)
    return 0


#-------------------------------------------------------------------
# Boucle principale
#-------------------------------------------------------------------

# initialise les varibles (#b: 0=>FALSE / 1=>TRUE)
var_set=0
delay_s=0
ready=0#b
error=0#b
qualif=0#b
couleur=0

while 1:
    # réinitialise les varibles (#b: 0=>FALSE / 1=>TRUE)
    var_set=0
    delay_s=0
    ready=0#b
    error=0#b
    
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
    
    if (qualif==0)and(couleur==0):
        # Création de la fenêtre
        with gui("Menu Principale", "600x300", bg='snow', font={'size':22}) as app_Welcome:
            app_Welcome.label("Pour un départ simultané", bg='lightgreen', fg='black')
            app_Welcome.buttons(["Qualifications"], [Qualif])
            app_Welcome.label("Pour un départ avec une retard du côté :", bg='yellow', fg='black')
            app_Welcome.buttons(["Rouge", "Bleu"], [Colour, Colour])
     
    # Check variables
    #PrintVar()
    
    if qualif==1:
        # Création de la fenêtre
        with gui("Qualifications", "600x300", bg='snow', font={'size':22}) as app_Qualif:
            app_Qualif.label("Pressez start pour donner le départ", bg='orange', fg='black')
            app_Qualif.buttons(["Start", "Menu"], [Start_Q, Exit_qualif])
            
    elif couleur==1:
        # Création de la fenêtre
        with gui("delay pour la piste rouge", "600x300", bg='red', font={'size':22}) as app_Select_red_delay:
            app_Select_red_delay.label("Definissez le retard pour le côté rouge", bg='tomato', fg='black')
            app_Select_red_delay.entry("delay", label=True, focus=True)
            app_Select_red_delay.buttons(["Select", "Menu", "Chg. de côté"], [Select_red_delay, Exit_red, Chg_red_delay])
    
    elif couleur==-1:
        # Création de la fenêtre
        with gui("delay pour la piste bleu", "600x300", bg='blue', font={'size':22}) as app_Select_blue_delay:
            app_Select_blue_delay.label("Definissez le retard pour le côté bleu", bg='deepskyblue', fg='black')
            app_Select_blue_delay.entry("delay", label=True, focus=True)
            app_Select_blue_delay.buttons(["Select", "Menu", "Chg. de côté"], [Select_blue_delay, Exit_blue, Chg_blue_delay])
            
    else:
        error=1
    
    #check the validity of delay_s
    maxmin_delay()
    
    # Check variables
    #PrintVar()
    
    if (error==0)and(ready==0)and(qualif==0)and(var_set==1):
        if couleur==1:
            # Création de la fenêtre
            with gui("Confirmation du délais", "600x300", bg='red', font={'size':22}) as app_Start_red:
                app_Start_red.label("delay pour le côté rouge (en secondes):", bg='tomato', fg='black')
                app_Start_red.label(delay_s, bg='yellow', fg='black')
                app_Start_red.buttons(["Start", "Cancel"], [Start_red,app_Start_red.stop])
    
        elif couleur==-1:
            # Création de la fenêtre
            with gui("Confirmation du délais", "600x300", bg='blue', font={'size':22}) as app_Start_blue:
                app_Start_blue.label("delay pour le côté bleu (en secondes):", bg='deepskyblue', fg='black')
                app_Start_blue.label(delay_s, bg='yellow', fg='black')
                app_Start_blue.buttons(["Start", "Cancel"], [Start_blue,app_Start_blue.stop])
    else:
        delay_s=0
    
        # Check variables
    #PrintVar()
    
    if (error==0)and(ready!=0):
        Launch()
        # Création de la fenêtre
        with gui("done", "600x300", bg='snow', font={'size':22}) as app_Launch:
            app_Launch.label("Le départ à été donné...", bg='snow', fg='black')
            app_Launch.buttons(["OK"], [app_Launch.stop])
        print("FIN de boucle")
    elif (error!=0):
        # Création de la fenêtre
        with gui("error", "600x300", bg='snow', font={'size':22}) as app_Error:
            app_Error.label("Un problème est survenu,", bg='snow', fg='black')
            app_Error.label("aucun départ n'est donné...", bg='snow', fg='black')
            app_Error.buttons(["OK"], [app_Error.stop])
        print("FIN avec des erreurs")
        couleur=0
        qualif=0
    elif (ready==0)and(var_set==1):
        couleur=0
        qualif=0
        print("FIN avec Cancel")
    else:
        print("FIN de boucle")
            
    
    
    
    