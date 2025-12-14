#membuat sapaan untuk user
print("Selamat datang di Generator Nama Band!")

#Meminta input nama kota dari user
#simpan input ke dalam variable kota
#\n digunakan agar kursor pindah ke baris baru ketika user mengetik
kota = input("Apa nama kota tempat kamu lahir?\n")

#Meminta input nama hewan peliharaan user
#simpan input ke dalam variable hewan
hewan = input("Apa nama hewan peliharaan kamu?\n")

#menggabungkan nama kota dan nama hewan
#tanda + digunakan untuk menggabungkan text (string concatenation)
print("Nama band kamu mungkin adalah " + kota + " " + hewan)