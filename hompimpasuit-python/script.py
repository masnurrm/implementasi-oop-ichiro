import suit
import hompimpa
import random

print('Ayo main Hompimpa Suit!')
player_name = input('Masukkan nama kamu: ')

player_total = int(input('Masukkan jumlah lawan kamu (2-10): '))
letter = 'abcdefghijklmnopqrstuvwxyz'
for i in range(1, player_total):
    bot_nama[i] = ''.join(random.sample(letter, 4))

for i in range(1, player_total):
    print(bot_nama[i])

# if player_total > 2:


print('Pilih tangan suitmu! (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Masukkan tangan suit (0-2): '))

if utils.validate(player_hand):
    computer_hand = random.randint(0,2)
    
    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'Computer')

    result = utils.judge(player_hand, computer_hand)
    print('Hasil: ' + result)
else:
    print('Masukkan kode angka tangan suit sesuai pilihan!')
