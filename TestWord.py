import sqlite3, random, Interface

con = sqlite3.connect("MaimBD.db")
cur = con.cursor()
listotv = [[], []]

winCoef = -1
loserCoef = 1


def HelloTestMeny(Ru_):

    sizetest = Interface.test_meny()
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
            if rendPoint(all_world_list[i][2], "RuWord", sizea,all_world_list[i][1]) == 1:
                cur.execute("UPDATE Glassary SET coif=:coi WHERE Id=:id", {"coi": all_world_list[i][3] + winCoef, "id": all_world_list[i][0]})
            else:
                print(all_world_list[i][3] + loserCoef)
                cur.execute("UPDATE Glassary SET coif=:coi WHERE Id=:id", {"coi": all_world_list[i][3] + loserCoef, "id": all_world_list[i][0]})


        elif Ru_ == "eng":
            if rendPoint(all_world_list[i][1], "EngWord", sizea, all_world_list[i][2]) == 1:
                cur.execute("UPDATE Glassary SET coif=:coi WHERE Id=:id", {"coi": all_world_list[i][3] + winCoef, "id": all_world_list[i][0]})
            else:
                cur.execute("UPDATE Glassary SET coif=:coi WHERE Id=:id",
                            {"coi": all_world_list[i][3] + loserCoef, "id": all_world_list[i][0]})
    con.commit()



def rendPoint(answer, word, sizea, question):
    word_list=[]
    tryanswer = random.randint(0, 4)
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
    return Interface.test_test(word_list, tryanswer, question)

