#Lingkaran
import math  # Library untuk operasi matematika

# Lambda function untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r * r

# Contoh penggunaan
jari_jari = 7
area = luas_lingkaran(jari_jari)

# Menampilkan hasil dengan format dua desimal
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")


