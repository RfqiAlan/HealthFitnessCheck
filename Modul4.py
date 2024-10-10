def rekomendasi_asupan_air(berat_badan):
    if isinstance(berat_badan, int):
        return berat_badan * 35 / 1000
    else:
        return "Masukkan dalam bentuk angka"
berat = rekomendasi_asupan_air(50)
print(f"{berat} liter")
