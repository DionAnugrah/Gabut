import array

jumlahSiswa = int(input("Masukkan jumlah siswa : "))
nilai = array.array('i', [0] * jumlahSiswa)

for i in range(jumlahSiswa):
    nilai[i] = int(input(f"Masukkan nilai siwa ke-{i+1} : "))
    total = sum(nilai)
    
rata = total/jumlahSiswa
max = max(nilai)
min = min(nilai)

print ("\nTotal           : ", total)
print ("Rata-rata       : ", rata)
print ("Nilai Tertinggi : ", max)
print ("Nilai Terendah  : ", min)

input()