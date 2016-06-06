import Pars_url
import sqlite3, datetime, time

root_url = 'http://9giap.do.am'
con = sqlite3.connect("MaimBD.db")
cur = con.cursor()
time_ubdate = 120  # частота обновлений в сек
numb = 0


def Start():
    numb = float(input("hours job = "))
    numb *= (60 * 60) / time_ubdate
    for i in range(0, int(numb)):
        cycle()
        print(i, "/", int(numb), datetime.datetime.now())
        time.sleep(time_ubdate)

    con.commit()
    print("exit")
    meny()


def meny():
    print("hello")
    print("0 - exit")
    print("1 - start")
    print("2 - print BD")

    ne = input("input: ")
    if ne == "2":
        print_bd()
        meny()
    elif ne == "1":
        Start()
    else:
        print("+")
        con.close()

def cycle():
    Pars_url.next_searth(root_url)
    now = datetime.datetime.now()
    for i in Pars_url.nameV:
        cur.execute("insert into glassary (name, data, V_and_U) values ( ? , ?, ?)", (i, now, "V"))
        print(i, now, "V")

    for i in Pars_url.nameU:
        cur.execute("insert into glassary (name, data, V_and_U) values ( ? , ?, ?)", (i, now, "U"))
        print(i, now, "U")  # print(Pars_url.nameV, Pars_url.nameU)

def print_bd():
    cur.execute("select name, data, V_and_U from glassary")
    for n, d, vu in cur.fetchall():
        print(n, d, vu)
    inp = input("press key")

meny()


# time.sleep(5)
# print(datetime.datetime.now())

# os.system("cls")  # print(time.clock())
# print( time.clock())


# cur.execute("create table glassary (ID integer primary key, name, data, V_and_U)")
