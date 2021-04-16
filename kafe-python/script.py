from drink import Drink
from signature import Signature
from food import Food
from snack import Snack

drink1 = Drink('Kopi Susu', 10000, 220)
drink2 = Drink('Espresso', 10000, 180)
drink3 = Drink('Latte', 10000, 220)
drink4 = Drink('Matcha Latte', 15000, 220)
drink5 = Drink('Red Velvet', 15000, 220)
drink6 = Drink('Taro', 15000, 220)
drink7 = Drink('Susu', 10000, 220)

drinks = [drink1, drink2, drink3, drink4, drink5, drink6, drink7]

signature1 = Signature('Summer Blast', 15000, 220)
signature2 = Signature('Peach Blossom', 15000, 220)
signature3 = Signature('Passion Fruit Sparkling Yakult', 17000, 220)
signature4 = Signature('Wedhang Uwuh', 100000, 180)

signatures = [signature1, signature2, signature3, signature4]

food1 = Food('Rice Bowl', 5000, 750)
food2 = Food('Indomie Goreng', 6000, 600)
food3 = Food('Indomie Kuah Kari Spesial', 6000, 650)

foods = [food1, food2, food3]


snack1 = Snack('French Fries', 8000, 350)
snack2 = Snack('Donat Tabur', 5000, 250)
snack3 = Snack('Onion Ring', 10000, 200)
snack4 = Snack('Risol Mayo', 8000, 300)

snacks = [snack1, snack2, snack3, snack4]

print('Selamat datang di Ikio Coffee')
print('Menu Ikio Coffee')
print(' ')

print('Minuman non-Signature')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print(' ')
print('Minuman Signature')
index = 0
for signature in signatures:
    print(str(index) + '. ' + signature.info())
    index += 1

print(' ')
print('Makanan')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print(' ')
print('Snack')
index = 0
for snack in snacks:
    print(str(index) + '. ' + snack.info())
    index += 1

print(' ')
print('--------------------')
print(' ')

total_price = 0

drink_confirm = input('Pesan Minuman Signature? (Ya/Tidak): ')
if drink_confirm == 'Ya' or drink_confirm == 'ya':
    signature_order = int(input('Masukkan Kode Minuman Signature: '))
    selected_signature = signatures[signature_order]
    count = int(input('Jumlah Minuman (Diskon 20% untuk pembelian 3 atau lebih): '))
    total_price += selected_signature.get_total_price(count)
else:
    drink_order = int(input('Masukkan Kode Minuman non-Signature: '))
    selected_drink = drinks[drink_order]
    count = int(input('Jumlah Minuman (Diskon 20% untuk pembelian 3 atau lebih): '))
    total_price += selected_drink.get_total_price(count)

food_confirm = input('Pesan Makanan? (Ya/Tidak): ')
if food_confirm == 'Ya' or food_confirm == 'ya':
    food_order = int(input('Masukkan Kode Makanan: '))
    selected_food = foods[food_order]
    count = int(input('Jumlah Makanan (Diskon 20% untuk pembelian 3 atau lebih): '))
    total_price += selected_food.get_total_price(count)

snack_confirm = input('Pesan Snack? (Ya/Tidak): ')
if snack_confirm == 'Ya' or snack_confirm == 'ya':
    snack_order = int(input('Masukkan Kode Snack: '))
    selected_snack = snacks[snack_order]
    count = int(input('Jumlah Snack: '))
    total_price += selected_snack.get_total_snack_price(count)

print(' ')
print('--------------------')
print(' ')

print('Total Harga Rp' + str(total_price))
total_pay = int(input('Jumlah Uang Anda (Rp): '))

if total_pay > total_price:
    print('Uang Kembalian Anda Rp' + str(total_pay - total_price))
elif total_pay < total_price:
    print('Uang Anda Kurang Rp' + str(total_price - total_pay) + '. Silahkan Tambah Uang Anda' )
    credit_pay = int(input('Masukkan Rp' + str(total_price - total_pay) + ': '))

print('Terima Kasih!')



