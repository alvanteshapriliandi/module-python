# 7. Menyimpan Data Dictionary Mahasiswa
# 📌 Soal:
# Buat dictionary yang menyimpan nama, usia, dan jurusan seorang mahasiswa, lalu cetak dictionary tersebut!

mahasiswa = {"nama": "Alvan", "usia": 21, "jurusan": 'Teknik Informatika'}

print(mahasiswa)
print("===============")

print("Berikut ini nama data dari mahasiswa tersebut:")
print("- Nama:", mahasiswa["nama"])
print("- Usia:", mahasiswa["usia"])
print("- Jurusan:", mahasiswa["jurusan"])
mahasiswa["universitas"] = "Universitas Kemerdekaan"
mahasiswa["ipk"] = 4.0
print("- Universitas:", mahasiswa["universitas"])
print("- IPK:", mahasiswa["ipk"])

print("===============")
print(mahasiswa)