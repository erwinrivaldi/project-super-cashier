#library
from tabulate import tabulate
import pandas as pd

class Transaction:

  def __init__ (self):
    self.keranjang_belanja = {}

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
    try:
      self.nama_item = input('Masukan nama barang: ')
      self.jumlah_item = int(input('Masukan jumlah barang: '))
      self.harga_item = int(input('Masukan harga barang: '))

      if self.jumlah_item <= 0 or self.harga_item <= 0:
          raise ValueError('Terdapat kesalahan penginputan, silakan coba kembali')

      self.total_harga_item = self.jumlah_item * self.harga_item
      self.keranjang_belanja[self.nama_item] = [self.jumlah_item, self.harga_item, self.total_harga_item]
      print(f'Anda telah menambahkan {self.nama_item} sejumlah {self.jumlah_item} dengan harga Rp {self.harga_item}')
    except:
        print('Terdapat kesalahan penginputan, silakan coba kembali')

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
    try:
      if nama_item in self.keranjang_belanja.keys():
        self.keranjang_belanja[update_nama_item] = self.keranjang_belanja.pop(nama_item)
        print(f'Anda telah mengganti {nama_item} menjadi {update_nama_item}')
    except:
        print('Item yang anda masukan tidak ada di dalam keranjang')

  def update_jumlah_item(self):
    '''
    Function untuk mengganti jumlah item yang sudah ada di keranjang belanja
    user

    args:
      nama_item (str) = nama barang yang akan diganti
      update_jumlah_item (int) = jumlah barang baru

    Returns:
      dict: Isi keranjang belanja user
    '''
    tabel_keranjang = pd.DataFrame(self.keranjang_belanja).T
    headers = ['Nama Item', 'Jumlah Item', 'Harga Item', 'Total Harga']
    print(tabulate(tabel_keranjang, headers = headers, tablefmt ="github"))
    
    nama_item = input('Masukan barang yang ingin diganti jumlahnya: ')
    update_jumlah_item = int(input('Masukan jumlah baru: '))
    try:
      if nama_item in self.keranjang_belanja.keys():
        self.keranjang_belanja[nama_item] = [update_jumlah_item, self.keranjang_belanja[nama_item][1], update_jumlah_item * self.keranjang_belanja[nama_item][1]]
        print(f'Item dalam keranjang anda: {self.keranjang_belanja.keys()}')
      else:
        print('Item yang anda masukan tidak ada di dalam keranjang')
    except ValueError:
      print(f'Jumlah barang harus dalam bentuk angka')
    
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
    tabel_keranjang = pd.DataFrame(self.keranjang_belanja).T
    headers = ['Nama Item', 'Jumlah Item', 'Harga Item', 'Total Harga']
    print(tabulate(tabel_keranjang, headers = headers, tablefmt ="github"))

    nama_item = input('Masukan barang yang ingin diganti harganya: ')
    update_harga_item = int(input('Masukan harga baru: '))
    try: 
      if nama_item in self.keranjang_belanja.keys():
        self.keranjang_belanja[nama_item] = (self.keranjang_belanja[nama_item][0], update_harga_item, self.keranjang_belanja[nama_item][0] * update_harga_item)
        print(f'Item dalam keranjang anda: {self.keranjang_belanja.keys()}')
      else:
        print('Item yang anda masukan tidak ada di dalam keranjang')
    except ValueError:
      print(f'Jumlah barang harus dalam bentuk angka')

  def delete_item(self):
    '''
    Function untuk menghapus item yang sudah ada di keranjang belanja
    user

    args:
      nama_item (str) = nama barang yang akan dihapus

    Returns:
      dict: Isi keranjang belanja user
    '''
    tabel_keranjang = pd.DataFrame(self.keranjang_belanja).T
    headers = ['Nama Item', 'Jumlah Item', 'Harga Item', 'Total Harga']
    print(tabulate(tabel_keranjang, headers = headers, tablefmt ="github"))

    nama_item = input('Masukan barang yang ingin dihapus: ')
    if nama_item in self.keranjang_belanja.keys():
      self.keranjang_belanja.pop(nama_item)
      print(f'Anda telah menghapus {nama_item} dari keranjang')
      print(f'Item dalam keranjang anda: {self.keranjang_belanja.keys()}')
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
    if self.keranjang_belanja == {}:
      print(f'Keranjang belanja kosong')
    else:
      tabel_keranjang = pd.DataFrame(self.keranjang_belanja).T
      headers = ['Nama Item', 'Jumlah Item', 'Harga Item', 'Total Harga']
      print(tabulate(tabel_keranjang, headers = headers, tablefmt ="github"))

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
    
    if total_belanja == 0:
      print(f'Keranjang belanja Anda masih kosong')
    elif total_belanja >= 500_000:
      harga_akhir = total_belanja * 0.90
      print(f'Selamat Anda Mendapatkan Diskon 10%. \nPembayaran akhir Anda Rp {harga_akhir }')
    elif total_belanja >= 300_000:
      harga_akhir = total_belanja * 0.92
      print(f'Selamat Anda Mendapatkan Diskon 8%. \nPembayaran akhir Anda Rp {harga_akhir}')
    elif total_belanja >= 200_000:
      harga_akhir = total_belanja * 0.95
      print(f'Selamat Anda Mendapatkan Diskon 5%. \nPembayaran akhir Anda Rp {harga_akhir}')
