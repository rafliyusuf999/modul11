class Mahasiswa:
    total_mahasiswa = 0  

    def __init__(self, nama, nim, angkatan):  # Constructor
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.total_mahasiswa += 1  

    def tampilkan_biodata(self):  # Method
        print(f"\nNama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Angkatan: {self.angkatan}")

    def running(self):
        print(f"{self.nama} tidur")

    def stop(self):
        print(f"{self.nama} makan.")

    def tampilkan_total_mahasiswa(self):  # Method biasa
        print(f"Total Mahasiswa: {Mahasiswa.total_mahasiswa}")

def main():
    print("Masukkan data mahasiswa:")
    nama = input("Nama: ")
    nim = input("NIM: ")
    angkatan = input("Angkatan: ")

    mahasiswa = Mahasiswa(nama, nim, angkatan)

    print("\nBiodata Mahasiswa:")
    mahasiswa.tampilkan_biodata()

    print("Kesibukan gw:")
    mahasiswa.running()
    mahasiswa.stop()

    print("\nInformasi Tambahan:")
    mahasiswa.tampilkan_total_mahasiswa()  # Dipanggil melalui instance

if __name__ == "__main__":
    main()
