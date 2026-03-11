class Sayohat:
    jami_chiptalar = 0

    def __init__(self, ism, pasport):
        if not Sayohat.pasport_tekshirish(pasport):
            print("Pasport xato!")
        self.ism = ism
        self.__pasport = pasport
        Sayohat.jami_chiptalar += 1

    @staticmethod
    def pasport_tekshirish(seriya):
        return len(seriya) == 9 and seriya[:2].isalpha() and seriya[2:].isdigit()

    @classmethod
    def marshrut_tavsiyasi(cls, shahar):
        if shahar in ["Samarqand", "Buxoro"]:
            return "Poyezd"
        elif shahar == "Toshkent":
            return "Uchish"
        else:
            return "Avtobus"


class Uchish(Sayohat):
    def __init__(self, ism, pasport, sinf):
        super().__init__(ism, pasport)
        self.sinf = sinf

    def chipta_tavsifi(self):
        return f"Samolyot - o'rindiq sinfi: {self.sinf}"


class Poyezd(Sayohat):
    def __init__(self, ism, pasport, vagon):
        super().__init__(ism, pasport)
        self.vagon = vagon

    def chipta_tavsifi(self):
        return f"Poyezd - vagon turi: {self.vagon}"


class Avtobus(Sayohat):
    def __init__(self, ism, pasport, orin):
        super().__init__(ism, pasport)
        self.orin = orin

    def chipta_tavsifi(self):
        return f"Avtobus - o'rindiq raqami: {self.orin}"



a = Uchish("Ali", "AB1234567", "Business")
b = Poyezd("Vali", "AC7654321", "Kupe")
c = Avtobus("Hasan", "AD1112223", 15)

print(a.chipta_tavsifi())
print(b.chipta_tavsifi())
print(c.chipta_tavsifi())

print("Jami chiptalar:", Sayohat.jami_chiptalar)
print("Tavsya:", Sayohat.marshrut_tavsiyasi("Samarqand"))
