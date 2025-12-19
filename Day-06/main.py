#game hangman
import random
# setup gambar dan kata
logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
'''
# gambar tahapan kalah (dari 6 nyawa sampai 0)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["gajah", "komputer", "python", "indonesia", "program", "kopi", "github"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#setup variable game
end_of_game = False
lives = 6 #player punya 6 nyawa

print(logo)

#buat tampilan kosong (contoh: _ _ _ _ _ )
display = []
for _ in range(word_length):
    display += "_"
    
#logika utama (while loop)
while not end_of_game:
    guess = input("Tebak satu huruf: ").lower()
    
    #cek apakah user pernah menebak huruf itu
    if guess in display:
        print(f"Kamu sudah menebak huruf '{guess}'. Coba huruf lain.")
        
    #cek tebakan benar
    #loop tiap posisi di kata rahasia
    for position in range(word_length):
        letter = chosen_word[position]
        #jika huruf di posisi itu sama dgn tebakan user
        if letter == guess:
            display[position] = letter
    
    #cek tebakan salah
    if guess not in chosen_word:
        print(f"Huruf '{guess}' tidak ada dalam kata. Nyawa berkurang.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("GAME OVER! Kamu kalah.")
            print(f"Kata rahasianya adalah: {chosen_word}")
    
    #tampilkan status tebakan saat ini (gabungkan list jadi string)
    print(f"{' '.join(display)}")
    
    #cek kondisi menang
    if "_" not in display:
        end_of_game = True
        print("SELAMAT! Kamu menang.")
    
    #tampilkan gambar orang sesuai nyawa
    print(stages[lives])