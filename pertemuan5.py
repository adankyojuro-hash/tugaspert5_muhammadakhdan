mahasiswa = {
  "10121001": "Asep",
  "10121002": "Budi",
  "10121003": "Cecep"
}

nilai = {
  "10121001": [50, 70, 40, 80],
  "10121002": [78, 78, 80, 65],
  "10121003": [57, 68, 67, 69]
}

rata_mahasiswa = {}
for nim in nilai:
  rata == sum(nilai[nim])/ len(nilai[nim])
  rata_mahasiswa[nim] = rata

nim_terbaik = max(rata_mahasiswa, key=rata_mahasiswa.get)

print("Mahasiswa Terbaik dan Terpintar :")
print("Nim  :", nim_terbaik)
print("Nama  :", mahasiswa[nim_terbaik])
print("Nilai  :", round(rata_mahasiswa[nim_terbaik], 2))

jumlah_mk = len(next(iter(nilai.values())))
rata_mk = []

for i in range(jumlah_mk):
  total = 0
  for nim in nilai:
    total += nilai[nim][i]
  rata = total / len(nilai)
  rata_mk.append(rata)

mk_terkecil = rata_mk.index(nim(rata_mk))

print("\nMata Kuliah Nilai Terkecil :")
print("MK", mk_terkecil + 1)
print("Nilai :", round(rata_ml[mk_terkecil], 2))
