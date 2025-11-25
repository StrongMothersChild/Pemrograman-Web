class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def kurangi_stok(self, jumlah):
        if jumlah <= self.stok:
            self.stok -= jumlah
            print(f"Stok {self.nama} berkurang {jumlah}. Sisa: {self.stok}")
        else:
            print(f"Stok {self.nama} tidak cukup!")

class Pelanggan:
    def __init__(self, nama):
        self.nama = nama

    def beli_produk(self, produk, jumlah):
        if produk.stok >= jumlah:
            total = produk.harga * jumlah
            print(f"{self.nama} membeli {jumlah} {produk.nama} (Rp{produk.harga} per item). Total: Rp{total}")
            produk.kurangi_stok(jumlah)
            return Transaksi(self, produk, jumlah)
        else:
            print("Transaksi gagal: stok tidak cukup!")
            return None

class Transaksi:
    def __init__(self, pelanggan, produk, jumlah):
        self.pelanggan = pelanggan
        self.produk = produk
        self.jumlah = jumlah
        self.total_harga = produk.harga * jumlah
        print(f"Transaksi dibuat untuk {pelanggan.nama} sebesar Rp{self.total_harga}.")

# simulasi
produk1 = Produk("Buku", 15000, 10)
produk2 = Produk("Pulpen", 5000, 20)
pelanggan1 = Pelanggan("Fathur")

transaksi1 = pelanggan1.beli_produk(produk1, 2)
transaksi2 = pelanggan1.beli_produk(produk2, 5)
