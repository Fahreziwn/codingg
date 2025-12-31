import sys
import time

def run_lirik():

    lirik = [
        
        ("Sudah paham 'kan sejauh ini?\n", 0.14,),
        
        ("Ku yang lama di sini", 0.08,),
        ("Menjagamu tak patah hati", 0.08,),
        ("Sedia aku sebelum hujan", 0.08,),
        ("Apa yang kau butuh, kuberikan\n", 0.08,),

        ("Ke mana pun tak akan kau temukan", 0.08,),
        ("Yang siapkan bekalmu di peperangan",0.08,),
        ("Jika tak setara, kumaafkan", 0.08,),
        ("Memang sebegitunya akuuu...", 0.08,),

    ]
    
    delay = [ 3.0, 1.0, 1.0, 2.0, 1.0, 0.20, 1.0, 1.0, 1.0]
    time.sleep(1)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')

run_lirik()