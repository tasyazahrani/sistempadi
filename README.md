# 🌾 Sistem Pakar Diagnosa Penyakit Tanaman Padi

Sistem pakar berbasis web untuk mendiagnosis hama dan penyakit pada tanaman padi menggunakan metode forward chaining dan certainty factor.

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

## 🚀 Cara Menjalankan

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Pastikan File Knowledge Base Ada

Buat file `data/knowledge_base.json` dengan struktur rules Anda.

Contoh minimal:
```json
{
  "R1": {
    "IF": ["Daun menguning", "Ada serangga pada tanaman"],
    "THEN": "Hama Wereng Coklat",
    "CF": 0.85,
    "rekomendasi": [
      "Gunakan insektisida berbahan aktif imidakloprid",
      "Tanam varietas tahan wereng"
    ],
    "source": "Kementerian Pertanian RI, 2023"
  }
}
```

### 3. Jalankan Aplikasi

```bash
streamlit run main.py
```

Aplikasi akan terbuka di browser pada `http://localhost:8501`

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