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
    global avance_s
    avance_s=0
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
    global avance_s
    global var_set
    avance_s = validNumEntry(app_Select_red_delay.getEntry("Avance"))
    var_set=1
    print("-avance [s]= ",avance_s)
    app_Select_red_delay.stop()
    
# gestion du bouton "Select" lorsque "Bleu" à été sélectionné
def Select_blue_delay():
    global avance_s
    global var_set
    avance_s = validNumEntry(app_Select_blue_delay.getEntry("Avance"))
    var_set=1
    print("-avance [s]= ",avance_s)
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
    global avance_s
    global var_set
    global ready
    global error
    print(" ")
    print("Check variables")
    print("-couleur   = ",couleur)
    print("-qualif    = ",qualif)
    print("-avance [s]= ",avance_s)
    print("-var_set   = ",var_set)
    print("-ready     = ",ready)
    print("-Error     = ",error)
    
def maxmin_avance():
    global avance_s
    error = 0
    max_s = 10 #secondes
    min_s = 0 #secondes
    if avance_s>max_s:
        avance_s=max_s
        error=1
    elif avance_s<min_s:
        avance_s=min_s
        error=1
    
    return error


#-------------------------------------------------------------------
# gestion du départ
#-------------------------------------------------------------------
def Launch():
    # define globals variables
    global qualif
    global couleur
    global avance_s
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

    # Signaux Chrono
    global SC_r
    global SC_b

    # Sorties de puissance
    global EA_r
    global EA_b
    global RP_r
    global RP_b
    
    # Locals variables
    delay=0.5
    init_time=time()
    
    r0=0; r1=0; r2=0; r3=0; r4=0; r5=0; r6=0; r8=0
    b0=0; b1=0; b2=0; b3=0; b4=0; b5=0; b6=0; b8=0
    x=0
    #marge=4
    decalage_s=avance_s/2
    #print(decalage_s)
    SP.on()
    while x==0:
        
        # gestion des GPIOs du coté rouge
        #-------------------------------------------------------------------
        #After 0 delay for red
        if ((init_time +decalage_s+(delay*0)-(couleur*decalage_s))<time())and(r0==0):
            LP1_r.on()
            BUZ_r.on()
            r0=1
            #print("r0 : ", time()-init_time)
            
        #After 1 delay for red
        if (init_time+decalage_s+(delay*1)-(couleur*decalage_s))<time()and(r1==0):
            BUZ_r.off()
            r1=1
            #print("r1 : ", time()-init_time)
            
        #After 2 delay for red
        if (init_time+decalage_s+(delay*2)-(couleur*decalage_s))<time()and(r2==0):
            LP2_r.on()
            BUZ_r.on()
            r2=1
            #print("r2 : ", time()-init_time)
            
        #After 3 delay for red
        if (init_time+decalage_s+(delay*3)-(couleur*decalage_s))<time()and(r3==0):
            BUZ_r.off()
            r3=1
            #print("r3 : ", time()-init_time)
            
        #After 4 delay for red
        if (init_time+decalage_s+(delay*4)-(couleur*decalage_s))<time()and(r4==0):
            LP3_r.on()
            BUZ_r.on()
            r4=1
            #print("r4 : ", time()-init_time)
            
        #After 5 delay for red
        if (init_time+decalage_s+(delay*5)-(couleur*decalage_s))<time()and(r5==0):
            BUZ_r.off()
            r5=1
            #print("r5 : ", time()-init_time)
            
        #After 6 delay for red
        if (init_time+decalage_s+(delay*6)-(couleur*decalage_s))<time()and(r6==0):
            LP4_r.on()
            BUZ_r.on()
            
            EA_r.on()
            
            r6=1
            #print("r6 : ", time()-init_time)
            
        #After 8 delay for red
        if (init_time+decalage_s+(delay*8)-(couleur*decalage_s))<time()and(r8==0):
            BUZ_r.off()
            r8=1
            print("Electro-aimants Rouge ouverts après : ", time()-init_time)
            
            
        # gestion des GPIOs du coté bleu
        #-------------------------------------------------------------------
        #After 0 delay for blue
        if ((init_time+decalage_s+(delay*0)+(couleur*decalage_s))<time())and(b0==0):
            LP1_b.on()
            BUZ_b.on()
            b0=1
            #print("b0 : ", time()-init_time)
            
            
        #After 1 delay for blue
        if (init_time+decalage_s+(delay*1)+(couleur*decalage_s))<time()and(b1==0):
            BUZ_b.off()
            b1=1
            #print("b1 : ", time()-init_time)
            
        #After 2 delay for blue
        if (init_time+decalage_s+(delay*2)+(couleur*decalage_s))<time()and(b2==0):
            LP2_b.on()
            BUZ_b.on()
            b2=1
            #print("b2 : ", time()-init_time)
            
        #After 3 delay for blue
        if (init_time+decalage_s+(delay*3)+(couleur*decalage_s))<time()and(b3==0):
            BUZ_b.off()
            b3=1
            #print("b3 : ", time()-init_time)
            
        #After 4 delay for blue
        if (init_time+decalage_s+(delay*4)+(couleur*decalage_s))<time()and(b4==0):
            LP3_b.on()
            BUZ_b.on()
            b4=1
            #print("b4 : ", time()-init_time)
            
        #After 5 delay for blue
        if (init_time+decalage_s+(delay*5)+(couleur*decalage_s))<time()and(b5==0):
            BUZ_b.off()
            b5=1
            #print("b5 : ", time()-init_time)
            
        #After 6 delay for blue
        if (init_time+decalage_s+(delay*6)+(couleur*decalage_s))<time()and(b6==0):
            LP4_b.on()
            BUZ_b.on()
            
            EA_b.on()
            
            b6=1
            #print("b6 : ", time()-init_time)
            
        #After 8 delay for blue
        if (init_time+decalage_s+(delay*8)+(couleur*decalage_s))<time()and(b8==0):
            BUZ_b.off()
            b8=1
            print("Electro-aimants Bleu ouverts après : ", time()-init_time)
            
        # condition de sortie de la boucle
        #-------------------------------------------------------------------
        #
        if (r8==1)and(b8==1):
            x=1
            EA_b.off()
            EA_r.off()
            SP.off()
    
    print("Temps d'execution du départ = ", time()-init_time)
    return 0


