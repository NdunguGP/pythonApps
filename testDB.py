import sqlite3

conn = sqlite3.connect('peter.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS allOrders(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS planning(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS photocomp(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS reading(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS drawing(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS litho(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS binding(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS letterpress(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS mono(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS photocompSP(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS readingSP(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS lithoSP(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS bindingSP(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS dispatch(OrderNo INTEGER, Department TEXT, Product TEXT, Quantity INTEGER)')


def new_Order():
    OrderNo = int(input ("Enter the new work order number: "))
    Department = input ("Enter the department: ")
    Product = input ("Enter the product name: ")
    qty = int(input ("Enter quantity: "))
    
    c.execute("INSERT INTO allOrders  VALUES (?,?,?,?)", (OrderNo, Department, Product, qty) )

    c.execute("INSERT INTO planning SELECT * FROM allOrders")
    conn.commit()

def move_order():
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


    if movefrom == 1 and moveto == 2:
##        if c.execute("SELECT * FROM planning WHERE OrderNo = ?",orderno):
##            c.execute("INSERT INTO photocomp SELECT * FROM planning WHERE OrderNo = ?",orderno )
##        else:
##            print("oder number was not found in planning section")

            c.execute("SELECT * FROM planning WHERE OrderNo = ?",(orderno,))
            data = c.fetchall()
            if len(data)==0:
                print('oder number {} was not found in planning section '.format(orderno))
            else:
                c.execute("INSERT INTO photocomp SELECT * FROM planning WHERE OrderNo = ?",(orderno,) )



def view_db ():
    for row in c.execute('SELECT * FROM allOrders ORDER BY OrderNo'):
        print(row)

while True:
    print("select action to perform")
    print()
    print("1- add item to db  2-view db 3-Quit 4-moveOrder")
    print()
    que = int(input())
    if que == 1:
        create_table()
        new_Order()
    if que == 2:
        view_db()
    if que == 4:
        move_order()
    if que == 3:
        break
c.close()
conn.close()
