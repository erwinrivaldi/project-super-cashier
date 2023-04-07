from tabulate import tabulate

class Transaction:

  keranjang_belanja = {}

  def __init__ (self, no_transaksi):
    self.no_transaksi = no_transaksi

  def add_item(self):
    '''
    Function untuk menambahkan item ke dalam keranjang belanja konsumen.

    args:
      nama_item (str) = nama barang yang akan diinput
      jumlah_item (int) = jumlah barang yang akan diinput
      harga_item (int) = harga barang yang akan diinput
      keranjang_belanja (dict) = menampung barang user  

    Returns:
      dict: Isi keranjang belanja user
    '''
    self.nama_item = input('Masukan nama barang: ')
    self.jumlah_item = int(input('Masukan jumlah barang: '))
    self.harga_item = int(input('Masukan harga barang: '))
    self.total_harga_item = self.jumlah_item * self.harga_item
    self.keranjang_belanja[self.nama_item] = self.jumlah_item, self.harga_item, self.total_harga_item
    print(f'Item yang telah ditambahkan: {self.keranjang_belanja}')
    return self.keranjang_belanja

  def update_nama_item(self):
    '''
    Function untuk mengganti nama item yang sudah ada di keranjang belanja
    user

    args:
      nama_item (str) = nama barang yang akan diganti
      update_nama_item (str) = nama barang baru

    Returns:
      dict: Isi keranjang belanja user
    '''
    nama_item = input('Masukan barang yang ingin diganti: ')
    update_nama_item = input('Masukan nama barang baru: ')
    if nama_item in self.keranjang_belanja.keys():
       self.keranjang_belanja[update_nama_item] = self.keranjang_belanja.pop(nama_item)
       print(f'Item dalam keranjang anda: {self.keranjang_belanja}')
       return self.keranjang_belanja
    else:
      print('Item yang anda masukan tidak ada di dalam keranjang')

  def update_jumlah_item(self, nama_item, update_jumlah_item):
    '''
    Function untuk mengganti jumlah item yang sudah ada di keranjang belanja
    user

    args:
      nama_item (str) = nama barang yang akan diganti
      update_jumlah_item (int) = jumlah barang baru

    Returns:
      dict: Isi keranjang belanja user
    '''
    nama_item = input('Masukan barang yang ingin diganti jumlahnya: ')
    update_jumlah_item = input('Masukan jumlah baru: ')
    if nama_item in self.keranjang_belanja.keys():
       self.keranjang_belanja[nama_item] = (update_jumlah_item, self.keranjang_belanja[nama_item][1], update_jumlah_item * self.keranjang_belanja[nama_item][1])
       print(f' Item dalam keranjang anda: {self.keranjang_belanja}')
       return self.keranjang_belanja
    else:
      print('Item yang anda masukan tidak ada di dalam keranjang')
    
  def update_harga_item(self):
    '''
    Function untuk mengganti harga item yang sudah ada di keranjang belanja
    user

    args:
      nama_item (str) = nama barang yang akan diganti
      update_harga_item (int) = harga barang baru

    Returns:
      dict: Isi keranjang belanja user
    '''
    nama_item = input('Masukan barang yang ingin diganti harganya: ')
    update_jumlah_item = input('Masukan harga baru: ')
    if nama_item in self.keranjang_belanja.keys():
       self.keranjang_belanja[nama_item] = (self.keranjang_belanja[nama_item][0], update_jumlah_item, self.keranjang_belanja[nama_item][0] * update_jumlah_item)
       print(f' Item dalam keranjang anda: {self.keranjang_belanja}')
       return self.keranjang_belanja
    else:
      print('Item yang anda masukan tidak ada di dalam keranjang')

  def delete_item(self):
    '''
    Function untuk menghapus item yang sudah ada di keranjang belanja
    user

    args:
      nama_item (str) = nama barang yang akan dihapus

    Returns:
      dict: Isi keranjang belanja user
    '''
    nama_item = input('Masukan barang yang ingin dihapus: ')
    if nama_item in self.keranjang_belanja.keys():
      self.keranjang_belanja.pop(nama_item)
      print(f' Anda telah menghapus {nama_item} dari keranjang')
      print(f' Item dalam keranjang anda: {self.keranjang_belanja}')
      return self.keranjang_belanja
    else:
      print('Item yang anda masukan tidak ada di dalam keranjang')

  def reset_transaction(self):
    '''
    Function untuk menghapus seluruh item yang sudah ada di keranjang belanja
    user

    args:
      -

    Returns:
      dict: Isi keranjang belanja user
    '''
    hapus_transaksi = input(f'Apakah anda ingin menghapus keranjang? (y/n) ').lower()
    if hapus_transaksi == 'y':
      self.keranjang_belanja.clear()
      print('Anda telah menghapus seluruh keranjang belanja anda')
    else:
      print(f'Silakan lanjutkan transaksi anda')

  def check_order(self):
    '''
    Function untuk cek isi keranjang belanja user 

    args:
      -

    Returns:
      tabel: Isi keranjang belanja user
    '''
    total_harga = 0
    for qty, price, tempTotal in self.keranjang_belanja.values():
      headers = ['Nama Item', 'Jumlah Item', 'Harga per Item', 'Total Harga']
    print(tabulate([(k,) + v for k, v in self.keranjang_belanja.items()], headers = headers, tablefmt = 'pipe'))

  def total_price(self):
    '''
    Function untuk menghitung total belanja user berdasarkan keranjang belanja
    user

    args:
      -

    Returns:
      str: Total belanja user
    '''
    total_belanja = 0
    for qty, price, tempTotal in self.keranjang_belanja.values():
      temp_keranjang_belanja = qty * price
      total_belanja += temp_keranjang_belanja
    print(f'Total belanja anda adalah Rp {total_belanja}')
    
    if total_belanja >= 500_000:
      harga_akhir = total_belanja * 0.90
      print(f'Selamat Anda Mendapatkan Diskon 10%. \nPembayaran akhir Anda Rp {harga_akhir }')
    elif total_belanja >= 300_000:
      harga_akhir = total_belanja * 0.92
      print(f'Selamat Anda Mendapatkan Diskon 8%. \nPembayaran akhir Anda Rp {harga_akhir}')
    elif total_belanja >= 200_000:
      harga_akhir = total_belanja * 0.95
      print(f'Selamat Anda Mendapatkan Diskon 5%. \nPembayaran akhir Anda Rp {harga_akhir}')

trx01 = Transaction("trx01")

trx01.add_item()

trx01.add_item()

trx01.delete_item()

trx01.reset_transaction()

trx01.add_item()

trx01.add_item()

trx01.check_order()

trx01.total_price()