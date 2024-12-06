class DataOOP:
    def __init__(self):
        self.nama = None
        self.nilai = None

    def deklarasi_data(self):
        self.nama = input("Masukkan Nama: ")
        self.nilai = input("Masukkan Nilai: ")
        print("Data berhasil dideklarasikan.")

    def tampilkan_data(self):
        print(self.nama if self.nama else "None")
        print(self.nilai if self.nilai else "None")

    def ubah_data(self):
        if self.nama is None and self.nilai is None:
            print("Data belum dideklarasikan.")
            return

        pilihan = input("Apa yang ingin diubah? (Nama/Nilai): ").lower()
        if pilihan == "nama":
            self.nama = input("Masukkan Nama baru: ")
            print("Nama berhasil diubah.")
        elif pilihan == "nilai":
            self.nilai = input("Masukkan Nilai baru: ")
            print("Nilai berhasil diubah.")
        else:
            print("Pilihan tidak valid.")

    def hapus_data(self):
        self.nama = None
        self.nilai = None
        print("Data berhasil dihapus.")

def main():
    data = DataOOP()

    while True:
        print("\n=====Program OOP=====\n" +
              "1. Deklarasi Data\n" +
              "2. Menampilkan Data\n" +
              "3. Mengubah Data\n" +
              "4. Menghapus Data\n" +
              "5. Keluar Aplikasi")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == "1":
            data.deklarasi_data()
        elif pilihan == "2":
            data.tampilkan_data()
        elif pilihan == "3":
            data.ubah_data()
        elif pilihan == "4":
            data.hapus_data()
        elif pilihan == "5":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()