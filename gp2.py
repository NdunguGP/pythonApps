
all_workOrder = []
planning = []
photocomp = []
reading = []
drawing = []
plateMaking = []
litho = []
letterpress = []
mono = []
binding = []
photocompSP = []
readingSP = []
drawingSP = []
plateMakingSP = []
lithoSP = []
bindingSP = []
dispatch = []


def new_workOrder ():
    new = int(input ("Enter the new work order number: "))
    if new not in all_workOrder:
        all_workOrder.append(new)
        planning.append(new)
    else:
        print("workoder number already exists")
    print("")
    print(all_workOrder)
    print("")

def move_Oder():

    print("Enter the workorder number to move")
    orderno = int(input())
    
    print("Select section to move from")
    print("========================================================================")
    print("=                                                                      =")
    print("=     1.Planning      2.Photocomp   3.ReadingSP        4.DrawingSP     =")
    print("=     5.Reading       6.Drawing     7.PlateMakingSP    8.LithoSP       =")
    print("=     9.PlateMaking  10.Litho      11.BindingSP       12.Dispatch      =")
    print("=    13.Letterpress  14.Mono       15.Binding         16.PhotocompSP   =")
    print("=                                                                      =")
    print("=                                                                      =")
    print("========================================================================")
    
    movefrom = int(input())
    
    print("Select section to move to")
    print("========================================================================")
    print("=                                                                      =")
    print("=     1.Planning      2.Photocomp   3.ReadingSP        4.DrawingSP     =")
    print("=     5.Reading       6.Drawing     7.PlateMakingSP    8.LithoSP       =")
    print("=     9.PlateMaking  10.Litho      11.BindingSP       12.Dispatch      =")
    print("=    13.Letterpress  14.Mono       15.Binding         16.PhotocompSP   =")
    print("=                                                                      =")
    print("=                                                                      =")
    print("========================================================================")

    moveto = int(input())

    if movefrom == 1:
        if orderno not in planning:
            print("The work order you entered was not found")
        else:
            planning.remove(orderno)
            if moveto == 2:
                photocomp.append(orderno)
            elif moveto == 3:
                readingSP.append(orderno)
            elif moveto == 4:
                drawingSP.append(orderno)
            elif moveto == 5:
                reading.append(orderno)
            elif moveto == 6:
                drawing.append(orderno)
            elif moveto == 7:
                plateMakingSP.append(orderno)
            elif moveto == 8:
                lithoSP.append(orderno)    
            elif moveto == 9:
                plateMaking.append(orderno)
            elif moveto == 10:
                litho.append(orderno)
            elif moveto == 11:
                bindingSP.append(orderno)
            elif moveto == 12:
                dispatch.append(orderno)
            elif moveto == 13:
                letterpress.append(orderno)
            elif moveto == 14:
                mono.append(orderno)
            elif moveto == 15:
                binding.append(orderno)
            elif moveto == 16:
                photocompSP.append(orderno)


    if movefrom == 2:
        if orderno not in photocomp:
            print("The work order you entered was not found")
        else:
            photocomp.remove(orderno)
            if moveto == 1:
                planning.append(orderno)
            elif moveto == 3:
                readingSP.append(orderno)
            elif moveto == 4:
                drawingSP.append(orderno)
            elif moveto == 5:
                reading.append(orderno)
            elif moveto == 6:
                drawing.append(orderno)
            elif moveto == 7:
                plateMakingSP.append(orderno)
            elif moveto == 8:
                lithoSP.append(orderno)    
            elif moveto == 9:
                plateMaking.append(orderno)
            elif moveto == 10:
                litho.append(orderno)
            elif moveto == 11:
                bindingSP.append(orderno)
            elif moveto == 12:
                dispatch.append(orderno)
            elif moveto == 13:
                letterpress.append(orderno)
            elif moveto == 14:
                mono.append(orderno)
            elif moveto == 15:
                binding.append(orderno)
            elif moveto == 16:
                photocompSP.append(orderno)


    if movefrom == 3:
        if orderno not in readingSP:
            print("The work order you entered was not found")
        else:
            readingSP.remove(orderno)
            if moveto == 2:
                photocomp.append(orderno)
            elif moveto == 1:
                planning.append(orderno)
            elif moveto == 4:
                drawingSP.append(orderno)
            elif moveto == 5:
                reading.append(orderno)
            elif moveto == 6:
                drawing.append(orderno)
            elif moveto == 7:
                plateMakingSP.append(orderno)
            elif moveto == 8:
                lithoSP.append(orderno)    
            elif moveto == 9:
                plateMaking.append(orderno)
            elif moveto == 10:
                litho.append(orderno)
            elif moveto == 11:
                bindingSP.append(orderno)
            elif moveto == 12:
                dispatch.append(orderno)
            elif moveto == 13:
                letterpress.append(orderno)
            elif moveto == 14:
                mono.append(orderno)
            elif moveto == 15:
                binding.append(orderno)
            elif moveto == 16:
                photocompSP.append(orderno)           
    

            
