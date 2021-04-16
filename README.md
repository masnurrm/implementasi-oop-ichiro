# Implementasi OOP
Implementasi OOP untuk tugas magang tim Ichiro

## Identitas
Nama: Nur Muhammad 'Ainul Yaqin <br/>
NRP: 5025201011 <br/>
Departemen: Teknik Informatika 2020 <br/>

<br/>

## Implementasi: Kafe Ikio 
### Penjelasan Umum
Program `kafe-python` ini menggunakan konsep kasir pada sebuah kafe. Program ini menggunakan 5 <i>class</>, yaitu `MenuItem`, `Drink`, `Signature`, `Food`, dan `Snack`. 

### Penjelasan Class
#### Class Menu Item
Pada <i>class</i> `MenuItem` ini, terdapat 4 fungsi. Pertama, fungsi `__init__` dengan parameter `self`, `name`, dan `price` digunakan untuk menginisialisasi nama dan harga menu. Kedua, fungsi `info` dengan parameter `self` digunakan untuk mengembalikan nama menu dan harga menu, yang selanjutnya akan digunakan untuk melakukan output `print`. Ketiga, fungsi `get_total_price` dengan parameter `self` dan `count` yang digunakan untuk menghitung harga dari menu yang dipilih, termasuk menambahkan diskon sesuai dengan jumlah pesanan `count`. Fungsi ini akan mengembalikan total harga dari menu tersebut. Terakhir, fungsi `get_total_snack_price` dengan parameter `self` dan `count` yang digunakan untuk menghitung harga dari menu snack dan mengembalikan total harga dari menu snack tersebut.

#### Class Drink
Pada <i>class</i> `Drink` ini, terdapat pewarisan atau <i>inheritance</i> dari class `MenuItem`. Terdapat 2 fungsi yang merupakan pewarisan dengan beberapa penambahan atau perubahan, yaitu fungsi `__init__` dan `info`. Pertama, pada fungsi `__init__` dengan parameter `self`, `name`, `price`, dan `volume`, terdapat pewarisan pada inisialisasi nama dan harga. Kemudian, ditambahkan inisialisasi pada volume dari minuman. Kedua, pada fungsi `info` juga terdapat pewarisan, dan hanya ditambahkan volume pada pengembaliannya.  

#### Class Signature
Pada <i>class</i> `Signature` ini, terdapat pewarisan atau <i>inheritance</i> dari class `MenuItem`. Terdapat 2 fungsi yang merupakan pewarisan dengan beberapa penambahan atau perubahan, yaitu fungsi `__init__` dan `info`. Pertama, pada fungsi `__init__` dengan parameter `self`, `name`, `price`, dan `volume`, terdapat pewarisan pada inisialisasi nama dan harga. Kemudian, ditambahkan inisialisasi pada volume dari minuman signature. Kedua, pada fungsi `info` juga terdapat pewarisan, dan hanya ditambahkan volume pada pengembaliannya.  

#### Class Food
Pada <i>class</i> `Food` ini, terdapat pewarisan atau <i>inheritance</i> dari class `MenuItem`. Terdapat 2 fungsi yang merupakan pewarisan dengan beberapa penambahan atau perubahan, yaitu fungsi `__init__` dan `info` serta ada fungsi `calorie_info`. Pertama, pada fungsi `__init__` dengan parameter `self`, `name`, `price`, dan `calorie_count`, terdapat pewarisan pada inisialisasi nama dan harga. Kemudian, ditambahkan inisialisasi pada kalori dari makanan. Kedua, pada fungsi `info` juga terdapat pewarisan, dan hanya ditambahkan kalori pada pengembaliannya. Dan ketiga, terdapat fungsi `calorie_info` dengan parameter `self` yang akan menampilkan nilai kalori makanan apabila fungsi dipanggil.

#### Class Snack
Pada <i>class</i> `Snack` ini, terdapat pewarisan atau <i>inheritance</i> dari class `MenuItem`. Terdapat 2 fungsi yang merupakan pewarisan dengan beberapa penambahan atau perubahan, yaitu fungsi `__init__` dan `info` serta ada fungsi `calorie_info`. Pertama, pada fungsi `__init__` dengan parameter `self`, `name`, `price`, dan `calorie_count`, terdapat pewarisan pada inisialisasi nama dan harga. Kemudian, ditambahkan inisialisasi pada kalori dari snack. Kedua, pada fungsi `info` juga terdapat pewarisan, dan hanya ditambahkan kalori pada pengembaliannya. Dan ketiga, terdapat fungsi `calorie_info` dengan parameter `self` yang akan menampilkan nilai kalori snack apabila fungsi dipanggil.


### Alur Program
Program ini diawali dengan menampilkan menu-menu minuman (non-signature maupun signature), makanan, serta snack di <b><a href='https://www.instagram.com/ikiocoffee/'>kafe Ikio<a></b>. Berikutnya, user akan diberikan pilihan apakah ia akan memilih jenis menu tersebut atau tidak. Apabila ia menjawab `Ya` atau `ya` pada suatu jenis menu, maka user dapat memilih pilihan menu pada jenis menu tersebut. Selanjutnya, user memasukkan jumlah pesanan yang diinginkan dan akan mendapat diskon sesuai dengan jenis menu. Jika user telah selesai melakukan pesanan, maka akan muncul jumlah uang yang harus dibayarkan dan user memasukkan uang untuk dibayarkan. Apabila uang yang dibayarkan tidak sesuai dengan jumlah yang harus dibayarkan, maka user akan menerima kembalian atau user harus membayar kekurangan uangnya. Jika sudah, program akan selesai.  

<br/>

## Implementasi: Hompimpa Suit
### Penjelasan Umum
Pada program `hompimpa-suit` ini,

### Penjelasan Class
#### Class Player
#### Class Suit

### Alur Program

<br/>

## Terima Kasih 
