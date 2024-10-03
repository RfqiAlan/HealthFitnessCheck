"""Menghitung kebutuhan kalori harian berdasarkan statistik tubuh dan tingkat aktivitas."""

def kebutuhan_kalori_harian(berat, tinggi, usia, jenis_kelamin, tingkat_aktivitas):

    # Validasi input angka
    if berat <= 0:
        raise ValueError("Berat badan harus lebih besar dari 0.")
    if tinggi <= 0:
        raise ValueError("Tinggi badan harus lebih besar dari 0.")
    if usia <= 0:
        raise ValueError("Usia harus lebih besar dari 0.")
    
    # Hitung BMR
    if jenis_kelamin == 'L' or jenis_kelamin == 'l':
        bmr = 10 * berat + 6.25 * tinggi - 5 * usia + 5
    elif jenis_kelamin == 'P' or jenis_kelamin == 'p':
        bmr = 10 * berat + 6.25 * tinggi - 5 * usia - 161
    else:
        raise ValueError("Jenis kelamin tidak valid. Gunakan 'L' untuk laki-laki atau 'P' untuk perempuan.")
    
    # tingkat aktivitas
    if tingkat_aktivitas == 'rendah':
        kalori_harian = bmr * 1.2
    elif tingkat_aktivitas == 'sedang':
        kalori_harian = bmr * 1.55
    elif tingkat_aktivitas == 'tinggi':
        kalori_harian = bmr * 1.9
    else:
        raise ValueError("Tingkat aktivitas tidak valid. Gunakan 'rendah', 'sedang', atau 'tinggi'.")
    
    return kalori_harian

print(kebutuhan_kalori_harian(50, 150, 18, "p", "rendah"))

# while True:
#     try:
#         # Input pengguna
#         berat = int(input('Masukkan berat badan (kg) : ')) 
#         tinggi = int(input('Masukkan tinggi badan (cm) : '))  
#         usia = int(input('Masukkan usia (tahun) : '))   
#         jenis_kelamin = str(input('Masukkan jenis kelamin (L/P) : ')).upper()  
#         tingkat_aktivitas = str(input('Masukkan tingkat aktivitas (rendah/sedang/tinggi) : ')).lower()  

#         # kebutuhan kalori
#         kebutuhan_kalori = kebutuhan_kalori_harian(berat, tinggi, usia, jenis_kelamin, tingkat_aktivitas)
#         print(f"Kebutuhan kalori harian: {kebutuhan_kalori:.2f} kalori")

#     except ValueError as e:
#         print(f"Kesalahan: {e}. Pastikan input valid, gunakan angka untuk berat, tinggi, dan usia.")
    
#     # apakah pengguna ingin menghitung lagi
#     ulang = input("Ingin menghitung lagi? (ya/tidak): ").lower()
#     if ulang == 'tidak':
#         print("Terima kasih! Program selesai.")
#         break

