# Function 1 : Body Mass Index (BMI)
def hitung_bmi(tinggi, berat):
    """Menghitung BMI berdasarkan tinggi badan (meter) dan berat badan (kg)."""
    bmi = berat / tinggi**2
    return bmi

def kategori_bmi(jenis_kelamin, bmi):
    """Menentukan kategori BMI berdasarkan jenis kelamin dan nilai BMI."""
    if jenis_kelamin == "1" or jenis_kelamin == "laki laki":
        if bmi < 18:
            return "kekurangan berat badan (laki-laki)"
        elif 18 <= bmi <= 23.9:
            return "normal (laki-laki)"
        elif 24 <= bmi <= 26.9:
            return "kelebihan berat badan (laki-laki)"
        else:
            return "obesitas (laki-laki)"
    elif jenis_kelamin == "2" or jenis_kelamin == "perempuan":
        if bmi < 19:
            return "kekurangan berat badan (perempuan)"
        elif 19 <= bmi <= 24.9:
            return "normal (perempuan)"
        elif 25 <= bmi <= 27.9:
            return "kelebihan berat badan (perempuan)"
        else:
            return "obesitas (perempuan)"
    else:
        return "Jenis kelamin tidak valid"

# Fungsi untuk menampilkan hasil BMI dan kategorinya
def tampilkan_hasil_bmi(tinggi, berat, jenis_kelamin):
    """Fungsi untuk menghitung dan menampilkan hasil BMI dan kategori.
    Args :
        tinggi (float) : tinggi badan dalam satuan meter.
        berat (float) : berat badan dalam satuan kg.
        jenis kelamin (str) : "1"/ "laki laki" "2" / "perempuan".
    Example :
        tampilkan_hasil_bmi(1.8, 50.9, "perempuan")"""
    bmi = hitung_bmi(tinggi, berat)  # Panggil fungsi hitung_bmi dan simpan hasilnya
    kategori = kategori_bmi(jenis_kelamin, bmi)  # Panggil fungsi kategori_bmi dengan hasil BMI
    print(f"Dengan tinggi badan {tinggi} m dan berat badan {berat} kg, nilai BMI anda adalah : {bmi:.2f}")
    print(f"Kategori BMI anda adalah : {kategori}")
"""Anda bisa mencoba memanggil fungsinya disini dengan format seperti pada example"""