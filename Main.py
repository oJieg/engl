import InpWord, TestWord, Interface
import sqlite3


def menMain():

    repty = Interface.general_memy()
    if repty == 'edit':
        InpWord.editMeny()
        menMain()
        # elif inp == '2':
        # outBD()
    elif repty == 'test':
        TestWord.HelloTestMeny("eng")
    # elif repty == "exit":

    elif repty == "new bd":
        con = sqlite3.connect("MaimBD.db")
        cur = con.cursor()
        cur.execute(
            "create table Glassary (ID integer primary key, EngWord, RuWord, coif DEFAULT 10, dataRepeat, Enable BLOB)")
# ________________________________________________________________________#
# _________________________________________________________________________#
# _________________________________________________________________________#


menMain()
