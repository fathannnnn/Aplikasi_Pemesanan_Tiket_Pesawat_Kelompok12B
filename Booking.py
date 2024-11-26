import random

def garis():
    print("-" * 40)

def tampilkan_menu():
    print("\nSelamat datang di Garuda Indonesia (Kelas Ekonomi)")
    print("Bandara Adi Soemarmo")

def tampilkan_list_penerbangan():
    print("\nKode Penerbangan | Kota Tujuan | Harga Tiket")
    print("------------------------------------------------")
    print("101              | JAKARTA     | Rp. 1.000.000")
    print("102              | PONTIANAK   | Rp. 1.300.000")
    print("103              | MEDAN       | Rp. 1.700.000")
    print("104              | PAPUA       | Rp. 4.500.000")
    print("105              | DENPASAR    | Rp. 1.200.000")
    print("------------------------------------------------")

def get_tujuan_dan_harga(kode_penerbangan):
    tujuan_harga = {
        "101": ("JAKARTA", 1000000),
        "102": ("PONTIANAK", 1300000),
        "103": ("MEDAN", 1700000),
        "104": ("PAPUA", 4500000),
        "105": ("DENPASAR", 1200000)
    }
    return tujuan_harga.get(kode_penerbangan, ("Kode Salah", 0))

jadwal_tersedia = ["07.00", "10.00", "14.00", "18.00", "21.00"]
def tampilkan_jadwal_penerbangan():
    return random.sample(jadwal_tersedia, 3)

def pilih_metode_pembayaran(jumlah_bayar):
    while True:
        print("\nSilakan pilih metode pembayaran:")
        print("1. Virtual Account")
        print("2. Minimarket")
        print("3. Kartu Kredit")
        
        pilihan = input("Masukkan nomor metode pembayaran (1/2/3): ")
        
        if pilihan == "1":
            metode = "Virtual Account"
            nomor_rekening = "00210923714"
            instruksi = f"Lakukan transfer ke Virtual Account: {nomor_rekening} sesuai dengan jumlah bayar Rp. {jumlah_bayar:,}"
            return metode, instruksi
        elif pilihan == "2":
            metode = "Minimarket"
            nomor_rekening = "00210923713"
            instruksi = f"Silakan datang ke minimarket terdekat dan gunakan nomor pembayaran: {nomor_rekening} dengan jumlah Rp. {jumlah_bayar:,}"
            return metode, instruksi
        elif pilihan == "3":
            metode = "Kartu Kredit"
            while True:
                nomor_kartu = input("Masukkan nomor Kartu Kredit Anda (16 digit): ")
                if len(nomor_kartu) == 16 and nomor_kartu.isdigit():
                    instruksi = f"Pembayaran dilakukan menggunakan Kartu Kredit nomor: {nomor_kartu}"
                    return metode, instruksi
                print("Nomor kartu kredit tidak valid. Harap masukkan 16 digit angka.")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")