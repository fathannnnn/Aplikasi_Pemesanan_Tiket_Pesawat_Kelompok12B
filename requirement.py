def validasi_email(email):
    return "@gmail" in email and ".com" in email and len(email.split("@gmail.com")[0]) >= 3

def validasi_nomor_hp(nomor):
    return (nomor.isdigit() and 
            len(nomor) >= 10 and 
            len(nomor) <= 13 and
            nomor.startswith("08"))
    
def validasi_tanggal_takeoff (tanggal_dipilih, tanggal_sekarang):
    if tanggal_dipilih > tanggal_sekarang :
        print(f"Tanggal penerbangan Anda: {tanggal_dipilih.strftime('%Y-%m-%d')}")
        return True
    else:
        print("Tanggal penerbangan harus di masa depan. Silakan masukkan tanggal yang valid.")
        return False
    
def validasi_jadwal_takeoff(jadwal_terpilih, pilihan_jam):
        if 1 <= pilihan_jam <= len(jadwal_terpilih) :
            jadwal_dipilih = jadwal_terpilih[pilihan_jam-1]
            print(f"Anda telah memilih jadwal: {jadwal_dipilih}")    
        else:
            print("Masukan nomoer yang valid.")            
        return jadwal_dipilih

def validasi_nik(nik):
    if not (nik.isdigit() and len(nik) == 16 and nik.startswith("")):
        return False
    
    kode_provinsi = int(nik[:2])
    if kode_provinsi < 1 or kode_provinsi > 38:
        return False
    
    kode_kabupaten = int(nik[2:4])
    if kode_kabupaten == 0:
        return False
    
    kode_kecamatan = int(nik[4:6])
    if kode_kecamatan == 0:
        return False
    
    tanggal_lahir = int(nik[6:8])
    if tanggal_lahir > 40:
        tanggal_lahir -= 40
    if tanggal_lahir < 1 or tanggal_lahir > 31:
        return False
    
    bulan_lahir = int(nik[8:10])
    if bulan_lahir < 1 or bulan_lahir > 12:
        return False
    
    tahun_lahir = int(nik[10:12])
    if tahun_lahir < 0 or tahun_lahir > 99:
        return False
    
    nomor_urut = int(nik[12:])
    if nomor_urut == 0:
        return False
    
    return True

def perhitungan_diskon(jumlah, harga):
    if jumlah == 3:
        potongan = (jumlah * harga) * 0.1  # Diskon 10% untuk 3 tiket atau lebih
    else:
        potongan = 0
        
    total = (jumlah * harga) - potongan
    pajak = total * 0.11  # PPN 11%
    jumlah_bayar = total + pajak
    return potongan, pajak, jumlah_bayar 