from datetime import date
import time

def animasi_mengetik(teks, kecepatan=0.1):
    for karakter in teks:
        print(karakter, end="", flush=True)
        time.sleep(kecepatan)
    print()

waktu = date.today()
tanggal = waktu.day
bulan = waktu.month
tahun = waktu.year

hari_indonesia = {
    "Monday": "Senin",
    "Tuesday": "Selasa",
    "Wednesday": "Rabu",
    "Thursday": "Kamis",
    "Friday": "Jumat",
    "Saturday": "Sabtu",
    "Sunday": "Minggu"
}
nama_hari_inggris = waktu.strftime("%A")
nama_hari = hari_indonesia[nama_hari_inggris]

while True:
    tgl = int(input("Masukkan tanggal lahir : "))
    bln = int(input("Masukkan bulan lahir   : "))
    thn = int(input("Masukkan tahun lahir   : "))

    if (tgl == tanggal and bln == bulan):
        umur = tahun - thn
        teks = f"\nSelamat Ulang Tahun yang ke -{umur} Dion!\n"
        animasi_mengetik(teks)
        break

    else:
        print("Ini Hari", nama_hari)