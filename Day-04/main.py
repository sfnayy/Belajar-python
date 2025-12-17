import random

batu = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
kertas = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)   
---.__________)
'''

gunting = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#menyimpan gambar dalam list
#urutannya penting 0=batu, 1=kertas, 2=gunting
gambar_game = [batu, kertas, gunting]

print("=== Selamat datang di permainan Batu, Kertas, Gunting ===")

#meminta input user
#meminta user memilih 0,1, atau 2
pilihan_user = int(input("Apa pilihanmu? Ketik 0 untuk Batu, 1 untuk kertas, atau 2 untuk Gunting.\n"))

#validasi: cek user input mengetik angka aneh atau tidak
if pilihan_user < 0 or pilihan_user >= 3:
    print("Pilihan tidak valid! Kamu kalah!")
else:
    #menampilkan pilihan user
    print(gambar_game[pilihan_user])
    
    #input komputer (random)
    print("Komputer memilih:")
    pilihan_komputer = random.randint(0, 2)
    print(gambar_game[pilihan_komputer])
    
#logika nentuin pemenang
#batu (0) menang lawan gunting (2)
#gunting (2) menang lawan kertas (1)
#kertas (1) menang lawan batu (0)

    if pilihan_user == 0 and pilihan_komputer == 2:
        print("Kamu menang! (Batu menghancurkan Gunting)")
    elif pilihan_user == 2 and pilihan_komputer == 0:
        print("Kamu kalah! (Batu menghancurkan Gunting)")
    elif pilihan_komputer > pilihan_user:
        print("Kamu kalah!")
    elif pilihan_user > pilihan_komputer:
        print("Kamu menang!")
    elif pilihan_user == pilihan_komputer:
        print("Seri!")