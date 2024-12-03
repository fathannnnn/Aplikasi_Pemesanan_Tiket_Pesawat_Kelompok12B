import json
import os
from datetime import datetime

def load_riwayat():
    if os.path.exists('riwayat_pemesanan.json'):
        with open('riwayat_pemesanan.json', 'r') as file:
            return json.load(file)
    return []

def save_riwayat(riwayat):
    with open('riwayat_pemesanan.json', 'w') as file:
        json.dump(riwayat, file, indent=4)

def simpan_pesanan(current_user, nama, nomor, email, tujuan, tanggal_takeoff, jadwal_dipilih, jumlah, harga,
                   potongan, pajak, jumlah_bayar, metode,penumpang_list):
    return {
    "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "username": current_user,
    "nama": nama,
    "nomor": nomor,
    "email": email,
    "tujuan": tujuan,
    "tanggal_keberangkatan": tanggal_takeoff,
    "jam_keberangkatan": jadwal_dipilih,
    "jumlah_tiket": jumlah,
    "identitas_penumpang": penumpang_list,
    "harga_tiket": harga,
    "potongan": potongan,
    "pajak": pajak,
    "total_bayar": jumlah_bayar,
    "metode_pembayaran": metode
            }