def trackWO():
    trace = int(input ("Enter the work oder number to track"))
    if trace in planning:
         print("workoder number {} iss inn planning section".format(trace))
    if trace in photocomp:
         print("workoder number {} iss inn photocomp section".format(trace))
    if trace in reading:
         print("workoder number {} iss inn reading section".format(trace))
    if trace in drawing:
         print("workoder number {} iss inn drawing section".format(trace))
    if trace in plateMaking:
         print("workoder number {} iss inn plateMaking section".format(trace))
    if trace in litho:
         print("workoder number {} iss inn litho section".format(trace))
    if trace in letterpress:
         print("workoder number {} iss inn letterpress section".format(trace))
    if trace in mono:
         print("workoder number {} iss inn mono section".format(trace))
    if trace in binding:
         print("workoder number {} iss inn binding section".format(trace))
    if trace in photocompSP:
         print("workoder number {} iss inn photocompSP section".format(trace))
    if trace in readingSP:
         print("workoder number {} iss inn readingSP section".format(trace))
    if trace in drawingSP:
         print("workoder number {} iss inn drawingSP section".format(trace))
    if trace in plateMakingSP:
         print("workoder number {} iss inn plateMakingSP section".format(trace))
    if trace in lithoSP:
         print("workoder number {} iss inn lithoSP section".format(trace))
    if trace in bindingSP:
         print("workoder number {} iss inn bindingSP section".format(trace))

def listWO():
    
    print("Select section to show work orders in that section")
    print("========================================================================")
    print("=                                                                      =")
    print("=     1.Planning      2.Photocomp   3.ReadingSP        4.DrawingSP     =")
    print("=     5.Reading       6.Drawing     7.PlateMakingSP    8.LithoSP       =")
    print("=     9.PlateMaking  10.Litho      11.BindingSP       12.Dispatch      =")
    print("=    13.Letterpress  14.Mono       15.Binding         16.PhotocompSP   =")
    print("=                                                                      =")
    print("=                                                                      =")
    print("========================================================================")

    tolist = int(input("Enter the section to list work oders:"))

    if tolist == 1:
        for item in planning:
            print(item)
        
    if tolist == 2:
        for item in photocomp:
            print(item)
    if tolist == 3:
        for item in readingSP:
            print(item)
    if tolist == 4:
        for item in drawingSP:
            print(item)        
    if tolist == 5:
        for item in reading:
            print(item)
    if tolist == 6:
        for item in photocomp:
            print(item)
    if tolist == 7:
        for item in photocomp:
            print(item)
    if tolist == 8:
        for item in photocomp:
            print(item)
    if tolist == 9:
        for item in photocomp:
            print(item)
    if tolist == 10:
        for item in photocomp:
            print(item)
    if tolist == 11:
        for item in photocomp:
            print(item)
    if tolist == 12:
        for item in photocomp:
            print(item)
    if tolist == 13:
        for item in photocomp:
            print(item)
    if tolist == 14:
        for item in photocomp:
            print(item)
    if tolist == 15:
        for item in photocomp:
            print(item)
    if tolist == 16:
        for item in photocomp:
            print(item)






            
def dispatch():
    dis = int(input ("Enter wo to dispatch"))

    if orderno not in dispatch:
        print("The work order you entered was not found")
    else:
        print("work order number {} dispatched".format(dis))
        dispatch.append(dis)    


while True:
    #start = input("Press enter/return to start or Q to quit")
    #if start.lower() == 'q':
    #    break

    print("Select task to perform")
    print("=======================================")
    print("=                                     =")
    print("=    1.Create new Order               =")
    print("=    2.Move Order                     =")
    print("=    3.Track an Order                 =")
    print("=    4.List Orders                    =")
    print("=    5.Dispatch job                   =")
    print("=    6.Quit                           =")
    print("=======================================")

    choice = int (input())

    if choice == 1:
        new_workOrder()
    if choice == 2:
        move_Oder()
    if choice == 3:
        trackWO()
    if choice == 4:
        listWO()
    if choice == 5:
        dispatch()
    if choice == 6:
        break
    
    
