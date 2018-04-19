import tkinter as tk
from tkinter import messagebox
import random as random

###Genel değişkenler
satır = 15
sutun = 15
mayınSayısı = 8
butonlar = {}
kalan_blok_sayısı = satır * sutun - mayınSayısı
print(kalan_blok_sayısı)
renk1 = '#%02x%02x%02x' % (64, 204, 208)
renk2 = '#40E0D0'

###Sınıflar
class buton():
    def __init__(self,satır,sutun,mayın = False):
        ###################
        self.satır = satır
        self.sutun = sutun
        self.mayın = mayın
        self.komsu_degeri = 0
        self.buton_kontrol = 0
        ###################
        ana.grid()
        ###################
        self.buton = tk.Button(ana,bg = renk1,fg='red',activebackground='red',activeforeground=renk2,command = self.mayın_coz,text = "     ")
        self.buton.grid(row = self.satır,column = self.sutun, sticky="nsew")
        ###################
        ana.grid_rowconfigure(self.satır,weight=1)
        ana.grid_columnconfigure(self.sutun,weight=1)
        ###################


    



    def mayın_coz(self):
        if self.buton_kontrol == 0:
                if self.mayın_mı() == True:
                    self.buton_kontrol = 1
                    self.buton.configure(text = "",image = mayın_resmi,bg = 'red',fg=renk1,activebackground='red',activeforeground='red')
                    oyun_bitimi(0)
                else:
                    if self.komsu_degeri == 0:
                        self.komsubul()
                    self.buton.configure(text = str(self.komsu_degeri),bg = 'red',fg=renk1,activebackground='red',activeforeground='red')
                    self.buton_kontrol = 1
                    global kalan_blok_sayısı
                    kalan_blok_sayısı -=1
                    if kalan_blok_sayısı == 0:
                        oyun_bitimi(1)
                
        
    def mayın_isaretle(self):
        self.mayın = True

    def mayın_mı(self):
        return self.mayın
    
    def komsuları_bul(self):
        try:
            if butonlar["buton"+str(self.satır-1)+","+str(self.sutun-1)].mayın_mı() == True:
                self.komsu_degeri += 1
        except:
            pass
        try:
            if butonlar["buton"+str(self.satır-1)+","+str(self.sutun)].mayın_mı() == True:
                self.komsu_degeri += 1
        except:
            pass
        try:
            if butonlar["buton"+str(self.satır-1)+","+str(self.sutun+1)].mayın_mı() == True:
                self.komsu_degeri += 1
        except:
            pass
        try:
            if butonlar["buton"+str(self.satır)+","+str(self.sutun-1)].mayın_mı() == True:
                self.komsu_degeri += 1
        except:
            pass
        try:
            if butonlar["buton"+str(self.satır)+","+str(self.sutun+1)].mayın_mı() == True:
                self.komsu_degeri += 1
        except:
            pass
        try:
            if butonlar["buton"+str(self.satır+1)+","+str(self.sutun-1)].mayın_mı() == True:
                self.komsu_degeri += 1
        except:
            pass
        try:
            if butonlar["buton"+str(self.satır+1)+","+str(self.sutun)].mayın_mı() == True:
                self.komsu_degeri += 1
        except:
            pass
        try:
            if butonlar["buton"+str(self.satır+1)+","+str(self.sutun+1)].mayın_mı() == True:
                self.komsu_degeri += 1
        except:
            pass
    def komsubul(self):
        if kontrol[0] != 1:
            try:
                if butonlar["buton"+str(self.satır-1)+","+str(self.sutun-1)].komsu_degeri == 0:
                    butonlar["buton"+str(self.satır-1)+","+str(self.sutun-1)].mayın_coz()
            except:
                kontrol[0] = 1
        if kontrol[1] != 1:
            try:
                if butonlar["buton"+str(self.satır-1)+","+str(self.sutun)].komsu_degeri == 0:
                    butonlar["buton"+str(self.satır-1)+","+str(self.sutun)].mayın_coz()
            except:
                kontrol[1] = 1
        if kontrol[2] != 1:
            try:
                if butonlar["buton"+str(self.satır-1)+","+str(self.sutun+1)].komsu_degeri == 0:
                    butonlar["buton"+str(self.satır-1)+","+str(self.sutun+1)].mayın_coz()
            except:
                kontrol[2] = 1
        if kontrol[3] != 1:
            try:
                if butonlar["buton"+str(self.satır)+","+str(self.sutun-1)].komsu_degeri == 0:
                    butonlar["buton"+str(self.satır)+","+str(self.sutun-1)].mayın_coz()
            except:
                kontrol[3] = 1
        if kontrol[4] != 1:
            try:
                if butonlar["buton"+str(self.satır)+","+str(self.sutun+1)].komsu_degeri == 0:
                    butonlar["buton"+str(self.satır)+","+str(self.sutun+1)].mayın_coz()
            except:
                kontrol[4] = 1
        if kontrol[5] != 1:
            try:
                if butonlar["buton"+str(self.satır+1)+","+str(self.sutun-1)].komsu_degeri == 0:
                    butonlar["buton"+str(self.satır+1)+","+str(self.sutun-1)].mayın_coz()
            except:
                kontrol[5] = 1
        if kontrol[6] != 1:
            try:
                if  butonlar["buton"+str(self.satır+1)+","+str(self.sutun)].komsu_degeri == 0:
                    butonlar["buton"+str(self.satır+1)+","+str(self.sutun)].mayın_coz()

            except:
                kontrol[6] = 1
        if kontrol[7] != 1:
            try:
                if  butonlar["buton"+str(self.satır+1)+","+str(self.sutun)].komsu_degeri == 0:
                    butonlar["buton"+str(self.satır+1)+","+str(self.sutun)].mayın_coz()
            except:
                kontrol[7] = 1
        
