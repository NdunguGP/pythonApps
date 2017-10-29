
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
    tomove = int(input("Enter the workorder to move: "))
    fromsec = input("Enter the section to move fromm")
    tosec = input ("Enter the section to move to")
    print(fromsec)
    print(tosec)
    if fromsec == planning:
        print("moving workoder from {}".format(fromsec))
        planning.remove(tomove)
        print("workoder in planning after removing {}".format(tomove))
        print(planning)

    if tosec == photocomp:
        photocomp.append(tomove)
        print("workoder in photocomp after adding {}".format(tomove))
        print(photocomp)
    if fromsec == planning and tosec == reading:
        planning.remove(tomove)
        reading.append(tomove)
    if fromsec == planning and tosec == drawing:
        planning.remove(tomove)
        drawing.append(tomove)


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
    print(  "1-planning,2-photocomp,3-reading,4-drawing ,5-plateMaking,6-litho,7-letterpress,8-mono,9-binding,10-photocompSP,11-readingSP,12-drawingSP,13-plateMakingSP,14-lithoSP,15-bindingSP,16-dispatch")
    tolist = input("Enter the section to list work oders:")
    if tolist == 1:
        print(planning)
    if tolist == 2:
        print(photocomp)
    if tolist == 3:
        print(reading)
    if tolist == 4:
        print(drawing)
    if tolist == 5:
        print(plateMaking)
    if tolist == 6:
        print(litho)
    if tolist == 7:
        print(letterpress)
    if tolist == 8:
        print(mono)
    if tolist == 9:
        print(binding)
    if tolist == 10:
        print(photocompSP)
    if tolist == 11:
        print(readingSP)
    if tolist == 12:
        print(drawingSP)
    if tolist == 13:
        print(plateMakingSP)
    if tolist == 14:
        print(lithoSP)
    if tolist == 15:
        print(bindingSP)

def dispatch():
    dis = input ("Enter wo to dispatch")
    print("work order number {} dispatched".format(dis))
    dispatch.append(dis)    


while True:
    start = input("Press enter/return to start or Q to quit")
    if start.lower() == 'q':
        break

    print("Select task to perform")
    print("=======================================")
    print("=                                     =")
    print("=    1.Create new Order               =")
    print("=    2.Move Order                     =")
    print("=    3.Dispatch job                   =")
    print("=    4.List Orders                    =")
    print("=    5.Track an Order                 =")
    print("=                                     =")
    print("=======================================")

    choice = int (input())

    if choice == 1:
        new_workOrder()
    if choice == 2:
        move_Oder()
    if choice == 3:
        dispatch()
    if choice == 4:
        listWO()
    if choice == 5:
        trackWO()
    
    
