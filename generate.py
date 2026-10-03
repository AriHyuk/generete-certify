import os
import csv
from PIL import Image, ImageDraw, ImageFont

# Konfigurasi Path
TEMPLATE_PATH = "template.png"
TTD_PATH = "ttd.png"
CSV_PATH = "peserta.csv"
OUTPUT_DIR = "out"

# Konfigurasi Font
# Windows biasanya punya arial.ttf, bisa disesuaikan dengan font lain
FONT_PATH = "C:\\Windows\\Fonts\\arial.ttf" 
FONT_SIZE_NAMA = 100
FONT_SIZE_NOMOR = 40

# Konfigurasi Warna
COLOR_NAMA = "black"
COLOR_NOMOR = "gray"

# Pastikan folder output ada
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_certificate(nama, nomor):
    try:
        # 1. Buka template (convert ke RGBA untuk support transparansi kalau ada)
        img = Image.open(TEMPLATE_PATH).convert("RGBA")
        draw = ImageDraw.Draw(img)
        
        # 2. Load font
        try:
            font_nama = ImageFont.truetype(FONT_PATH, FONT_SIZE_NAMA)
            font_nomor = ImageFont.truetype(FONT_PATH, FONT_SIZE_NOMOR)
        except IOError:
            print(f"⚠️ Font {FONT_PATH} tidak ditemukan. Menggunakan font default.")
            font_nama = ImageFont.load_default()
            font_nomor = ImageFont.load_default()

        # Dapatkan ukuran gambar template
        img_w, img_h = img.size

        # 3. Menulis Nama
        # Posisi default: di tengah gambar. Sesuaikan y_nama dengan desain template!
        bbox_nama = draw.textbbox((0, 0), nama, font=font_nama)
        text_w = bbox_nama[2] - bbox_nama[0]
        text_h = bbox_nama[3] - bbox_nama[1]
        x_nama = (img_w - text_w) / 2
        y_nama = (img_h - text_h) / 2 - 50 # Di tengah agak ke atas
        
        draw.text((x_nama, y_nama), nama, fill=COLOR_NAMA, font=font_nama)

        # 4. Menulis Nomor Sertifikat
        bbox_nomor = draw.textbbox((0, 0), nomor, font=font_nomor)
        no_w = bbox_nomor[2] - bbox_nomor[0]
        no_h = bbox_nomor[3] - bbox_nomor[1]
        x_nomor = (img_w - no_w) / 2
        y_nomor = y_nama + text_h + 50 # Di bawah nama
        
        draw.text((x_nomor, y_nomor), nomor, fill=COLOR_NOMOR, font=font_nomor)

        # 5. Menempel Tanda Tangan (Opsional)
        if os.path.exists(TTD_PATH):
            ttd = Image.open(TTD_PATH).convert("RGBA")
            
            # (Opsional) Resize TTD jika ukurannya kebesaran
            # w_percent = (300 / float(ttd.size[0]))
            # h_size = int((float(ttd.size[1]) * float(w_percent)))
            # ttd = ttd.resize((300, h_size), Image.Resampling.LANCZOS)
            
            # Posisi TTD (contoh: pojok kanan bawah)
            x_ttd = img_w - ttd.size[0] - 100
            y_ttd = img_h - ttd.size[1] - 100
            
            # Paste TTD sebagai layer transparan
            img.paste(ttd, (x_ttd, y_ttd), ttd)
        
        # 6. Simpan hasil akhir
        # Bersihkan nama untuk penamaan file yang aman
        safe_name = "".join([c for c in nama if c.isalpha() or c.isdigit() or c==' ']).rstrip()
        output_path = os.path.join(OUTPUT_DIR, f"{nomor}_{safe_name}.png")
        
        # Convert ke RGB untuk simpan sbg JPG atau PNG solid
        img.convert("RGB").save(output_path)
        print(f"✅ Berhasil: {output_path}")

    except Exception as e:
        print(f"❌ Error memproses '{nama}': {e}")

def main():
    if not os.path.exists(TEMPLATE_PATH):
        print(f"❌ File template '{TEMPLATE_PATH}' tidak ditemukan!")
        return

    if not os.path.exists(CSV_PATH):
        print(f"❌ File CSV '{CSV_PATH}' tidak ditemukan!")
        return

    print("🚀 Memulai pembuatan sertifikat...")
    
    # Baca data dari CSV
    with open(CSV_PATH, mode='r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        # Asumsi baris pertama adalah header: "Nama", "Nomor"
        header = next(reader, None) 
        
        for idx, row in enumerate(reader, start=1):
            if len(row) >= 2:
                nama = row[0].strip()
                nomor = row[1].strip()
                generate_certificate(nama, nomor)
            else:
                print(f"⚠️ Baris {idx} tidak valid (butuh minimal 2 kolom): {row}")
                
    print("🎉 Proses selesai!")

if __name__ == "__main__":
    main()