####Genel Fonksiyonlar
def ekranı_ortala():
        ana.update_idletasks()
        width = ana.winfo_width()
        height = ana.winfo_height()
        x = (ana.winfo_screenwidth() // 2) - (width // 2)
        y = (ana.winfo_screenheight() // 2) - (height // 2)
        ana.geometry('{}x{}+{}+{}'.format(width, height, x, y))
         

def oyun_bitimi(deger):
    for i in butonlar.keys():
        butonlar[i].buton_kontrol = 1
        if butonlar[i].mayın_mı() == True:
            butonlar[i].buton.configure(text = "",image = mayın_resmi,bg = 'green',fg=renk1,activebackground='green',activeforeground='green')
            #butonlar[i].buton.configure(state = "disable",image = mayın_resmi,bg = 'green',fg=renk1,activebackground='green',activeforeground='green')
        
    if deger == 0:
        kayıp_mesajı = messagebox.showerror("Bilgi","Oyunu kaybettin")
    elif deger == 1:
        kazan_mesajı = messagebox.showinfo("Bilgi","Oyunu kazandınız tebrikler")

####Ana ekran
ana = tk.Tk()
ana.title("MAYIN TARLASI")
ana.configure(bg = renk1)
mayın_resmi = tk.PhotoImage(file="mayın.gif")
ana.update_idletasks()
width = ana.winfo_width()
height = ana.winfo_height()


##2 Boyutlu Matrix Oluşturma For İle##
matrix = []
for x in range(satır):
    satır_list = []
    for y in range(sutun):
        satır_list.append(0)
        butonlar["buton"+str(x)+","+str(y)] = buton(x,y)
    matrix.append(satır_list)

##Mayın İşaretle
x = mayınSayısı
while x != 0:
    mayın = random.choice(list(butonlar.keys()))
    print(mayın)
    if butonlar[mayın].mayın_mı()==False:
        butonlar[mayın].mayın_isaretle()
        x -= 1
    else:
        continue
##Komşuları Bul
for x in range(satır):
    for y in range(sutun):
        butonlar["buton"+str(x)+","+str(y)].komsuları_bul()
##Kontrol Listesi
kontrol = {}
for i in range(0,8):
    kontrol[i]=0


ekranı_ortala()
