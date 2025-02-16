# 3. Struktur Data dalam Python
# 3.1 List (list)
# List adalah koleksi data yang bisa berubah (mutable), bisa berisi berbagai tipe data.

# ✅ Contoh List:

angka = [1, 2, 3, 4, 5]
campuran = [10, "Python", 3.14, True]

print(type(angka))  # Output: <class 'list'>

# Operator pada list

print(angka[0])      # Akses elemen pertama (1)
print(angka[-1])     # Akses elemen terakhir (5)
angka.append(6)      # Menambah elemen
angka.remove(3)      # Menghapus elemen
print(len(angka))    # Menghitung jumlah elemen

# 3.2 Tuple (tuple)
# Tuple mirip dengan list, tetapi tidak bisa diubah (immutable).

# ✅ Contoh Tuple:

data = (1, 2, 3, "Python")

print(type(data))

# Akses element tuple

# data[0] = 100 # kamu bisa uncomment baris code ini untuk melihat errornya

# 3.3 Dictionary (dict)
# Dictionary menyimpan data dalam bentuk key-value.

# ✅ Contoh Dictionary:

mahasiswa = {
    "nama": "Alvan",
    "umur": 21,
    "jurusan": "Informatika"
}

print(type(mahasiswa))  # Output: <class 'dict'>

# Mengakses nilai dalam dictionary
print(mahasiswa["nama"])  # Output: Alice

# Menambah elemen baru
mahasiswa["universitas"] = "Universitas ABC"

print(mahasiswa)