#-------------------------------------------------------------------
# Boucle principale
#-------------------------------------------------------------------
qualif=0#b
couleur=0

while 1:
    # initialise varibles (#b: 0=>FALSE / 1=>TRUE)
    var_set=0
    avance_s=0
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
        with gui("Initialisation", "600x300", bg='snow', font={'size':22}) as app_Welcome:
            app_Welcome.label("Pour un départ sans délais", bg='lightgreen', fg='black')
            app_Welcome.buttons(["Qualifications"], [Qualif])
            app_Welcome.label("Pour un départ avec une avance du côté :", bg='yellow', fg='black')
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
        with gui("Avance pour la piste rouge", "600x300", bg='red', font={'size':22}) as app_Select_red_delay:
            app_Select_red_delay.label("Definissez l'avance pour le côté rouge", bg='tomato', fg='black')
            app_Select_red_delay.entry("Avance", label=True, focus=True)
            app_Select_red_delay.buttons(["Select", "Menu", "Chg. de côté"], [Select_red_delay, Exit_red, Chg_red_delay])
    
    elif couleur==-1:
        # Création de la fenêtre
        with gui("Avance pour la piste bleu", "600x300", bg='blue', font={'size':22}) as app_Select_blue_delay:
            app_Select_blue_delay.label("Definissez l'avance pour le côté bleu", bg='deepskyblue', fg='black')
            app_Select_blue_delay.entry("Avance", label=True, focus=True)
            app_Select_blue_delay.buttons(["Select", "Menu", "Chg. de côté"], [Select_blue_delay, Exit_blue, Chg_blue_delay])
            
    else:
        error=1
    
    #check the validity of avance_s
    error=maxmin_avance()
    
    # Check variables
    #PrintVar()
    
    if (error==0)and(ready==0)and(qualif==0)and(var_set==1):
        if couleur==1:
            # Création de la fenêtre
            with gui("Confirmation du délais", "600x300", bg='red', font={'size':22}) as app_Start_red:
                app_Start_red.label("Avance pour le côté rouge (en secondes):", bg='tomato', fg='black')
                app_Start_red.label(avance_s, bg='yellow', fg='black')
                app_Start_red.buttons(["Start", "Cancel"], [Start_red,app_Start_red.stop])
    
        elif couleur==-1:
            # Création de la fenêtre
            with gui("Confirmation du délais", "600x300", bg='blue', font={'size':22}) as app_Start_blue:
                app_Start_blue.label("Avance pour le côté bleu (en secondes):", bg='deepskyblue', fg='black')
                app_Start_blue.label(avance_s, bg='yellow', fg='black')
                app_Start_blue.buttons(["Start", "Cancel"], [Start_blue,app_Start_blue.stop])
    else:
        avance_s=0
    
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
            
    
    
    
    