# project-super-cashier

## Latar Belakang Masalah 
Sebuah toko mempunyai kebutuhan untuk membuat program yang mengijinkan konsumen untuk melakukan transaksi secara mandiri.

## Feature Requirements
1. Menambahkan item 
2. Mengubah nama, jumlah dan harga dari item
3. Menghapus item dari keranjang belanja
4. Menghapus seluruh item dari keranjang belanja
5. Cek item apa saja yang ada di keranjang belanja 
6. Menghitung total belanja & diskon 

##Flowchart
1. Karena setiap transaksi unik, maka input pertama yang kita butuhkan dari user adalah nomor transaksi. Bentuk nomor transaksi bisa berbentuk trxXX atau transaksi01.
2. Lalu kita membutuhkan input nama barang, jumlah barang dan juga harga barang dari user dengan metode add_item().
3. Setelah user input barang, maka data tersebut akan tersimpan dalam keranjang belanja user.
4. User bisa kembali menambahkan barang dengan metode add_item().
5. Jika ada barang, baik nama, jumlah maupun harga yang direvisi, user bisa menggunakan metode update_nama_item(), update_jumlah_item() atau update_harga_item().
6. Jika user mau cek barang apa saja yang ada di keranjang belanja bisa menggunakan metode check_order().
7. Untuk menghapus barang dari keranjang konsumen bisa menggunakan metode delete_item(). Jika mau menghapus seluruh item di keranjang bisa gunakan reset_transaction().
8. Untuk perhitungan akhir saat user sudah selesai berbelanja bisa menggunakan metode _total_price(). Seluruh item di keranjang belanja konsumen akan dihitung dengan mengalikan jumlah barang dengan harga barang.
