import sqlite3, Interface

con = sqlite3.connect("MaimBD.db")
cur = con.cursor()


def editMeny():

    repty = Interface.inpyt_meny(outBD())

    if repty == 'add':
        add()
    elif repty == 'exit':
        return 0
    #elif repty == "del":
        #delword()


def add():
    listA = Interface.add_meny()
    for x in range(0, len(listA[0])):
        cur.execute("insert into Glassary (EngWord, RuWord) values ( ? , ?)", (listA[0][x], listA[1][x]))
    con.commit()
    # cur.close()


#def delword():
  # inp = input("inpyt id delite: ")
  # cur.execute("delete from Glassary where ID =:id ", {"id": inp})
  #  con.commit()


def outBD():
    cur.execute("select ID, EngWord, RuWord, coif from Glassary")
    return cur.fetchall()
