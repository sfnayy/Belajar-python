def is_leap(year):
    """
    Mengecek apakah sebuah tahun adalah kabisat (leap year).
    mengembalikan True jika kabisat, false jika tidak.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(year, month):
    """
    Menerima input tahun dan bulan (1-12),
    lalu mengembalikan jumlah hari dalam bulan tersebut.
    """
    #list jumlah hari dari jan-des (index 0 = jan 31 hari)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    #validasi input (multiple return untuk error handling)
    if month > 12 or month < 1:
        return "Bulan tidak valid."
    
    #logika khusus: kalau kabisat dan bulan feb (bulan ke 2)
    #kita pakai fungsi is_leap() yg sudah dibuat
    if is_leap(year) and month == 2:
        return 29
    
    #kalau bukan februari kabisat, ambil dari list
    #month - 1 kana index list mulai dari 0. (jan = 1-1 = 0)
    return month_days[month - 1]

#main program
year = int(input("Masukkan Tahun: "))
month = int(input("Masukkan bulan (1-12): "))

days = days_in_month(year,month)
print(f"Jumlah hari: {days}")