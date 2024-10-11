
<h1 align="center">NoteMaster</h1>

HealthFitness adalah paket Python yang berisi kumpulan fungsi-fungsi dalam sebuah program atau modul yang bertujuan untuk membantu pengguna memantau dan memperkirakan berbagai aspek kesehatan dan kebugaran tubuh. Paket ini dirancang untuk menyediakan alat-alat sederhana yang bisa menghitung berbagai metrik kesehatan berdasarkan input pengguna, seperti berat badan, tinggi badan, usia, aktivitas, dan lain-lain

## Fitur
- **Pengecekan BMI (Body Mass Index)**:
  - Mengetahui Nilai BMI
  - Mengetahui Kategori BMI
- **Kebutuhan Kalori Harian**:
  - Mengetahui Kalori yang dibutuhkan dalam sehari berdasarkan tingkat aktivitas
- **Menghitung Kalori Yang digunakan**:
  - Mengetahui kalori yang di pakai seharian berdasarkan aktivitas dan lama aktivitas
- **Zona detak jantung**:
  - Mengetahui zona detak jantung aerobik dan anaerobik dan detak jantung maksium berdasarkan usia
  -parameter tinggi hanya 1.3 sampai 2 meter
- **Step To Meter**:
  - Mengkonversi Banyak langkah menjadi jarak dalam satuan meter
- **Asupan Air**:
  - Mengetahui kebutuhan air di tubuh dalam satuan liter berdasarkan berat badan


## Instalasi

Untuk menginstal paket HealthFitness, gunakan pip:

```bash
pip install HealthFitness
```

## Cara Menggunakan

Berikut adalah beberapa contoh cara menggunakan paket HealthFitness:

### Menghitung BMI
```python
from Health_and_Fitness_Check import check_bmi
check_bmi(1.8, 70.3, "2")
```

### Kebutuhan kalori harian

```python
from Health_and_Fitness_Check import kebutuhan_kalori_harian
kebutuhan_kalori_harian(70, 170, 19, "L", "sedang")
```

### Air yang harus di konsumsi

```python
from Health_and_Fitness_Check import rekomendasi_asupan_air
rekomendasi_asupan_air(70)
```

### Mengitung Kalori Terpakai 

```python
from Health_and_Fitness_Check import hitung_kalori
hitung_kalori(70, 60, jogging)
```

### Step To Meter

```python
from Health_and_Fitness_Check import jarak_langkah
jarak_langkah("L", 1.7, 2000)
```

### Mengecek Zona Detak Jantung
```python
from Health_and_Fitness_Check import zona_detak_jantung_latihan
zona_detak_jantung_latihan(12)
```

## Tentang Modul

Paket HealthFitness terdiri dari modul-modul berikut:

### `module BMI`

#### `check_bmi(tinggi, berat, jenis_kelamin)`
Fungsi ini digunakan untuk mengitung BMI dengan format yang sesuai berdasarkan tipe data yang dipilih.

**Parameter:**
- `tinggi (float)` : tinggi badan dalam satuan meter.
- `berat (float)` : berat badan dalam satuan kg.
- `jenis kelamin (str)` : "1"/ "laki laki" "2" / "perempuan"

**Contoh Penggunaan:**
```python
BMI = check_bmi(1.8, 70.3, "2")
print(BMI)
```
**Output:**
```
Dengan tinggi badan 1.8 m dan berat badan 70.3 kg, nilai BMI Anda adalah: 21.70
Kategori BMI Anda adalah: Normal (Perempuan)
```
### `module Kebutuhan Kalori Harian`

#### `kebutuhan_kalori_harian(berat, tinggi, usia, jenis_kelamin, tingkat_aktivitas`
Fungsi ini digunakan untuk menghitung kebutuhan kalori anda dalam sehari sesuai aktivitas anda

**Parameter:**
- `berat (float)`: Berat badan dalam kilogram
-` tinggi (float)` : tinggi dalam centimeter
- `usia (int)`: Umur dalam angka
- `jenis_kelamin (str)`: untuk laki-laki di simbolkan "L", sedangkan perempuan "P"
- `tingkat_aktifitas (str)`: rendah, sedang dan tinggi

**Contoh Penggunaan:**
```python
KebutuhanKalori = kebutuhan_kalori_harian(70, 170, 18, "L", "sedang")
print(kebutuhanKalori)
```

**Output:**
```
2,600.125 kalori
```

### `module Kalori Yang digunakan`

#### `hitung_kalori(berat_badan, durasi, aktivitas)`
Menghitung jumlah kalori yang kita butuhkan dalam sehari berdasarkan aktvitas
**Parameter**
- `berat_badan (float)`: Berat badan dalam kilogram.
- `durasi (float)`: Durasi aktivitas dalam menit.
- `aktivitas (str)`: Jenis aktivitas yang dilakukan.

**Aktifitas Tersedia**
- duduk di meja
- berjalan santai
- bersepeda ringan
- jogging 
- berenang
- lari cepat

**Contoh Penggunaan:**
```python
KaloriHariIni = hitung_kalori(70, 60, jogging)
print(KaloriHariIni)
```

**Output:**
```
551.25.
```
**Catatan**
Untuk update aktivitas akan menunggu update dari developer 

### `module zona detak jantung`
Menghitung zona detak jantung aerobik dan anerobik serta maksimum detak jantun berdasrakan usia.

#### `zona_detak_jantung_latihan(usia)`
**Parameter:**
- `usia (int)`: Umur dalam angka.

**Contoh Penggunaan:**
```python
zona = zona_detak_jantung_latihan(18)
print(zona)
```

**Output:**
```
Detak jantung maksimum untuk usia 19 tahun adalah 201 bpm.
Zona Aerobik: 140.7 - 160.8 bpm
Zona Anaerobik: 160.8 - 180.9 bpm
```

### `Module step to meter`
- Menghitung jarak dari banyak langkah yang ditempuh berdasarkan jenis kelamin dan tinggi badan.

#### `hitung_jarak(banyak_langkah, jenis_kelamin, tinggi)`
Fungsi ini digunakan untuk mengkonversi dari banyak langkah ke jarak dalam meter.

**Parameter:**
- `jenis_kelamin (str)`: untuk laki-laki disimbolkan "L", sedangkan perempuan "P"
- `tinggi_badan (float)`: tinggi badan dalam satuan meter
- `banyak_langkah (int)`: jumlah langkah yang ditempuh

**Contoh Penggunaan:**
```python
jarak = jarak_langkah("L", 1.7, 2000)
print(jarak)
```

**Output:**
```
Jarak yang ditempuh: 1,350.0 meter
```
**Catatan**
```
tinggi badan hanya bisa di gunakan di rentang 1.5 sampai 2 meter 
```

### `module Asupan air`

#### `rekomendasi_asupan_air(berat_badan)`
Fungsi ini digunakan untuk Menghitung Kebutuhan Air dalam sehari.

**Parameter:**
- `berat_badan (int)` : Berat Badan dalam kilogram.

**Contoh Penggunaan:**
```python
kebutuhanAir = rekomendasi_asupan_air(70)
```

**Output:**
```
2.45 liter.
```

## Kontak
Untuk pertanyaan lebih lanjut, silakan hubungi:
- rifqialan46475@gmail.com