import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def kirim_invoice_email(nama, nomor, email, tujuan, tanggal_takeoff, jadwal_dipilih, 
                        jumlah, harga, potongan, pajak, metode, instruksi, jumlah_bayar, penumpang_list):
    sender_email = "cakrawalaair1@gmail.com"  # ganti dengan email anda
    receiver_email = email  # gunakan parameter email yang diberikan
    password = "crnb tkrx ybje mgmh"  # ganti dengan password email anda
    
    penumpang_html = ""
    for i, penumpang in enumerate(penumpang_list, 1):
        penumpang_html += f"""
        <tr>
            <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>Penumpang {i}</strong></td>
            <td style="padding: 10px; border-bottom: 1px solid #ddd;">{penumpang['nama']}</td>
            <td style="padding: 10px; border-bottom: 1px solid #ddd;">{penumpang['nik']}</td>
        </tr>
        """
        
    # Buat HTML template untuk invoice
    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
        <div style="background-color: #f4f4f4; padding: 20px; border-radius: 10px;">
            <h2 style="color: #333; text-align: center;">Invoice Tiket Pesawat Cakrawala Air</h2>
            
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>Nama Pembeli</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;">{nama}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>Nomor Handphone</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;">{nomor}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>Email</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;">{email}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>Kota Tujuan</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;">{tujuan}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>Tanggal Take Off</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;">{tanggal_takeoff}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>Jam Take Off</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;">{jadwal_dipilih}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>Jumlah Beli</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;">{jumlah} Tiket</td>
                </tr>
            </table>
            
            <h3 style="color: #333; text-align: center;">Detail Penumpang</h3>
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
                <tr>
                    <th style="padding: 10px; border-bottom: 1px solid #ddd; text-align: left;">No</th>
                    <th style="padding: 10px; border-bottom: 1px solid #ddd; text-align: left;">Nama Penumpang</th>
                    <th style="padding: 10px; border-bottom: 1px solid #ddd; text-align: left;">NIK</th>
                </tr>
                {penumpang_html}
            </table>

            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>Harga Tiket</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd; text-align: right;">Rp. {harga:,}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>Potongan</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd; text-align: right;">Rp. {potongan:,}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>PPN 11%</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd; text-align: right;">Rp. {pajak:,}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>Jumlah Bayar</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd; text-align: right; font-weight: bold;">Rp. {jumlah_bayar:,}</td>
                </tr>
            </table>

            <div style="background-color: #e9e9e9; padding: 10px; border-radius: 5px;">
                <p><strong>Metode Pembayaran:</strong> {metode}</p>
                <p><strong>Instruksi:</strong> {instruksi}</p>
            </div>

            <p style="text-align: center; margin-top: 20px; color: #666;">
                Terima kasih telah memilih Cakrawala Air.<br>
                Selamat menikmati penerbangan!
            </p>
        </div>
    </body>
    </html>
    """
    
    # Buat email dengan HTML
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Invoice Tiket Pesawat Cakrawala Air"

    # Tambahkan body HTML ke dalam email
    msg.attach(MIMEText(html_body, 'html'))

    try:
        # Menghubungkan ke server SMTP Gmail dan mengirimkan email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email berhasil dikirim!")
            return True
    except Exception as e:
        print(f"Error detail: {e}")
        return False
