**KELOMPOK 12 B**
1. Irfan Nur Huda          (I0324050)
2. Shinta Marito M         (I0324068)
3. Muhammad Fathan Hakim   (I0324089)
   
# ✈️ Aplikasi Pemesanan Tiket Pesawat Maskapai Cakrawala Air di Bandara Adi Soemarmo Kota Solo
Aplikasi ini merupakan platform sederhana untuk melakukan pemesanan melalui maskapai Cakrawala Air yang berlokasi di bandara Adi Soemarmo kota Solo. Aplikasi ini menyediakan berbagai pilihan tujuan penerbangan di Indonesia dengan berbagai pilihan jam terbang yang fleksibel. Pengguna dapat membuat akun dengan mudah serta memesan tiket, melihat riwayat pemesanan, dan memilih metode pembayaran.
## ✨Fitur Aplikasi
- 🔐**Pendaftaran dan Login Akun** : Aplikasi akan meminta pengguna untuk **memasukkan akun pribadi**. Jika belum memiliki akun, pengguna dapat membuatnya terlebih dahulu.
- 🧾**Riwayat Pemesanan**: Tersedia fitur untuk melihat **riwayat pemesanan tiket** yang telah dilakukan sebelumnya.
- 🎫**Pemesanan Tiket**🎫
  - Setelah login, pengguna bisa memilih menu "Pesan Tiket" untuk mengisi data **pemesan** .
  - Masukkan detail pemesanan seperti **nama pembeli**, **nomor handphone**, **email**.
  - Pilih **kode penerbangan** untuk memilih kota tujuan dan isi **tanggal takeoff**, serta **jamnya**.
  - Tentukan **jumlah tiket** yang akan dibeli dengan jumlah tiket maksimal 5.
  - Pembelian tiket dalam jumlah tertentu akan mendapatkan **potongan harga**. Tiket ini juga **dikenakan PPN**.
  - Masukkan **nama penumpang** dan **NIK** setiap masing-masing tiket.
  - Pilih metode pembayaran untuk melakukan transaksi.
  - Setelah itu Invoice dicetak dan dikirim ke email pembeli serta berisi instruksi pembayaran.
- 💳**Metode Pembayaran**💳
  - Virtual Account
  - Pembayaran di Minimarket
  - Kartu Kredit
- [flowchart_kelompok12B.pdf](https://github.com/user-attachments/files/18051011/flowchart_kelompok12B.pdf)
Flowchart ini menjelaskan proses pemesanan tiket mulai dari tahap login atau registrasi hingga pembayaran selesai. Awalnya, sistem memuat data riwayat dalam format JSON, lalu pengguna diberi pilihan untuk login atau membuat akun baru. Jika login berhasil, pengguna masuk ke menu utama dengan tiga opsi: memesan tiket, melihat riwayat transaksi, atau keluar dari sistem.

Saat memesan tiket, pengguna diminta mengisi data pribadi seperti nama, nomor HP, dan email. Setelah data tersebut diverifikasi, pengguna memasukkan informasi penerbangan, termasuk kode penerbangan, tanggal, jam keberangkatan, serta jumlah tiket yang ingin dipesan. Jika membeli tiga tiket atau lebih, pengguna otomatis mendapat diskon 10%. Selanjutnya, pengguna menginput nama penumpang dan NIK sebelum melanjutkan ke tahap pembayaran.

Sistem menyediakan tiga metode pembayaran: virtual account, kartu kredit (dengan memasukkan nomor kartu), atau melalui minimarket. Harga tiket dihitung dengan menambahkan PPN, lalu semua detail transaksi disimpan ke file JSON. Setelah pembayaran berhasil, sistem menampilkan invoice sebagai bukti pembelian. Alur ini dirancang untuk memberikan pengalaman pemesanan tiket yang mudah dan terorganisir bagi pengguna.
- ![site map kelompok 12B](https://github.com/shintamarito/TUTORPOSI24/blob/main/sitemap%20klmpk%2012.jpg)
