import sys
import time

def run_lirik():
    lirik = [
        ("Jangan salahkan faham ", 0.09),
        ("ku kini ", 0.2),
        ("Tertuju ohh....", 0.2),
        ("Siapa yang tau", 0.1),
        ("Siapa yang mau", 0.1),
        ("Kau disana", 0.1),
        ("Aku di seberangmu", 0.1),
    ]
    
    delay = [0.3, 2.0, 0.5, 2.0, 2.0, 1.0, 0.4,]
    time.sleep(1)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
        
run_lirik()
        
            