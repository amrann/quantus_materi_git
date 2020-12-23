class LuasSegititiga():
    def hitung(self, alas:float, tinggi:float):
        return 0.5*alas*tinggi

class PrismaSegitiga():
    def hitung(self, alas:float, tinggi:float, rusuk1:float, rusuk2:float, rusuk3:float):
        return tinggi*(rusuk1 + rusuk2 + rusuk3) + (2 * alas)