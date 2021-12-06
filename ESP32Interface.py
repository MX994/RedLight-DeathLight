import requests
from time import sleep

class ESP32Communication:
    def __init__(self):
        self.addrBase = 'http://nerfornothing.local/'

    def check_conn(self): 
        # A blocking routine to ensure we are connected to the ESP32. 
        self.__req('')

    def __req(self, suffix):
        # 
        r = requests.get(self.addrBase + suffix)        
        while (r.status_code != 200):
            print("Connection failed. Retrying in 5 seconds...")
            sleep(5)
            r = requests.get(self.addrBase + suffix)

    def fire(self, ntimes):
        self.check_conn()
        self.__req('toggleMotor')
        sleep(0.4)
        self.__req('toggleTrigger')
        sleep(0.2 * ntimes)
        self.__req('toggleTrigger')
        self.__req('toggleMotor')

        