print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Selamat datang di Pulau Harta Karun.")
print("Misi kamu adalah mendari harta karun yang hilang.")
      
#challenge satu
pilihan1 = input("Kamu berada di persimpangan jalan. Mau ke mana? ketik 'kiri' atau 'kanan'\n")

#kita gunakan .lower() agar inputan user tidak case sensitive
if pilihan1.lower() == "kiri":
    #challenge 2 (masuk ke dalam if pertama)
    pilihan2 = input("Kamu sampai di danau. Ada pulau di tengah nya. Mau 'berenang' atau 'tunggu' perahu?\n")
    if pilihan2.lower() == "tunggu":
        #challenge 3 (masuk kedalam if kedua)
        pilihan3 = input("Kamu sampai di pulau dengan selamat. Ada 3 pintu: Merah, Biru, dan Kuning. Pilih warna apa?\n")
        if pilihan3.lower() == "kuning":
            print("Horeee! kamu menemukan harta karun! Kamu menang!")
        elif pilihan3.lower() == "merah":
            print("Api menyembur dari pintu! Kamu terbakar! Game Over. 🔥")
        elif pilihan3.lower() == "biru":
            print("Kamu masuk ke ruangan monster! Kamu dimakan! Game Over. 👹")
        else:
            print("Pintu yang kamu pilih tidak ada! Game Over. 🚪")
        
    else:
        print("Kamu diserang buaya saat berenang! Game Over. 🐊")
else:
    print("Kamu jatuh ke jurang! Game Over. ⛰️")
    