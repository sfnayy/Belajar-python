#Secret Auction Program
import os

def clear_screen():
    #fungsi untuk membersihkan layar terminal
    if os.name == 'nt':
        os.system('cls')
    #cek jika maclinux, perintahnya clear
    else:
        os.system('clear')
        
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Selamat datand di Pelelangan Rahasia")

#Membuat dictionary kosong
#Isinya akan seperti {'Sofyan': 150000, 'Laut': 200000}
bids = {}

#Fungsi cari yang menang
def cari_lelang_tertinggi(bidding_record):
    tertinggi = 0
    pemenang = ""
    
    #looping di dictionary
    #variabel 'bidder' diisi key (nama orang)
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder] #ngambil value (harga)
        
        if bid_amount > tertinggi:
            tertinggi = bid_amount
            pemenang = bidder
    
    print(f"Pemenangnya adalah {pemenang} dengan tawaran sebesar RP. {tertinggi}")

#loop input data
finished = False
while not finished:
    nama = input("Masukkan nama penawar: ")
    harga = int(input("Masukkan harga penawaran: RP. "))
    
    #simpan ke dictionary kosong 
    #format: dictionary[key] = value
    bids[nama] = harga
    
    lanjut = input("Apakah ada penawar lain? Ketik 'yes' atau 'no'.\n")
    
    if lanjut.lower() == "no":
        finished = True
        cari_lelang_tertinggi(bids)
    elif lanjut == "yes":
        #bersihkan layar (cetak banyak baris baru)
        #agar orang selanjutnya tidak melihat penawaran sebelumnya
        clear_screen()
        