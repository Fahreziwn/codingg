import sys
import time

def run_lirik():
    lirik = [ 
        ("Di kehidupan kedua ", 0.09), 
        ("S'moga kau tak terlalu keras kepala", 0.09), 
        ("Atau mungkin ini bukan yang pertama", 0.1),
        ("Dan kita diberi kesempatan berubah", 0.1),
        ("Kuyakin nyawa kita bertautan", 0.1),
        ("Khatam berbagai cobaan", 0.1), 
        ("Selalu menertawakan ramalan bintang", 0.09), 
        ("kartu tarot", 0.1), 
        ("Orang pintar pembaca nasib", 0.09), 
       
    ]
    
    delay = [2.0, 1.0, 0.10, 0.6, 2.0, 2.0, 0.2, 0.4, 0.4]
    time.sleep(1)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
        
run_lirik()