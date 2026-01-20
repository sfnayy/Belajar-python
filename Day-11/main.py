import random
import os

#fungsi clear screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
#fungsi bagi kartu
def deal_card():
    """Mengembalikan Kartu Acak Dari Deck"""
    #11 = As, 10 = 10, J, Q , K
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#fungsi hitung score
def calculate_score(cards):
    """Menerima list kartu lalu mengembalikan skornya"""
    #cek blackjack (cuma 2 kartu, total=21)
    #pakai 0 buat kode "blackjack"
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    #cek As 11. kalo total > 21 ubah As jadi 1
    if 11 in cards and sum (cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)


#fungsi nentuin pemenang
def compare(user_score, comp_score):
    #urutan pengecekan penting
    if user_score == comp_score:
        return "Seri!"
    elif comp_score == 0:
        return "Kalah, Lawan mendapatkan Blackjack!"
    elif user_score == 0:
        return "Menang dengan Blackjack!"
    elif user_score > 21:
        return "Nilai kamu lebih dari 21(Bust), Kamu kalah!"
    elif comp_score > 21:
        return "Lawan Bust, Kamu menang!"
    elif user_score > comp_score:
        return "Kamu menang!"
    else:
        return "Kamu kalah!"

#logika utama
def play_game():
    print("=== WELCOME TO BLACKJACK ===")
    
    user_cards = []
    comp_cards = []
    is_game_over = False
    
    #bagi kartu awal ke user dan comp
    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())
        
    #loop user
    while not is_game_over:
        #itung score sekarang
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        
        print(f"Kartu kamu: {user_cards}, skor saat ini: {user_score}")
        print(f" Kartu pertama komp: {comp_cards[0]}")
        
        #cek kondisi stop (blackjack or bust)
        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            #tanya user nambah kartu atau tidak
            user_should_deal = input("Ketik 'y' untuk tambah kartu, ketik 'n' untuk stop: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                clear_screen()
            else:
                is_game_over = True
                
    #loop comp
    #comp wajib ambil kartu sampe skor min. 17 atau kurang dari blackjack
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)
        
    #final results
    print(f"kartu final kamu: {user_cards}, skor akhir: {user_score}")
    print(f"Kartu final komp: {comp_cards}, skor akhir: {comp_score}")
    print(compare(user_score, comp_score))
    
#loop restart game
while input("Apakah mau main game Blackjack? ketik 'y' atau 'n': ") == 'y':
    clear_screen()
    play_game()