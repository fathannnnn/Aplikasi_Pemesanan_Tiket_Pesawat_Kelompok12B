import random
import os
import hashlib

def garis():
    print("-" * 100)

def tampilkan_menu():
    print("\nSelamat datang di Cakrawala Air (Kelas Ekonomi)")
    print("Bandara Adi Soemarmo")

def tampilkan_list_penerbangan():
    print("\nKode Penerbangan   |       Kota Tujuan       | Harga Tiket")
    print("-------------------------------------------------------------")
    print("101                | ACEH BESAR              | Rp. 5.000.000")
    print("102                | DELI SERDANG            | Rp. 4.300.000")
    print("103                | PADANG PARIAMAN         | Rp. 3.700.000")
    print("104                | PEKANBARU               | Rp. 4.500.000")
    print("105                | BATAM KEPULAUAN RIAU    | Rp. 3.200.000")
    print("106                | TANGGERANG              | Rp. 4.200.000")
    print("107                | DKI JAKARTA             | Rp. 3.200.000")
    print("108                | MAJALENGKA              | Rp. 2.200.000")
    print("109                | YOGYAKARTA              | Rp. 2.300.000")
    print("110                | SIDOARJO                | Rp. 3.200.000")
    print("111                | BADUNG                  | Rp. 4.800.000")
    print("112                | LOMBOK TENGAH           | Rp. 5.200.000")
    print("113                | BALIKPAPAN              | Rp. 4.500.000")
    print("114                | SULAWESI SELATAN        | Rp. 4.700.000")
    print("115                | MANADO                  | Rp. 4.100.000")
    print("116                | JAYAPURA                | Rp. 6.200.000")
    print("117                | LABUAN BAJO             | Rp. 5.600.000")
    print("-------------------------------------------------------------")
    print("\n🎉 PROMO SPESIAL 🎉")
    print("- Pembelian 3 Tiket atau lebih: Diskon 10%")
    print("-------------------------------------------------------------")

def get_tujuan_dan_harga(kode_penerbangan):
    tujuan_harga = {
        "101": ("ACEH BESAR", 5000000),
        "102": ("DELI SERDANG", 4300000),
        "103": ("PADANG PARIAMAN", 3700000),
        "104": ("PEKANBARU", 4500000),
        "105": ("BATAM KEPULAUAN RIAU", 3200000),
        "106": ("TANGGERANG", 4200000),
        "107": ("DKI JAKARTA", 3200000),
        "108": ("MAJALENGKA", 2200000),
        "109": ("YOGYAKARTA", 2300000),
        "110": ("SIDOARJO", 3200000),
        "111": ("BADUNG", 4800000),
        "112": ("LOMBOK TENGAH", 5200000),
        "113": ("BALIKPAPAN", 4500000),
        "114": ("SULAWESI SELATAN", 4700000),
        "115": ("MANADO", 4500000),
        "116": ("JAYAPURA", 6200000),
        "117": ("LABUAN BAJO", 5600000)

        
        
    }
    return tujuan_harga.get(kode_penerbangan, ("Kode Salah", 0))

jadwal_tersedia = ["07.00", "10.00", "14.00", "18.00", "21.00"]
def jadwal_harian(date_str, tujuan, num_slots=3):
    seed_string = f"{date_str}-{tujuan}"
    hash_obj = hashlib.md5(seed_string.encode())
    seed = int(hash_obj.hexdigest()[:8], 16)
    rng = random.Random(seed)
    schedule = rng.sample(jadwal_tersedia, num_slots)
    return sorted(schedule)

def tampilkan_jadwal_penerbangan(tanggal_takeoff, tujuan):
    return jadwal_harian(tanggal_takeoff, tujuan)

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
            
def output_hasil(nama, nomor, email, tujuan, tanggal_takeoff, jadwal_dipilih, jumlah, harga, 
                 potongan, pajak, metode, instruksi, jumlah_bayar, penumpang_list):
    garis()
    print("Prokom Air (Kelas Ekonomi)")
    print("Nama Pembeli    : ", nama)
    print("Nomor Handphone : ", nomor)
    print("Email           : ", email)
    print("Kota Tujuan     : ", tujuan)
    print("Tanggal Take Off: ", tanggal_takeoff)
    print("Jam Take Off    : ", jadwal_dipilih)
    print("Jumlah Beli     : ", jumlah)
    print("Daftar Penumpang : ")
    for i in range(0, len(penumpang_list)):
        print(f"    Penumpang {i+1}:")
        print(f"    Nama         : {penumpang_list[i]["nama"]}")
        print(f"    NIK          : {penumpang_list[i]["nik"]}")    
    garis()
    print(f"Harga Tiket       : Rp. {harga:,}")
    print(f"Potongan          : Rp. {potongan:,}")
    print(f"PPN 11%           : Rp. {pajak:,}")
    print("Metode Pembayaran : ", metode)
    print("Instruksi         : ", instruksi)
    garis()
    print("Pelunasan Pembayaran Tiket")
    print(f"Jumlah Bayar : Rp. {jumlah_bayar:,}")
    print("\n--TERIMA KASIH TELAH MEMILIH CAKRAWALA AIR--")
    print("-------------ENJOY YOUR FLIGHT--------------")
    print("----------------SAFE FLIGHT!----------------")
