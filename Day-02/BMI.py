#Program menghitung Body Mass Index (BMI)
print("=== Kalkulator BMI ===")

#input data
#menggunakan int() karena user pasti mengetik angka bulat contoh 170 atau 150
tinggi_cm = int(input("Masukkan tinggi badan (dalam cm): "))

#Berat badan menggunakan float() karena berat badan bisa desimal contoh 55.5 atau 70.2
berat = float(input("Masukkan berat badan (dalam kg): "))

#konversi logika
#user mengerti tinggi badan dalam cm, tapi rumus BMI pakai meter
#kita bagi 100 untuk mengubah cm ke meter
tinggi_meter = tinggi_cm / 100

#proses hitung rumus BMI (sekarang variable tinggi_meter isinya sudah desimal)
bmi = berat / (tinggi_meter ** 2)

#tampilkan hasil
bmi_format = round(bmi, 1)

#logika menentukan kategori BMI
if bmi < 18.5:
    kategori = "Kekurangan berat badan (kurus)"
elif bmi < 25:
    kategori = "Berat badan normal"
elif bmi < 30:
    kategori = "Kelebihan berat badan (gemuk)"
else:
    #bmi 30 atau lebih
    kategori = "Obesitas"

print(f"\nHasil Analisa:")
print(f"BMI Anda adalah: {bmi_format}")
print(f"Kategori: {kategori}")