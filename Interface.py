import sqlite3
import InpWord, Interface, TestWord
#class io_us:

gl = 0

def menMain():
    print("hello")
    print("1-add word")
    print("2-out word")
    print("3- exet")
    print("0-create table")

    ex = 0
    while ex == 0:
        inp = input("input command:  ")
        if inp == '1':
            InpWord.add()
        elif inp == '2':
            outBD()
        elif inp == "3":
            ex = 1
            break
        elif inp == "0":
            con = sqlite3.connect("MaimBD.db")
            cur = con.cursor()
            cur.execute("create table Glassary (ID integer primary key, EngWord, RuWord, coif, dataRepeat, Enable BLOB)")





def outBD():
    con = sqlite3.connect("MaimBD.db")
    cur = con.cursor()
    cur.execute("select ID, EngWord, RuWord, coif, dataRepeat, Enable from Glassary")
    for n, i, k, z, x, c in cur.fetchall():
        print(n, i, k, z, x, c)





