from user_manager import UserManager
from storage import load_riwayat, save_riwayat, simpan_pesanan
from requirement import validasi_email, validasi_nomor_hp, validasi_tanggal_takeoff, perhitungan_diskon, validasi_nik
from Booking import tampilkan_menu, tampilkan_list_penerbangan, tampilkan_jadwal_penerbangan, get_tujuan_dan_harga, pilih_metode_pembayaran, garis, output_hasil, clear_screen
from datetime import datetime
from Email_sender import kirim_invoice_email  

def main():
    user_manager = UserManager()
    riwayat_pemesanan = load_riwayat()
    current_user = None
    
    while True:
        if current_user is None:
            print("\n=== SISTEM PEMESANAN TIKET PESAWAT ===")
            print("1. Login")
            print("2. Register")
            print("3. Keluar")
            
            pilihan = input("Pilih menu (1/2/3): ")
            
            if pilihan == "1":
                clear_screen()
                username = user_manager.login()
                if username:
                    current_user = username
                    clear_screen()
                    print(f"Selamat datang, {username}!")
            elif pilihan == "2":
                clear_screen()
                user_manager.register()
            elif pilihan == "3":
                clear_screen()
                print("\nTerima kasih telah menggunakan layanan kami!")
                break
            else:
                print("Pilihan tidak valid!")
            continue
        
        tampilkan_menu()
        print("\nPilihan Menu:")
        print("1. Pesan Tiket")
        print("2. Lihat Riwayat Pemesanan")
        print("3. Logout")
        
        pilihan = input("Masukkan pilihan (1/2/3): ")
        
        if pilihan == "1":
            clear_screen()
            # Proses Pembelian
            print("\nForm Pemesanan Tiket")
            
            # Input dan validasi nama
            while True:
                nama = input("Nama Pembeli : ")
                if not nama.strip():
                    print("Nama tidak boleh kosong. Silakan isi ulang.")
                elif not nama.replace(" ", "").isalpha():  
                    print("Nama hanya boleh terdiri dari huruf. Silakan isi ulang.")
                else:
                    break
            
            # Validasi nomor handphone
            while True:
                nomor = input("Nomor Handphone : ")
                if validasi_nomor_hp(nomor):
                    break
                print("Nomor handphone tidak valid. Harus panjang 10-13 digit dan diawali 08.")
            
            # Validasi email
            while True:
                email = input("Email : ")
                if validasi_email(email):
                    clear_screen()
                    break
                print("Format email tidak valid. Harap masukkan email yang benar.")
            
            # Tampilkan list penerbangan
            tampilkan_list_penerbangan()
            
            # Validasi kode penerbangan
            while True:
                kode_penerbangan = input("\nKode Tujuan Penerbangan = ")
                tujuan, harga = get_tujuan_dan_harga(kode_penerbangan)
                if tujuan != "Kode Salah":
                    break
                print("Kode penerbangan tidak valid. Silakan masukkan kode yang benar.")
            
            #Validsi tanggal takeoff
            while True:
                tanggal_takeoff = input("Tanggal takeoff (YYYY-MM-DD) :")
                try:
                    tanggal_dipilih = datetime.strptime(tanggal_takeoff, "%Y-%m-%d")
                    tanggal_sekarang = datetime.now()
                    
                    if validasi_tanggal_takeoff(tanggal_dipilih, tanggal_sekarang):
                        break
                except ValueError:
                    print("Format tanggal salah, masukan dengan format YYYY-MM-DD")
                    
            #tampilkan jadwal takeoff
            jadwal_terpilih = tampilkan_jadwal_penerbangan(tujuan, tanggal_takeoff)
            
            #validasi jadwal takeoff
            print("Jadwal Penerbangan Tersedia untuk ", tujuan, "pada tanggal ", tanggal_takeoff)
            print("Pilih Jadwal Take Off")
            for i, jadwal in enumerate(jadwal_terpilih, 1):
                print(f"{i}. {jadwal}")
            while True :
                try :
                    pilihan_jam = int(input("Masukan pilihan anda (1/2/3) :"))
                    if 1 <= pilihan_jam <= len(jadwal_terpilih) :
                        jadwal_dipilih = jadwal_terpilih[pilihan_jam-1]
                        print(f"Anda telah memilih jadwal: {jadwal_dipilih}")
                        break
                    else:
                        print("Masukan nomor yang valid.")
                except ValueError:
                    print("Harap masukan anggka.")
                    
            # Validasi jumlah tiket
            while True:
                try:
                    jumlah = int(input("Jumlah Pembelian Tiket (Maksimal 5 Tiket) : "))
                    if 1 <= jumlah <= 5:
                        break
                    print("Jumlah tiket maksimal hingga 5.")
                except ValueError:
                    print("Masukkan angka yang valid.")
                    
            #Input Nama Penumpang
            penumpang_list = []
            nik_terpakai = set()
            for i in range (jumlah):
                print(f"\nMasukan identitas untuk penumpang ke-{i+1}:")
                while True :
                    penumpang = input("Nama penumpang : ")
                    if not penumpang.strip():
                        print("Nama tidak boleh kosong")
                    elif not penumpang.replace(" ", "").isalpha():
                        print("Nama hanya boleh terdiri dari huruf, Silahkan coba lagi.")
                    else :
                        break
                    
                while True:
                    nik = input("Masukan NIK (16 Digit Angka) : ")
                    if not validasi_nik(nik):
                        print ("Masukan NIK dengan benar!")
                        continue
                        
                    if nik in nik_terpakai:
                        print("NIK sudah digunakan penumpang lain. Silahkan masukan NIK lain.")
                        continue
                    
                    nik_terpakai.add(nik)
                    break
                    
                penumpang_list.append({"nama": penumpang, "nik": nik})
                clear_screen()
                    
            # Perhitungan
            potongan, pajak, jumlah_bayar = perhitungan_diskon(jumlah, harga)

            # Pilih metode pembayaran
            metode, instruksi = pilih_metode_pembayaran(jumlah_bayar)
             
            # Simpan ke riwayat
            pemesanan = simpan_pesanan(current_user, nama, nomor, email, tujuan, tanggal_takeoff, 
                                       jadwal_dipilih, jumlah, harga, potongan, pajak, jumlah_bayar, metode,
                                       penumpang_list) 
            riwayat_pemesanan.append(pemesanan)
            save_riwayat(riwayat_pemesanan)
            
            # Kirim invoice email
            kirim_invoice_email(nama, nomor, email, tujuan, tanggal_takeoff, jadwal_dipilih, 
                                jumlah, harga, potongan, pajak, metode, instruksi, jumlah_bayar, penumpang_list)
            
            input("\nTekan Enter untuk lanjut ke tampilan Invoice")
            clear_screen()
            
            # Output
            output_hasil(nama, nomor, email, tujuan, tanggal_takeoff, jadwal_dipilih, jumlah, harga, 
                         potongan, pajak, metode, instruksi, jumlah_bayar, penumpang_list)
            input("\nTekan Enter untuk lanjut ke tampilan Menu")
            clear_screen()
            
        elif pilihan == "2":
            clear_screen()
            user_riwayat = [r for r in riwayat_pemesanan if r['username'] == current_user]
            if not user_riwayat:
                print("\nBelum ada riwayat pemesanan.")
                continue 
            
            print("\nRIWAYAT PEMESANAN:")
            for idx, pesanan in enumerate(user_riwayat, 1):
                print(f"\nPemesanan #{idx}")
                print(f"Tanggal          : {pesanan['tanggal']}")
                print(f"Nama             : {pesanan['nama']}")
                print(f"Tujuan           : {pesanan['tujuan']}")
                print(f"Tanggal Take Off : {pesanan['tanggal_keberangkatan']}")
                print(f"Jam Take Off     : {pesanan['jam_keberangkatan']}")
                print(f"Jumlah Tiket     : {pesanan['jumlah_tiket']}")
                for i, penumpang in enumerate(pesanan['identitas_penumpang']):
                    print(f"    Penumpang {i+1}:")
                    print(f"    Nama         : {penumpang['nama']}")
                    print(f"    NIK          : {penumpang['nik']}")
                print(f"Total Pembayaran : Rp. {pesanan['total_bayar']:,}")
                print(f"Metode Pembayaran: {pesanan['metode_pembayaran']}")
                garis()
            
            input("\nTekan Enter untuk kembali ke menu utama")
            
        elif pilihan == "3":
            clear_screen()
            print(f"\nBerhasil logout dari akun {current_user}!")
            current_user = None
        
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            
if __name__ == "__main__":
    main()