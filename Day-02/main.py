#Project Day 2: Tip Calculator
#Belajar menggunakan Tipe data int dan float, matematika, dan f-string

print("=== Selamat datang di Tip Calculator ===")

#pertama input tagihan
#kita pakai float() karena uang bisa desimal atau angka besar
tagihan = float(input("Masukkan total tagihan makanan: Rp. "))

#lalu input persen tip
#pakai int() karna biasanya persen itu bilangan bulat (10%, 12%, 15%)
tip = int(input("Masukkan persentase tip yang ingin Anda berikan (10, 12, atau 15): "))

#input jumlah orang
orang = int(input("Berapa orang yang ikut membayar tagihan? "))

#proses hitung
persen_desimal = tip / 100
total_uang_tip = tagihan * persen_desimal
total_semua = tagihan + total_uang_tip
bayar_per_orang = total_semua / orang

#membulatkan hasil jadi 2 angka di belakang koma
hasil_akhir =  round(bayar_per_orang, 2)
# atau format khusus agar pasti muncul 2 desimal 
hasil_format = "{:.2f}".format(bayar_per_orang)

#tampilkan hasil
print(f"setiap orang harus membayar: Rp. {hasil_format}")