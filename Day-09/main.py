import os

#fungsi clear screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
#membuat fungsi matematika
#menggunakan return bukan print
def tambah(n1,n2):
    return n1 + n2

def kurang(n1,n2):
    return n1 - n2

def kali(n1,n2):
    return n1 * n2

def bagi(n1,n2):
    return n1 / n2

def pangkat(n1,n2):
    return n1 ** n2

#dict operasi
#menyimpan simbol dan fungsi math
operasi = {
    "+": tambah,
    "-": kurang,
    "*": kali,
    "/": bagi,
    "^": pangkat
}

#fungsi utama kalkulator
def kalkulator():
    print("=== KALKULATOR PYTHON ===")
    
    #input angka pertama
    num1 = float(input("Masukkan angka pertama: "))
    
    #ngambil semua simbol dari dict dan gabungin dengan koma
    #" ".join() artinya: gabungin semua item dengan pemisah spasi
    simbol_simbol = " , ".join(operasi)
    print(f"Operasi tersedia: {simbol_simbol}")
        
    lanjut = True
    
    while lanjut:
        operation_symbol = input("Pilih simbol operasi: ")
        num2 = float(input("Masukkan angka berikutnya: "))
        
        #ngambil fungsi dari dict
        #kalo user ngetik "+", maka fungsi kalkulasi jadi tambah
        
        kalkulasi = operasi[operation_symbol]
        
        #menjalankan fungsi terpilih
        #answer = tambah(num1, num2)
        answer = kalkulasi(num1, num2)
        
        #logika format angka
        #cek apakah jawabannya bilangan bulat
        if answer.is_integer():
            answer_print = int(answer)
        else:
            answer_print = answer
            
        print(f"{num1} {operation_symbol} {num2} = {answer_print}")
        
        #logika lanjut atau ulang
        pilih = input(f"Ketik 'y' untuk lanjut menghitung dengan {answer_print}, atau 'n' untuk mulai baru: ")
        
        if pilih == 'y':
            #hasil answer jadi angka pertama berikutnya
            num1 = answer
        else:
            lanjut = False
            clear_screen()
            #panggil fungsi kalkulator lagi
            kalkulator()

#panggil kalkulator
kalkulator()