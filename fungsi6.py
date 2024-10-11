def zona_detak_jantung_latihan(usia):
    try:
        if usia <= 0:
            print("Error: Usia harus berupa angka positif.")
            return

        detak_jantung_maksimum = 220 - usia

        if usia < 20:
            zona_aerobik = (detak_jantung_maksimum * 0.70, detak_jantung_maksimum * 0.80)
            zona_anaerobik = (detak_jantung_maksimum * 0.80, detak_jantung_maksimum * 0.90)
        elif usia < 40:
            zona_aerobik = (detak_jantung_maksimum * 0.65, detak_jantung_maksimum * 0.75)
            zona_anaerobik = (detak_jantung_maksimum * 0.75, detak_jantung_maksimum * 0.85)
        else:
            zona_aerobik = (detak_jantung_maksimum * 0.60, detak_jantung_maksimum * 0.70)
            zona_anaerobik = (detak_jantung_maksimum * 0.70, detak_jantung_maksimum * 0.80)

        print(f"Detak jantung maksimum untuk usia {usia} tahun adalah {detak_jantung_maksimum:.2f} bpm.")
        print(f"Zona Aerobik: {zona_aerobik[0]:.1f} - {zona_aerobik[1]:.1f} bpm")
        print(f"Zona Anaerobik: {zona_anaerobik[0]:.1f} - {zona_anaerobik[1]:.1f} bpm")
        
    except:
        print(f"Inputan invalid")