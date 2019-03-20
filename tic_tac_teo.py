print("""
*******************************************************
                     TIC TAC TEA 
oyun:
-3 satir ve 3 sutundan olusur.
-oyun iki kisiliktir birinci oyuncu X ikinci oyuncu O koyarak oynar.
-ayni satir, ayni sutun veya capraz ayni harfler geldiginde oyun kazanilir aksi 
taktirde oyun berabere biter. 

kullanici--> X
bilgisayar--> O

""")

import random
def tahta_olustur():
    global tahta
    tahta = []
    sayac=1
    for i in range(0,3):
        satir=[]
        for i in range(0,3):
            satir.append(sayac)
            sayac+=1
        tahta.append(satir)
tahta_olustur()

def tahta_yazdir():
    for i in range(3):
        for j in range(3):
            print(tahta[i][j],end=" ")
            if j<2:
                print("|",end=" ")
        print("\n",end="")
        if i<2:
            print("----------")


def xo(kordinat,xo):
    if kordinat<0 or kordinat>9:
        print("HATALI KORDINAT TUSLADINIZ!!")
        return
    else:
        if kordinat<=3:
            tahta[0][kordinat-1]=xo
        elif kordinat<=6:
            tahta[1][kordinat%3-1]=xo
        else:
            tahta[2][kordinat%3-1]=xo

def kazanan_x():
    boolean = False
    if tahta[0][0]=="X" and tahta[0][1]=="X" and tahta[0][2]=="X":
        boolean=True
    if tahta[1][0]=="X" and tahta[1][1]=="X" and tahta[1][2]=="X":
        boolean=True
    if tahta[2][0]=="X" and tahta[2][1]=="X" and tahta[2][2]=="X":
        boolean=True
    if tahta[0][0]=="X" and tahta[1][0]=="X" and tahta[2][0]=="X":
        boolean=True
    if tahta[0][1]=="X" and tahta[1][1]=="X" and tahta[2][1]=="X":
        boolean=True
    if tahta[0][2]=="X" and tahta[1][2]=="X" and tahta[2][2]=="X":
        boolean=True
    if tahta[0][0]=="X" and tahta[1][1]=="X" and tahta[2][2]=="X":
        boolean=True
    if tahta[0][2]=="X" and tahta[1][1]=="X" and tahta[2][0]=="X":
        boolean=True
    return boolean
def kazanan_o():
    boolean = False
    if tahta[0][0]=="O" and tahta[0][1]=="O" and tahta[0][2]=="O":
        boolean=True
    if tahta[1][0]=="O" and tahta[1][1]=="O" and tahta[1][2]=="O":
        boolean=True
    if tahta[2][0]=="O" and tahta[2][1]=="O" and tahta[2][2]=="O":
        boolean1=True
    if tahta[0][0]=="O" and tahta[1][0]=="O" and tahta[2][0]=="O":
        boolean=True
    if tahta[0][1]=="O" and tahta[1][1]=="O" and tahta[2][1]=="O":
        boolean=True
    if tahta[0][2]=="O" and tahta[1][2]=="O" and tahta[2][2]=="O":
        boolean=True
    if tahta[0][0]=="O" and tahta[1][1]=="O" and tahta[2][2]=="O":
        boolean=True
    if tahta[0][2]=="O" and tahta[1][1]=="O" and tahta[2][0]=="O":
        boolean=True
    return boolean
def berabere():
    if tahta[0][0] != 1 and tahta[0][1] != 2 and tahta[0][2] != 3 and tahta[1][0] != 4 and tahta[1][1] != 5 and \
            tahta[1][2] != 6 and tahta[2][0] != 7 and tahta[2][1] != 8 and tahta[2][2] != 9:
        return True

def bilgisayar_kz():
    if ((tahta[0][1]=="O" and tahta[0][2]=="O") or (tahta[1][0]=="O" and tahta[2][0]=="O") or (tahta[1][1]=="O" and tahta[2][2]=="O")) \
            and tahta[0][0]==1:
        return 1
    if ((tahta[0][0] == "O" and tahta[0][2] == "O") or (tahta[1][1] == "O" and tahta[2][1] == "O")) and tahta[0][1]==2:
        return 2
    if ((tahta[0][0] == "O" and tahta[0][1] == "O") or (tahta[1][2] == "O" and tahta[2][2] == "O") or (tahta[1][1]=="O" \
        and tahta[2][0]=="O")) and tahta[0][2]==3:
        return 3
    if ((tahta[0][0] == "O" and tahta[2][0] == "O") or (tahta[1][1] == "O" and tahta[1][2] == "O")) and tahta[1][0]==4:
        return 4
    if ((tahta[0][0]=="O" and tahta[2][2]=="O") or (tahta[0][2]=="O" and tahta[2][0]=="O") or (tahta[1][0]=="O" and tahta[1][2]=="O") \
            or (tahta[0][1]=="O" and tahta[2][1]=="O")) and tahta[1][1]==5:
        return 5
    if ((tahta[0][2]=="O" and tahta[2][2]=="O") or (tahta[1][0]=="O" and tahta[1][1]=="O")) and tahta[1][2]==6:
        return 6
    if ((tahta[0][0] == "O" and tahta[1][0] == "O") or (tahta[2][1] == "O" and tahta[2][2] == "O") or (tahta[1][1]=="O" and tahta[0][2]=="O")) and tahta[2][0]==7:
        return 7
    if ((tahta[0][1]=="O" and tahta[1][1]=="O") or (tahta[2][0]=="O" and tahta[2][2]=="O")) and tahta[2][1]==8:
        return 8
    if ((tahta[0][0] == "O" and tahta[1][1] == "O") or (tahta[2][0] == "O" and tahta[2][1] == "O") or (tahta[0][2]=="O" and tahta[1][2]=="0")) and tahta[2][2]==9:
        return 9
    else:
        return 0

