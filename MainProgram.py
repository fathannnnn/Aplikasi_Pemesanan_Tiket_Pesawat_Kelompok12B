import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from user_manager import UserManager
from storage import load_riwayat, save_riwayat, simpan_pesanan
from requirement import validasi_email, validasi_nomor_hp, validasi_tanggal_takeoff, perhitungan_diskon
from Booking import tampilkan_menu, tampilkan_list_penerbangan, tampilkan_jadwal_penerbangan, get_tujuan_dan_harga, pilih_metode_pembayaran, garis, output_hasil
from datetime import datetime


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
                username = user_manager.login()
                if username:
                    current_user = username
                    print(f"Selamat datang, {username}!")
            elif pilihan == "2":
                user_manager.register()
            elif pilihan == "3":
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
                    jumlah = int(input("Jumlah Pembelian Tiket : "))
                    if jumlah > 0:
                        break
                    print("Jumlah tiket harus lebih dari 0.")
                except ValueError:
                    print("Masukkan angka yang valid.")

            # Perhitungan
            potongan, pajak, jumlah_bayar = perhitungan_diskon(jumlah, harga)

            # Pilih metode pembayaran
            metode, instruksi = pilih_metode_pembayaran(jumlah_bayar)
             
        
            # Simpan ke riwayat
            pemesanan = simpan_pesanan(current_user, nama, nomor, email, tujuan, tanggal_takeoff, jadwal_dipilih, jumlah, harga, potongan, pajak, jumlah_bayar, metode) 
            riwayat_pemesanan.append(pemesanan)
            save_riwayat(riwayat_pemesanan)

def kirim_invoice_email(penerima, nama, nomor, email, tujuan, tanggal_takeoff, jadwal_dipilih, 
                        jumlah, harga, potongan, pajak, metode, instruksi, jumlah_bayar):
    sender_email = "cakrawalaair1@gmail.com"  # ganti dengan email anda
    receiver_email = email  # gunakan parameter email yang diberikan
    password = "crnb tkrx ybje mgmh"  # ganti dengan password email anda
    
    # Buat isi pesan dengan format invoice
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Invoice Tiket Pesawat Cakrawala Air"

    body = f"""
    Terima kasih telah memesan tiket di Cakrawala Air!

    Detail Pemesanan:
    --------------------------------------------------------------------------
    Nama Pembeli            : {nama}
    Nomor Handphone         : {nomor}
    Email                   : {email}
    Kota Tujuan             : {tujuan}
    Tanggal Take Off        : {tanggal_takeoff}
    Jam Take Off            : {jadwal_dipilih}
    Jumlah Beli             : {jumlah} Tiket
    ---------------------------------------------------------------------------
    Harga Tiket             : Rp. {harga:,}
    Potongan                : Rp. {potongan:,}
    PPN 11%                 : Rp. {pajak:,}
    Metode Pembayaran       : {metode}
    Instruksi               : {instruksi}
    ---------------------------------------------------------------------------
    Jumlah Bayar            1: Rp. {jumlah_bayar:,}

    Terima kasih telah memilih Cakrawala Air.
    Selamat menikmati penerbangan!
    """
    
    # Tambahkan body ke dalam email
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Menghubungkan ke server SMTP Gmail dan mengirimkan email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email berhasil dikirim!")
    except Exception as e:
        print(f"Error saat mengirim email: {e}")

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
                username = user_manager.login()
                if username:
                    current_user = username
                    print(f"Selamat datang, {username}!")
            elif pilihan == "2":
                user_manager.register()
            elif pilihan == "3":
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
                    jumlah = int(input("Jumlah Pembelian Tiket : "))
                    if jumlah > 0:
                        break
                    print("Jumlah tiket harus lebih dari 0.")
                except ValueError:
                    print("Masukkan angka yang valid.")

            # Perhitungan
            potongan, pajak, jumlah_bayar = perhitungan_diskon(jumlah, harga)

            # Pilih metode pembayaran
            metode, instruksi = pilih_metode_pembayaran(jumlah_bayar)
             
            # Simpan ke riwayat
            pemesanan = simpan_pesanan(current_user, nama, nomor, email, tujuan, tanggal_takeoff, jadwal_dipilih, jumlah, harga, potongan, pajak, jumlah_bayar, metode) 
            riwayat_pemesanan.append(pemesanan)
            save_riwayat(riwayat_pemesanan)
            
            # Kirim invoice email
            kirim_invoice_email(current_user, nama, nomor, email, tujuan, tanggal_takeoff, jadwal_dipilih, 
                                jumlah, harga, potongan, pajak, metode, instruksi, jumlah_bayar)
            
            # Output
            output_hasil(nama, nomor, email, tujuan, tanggal_takeoff, jadwal_dipilih, jumlah, harga, potongan, pajak, metode, instruksi, jumlah_bayar)
            
            input("\nTekan Enter untuk lanjut ke tampilan Invoice")

        elif pilihan == "2":
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
                print(f"Total Pembayaran : Rp. {pesanan['total_bayar']:,}")
                print(f"Metode Pembayaran: {pesanan['metode_pembayaran']}")
                garis()
            
            input("\nTekan Enter untuk kembali ke menu utama")
            
        elif pilihan == "3":
            print(f"\nBerhasil logout dari akun {current_user}!")
            current_user = None
        
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            
if __name__ == "__main__":
    main()