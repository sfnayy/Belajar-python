import random

#Database Karakter
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("=== PyPassword Generator ===")

# input keinginan user
nr_letters = int(input("Berapa banyak huruf yang diinginkan?\n"))
nr_symbols = int(input("Berapa banyak simbol yang diinginkan?\n"))
nr_numbers = int(input("Berapa banyak angka yang diinginkan?\n"))

# proses kumpul karakter
# buat list kosong untuk menampung hasil acakan
password_list = []

#loop untuk mengambil huruf
# range (0,5) artinya loop berjalan 5 kali
for char in range(0, nr_letters):
    # Tambahkan huruf acak ke dalam list
    password_list.append(random.choice(letters))
    
#loop untuk mengambil simbol
for char in range(0, nr_symbols):
    # Tambahkan simbol acak ke dalam list
    password_list.append(random.choice(symbols))
    
#loop untuk mengambil angka
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
    
#mengacak urutan (shuffle)
#agar password tidak mudah ditebak polanya
random.shuffle(password_list)

# menggabungkan list jadi string
# kita ubah dari ['a', '1', '%'] jadi "a1%"
password=""
for char in password_list:
    password += char
    
print(f"Password yang dihasilkan: {password}")