def kazanma_derecesi():
    if ((tahta[0][1]=="X" and tahta[0][2]=="X") or (tahta[1][0]=="X" and tahta[2][0]=="X") or (tahta[1][1]=="X" and tahta[2][2]=="X")) and tahta[0][0]==1:
        return 1
    if ((tahta[0][0] == "X" and tahta[0][2] == "X") or (tahta[1][1] == "X" and tahta[2][1] == "X")) and tahta[0][1]==2:
        return 2
    if ((tahta[0][0] == "X" and tahta[0][1] == "X") or (tahta[1][2] == "X" and tahta[2][2] == "X") or (tahta[1][1]=="X" and tahta[2][0]=="X")) and tahta[0][2]==3:
        return 3
    if ((tahta[0][0] == "X" and tahta[2][0] == "X") or (tahta[1][1] == "X" and tahta[1][2] == "X")) and tahta[1][0]==4:
        return 4
    if ((tahta[0][0]=="X" and tahta[2][2]=="X") or (tahta[0][2]=="X" and tahta[2][0]=="X") or (tahta[1][0]=="X" and tahta[1][2]=="X") \
            or (tahta[0][1]=="X" and tahta[2][1]=="X")) and tahta[1][1]==5:
        return 5
    if ((tahta[0][2]=="X" and tahta[2][2]=="X") or (tahta[1][0]=="X" and tahta[1][1]=="X")) and tahta[1][2]==6:
        return 6
    if ((tahta[0][0] == "X" and tahta[1][0] == "X") or (tahta[2][1] == "X" and tahta[2][2] == "X") or (tahta[1][1]=="X" and tahta[0][2]=="X")) and tahta[2][0]==7:
        return 7
    if ((tahta[0][1]=="X" and tahta[1][1]=="X") or (tahta[2][0]=="X" and tahta[2][2]=="X")) and tahta[2][1]==8:
        return 8
    if ((tahta[0][0] == "X" and tahta[1][1] == "X") or (tahta[2][0] == "X" and tahta[2][1] == "X") or (tahta[0][2]=="X" and tahta[1][2]=="X")) and tahta[2][2]==9:
        return 9
    else:
        return 0

sayac=1
oyuncu = 1
girilen_sayilar = [1,2,3,4,5,6,7,8,9]
while True:
    tahta_yazdir()
    if kazanan_x()==True:
        print("1.OYUNCU KAZANDI")
        break
    if kazanan_o()==True:
        print("2.OYUNCU KAZANDI")
        break
    if berabere()==True:
        print("BERABERE!!")
        break

    print("\n")

    if oyuncu==1:
        print("kullanici:",end="")
        girdi=int(input())
        for i in girilen_sayilar:
            if i==girdi:
                sayac=0
        if sayac==0:
            xo(girdi, "X")
            girilen_sayilar.remove(girdi)
        else:
            print("bu index dolu lütfen baþka bir index girin:", end=" ")
            girdi = int(input())
            continue

    else:
        if bilgisayar_kz()!=0:
            print("bilgisayar kazanma derecesi:", bilgisayar_kz())
            for i in girilen_sayýlar:
                if i == bilgisayar_kz():
                    sayac = 0
            if sayac == 0:
                xo(bilgisayar_kz(), "O")
            else:
                continue
        elif kazanma_derecesi()!=0:
            print("derece kontrol:", kazanma_derecesi())
            for i in girilen_sayilar:
                if i == kazanma_derecesi():
                    sayac = 0
            if sayac==0:
                xo(kazanma_derecesi(),"O")
            else:
                continue
        else:
            rnd=random.choice(girilen_sayilar)
            for i in girilen_say,lar:
                if i == rnd:
                    sayac=0
            if sayac == 0:
                xo(rnd, "O")
                print("rnd:", rnd)
                girilen_sayilar.remove(rnd)
            else:
                if sayac == 0:
                    xo(rnd, "O")
                    print("rnd:", rnd)
                    girilen_sayilar.remove(rnd)
                else:
                    rnd = random.choice(girilen_sayilar)
                    continue
    if oyuncu==1:
        oyuncu=2
    else:
        oyuncu=1
