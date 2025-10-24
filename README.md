# 🌾 Sistem Pakar Diagnosa Penyakit Tanaman Padi

## 📋 Deskripsi Sistem

Sistem Pakar untuk Diagnosis Hama dan Penyakit Umum pada Tanaman Padi adalah aplikasi berbasis web yang menggunakan teknologi kecerdasan buatan untuk membantu petani dan penyuluh pertanian dalam mengidentifikasi hama serta penyakit yang menyerang tanaman padi. 

Sistem ini dibangun dengan metode **Expert System** yang mengimplementasikan **Forward Chaining** dan **Backward Chaining** untuk melakukan diagnosis berdasarkan gejala-gejala visual yang diamati pada tanaman padi, seperti perubahan warna daun, bercak, kondisi batang, atau bentuk malai.

### 🎯 Tujuan Sistem
- Membantu petani melakukan diagnosis dini terhadap hama dan penyakit
- Memberikan rekomendasi penanganan yang tepat dan efektif
- Meningkatkan produktivitas pertanian padi
- Mengurangi kerugian akibat serangan hama dan penyakit

### 🌟 Keunggulan
- ✅ Diagnosis akurat dengan perhitungan **Certainty Factor**
- ✅ Rekomendasi penanganan hayati dan kimiawi
- ✅ Penjelasan alur penalaran yang transparan
- ✅ Interface yang mudah digunakan
- ✅ Basis pengetahuan tervalidasi dari pakar

## 📁 Struktur Folder

```
rice-expert-system/
│
├── main.py                      # Entry point aplikasi
├── requirements.txt             # Python dependencies
│
├── core/                        # Core logic
│   ├── __init__.py
│   ├── knowledge_base.py        # Knowledge base management
│   ├── inference_engine.py      # Forward chaining engine
│   └── explanation_facility.py  # Explanation generator
│
├── ui/                          # User interface
│   ├── __init__.py
│   └── gui_interface.py         # Streamlit GUI (UPDATED)
│
├── utils/                       # Utility functions
│   ├── __init__.py
│   └── search_filter.py         # Search & filter functions
│
└── data/                        # Data files
    ├── knowledge_base.json      # Rules database
    └── history.json             # Consultation history
```

## 🚀 Instalasi dan Cara Menjalankan

