import sqlite3, random, Interface

con = sqlite3.connect("MaimBD.db")
cur = con.cursor()
listotv = [[], []]

winCoef = -1
loserCoef = 1

size_small = 3
size_mediym = 10
size_big = 20


def HelloTestMeny(Ru_):

    otv = Interface.test_meny()
    if  otv == "small":
        sizetest = size_small
    elif otv == "mediym":
        sizetest = size_mediym
    elif otv == "big":
        sizetest = size_big

    cur.execute("select ID from Glassary Order by ID Desc")
    sizea = cur.fetchmany(1)
    if sizetest > sizea[0][0]:
        sizetest = sizea[0][0]

    if sizetest != 0:
        testMenu(sizetest, Ru_)


def testMenu(sizetest, Ru_):

    cur.execute("select ID, EngWord, RuWord, coif from Glassary Order by coif")
    all_world_list = cur.fetchmany(sizetest)  # составляем список задействованых слов

    cur.execute("select ID from Glassary Order by ID Desc")
    sizea = cur.fetchmany(1)
    sizea = sizea[0][0]


    for i in range(sizetest):

        if Ru_ == "ru":  # !!!!!!!!!!!! если ру то русское слово в вариантах
            otv = rendPoint(all_world_list[i][2], "RuWord", sizea)
            if Interface.test_test(otv, all_world_list[i][1], i, sizetest) == 1:
                cur.execute("UPDATE Glassary SET coif=:coi WHERE Id=:id", {"coi": all_world_list[i][3] + winCoef, "id": all_world_list[i][0]})
            else:
                print(all_world_list[i][3] + loserCoef)
                cur.execute("UPDATE Glassary SET coif=:coi WHERE Id=:id", {"coi": all_world_list[i][3] + loserCoef, "id": all_world_list[i][0]})


        elif Ru_ == "eng":
            otv = rendPoint(all_world_list[i][1], "RuWord", sizea)
            if Interface.test_test(otv, all_world_list[i][2], i, sizetest) == 1:
                cur.execute("UPDATE Glassary SET coif=:coi WHERE Id=:id", {"coi": all_world_list[i][3] + winCoef, "id": all_world_list[i][0]})
            else:
                cur.execute("UPDATE Glassary SET coif=:coi WHERE Id=:id",
                            {"coi": all_world_list[i][3] + loserCoef, "id": all_world_list[i][0]})
    con.commit()



def rendPoint(answer, word, sizea):
    word_list = []
    tryanswer = random.randint(0, 4)
    word_list.append(tryanswer)
    for i in range(0, 5):

        if tryanswer == i:
            word_list.append(answer)
        else:
            ex = 0
            while ex == 0:
                if word == "RuWord":
                    cur.execute("select RuWord from  Glassary WHERE ID=:id ", {"id": random.randint(1, sizea)})
                elif word == "EngWord":
                    cur.execute("select EngWord from  Glassary WHERE ID=:id ", {"id": random.randint(1, sizea)})
                z = cur.fetchall()
                if z[0][0] != answer:
                    break
            word_list.append(z[0][0])
    return word_list
        #Interface.test_test(word_list, tryanswer)

