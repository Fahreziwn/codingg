import sys 
import time

def jalanin_lirik():
    lirik = [
        ("Yang datang dan pergi", 0.2),
        ("Kan membuatmu mengerti", 0.2),
        ("Kadang kita perlu tersakiti", 0.2),
        ("Tuk mengenal perih", 0.1),
        ("Yang datang dan pergi", 0.2),
        ("Semua yang harus dilalui", 0.1),
        ("Kadang kita perlu tersakiti", 0.2),
        ("Tuk menjadi manusia", 0.2),
    ]
    
    delay = [0.3, 0.4, 0.3, 0.2, 0.2, 0.2, 0.2, 0.1]
    print("\n==Jakarta Hari Ini==")
    time.sleep(0.2)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    print("// Code by Fahrezi")
    
jalanin_lirik()
