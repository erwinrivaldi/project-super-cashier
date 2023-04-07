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
1. Karena setiap transaksi unik, maka input pertama yang kita butuhkan dari user adalah nomor transaksi. Bentuk nomor transaksi bisa berbentuk trxXX atau transaksi01.
2. Lalu kita membutuhkan input nama barang, jumlah barang dan juga harga barang dari user dengan metode add_item().
3. Setelah user input barang, maka data tersebut akan tersimpan dalam keranjang belanja user.
4. User bisa kembali menambahkan barang dengan metode add_item().
5. Jika ada barang, baik nama, jumlah maupun harga yang direvisi, user bisa menggunakan metode update_nama_item(), update_jumlah_item() atau update_harga_item().
6. Jika user mau cek barang apa saja yang ada di keranjang belanja bisa menggunakan metode check_order().
7. Untuk menghapus barang dari keranjang konsumen bisa menggunakan metode delete_item(). Jika mau menghapus seluruh item di keranjang bisa gunakan reset_transaction().
8. Untuk perhitungan akhir saat user sudah selesai berbelanja bisa menggunakan metode _total_price(). Seluruh item di keranjang belanja konsumen akan dihitung dengan mengalikan jumlah barang dengan harga barang.

## Test Case
1. Menambahkan Item
<img width="593" alt="testcase1" src="https://user-images.githubusercontent.com/128563448/230598839-d75eee53-e65d-4dbc-b8e0-4cb89f9b7f90.png">

2. Menghapus Item
<img width="609" alt="testcase2" src="https://user-images.githubusercontent.com/128563448/230598911-1b3c5850-0c4f-4c35-aee7-35e76712cf01.png">

3. Reset Transaksi
<img width="497" alt="testcase3" src="https://user-images.githubusercontent.com/128563448/230598964-60888261-b336-4d32-9f28-a559d6d992a0.png">

4. Cek Keranjang Belanja & Total Transaksi
<img width="514" alt="testcase4" src="https://user-images.githubusercontent.com/128563448/230599016-c9a312a8-3050-4c54-8ffe-e429f0986d73.png">