### 📋 Prasyarat
Sebelum memulai, pastikan Anda sudah menginstall:
- **Python 3.8 atau lebih tinggi** ([Download Python](https://www.python.org/downloads/))
- **pip** (biasanya sudah terinstall bersama Python)
- **Git** (opsional, untuk clone repository)

### 📥 Langkah 1: Clone Project

**Clone dengan Git**
```bash
git clone https://github.com/username/sistem-pakar-padi.git
cd sistem-pakar-padi
```

### 🔧 Langkah 2: Buat Virtual Environment

Buka **Command Prompt** atau **PowerShell** di folder project, lalu jalankan:

```bash
python -m venv venv
```

> **📌 Catatan:** Virtual environment berfungsi untuk mengisolasi dependencies project agar tidak bentrok dengan project Python lainnya.

### ⚡ Langkah 3: Aktifkan Virtual Environment

**Untuk Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Untuk Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Untuk Linux/Mac:**
```bash
source venv/bin/activate
```

Jika berhasil, terminal Anda akan menampilkan `(venv)` di awal baris:
```bash
(venv) PS D:\Coding\Sistem-pakar-tanaman-padi> (sebagai contoh saja)
```

> **⚠️ Troubleshooting PowerShell:**  
> Jika muncul error "running scripts is disabled", jalankan:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### 📦 Langkah 4: Install Dependencies

Install Streamlit dan library yang diperlukan:

```bash
pip install streamlit
```

```bash
pip install streamlit jsonschema
```

**Atau install semua dependencies sekaligus:**
```bash
pip install -r requirements.txt
```

### ✅ Langkah 5: Verifikasi Instalasi

Cek apakah Streamlit sudah terinstall dengan benar:

```bash
streamlit --version
```

Output yang diharapkan:
```
Streamlit, version 1.28.0
```

### 🎮 Langkah 6: Jalankan Aplikasi

Jalankan aplikasi dengan perintah:

```bash
streamlit run main.py
```

Aplikasi akan otomatis terbuka di browser default Anda pada alamat:
```
http://localhost:8501
```

Jika tidak terbuka otomatis, buka browser dan akses URL di atas.

### 🛑 Menghentikan Aplikasi

Untuk menghentikan aplikasi, tekan `Ctrl + C` di terminal.

### 📤 Menonaktifkan Virtual Environment

Setelah selesai, nonaktifkan virtual environment dengan:

```bash
deactivate
```

## ✨ Fitur Utama

### 🔍 Panel Diagnosis (Kiri)
- **Search Gejala**: Cari dan filter gejala berdasarkan keyword
- **Pilih Gejala**: Checkbox dengan grid layout untuk memilih multiple gejala
- **Diagnosis Button**: Jalankan forward chaining untuk mendapatkan hasil
- **Hasil Diagnosis**:
  - Nama penyakit/hama
  - Confidence Factor (CF)
  - Penjelasan reasoning
  - Rekomendasi penanganan (numbered list)
  - Sumber referensi

### 🕘 Panel History (Kanan)
- **Search History**: Filter history berdasarkan keyword
- **Tampilan History**: Card dengan info lengkap konsultasi
- **Export Options**:
  - 📥 Download TXT (laporan lengkap)
  - 📥 Download CSV (format tabel)
- **Delete Button**: Hapus history yang tidak diperlukan

### 🎨 Desain Modern
- Gradient header hijau yang eye-catching
- Card-based layout dengan shadows
- Hover effects pada interactive elements
- Responsive design untuk berbagai ukuran layar
- Badge untuk menampilkan CF
- Numbered circles untuk rekomendasi

## 📝 File yang Diperbarui

### `gui_interface.py` - Perubahan Utama:
1. ✅ Custom CSS untuk styling modern (gradient, shadows, hover effects)
2. ✅ Card-based layout untuk semua komponen
3. ✅ Grid layout untuk checkbox gejala (2 kolom)
4. ✅ Badge untuk CF percentage
5. ✅ Numbered circles untuk rekomendasi
6. ✅ Delete button untuk history
7. ✅ Improved spacing dan typography
8. ✅ Responsive columns (2:1 ratio untuk main:history)

### `__init__.py` - Simplified:
- Hanya export `GUI` class
- Removed unused imports

## 📊 Data Format

### Knowledge Base (JSON)
```json
{
  "RULE_ID": {
    "IF": ["gejala1", "gejala2"],
    "THEN": "Nama Penyakit",
    "CF": 0.85,
    "rekomendasi": ["rekomendasi1", "rekomendasi2"],
    "source": "Sumber referensi"
  }
}
```

### History (JSON)
```json
[
  {
    "id": "20250124120000",
    "timestamp": "2025-01-24 12:00:00",
    "gejala": ["gejala1", "gejala2"],
    "consequent": "Hama Wereng",
    "cf": 0.85,
    "rekomendasi": ["rekomendasi1"],
    "source": "Sumber",
    "reasoning": "Penjelasan reasoning..."
  }
]
```

## 🐛 Troubleshooting

### Error: "File knowledge base tidak ditemukan"
- Pastikan folder `data/` ada
- Buat file `data/knowledge_base.json` dengan format yang benar

### History tidak tersimpan
- Pastikan folder `data/` memiliki write permission
- Check apakah file `data/history.json` ter-create

### Styling tidak muncul
- Clear browser cache (Ctrl+F5)
- Restart Streamlit server

## 📚 Dependencies

- **Streamlit** >= 1.28.0: Web framework
- **Pandas** >= 2.0.0: Data manipulation (optional)
- **NumPy** >= 1.24.0: Numerical computing (optional)

## 👨‍💻 Development

Untuk development mode dengan auto-reload:
```bash
streamlit run main.py --server.runOnSave true
```

## 📄 License

Sesuaikan dengan lisensi proyek Anda.

## 🤝 Contributing

Kontribusi sangat diterima! Silakan buat pull request atau issue.

---

**Dibuat dengan ❤️ menggunakan Streamlit**