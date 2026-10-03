# Generate Certify 🎓

Script Python otomatis untuk membuat ratusan/ribuan sertifikat secara massal menggunakan gambar template (.png/.jpg) dan daftar nama peserta dari file CSV. 

## 📦 Requirements

Pastikan Python sudah terinstal di komputer kamu, kemudian install library `Pillow`:

```bash
pip install Pillow
```

## 📂 Struktur Folder yang Dibutuhkan

Sebelum menjalankan script, pastikan struktur folder dan file kamu seperti ini:

```
generete-certify/
├── generate.py       # Script utama
├── template.png      # Template sertifikat kosong (tanpa nama)
├── ttd.png           # (Opsional) Gambar tanda tangan transparan
├── peserta.csv       # Data peserta (Nama dan Nomor Sertifikat)
└── out/              # Folder tempat sertifikat hasil generate disimpan (dibuat otomatis)
```

## 📄 Format CSV (`peserta.csv`)
Buat file `peserta.csv` menggunakan Excel, Google Sheets, atau teks editor. 
- Baris pertama (header) akan diabaikan.
- Kolom pertama berisi **Nama**, kolom kedua berisi **Nomor Sertifikat**.

**Contoh isi `peserta.csv`:**
```csv
Nama,Nomor Sertifikat
Budi Santoso,CERT/2026/001
Siti Aminah,CERT/2026/002
John Doe,CERT/2026/003
```

## ⚙️ Cara Menggunakan (Configuration)

Buka `generate.py` di teks editor kamu dan sesuaikan variabel konfigurasi di bagian atas jika diperlukan:

```python
# Konfigurasi Path
TEMPLATE_PATH = "template.png"
TTD_PATH = "ttd.png"
CSV_PATH = "peserta.csv"
OUTPUT_DIR = "out"

# Konfigurasi Font
FONT_PATH = "C:\\Windows\\Fonts\\arial.ttf" # Ganti sesuai font komputermu
FONT_SIZE_NAMA = 100
FONT_SIZE_NOMOR = 40

# Konfigurasi Warna
COLOR_NAMA = "black"
COLOR_NOMOR = "gray"
```

> **Tips Kordinat**: Script secara default menempatkan nama & nomor di tengah-tengah sertifikat. Kalau tidak pas dengan template kamu, kamu bisa atur variabel `x_nama`, `y_nama`, `x_nomor`, dan `y_nomor` di dalam baris kode.

## 🚀 Cara Menjalankan

Buka terminal/CMD di dalam folder project, lalu jalankan:

```bash
python generate.py
```

Selesai! Hasil sertifikat (misalnya `CERT2026001_BudiSantoso.png`) akan otomatis digenerate ke dalam folder `out/`.
