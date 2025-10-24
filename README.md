# 🌾 Sistem Pakar Diagnosis Hama dan Penyakit Tanaman Padi

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Sistem Cerdas untuk Membantu Petani Mengidentifikasi dan Menangani Masalah pada Tanaman Padi**

[Fitur](#-fitur-utama) • [Instalasi](#-instalasi-dan-cara-menjalankan) • [Dokumentasi](#-penjelasan-fitur) • [Demo](#-screenshot--demo)

</div>

---

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

---

## 🚀 Instalasi dan Cara Menjalankan

### 📋 Prasyarat
Sebelum memulai, pastikan Anda sudah menginstall:
- **Python 3.8 atau lebih tinggi** ([Download Python](https://www.python.org/downloads/))
- **pip** (biasanya sudah terinstall bersama Python)
- **Git** (opsional, untuk clone repository)

### 📥 Langkah 1: Download atau Clone Project

**Opsi A: Download ZIP**
```bash
# Download dari repository, lalu extract ke folder yang diinginkan
# Misalnya: D:\Coding\Sistem-pakar-tanaman-padi
```

**Opsi B: Clone dengan Git**
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
(venv) PS D:\Coding\Sistem-pakar-tanaman-padi>
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

---

## 🎨 Fitur Utama

### 1️⃣ **Knowledge Base (Basis Pengetahuan)** - Bobot: 15%

Sistem ini memiliki basis pengetahuan komprehensif yang terdiri dari:

#### 📚 Factual Knowledge
- 10+ jenis hama dan penyakit umum pada tanaman padi
- 40+ gejala visual yang dapat diidentifikasi
- Data karakteristik setiap penyakit/hama
- Informasi penanganan yang telah divalidasi

#### 🧠 Heuristic Knowledge
- 50+ IF-THEN Rules berdasarkan pengalaman pakar
- Aturan kombinasi gejala untuk diagnosis akurat
- Certainty Factor (CF) untuk setiap rule
- Pattern matching untuk identifikasi pola penyakit

#### 📋 Format Rules

```python
rules = {
    'R1': {
        'IF': ['daun_berwarna_coklat', 'bercak_berbentuk_diamond'],
        'THEN': 'kemungkinan_blast',
        'CF': 0.7,
        'explanation': 'Bercak coklat berbentuk diamond adalah ciri khas penyakit blast'
    },
    'R2': {
        'IF': ['kemungkinan_blast', 'batang_menghitam'],
        'THEN': 'penyakit_blast',
        'CF': 0.9,
        'explanation': 'Kombinasi bercak diamond dan batang menghitam mengkonfirmasi blast'
    }
}
```

#### 📖 Sumber Pengetahuan
- Balai Besar Penelitian Tanaman Padi (BB Padi)
- Buku "Hama dan Penyakit Padi" - Dr. Ir. Suprihanto, M.Si
- Jurnal Internasional: Journal of Plant Protection Research
- Konsultasi dengan pakar dari Dinas Pertanian

---

### 2️⃣ **Inference Engine (Mesin Inferensi)** - Bobot: 20%

Sistem mengimplementasikan dua metode inferensi:

#### 🔄 Forward Chaining (Data-Driven)
Proses reasoning yang dimulai dari fakta menuju kesimpulan:

```
┌─────────────┐      ┌──────────────┐      ┌──────────────┐
│ Input Gejala│ ───> │ Evaluasi     │ ───> │  Kesimpulan  │
│             │      │ Rules        │      │  Diagnosis   │
└─────────────┘      └──────────────┘      └──────────────┘
```

**Karakteristik:**
- Dimulai dari fakta yang diketahui
- Mengaplikasikan rules untuk mencari kesimpulan
- Cocok untuk diagnosis dan monitoring
- Menampilkan step-by-step reasoning

#### ⏪ Backward Chaining (Goal-Driven)
Proses reasoning yang dimulai dari hipotesis menuju verifikasi:

```
┌─────────────┐      ┌──────────────┐      ┌──────────────┐
│  Hipotesis  │ <─── │ Verifikasi   │ <─── │ Cari Fakta   │
│  Penyakit   │      │ Gejala       │      │ Pendukung    │
└─────────────┘      └──────────────┘      └──────────────┘
```

**Karakteristik:**
- Dimulai dari goal/hipotesis
- Bekerja mundur untuk membuktikan fakta
- Cocok untuk planning dan design
- Menanyakan pertanyaan spesifik untuk konfirmasi

#### 📊 Trace Penalaran

Sistem menampilkan setiap langkah penalaran secara detail:

```
╔═══════════════════════════════════════════════════════════╗
║  TRACE PENALARAN SISTEM                                   ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Step 1: Identifikasi Gejala Awal                        ║
║  ─────────────────────────────────────                    ║
║  Rule: R5 (Forward Chaining)                             ║
║  IF: daun_berwarna_coklat [✓] AND                        ║
║      bercak_berbentuk_diamond [✓]                        ║
║  THEN: kemungkinan_blast                                  ║
║  CF: 0.7 (70%)                                            ║
║                                                           ║
║  Step 2: Konfirmasi Diagnosis                            ║
║  ─────────────────────────────────────                    ║
║  Rule: R8 (Forward Chaining)                             ║
║  IF: kemungkinan_blast [✓] AND                           ║
║      batang_menghitam [✓]                                ║
║  THEN: penyakit_blast                                     ║
║  CF: 0.9 × 0.7 = 0.63                                    ║
║                                                           ║
║  Step 3: Final Calculation                               ║
║  ─────────────────────────────────────                    ║
║  Confidence Adjustment: +22%                              ║
║  • Multiple strong symptoms: +15%                        ║
║  • No contradicting symptoms: +7%                        ║
║                                                           ║
║  FINAL CF: 0.85 (85%)                                    ║
║  DIAGNOSIS: Penyakit Blast                               ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

### 3️⃣ **Working Memory (Memori Kerja)** - Bobot: 8%

Working memory menyimpan dan mengelola data selama proses inferensi:

#### 💾 Struktur Data

```python
working_memory = {
    # Fakta dari user input
    'facts': {
        'daun_berwarna_coklat': True,
        'bercak_berbentuk_diamond': True,
        'batang_menghitam': True,
        'daun_menggulung': False
    },
    
    # Hasil intermediate dari inferensi
    'intermediate_results': {
        'kemungkinan_blast': 0.7,
        'kemungkinan_hawar': 0.3
    },
    
    # Riwayat penalaran
    'reasoning_history': [
        {
            'step': 1,
            'rule': 'R5',
            'input': ['daun_berwarna_coklat', 'bercak_berbentuk_diamond'],
            'output': 'kemungkinan_blast',
            'cf': 0.7
        },
        {
            'step': 2,
            'rule': 'R8',
            'input': ['kemungkinan_blast', 'batang_menghitam'],
            'output': 'penyakit_blast',
            'cf': 0.63
        }
    ],
    
    # Rules yang telah digunakan
    'used_rules': ['R5', 'R8'],
    
    # Timestamp
    'timestamp': '2025-10-24 14:30:15'
}
```

#### ⚙️ Fitur Working Memory
- ✅ Update dinamis saat proses inferensi berlangsung
- ✅ Tracking lengkap riwayat penalaran
- ✅ Penyimpanan hasil intermediate untuk efficiency
- ✅ Validasi konsistensi data
- ✅ Clear memory untuk diagnosis baru
- ✅ Export/import data untuk analisis

---

### 4️⃣ **User Interface** - Bobot: 10%

#### 🖥️ Input Interface

**Form Gejala Interaktif:**
- ✅ Checkbox untuk setiap gejala visual
- ✅ Kategori gejala (Daun, Batang, Malai, Akar, Umum)
- ✅ Radio button untuk tingkat keparahan
- ✅ Dropdown untuk pilihan spesifik
- ✅ Validasi input real-time
- ✅ Gambar referensi untuk setiap gejala
- ✅ Tooltip penjelasan gejala

**Fitur Tambahan:**
- 🔄 Reset form dengan satu klik
- 💾 Simpan data untuk diagnosis ulang
- 📋 Mode konsultasi terpandu (wizard)
- 🎯 Quick diagnosis untuk kasus umum
- 📱 Responsive design untuk mobile

#### 📤 Output Interface

**Hasil Diagnosis:**
```
╔═════════════════════════════════════════════════════════╗
║  🎯 HASIL DIAGNOSIS                                     ║
╠═════════════════════════════════════════════════════════╣
║                                                         ║
║  Penyakit: BLAST (Pyricularia oryzae)                  ║
║                                                         ║
║  Tingkat Kepercayaan:                                   ║
║  ████████████████████░░░░ 85%                          ║
║                                                         ║
║  Status: ⚠️ MEMERLUKAN PENANGANAN SEGERA               ║
║                                                         ║
║  Gejala Terdeteksi: 8 dari 10 gejala cocok             ║
║  Rules Digunakan: R5, R8, R12                          ║
║  Waktu Proses: 0.234 detik                             ║
║                                                         ║
╠═════════════════════════════════════════════════════════╣
║  📋 Detail Gejala:                                      ║
║  • Daun berwarna coklat (CF: 0.7)                      ║
║  • Bercak berbentuk diamond (CF: 0.9)                  ║
║  • Batang menghitam (CF: 0.8)                          ║
║                                                         ║
╠═════════════════════════════════════════════════════════╣
║  [📄 Lihat Rekomendasi] [🔍 Lihat Penjelasan]          ║
║  [📊 Export PDF] [↩️ Diagnosis Baru]                   ║
║                                                         ║
╚═════════════════════════════════════════════════════════╝
```

**Rekomendasi Penanganan:**
- 🌿 Penanganan Hayati (organik)
- 🧪 Penanganan Kimiawi (pestisida)
- 📏 Dosis dan cara aplikasi
- ⏰ Waktu penanganan optimal
- 🛡️ Pencegahan di masa depan
- 💰 Estimasi biaya penanganan

**Visualisasi:**
- 📊 Grafik tingkat kepercayaan
- 📈 Chart perbandingan kemungkinan penyakit
- 🗓️ Timeline penalaran
- 🖼️ Galeri gambar referensi penyakit/hama
- 🗺️ Peta sebaran penyakit (jika ada data GPS)

---

### 5️⃣ **Explanation Facility** - Bobot: 7%

Sistem menyediakan penjelasan lengkap dan transparan tentang proses diagnosis:

#### ❓ WHY (Mengapa)

Menjelaskan alasan sistem menanyakan pertanyaan tertentu:

```
╔═══════════════════════════════════════════════════════════╗
║  ❓ MENGAPA SISTEM MENANYAKAN INI?                        ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Pertanyaan: "Apakah daun berwarna coklat?"              ║
║                                                           ║
║  Alasan:                                                  ║
║  • Warna daun adalah indikator penting untuk diagnosis   ║
║    5 jenis penyakit berbeda                              ║
║                                                           ║
║  • Informasi ini dibutuhkan oleh:                        ║
║    - Rule R1, R3, R5, R7, R12                           ║
║    - 15 rules turunan lainnya                            ║
║                                                           ║
║  • Tingkat kepentingan: ⭐⭐⭐⭐⭐ (Sangat Penting)        ║
║                                                           ║
║  • Impact terhadap akurasi:                              ║
║    Dapat meningkatkan akurasi diagnosis hingga 20%       ║
║                                                           ║
║  • Kombinasi dengan gejala lain:                         ║
║    Jika dikombinasikan dengan "bercak pada daun",        ║
║    dapat langsung mengarah ke diagnosis spesifik         ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

#### 🔍 HOW (Bagaimana)

Menjelaskan bagaimana sistem sampai pada kesimpulan:

```
╔═══════════════════════════════════════════════════════════╗
║  🔍 BAGAIMANA SISTEM SAMPAI PADA KESIMPULAN INI?          ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Diagnosis: Penyakit Blast                               ║
║  Kepercayaan: 85%                                         ║
║                                                           ║
║  ─────────────────────────────────────────────────────   ║
║                                                           ║
║  📥 Input Gejala (User):                                  ║
║  ✓ Daun berwarna coklat                                  ║
║  ✓ Bercak berbentuk diamond                              ║
║  ✓ Batang menghitam                                      ║
║  ✓ Tanaman tampak layu                                   ║
║                                                           ║
║  ─────────────────────────────────────────────────────   ║
║                                                           ║
║  🔄 Proses Inferensi:                                     ║
║                                                           ║
║  Tahap 1: Pattern Matching Awal                          ║
║  ┌─────────────────────────────────────────┐            ║
║  │ Rule R5 (CF: 0.7)                       │            ║
║  │ IF: daun_berwarna_coklat AND            │            ║
║  │     bercak_berbentuk_diamond            │            ║
║  │ THEN: kemungkinan_blast                 │            ║
║  │                                         │            ║
║  │ Status: ✓ TERPENUHI                    │            ║
║  │ Hasil: kemungkinan_blast (CF: 0.7)     │            ║
║  └─────────────────────────────────────────┘            ║
║           ↓                                              ║
║  Tahap 2: Konfirmasi Diagnosis                          ║
║  ┌─────────────────────────────────────────┐            ║
║  │ Rule R8 (CF: 0.9)                       │            ║
║  │ IF: kemungkinan_blast AND               │            ║
║  │     batang_menghitam                    │            ║
║  │ THEN: penyakit_blast                    │            ║
║  │                                         │            ║
║  │ Status: ✓ TERPENUHI                    │            ║
║  │ CF Calculation: 0.7 × 0.9 = 0.63       │            ║
║  └─────────────────────────────────────────┘            ║
║           ↓                                              ║
║  Tahap 3: Confidence Adjustment                         ║
║  ┌─────────────────────────────────────────┐            ║
║  │ Base CF: 0.63                           │            ║
║  │                                         │            ║
║  │ Adjustment Factors:                     │            ║
║  │ + Multiple strong symptoms: +0.15       │            ║
║  │ + No contradicting symptoms: +0.07      │            ║
║  │ + Gejala tambahan (layu): +0.05        │            ║
║  │                                         │            ║
║  │ Final CF: 0.63 + 0.27 = 0.90           │            ║
║  │                                         │            ║
║  │ Normalized: 90% × 0.95 = 85%           │            ║
║  └─────────────────────────────────────────┘            ║
║                                                           ║
║  ─────────────────────────────────────────────────────   ║
║                                                           ║
║  ✅ Kesimpulan Final:                                     ║
║  Berdasarkan 4 gejala yang terdeteksi dan evaluasi       ║
║  3 rules utama, sistem menyimpulkan dengan kepercayaan   ║
║  85% bahwa tanaman Anda terkena Penyakit Blast.          ║
║                                                           ║
║  📊 Confidence Level: TINGGI (>80%)                       ║
║  🎯 Rekomendasi: Penanganan Segera Diperlukan            ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

#### 📋 Reasoning Chain

Tampilan visual alur penalaran lengkap:

```
Gejala Input
    ↓
[R5] Pattern Recognition
    ├─ daun_berwarna_coklat ✓
    └─ bercak_berbentuk_diamond ✓
    → kemungkinan_blast (CF: 0.7)
    ↓
[R8] Diagnosis Confirmation  
    ├─ kemungkinan_blast ✓
    └─ batang_menghitam ✓
    → penyakit_blast (CF: 0.63)
    ↓
[ADJ] Confidence Adjustment
    ├─ Multiple symptoms: +15%
    ├─ No contradiction: +7%
    └─ Extra symptoms: +5%
    → Final CF: 85%
    ↓
🎯 DIAGNOSIS: Penyakit Blast (85%)
```

---

## 📸 Screenshot & Demo

### 1. 🏠 Halaman Utama (Dashboard)

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║              🌾 SISTEM PAKAR DIAGNOSIS PADI 🌾             ║
║                                                            ║
║     Sistem Cerdas untuk Identifikasi Hama & Penyakit     ║
║                      Tanaman Padi                          ║
║                                                            ║
║  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   ║
║  │  🔍 Mulai    │  │  📊 Riwayat  │  │  📚 Panduan  │   ║
║  │  Diagnosis   │  │  Diagnosis   │  │  Lengkap     │   ║
║  └──────────────┘  └──────────────┘  └──────────────┘   ║
║                                                            ║
║  ┌────────────────────────────────────────────────────┐  ║
║  │  📈 Statistik Penggunaan                           │  ║
║  │  • Total Diagnosis: 1,247                         │  ║
║  │  • Akurasi Rata-rata: 87.5%                       │  ║
║  │  • Penyakit Terbanyak: Blast (35%)                │  ║
║  └────────────────────────────────────────────────────┘  ║
║                                                            ║
║  ┌────────────────────────────────────────────────────┐  ║
║  │  🔥 Trending Issues                                │  ║
║  │  1. Penyakit Blast ────────────── 35% ████████    │  ║
║  │  2. Hama Wereng Coklat ────────── 28% ██████      │  ║
║  │  3. Hawar Daun Bakteri ────────── 22% █████       │  ║
║  └────────────────────────────────────────────────────┘  ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

### 2. 📝 Form Input Gejala

```
╔════════════════════════════════════════════════════════════╗
║  📝 INPUT GEJALA TANAMAN                                   ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  🍃 Kondisi Daun:                                          ║
║  ┌────────────────────────────────────────────────────┐  ║
║  │  ☑ Daun berwarna coklat                           │  ║
║  │  ☑ Bercak berbentuk diamond (◇)                   │  ║
║  │  ☐ Daun menggulung                                │  ║
║  │  ☐ Daun berlubang                                 │  ║
║  │  ☐ Daun menguning dari ujung                      │  ║
║  │  ☐ Daun berbercak kuning                          │  ║
║  └────────────────────────────────────────────────────┘  ║
║                                                            ║
║  🌱 Kondisi Batang:                                        ║
║  ┌────────────────────────────────────────────────────┐  ║
║  │  ☑ Batang menghitam                               │  ║
║  │  ☐ Batang membusuk                                │  ║
║  │  ☐ Batang terlihat kering                         │  ║
║  │  ☐ Batang mudah patah                             │  ║
║  │  ☐ Ada lubang pada batang                         │  ║
║  └────────────────────────────────────────────────────┘  ║
║                                                            ║
║  🌾 Kondisi Malai:                                         ║
║  ┌────────────────────────────────────────────────────┐  ║
║  │  ☐ Malai kosong/hampa                             │  ║
║  │  ☐ Malai berbercak coklat                         │  ║
║  │  ☐ Malai tidak keluar sempurna                    │  ║
║  │  ☐ Malai berwarna kehitaman                       │  ║
║  └────────────────────────────────────────────────────┘  ║
║                                                            ║
║  🌿 Kondisi Umum Tanaman:                                  ║
║  ┌────────────────────────────────────────────────────┐  ║
║  │  ☑ Tanaman tampak layu                            │  ║
║  │  ☐ Pertumbuhan terhambat/kerdil                   │  ║
║  │  ☐ Ada serangga terlihat                          │  ║
║  └────────────────────────────────────────────────────┘  ║
║                                                            ║
║  📏 Tingkat Keparahan Serangan:                            ║
║  ┌────────────────────────────────────────────────────┐  ║
║  │  ○ Ringan (< 25% area terdampak)                  │  ║
║  │  ● Sedang (25-50% area terdampak)                 │  ║
║  │  ○ Berat (> 50% area terdampak)                   │  ║
║  └────────────────────────────────────────────────────┘  ║
║                                                            ║
║  🗓️ Informasi Tambahan (Opsional):                        ║
║  ┌────────────────────────────────────────────────────┐  ║
║  │  Umur Tanaman: [60 hari setelah tanam        ▼]  │  ║
║  │  Musim:#   s i s t e m p a d i  
 