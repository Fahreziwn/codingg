import sys
import time

def run_lirik():
    lirik = [
        ("Bertanyaa...", 0.4),
        ("Mengapa kita", 0.3),
        ("Masih disini", 0.3),
        ("Tersenyumm...\n", 0.4),
        ("Alasan masih bersama", 0.2),
        ("Bukan ", 0.2),
        ("karena terlanjur lama", 0.2),
        ("Tapi rasanyaa", 0.3),
        ("Yang masih samaaaa...\n", 0.2),
        ("Seperti sejak pertama", 0.2),
        ("Jumpa", 0.2),
        ("Dirimu di kala senja", 0.2),
        ("Duduk berduaaa", 0.3),
        ("Tanpa suaraaa...", 0.3),
    ]
    
    delay = [0.02, 0.2, 0.2, 0.7, 0.1, 0.1, 0.2, 0.2, 0.8, 0.1, 0.1, 0.2, 0.2, 0.2 ]
    time.sleep(1)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
        
run_lirik()