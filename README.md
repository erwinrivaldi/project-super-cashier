# Project Super Cashier

## Latar Belakang Masalah 
Sebuah toko mempunyai kebutuhan untuk membuat program yang mengijinkan konsumen untuk melakukan transaksi secara mandiri.

## Feature Requirements
1. Menambahkan item 
2. Mengubah nama, jumlah dan harga dari item
3. Menghapus item dari keranjang belanja
4. Menghapus seluruh item dari keranjang belanja
5. Cek item apa saja yang ada di keranjang belanja 
6. Menghitung total belanja & diskon 

## Flowchart
1. Karena setiap transaksi unik, maka input pertama yang kita butuhkan dari user adalah nomor transaksi. 
2. Lalu kita membutuhkan input nama barang, jumlah barang dan juga harga barang dari user dengan metode add_item().
3. Setelah user input barang, maka data tersebut akan tersimpan dalam keranjang belanja user.
4. User bisa kembali menambahkan barang dengan metode add_item().
5. Jika ada barang, baik nama, jumlah maupun harga yang direvisi, user bisa menggunakan metode update_nama_item(), update_jumlah_item() atau update_harga_item().
6. Jika user mau cek barang apa saja yang ada di keranjang belanja bisa menggunakan metode check_order().
7. Untuk menghapus barang dari keranjang konsumen bisa menggunakan metode delete_item(). Jika mau menghapus seluruh item di keranjang bisa gunakan reset_transaction().
8. Untuk perhitungan akhir saat user sudah selesai berbelanja bisa menggunakan metode _total_price(). Seluruh item di keranjang belanja konsumen akan dihitung dengan mengalikan jumlah barang dengan harga barang.

## Test Case
1. Menambahkan Item
<img width="749" alt="testcase1" src="https://user-images.githubusercontent.com/128563448/230774894-d7d0ccaa-18c9-4d8e-b70a-4f8b9c76738e.png">

2. Menghapus Item
<img width="749" alt="testcase2" src="https://user-images.githubusercontent.com/128563448/230774911-62f8b117-4cd9-4b0f-8247-c8c6398857a6.png">

3. Reset Transaksi
<img width="745" alt="testcase3" src="https://user-images.githubusercontent.com/128563448/230774917-cd59a676-1dff-4d2e-ad66-7a63c2794b49.png">

4. Cek Keranjang Belanja & Total Transaksi
<img width="753" alt="testcase4" src="https://user-images.githubusercontent.com/128563448/230774920-50077d03-0a06-42fd-9584-c1a99f5b45a1.png">

## Future Work
Ke depannya ada beberapa hal yang bisa dikembangkan lagi dari project ini:
1. Customer bisa memasukan nama dan mendapatkan nomor transaksi yang telah digenerate secara random oleh program
2. Fitur memasukan kode / kupon untuk mendapatkan diskon tambahan atau gratis ongkir
3. Fitur untuk merekam transaksi yang telah selesai 
