import csv
import random
from datetime import date, timedelta

produk = {"Kopi": 15000, "Teh": 8000, "Roti": 12000, "Susu": 10000, "Cokelat": 18000}
random.seed(42)  # supaya hasilnya sama di semua komputer

with open("data/raw/transaksi.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id_transaksi", "tanggal", "produk", "qty", "harga"])

    # 200 baris data normal
    for i in range(1, 201):
        nama = random.choice(list(produk))
        tgl = date(2026, 11, 1) + timedelta(days=random.randint(0, 20))
        w.writerow([i, tgl, nama, random.randint(1, 10), produk[nama]])

    # 3 baris data kotor (bahan latihan transformasi & validasi)
    w.writerow([201, "2026-11-05", "Kopi", "", 15000])   # qty kosong
    w.writerow([202, "2026-11-06", "Teh", -3, 8000])     # qty negatif
    w.writerow([5, "2026-11-07", "Roti", 2, 12000])      # id duplikat

print("transaksi.csv dibuat")
