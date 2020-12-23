class LuasKubus():
    def hitung_LuasKubus(self,sisi:float):
        return 6*sisi*sisi

class LuasBalok():
    def hitung_LuasBalok(self, panjang:float, lebar:float, tinggi:float):
        return 2*(panjang*lebar + lebar*tinggi + tinggi*panjang)