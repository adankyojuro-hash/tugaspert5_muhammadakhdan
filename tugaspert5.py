def input_matrik(r, c):
  return [[int(input(f"[{i+1}][{j+1}]: ")) for j in range(c)] for i in range(r)]

def tampilkan(m):
  for i in m:
    print(i)

while True:
  print("\n1.Tambah 2.Kurang 3.Kali 0.Exit")
  p = int(input("pilih: "))
  if p == 0:
    break

if p in [1, 2]:
  r = int(input("Baris: "))
  c = int(input('Kolom: "))
  print("Matrix A")
  A = input_matrik(r, c)
  print("Matrix B")
  B = input_matrix(r, c)

  hasil = [[A[i][j] + B[i][j] if p == 1 else A[i][j] - B[i][j]
            for j in range(c)] for i in range(r)]

  print("Hasil:")
  tampilkan(hasil)

elif p == 3:
  r1 = int(input("Baris A: "))
  c1 = int(input("Kolom A: "))
  r2 = int(input("Baris B: "))
  c2 = int(imput("Kolom B: "))

  if c1 != r2:
     print("Tidak bisa dikalikan!")
     continue

  print("Matrix A")
  A = input_matrix(r1, c1)
  print("Matrix B")
  B = input_matrix(r2, c2)
  
  hasil = [[sum(A[i][k]*B[k][j] for k in range(c1))
            for j in range(c2)] for i in range(r1)]
  
  print("Hasil:")
  tampilkan(hasil)

else:
  print("Pilihan Salah!!")
  
