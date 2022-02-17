import pyfiglet
import os
import time


while True:
    ascii_banner = pyfiglet.figlet_format("CryptoCurrency")
    print(ascii_banner)
    os.system("curl rate.sx")
    time.sleep(6)
    
