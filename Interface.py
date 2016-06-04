import os


def general_memy():
    ex = 0
    while ex == 0:
        os.system("cls")
        print("hello")
        print("1-edit word")
        print("2-test")
        print("0- exet")
        print("3-create table")
        inp = input("input command:  ")
        if inp == '1':
            return "edit"
        elif inp == '2':
            return "test"
        elif inp == "3":
            return "new bd"
        elif inp == "0":
            return "exit"




def inpyt_meny(BD):
    # print(BD)
    ex = 0
    while ex == 0:
        os.system("cls")
        print("hello")
        for n, i, k, w in BD:
            print(n, i, k, w)
        print("______________")
        print(" 1 - add word")
        print(" 0 - exit")
        print(" 3 - del")
        print("______________")
        inp = input("input command:  ")
        if inp == '1':
            return "add"
        elif inp == '0':
            return "exit"
        elif inp == "3":
            return "del"

def add_meny():

    listA = [[], []]
    ex = 0
    while ex == 0:
        inp = input("eng:  ")
        inp2 = input("ru: ")
        listA[0].append(inp)
        listA[1].append(inp2)

        if input("0 - exit") == "0":
            return listA

def test_meny():
    ex = 0  # кол-во вопросов
    while ex == 0:
        os.system("cls")
        print("hello")
        print("elect size")
        print("1- size small")
        print("2- size mediym ")
        print("3 size big")
        print("0 - exit")
        inp = input("input command:  ")
        if inp == '1':
           return "small"
        elif inp == "2":
           return "mediym"
        elif inp == "3":
            return "big"
        elif inp == "0":
            return "exit"

def test_test(word_list, question, n, nMax):

    os.system("cls")
    print("№", n+1, "/", nMax)
    print(question)
  #  print(word_list)
    for x in range(1, len(word_list)):
        print(x, word_list[x])
    inp = input("??")

    if inp == str(word_list[0]+1):

        print("win")
        input("pess any key")
        return 1
    else:

        print("luz")
        print(word_list[word_list[0]+1])
        input("pess any key")
        return 0




