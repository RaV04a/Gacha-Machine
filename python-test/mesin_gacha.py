import random

MAX_GACHA = 750
MIN_GACHA = 150

gacha_item = [
    {"name": "Komi", "rarity": "Anti_Karbit" ,"chance": 2},
    {"name": "Mahiru", "rarity": "Cukup_Karbit" ,"chance": 15},
    {"name": "Kaoruko", "rarity": "Karbit" ,"chance": 30},
    {"name": "firefly", "rarity": "Karbit_Parah" ,"chance": 50}, 
]

def get_gacha_machine_roll(items):

        all_items = []
        for item in items:
                all_items.extend([item] * item["chance"])
        
        return random.choice(all_items)

def modal():
    while True:
        jumlah = input("Tolong masukan modal!")
        if jumlah.isdigit():
            jumlah = int(jumlah)
            if jumlah > 0:
                break
            else:
                print("modal harus lebih besar dari 0.")
        else:
            print("Tolong input dengan format angka.")

    return jumlah


def get_gacha():
      while True:
        gacha = input(str(MIN_GACHA) + " untuk 1x gacha" + " dan " + str(MAX_GACHA) + " untuk 5x gacha!")
        if gacha.isdigit():
            gacha = int(gacha)
            if MIN_GACHA <= gacha <= MAX_GACHA:
                break
            else:
                print("Modal yang dimasukan kurang dari minimum.")
        else:
            print("Tolong input dengan format angka.")
            
      return gacha


def main():
  
    saldo = modal()
    gacha = get_gacha()

    while True:
        v_gacha = get_gacha()
        sisa_saldo = saldo - v_gacha

        if v_gacha > sisa_saldo:
            print(f"maaf saldo anda tidak mencukupi,sisa saldo anda adalah: {saldo}")
        else:
            break

    print("berikut adalah hasil gacha anda!")

    if gacha == MAX_GACHA:
        for i in range(5):
            item = get_gacha_machine_roll(gacha_item)
            print(f"hasil {i+1}: {item['name']} tingkat kelangkaan: {item['rarity']}")
    elif gacha == MIN_GACHA:
        item = get_gacha_machine_roll(gacha_item)
        print(f"Selamat anda mendapatkan waifu: {item['name']} tingkat kelangkaan: {item['rarity']}")
        
if __name__ == "__main__":
    main()