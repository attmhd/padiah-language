import sys
import os
import traceback # Untuk mendapatkan informasi detail error
from .translator import terjemahkan_ke_python

def main():
    if len(sys.argv) < 2:
        print("Penggunaan: padang <nama_file.pdh>")
        sys.exit(1)

    nama_file_input = sys.argv[1]

    # Cek apakah file ada
    if not os.path.exists(nama_file_input):
        print(f"Error: File '{nama_file_input}' indak basuo, sanak.")
        sys.exit(1)

    # Cek apakah ekstensi file benar
    if not nama_file_input.endswith(".pdh"):
        print(f"Error: File '{nama_file_input}' bukan file .pdh. Sanak salah jalan ko.")
        sys.exit(1)

    try:
        with open(nama_file_input, 'r', encoding='utf-8') as file_pdh:
            kode_minang_string = file_pdh.read()
    except Exception as e:
        print(f"Error saat mambaco file '{nama_file_input}': {e}")
        sys.exit(1)

    # Terjemahkan kode
    kode_python_terjemah = terjemahkan_ke_python(kode_minang_string)

    print(f"--- Manjalankan '{nama_file_input}' ---")
    try:
        # Eksekusi kode Python yang sudah diterjemahkan
        # Parameter kedua {} penting agar exec tidak mengganggu scope eksekutor
        exec(kode_python_terjemah, {})
    except Exception as e:
        # Menangkap error apa pun yang terjadi saat eksekusi
        tb_lines = traceback.format_exc().splitlines()

        line_info = "indak dapek diketahui barisnyo."
        # Mencari nomor baris error dari traceback
        for line in tb_lines:
            if "<string>" in line and "line" in line:
                try:
                    line_num_str = line.split("line ")[1].split(",")[0].strip()
                    line_info = f"baris {line_num_str}"
                except IndexError:
                    pass

        # Pesan error parodi Anda!
        print(f"\n***** Marah mu ma aku, {line_info}! *****")
        print(f"Pasan asali: {e}") # Menampilkan pesan error asli Python sebagai info tambahan
        print("Penjelasan: Nampaknyo ado nan indak sasuai jo aturan awak.")
        print("Silakan cek baliak, sanak!")
