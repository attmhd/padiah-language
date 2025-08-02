# Padiah Language

**Padiah Language** adalah bahasa pemrograman parodi dengan sintaks Minang, dibuat untuk hiburan, edukasi, dan eksperimen. Proyek ini menerjemahkan kode berbahasa Minang ke Python dan mengeksekusinya secara langsung.

## Fitur

- Sintaks Minang yang unik dan lucu.
- Interpreter yang menerjemahkan ke Python.
- Error handling dengan pesan khas Minang.
- Mudah dikembangkan dan ditambah kata kunci baru.

## Instalasi

Pastikan Python 3.10 atau lebih baru sudah terpasang.

Clone repo ini dan install secara lokal:

```bash
git clone https://github.com/attmhd/padiah-language.git
cd padiah-language
pip install .
```

Atau langsung via pip:

```bash
pip install git+https://github.com/attmhd/padiah-language.git
```

## Cara Pakai

Buat file dengan ekstensi `.pdh`, misal `contoh.pdh`:

```pdh
Buek x = 5
Kok x > 3
    Katoan "X ciek bana!"
Kalau indak
    Katoan "X ketek bana!"
Alah sasuai
```

Jalankan dengan perintah:

```bash
padiah contoh.pdh
```

Output yang dihasilkan:

```
--- Manjalankan 'contoh.pdh' ---
X ciek bana!
```

Jika terjadi error, pesan akan muncul dengan gaya Minang:

```
***** Marah mu ma aku, baris 2! *****
Pasan asali: NameError: name 'y' is not defined
Penjelasan: Nampaknyo ado nan indak sasuai jo aturan awak.
Silakan cek baliak, sanak!
```

## Kata Kunci Sintaks

- `Buek` → assignment (misal: `Buek x = 5`)
- `Katoan` → print (misal: `Katoan "Halo Dunia"`)
- `Kok` → if (misal: `Kok x > 3`)
- `Kalau indak` → else
- `Alah sasuai` → pass

## Kontribusi

Silakan fork dan pull request untuk menambah fitur atau kata kunci baru. Laporan bug dan saran sangat diterima!

1. Fork repo ini.
2. Buat branch baru untuk fitur atau perbaikan.
3. Pull request dengan penjelasan perubahan.
4. Diskusi dan review bersama.

## Lisensi

MIT License

---

**Padiah Language** – "Marah mu ma aku, sanak!"
