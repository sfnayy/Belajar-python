#kode caesar cipher
# list alphabet tulis dobel 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    
    #logika jika decode(mundur)
    if cipher_direction == "decode":
        shift_amount *= -1
        
    for char in start_text:
        #cek karakter ada di alphabet (kalau spasi atau angka tidak dihitung)
        if char in alphabet:
            #cari posisi huruf
            position = alphabet.index(char)
            
            #geser posisi baru
            new_position = position + shift_amount
            
            #ambil huruf di posisi baru dan masukkan ke end_text
            end_text += alphabet[new_position]
        else:
            #jika bukun huruf di posisi baru dan masukkan ke hasil
            end_text += char
            
    print(f"Pesan hasil {cipher_direction} adalah: {end_text}")
    
#main logic
print("=== CAESAR CIPHER ===")

should_continue = True
while should_continue:
    direction = input("Ketik 'encode' untuk mengenkripsi, 'decode' untuk mendekripsi:\n")
    text = input("Masukkan pesan Anda:\n").lower()
    shift = int(input("Masukkan jumlah pergeseran:\n"))
    
    #trik: kalau user masukin angka 100 kita modulus 26 agar tidak error
    #karena 26 huruf alphabet, geser 27 itu sama saja geser 1.
    shift = shift % 26
    #memanggil fungsi caesar
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    #tanya user mau lanjut atau tidak
    result = input("Apakah Anda ingin melanjutkan? Ketik 'yes' atau 'no'.\n")
    if result == "no":
        should_continue = False
        print("Terima kasih telah menggunakan program ini. Sampai jumpa lagi!")