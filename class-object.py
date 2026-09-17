
"""
==============================================================
                CLASS  va  OBJECT  (Klass va Obyekt)
==============================================================
 
CLASS (Klass) — bu obyekt yaratish uchun QOLIP (shablon).
    - O'zi hali "jonli" narsa emas, faqat tuzilmani belgilaydi.
    - Xotirada real joy egallamaydi.
    - Bitta dasturda odatda bitta marta e'lon qilinadi.
 
OBJECT (Obyekt) — bu klassdan yaratilgan ANIQ NUSXA (instance).
    - Klass asosida yasalgan HAQIQIY narsa.
    - Xotirada o'zining alohida joyini egallaydi.
    - Bitta klassdan CHEKSIZ ko'p obyekt yaratish mumkin.
 
    Metafora:
        Class  -> tort qolipi   (forma, shakl)
        Object -> haqiqiy tort  (yeyish mumkin bo'lgan, real narsa)
==============================================================
"""




class Mashina: #class - obyekt yaratish uchun shablon (template)
    # __init__ - konstruktor metodi, obyekt yaratilganda avtomatik ishga tushadi
    def __init__(self, marka, rang):  #self - obyektning o'zini bildiradi, self.marka va self.rang esa obyektning atributlari
        self.marka = marka      # atribut (xususiyat)
        self.rang = rang        # atribut (xususiyat)

    def yur(self):              # metod (xatti-harakat)
        print(f"{self.marka} mashinasi yuryapti")
# Object — bu klassdan yaratilgan aniq nusxa (instance). Klass — qolip bo'lsa, obyekt — o'sha qolip asosida yasalgan haqiqiy narsa.
# Obyekt yaratish (instantiation)
mashina1 = Mashina("Toyota", "qizil")
mashina2 = Mashina("BMW", "qora")

# Obyektning atributlariga murojaat
print(mashina1.marka)   # Toyota
print(mashina2.rang)    # qora

# Obyektning metodini chaqirish
mashina1.yur()   # Toyota mashinasi yuryapti
mashina2.yur()   # BMW mashinasi yuryapti

class Talaba: #class obyekt yaratish uchun shablon (template)
    def __init__(self, ism, yosh, fakultet):
        self.ism = ism
        self.yosh = yosh
        self.fakultet = fakultet

    def salomlash(self):
        print(f"Salom, mening ismim {self.ism}, men {self.fakultet} fakultetida o'qiyman")

    def tugilgan_yil(self):
        return 2026 - self.yosh

# Ikkita talaba obyektini yaratamiz
talaba1 = Talaba("Ali", 20, "Kompyuter fanlari")
talaba2 = Talaba("Vali", 22, "Iqtisodiyot")

talaba1.salomlash()
# Salom, mening ismim Ali, men Kompyuter fanlari fakultetida o'qiyman

print(talaba1.tugilgan_yil())   # 2006
"""
==================================================================
        CLASS va OBJECT QANDAY TURLARGA BO'LINADI?
==================================================================
"""
 
 
# ==================================================================
#   1-QISM: ATRIBUTLAR (ATTRIBUTES) - 2 TURGA BO'LINADI
# ==================================================================
 
class Talaba:
 
    # ---- a) CLASS ATRIBUT ----
    # Barcha obyektlar uchun UMUMIY, klass ichida to'g'ridan-to'g'ri
    # yoziladi, self orqali emas.
    universitet = "TATU"
 
    def __init__(self, ism):
        # ---- b) INSTANCE ATRIBUT ----
        # Har bir obyektga ALOHIDA tegishli, self orqali yaratiladi.
        self.ism = ism
 
 
# ==================================================================
#   2-QISM: METODLAR (METHODS) - 3 TURGA BO'LINADI
# ==================================================================
 
class Namuna:
 
    # ---- a) INSTANCE METHOD ----
    # Eng ko'p ishlatiladigan tur. self qabul qiladi,
    # obyekt orqali chaqiriladi.
    def instance_metod(self):
        print("Bu - instance method, obyekt orqali ishlaydi")
 
    # ---- b) CLASS METHOD ----
    # Klassning o'ziga tegishli. @classmethod bilan belgilanadi,
    # self o'rniga cls oladi.
    @classmethod
    def class_metod(cls):
        print("Bu - class method, klassning o'ziga tegishli")
 
    # ---- c) STATIC METHOD ----
    # Na obyektga, na klassga bog'liq emas.
    # @staticmethod bilan belgilanadi.
    @staticmethod
    def static_metod():
        print("Bu - static method, mustaqil ishlaydi")
 
 
# ==================================================================
#   3-QISM: OOP'NING 4 TA ASOSIY TAMOYILI
# ==================================================================
#
#   1) ENCAPSULATION (Inkapsulyatsiya)
#      -> Ma'lumotni yashirish, faqat metodlar orqali kirish
#
#   2) INHERITANCE (Meros olish)
#      -> Bir klass boshqa klassdan xususiyat oladi
#
#   3) POLYMORPHISM (Ko'p shakllilik)
#      -> Bir xil metod turli klasslarda boshqacha ishlashi
#
#   4) ABSTRACTION (Abstraksiya)
#      -> Faqat kerakli qismini ko'rsatib, murakkablikni yashirish
#
# ==================================================================
 
 
# ---------------- SINOV UCHUN CHAQIRUVLAR ----------------
talaba1 = Talaba("Ali")
print(talaba1.ism)           # Ali          -> instance atribut
print(talaba1.universitet)   # TATU         -> class atribut
 
obj = Namuna()
obj.instance_metod()         # instance method chaqiruvi
Namuna.class_metod()         # class method chaqiruvi
Namuna.static_metod()        # static method chaqiruvi