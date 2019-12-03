from gpiozero import LED, Button
from time import sleep, time

#save actual time
T_init=time()

#define Functions
# def pressed():
#     print("Output state is FALSE")
#     print(" ")
#     return 0
# 
# def released():
#     print("Output state is TRUE")
#     print(" ")
#     return 1

#definition des E/S
O_13 = LED(13)
I_18 = Button(18)

#I_18.when_pressed = pressed
#I_18.when_released = released

#definition des variables
delay=0.01 #sec
delay_test3=20 #sec
print("delay = ", delay, "sec")
print("delay_test3 = ", delay_test3, "sec")

#parametres
test_active=0
print("test_active = ", test_active)

#print execution time
print("Init execution time = ", time()-T_init)
print(" ")
print("-----------------------------------------------")
print(" ")
sleep(delay*5)

if (test_active == 1) or (test_active == 0):

    # Start of Test 1
    print("Test 1")
    print(" ")
    print("-----------------------------------------------")
    print(" ")

    #save actual time
    T_test1=time()
    O_13.off()

    #Start Test 1
    print("Test 1 begin after ", time()-T_test1, "sec")

    #Check input state
    print("After ", time()-T_test1, "sec")
    print("Output state is",not(I_18.is_pressed))
    print(" ")

    #set input value
    sleep(delay)
    O_13.on()

    #Check input state
    print("After ", time()-T_test1, "sec")
    print("Output state is",not(I_18.is_pressed))

    #set input value
    sleep(delay)
    O_13.off()

    #Check input state
    print("After ", time()-T_test1, "sec")
    print("Output state is",not(I_18.is_pressed))

    #set input value
    sleep(delay)
    O_13.on()

    #Check input state
    print("After ", time()-T_test1, "sec")
    print("Output state is",not(I_18.is_pressed))

    #set input value
    sleep(delay)
    O_13.off()

    #Check input state
    print("After ", time()-T_test1, "sec")
    print("Output state is",not(I_18.is_pressed))

    #print execution time
    print(" ")
    print("Test 1 execution time = ", time()-T_test1)
    print(" ")
    print("-----------------------------------------------")
    print(" ")
else:
    print("Test 1 skipped")
sleep(delay*5)

if (test_active == 2) or (test_active == 0):
    #-------------------------------------------------------------------
    #-------------------------------------------------------------------
    # Start of Test 2
    print("Test 2")
    print(" ")
    print("-----------------------------------------------")
    print(" ")

    #save actual time & test speed
    T_test2=time()
    O_13.off()

    print("Test 2 begin after ", time()-T_test2, "sec")

    # test accuracy of a difference of the function "time()"
    #Check input state
    print("After ", time()-T_test2, "sec")
    print("Output state is",not(I_18.is_pressed))
    print(" ")

    i=0
    while i>=0:
        if (time()-T_test2)>1*delay:
            O_13.on()
            print("Number of loops = ",i)
            i=-1
            #print("1")
        else:
            #print("0")
            i=i+1
            
    #Check input state
    print("After ", time()-T_test2, "sec")
    print("Output state is",not(I_18.is_pressed))

    i=0
    while i>=0:
        if (time()-T_test2)>2*delay:
            O_13.off()
            print("Number of loops = ",i)
            i=-1
            #print("1")
        else:
            #print("0")
            i=i+1
            
    #Check input state
    print("After ", time()-T_test2, "sec")
    print("Output state is",not(I_18.is_pressed))
        
    i=0
    while i>=0:
        if (time()-T_test2)>3*delay:
            O_13.on()
            print("Number of loops = ",i)
            i=-1
            #print("1")
        else:
            #print("0")
            i=i+1
            
    #Check input state
    print("After ", time()-T_test2, "sec")
    print("Output state is",not(I_18.is_pressed))
        
    i=0
    while i>=0:
        if (time()-T_test2)>4*delay:
            O_13.off()
            print("Number of loops = ",i)
            i=-1
            #print("1")
        else:
            #print("0")
            i=i+1
            
    #Check input state
    print("After ", time()-T_test2, "sec")
    print("Output state is",not(I_18.is_pressed))
        
    #End of test 2
    print(" ")
    print("Test 2 execution time = ", time()-T_test2)
    print(" ")
    print("-----------------------------------------------")
    print(" ")
else:
    print("Test 2 skipped")
sleep(delay*5)

if (test_active == 3) or (test_active == 0):
    #-------------------------------------------------------------------
    #-------------------------------------------------------------------
    # Start of Test 3
    print("Test 3")
    print(" ")
    print("-----------------------------------------------")
    print(" ")

    #save actual time & test speed
    T_test3=time()
    O_13.on()

    print("Test 3 begin after ", time()-T_test3, "sec")

    # test accuracy of a difference of the function "time()"
    #Check input state
    print("After ", time()-T_test3, "sec")
    print("Output state is",not(I_18.is_pressed))
    print(" ")

    i=0
    while i>=0:
        if (time()-T_test3)>1*delay_test3:
            print("Number of loops = ",i)
            i=-1
            O_13.off()
            #print("1")
        else:
            #print("0")
            i=i+1
            
    #Check input state
    print("After ", time()-T_test3, "sec")
    print("Output state is",not(I_18.is_pressed))


    #End of test 3
    print(" ")
    print("Test 3 execution time = ", time()-T_test3)
    print(" ")
    print("-----------------------------------------------")
    print(" ")
else:
    print("Test 3 skipped")
sleep(delay*5)
