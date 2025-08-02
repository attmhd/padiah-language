# padiah/penerjemah.py

def terjemahkan_ke_python(kode_minang_string):
    kode_python_baris = []

    for i, baris in enumerate(kode_minang_string.splitlines()):
        # Dapatkan indentasi asli dari baris
        indentasi_asli = len(baris) - len(baris.lstrip())
        baris_bersih = baris.strip()

        # Jika baris kosong, pertahankan saja
        if not baris_bersih:
            kode_python_baris.append("")
            continue

        baris_terjemah = baris_bersih

        # Logika terjemahan kata kunci
        if baris_bersih.startswith("Katoan"):
            # Untuk Katoan, ambil isinya dan bungkus dengan print()
            konten_print = baris_bersih[len("Katoan"):].strip()
            baris_terjemah = f"print({konten_print})"
        elif baris_bersih.startswith("Buek"):
            # 'Buek' hanya dihapus
            baris_terjemah = baris_bersih[len("Buek"):].strip()
        elif baris_bersih.startswith("Kok"):
            # 'Kok' menjadi 'if' dan tambahkan ':'
            kondisi = baris_bersih[len("Kok"):].strip()
            baris_terjemah = f"if {kondisi}:"
        elif baris_bersih.startswith("Kalau indak"):
            # 'Kalau indak' menjadi 'else:'
            baris_terjemah = "else:"
        elif baris_bersih.startswith("Alah sasuai"):
            # 'Alah sasuai' menjadi 'pass'
            baris_terjemah = "pass"
        # Tambahkan kata kunci lainnya di sini jika ada

        # Tambahkan indentasi asli ke baris yang sudah diterjemahkan
        kode_python_baris.append(" " * indentasi_asli + baris_terjemah)

    return "\n".join(kode_python_baris)
