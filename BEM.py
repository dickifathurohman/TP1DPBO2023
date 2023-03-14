# Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
# Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.

from BEMMember import BEMMember

class BEM: #Deklarasi untuk kelas BEM, karena dia merupakan Super/Base class jadi tidak mewarisi atribut dari yg lain
	
    __name = "" #nama bem
    __cabinet = "" #nama kabinet
    __year = "" #tahun periode
    __members = [] #didalam bem ada member-member yang tergabung kedalamnya

    # Constructor dengan atribut sebagai parameternya
    def __init__(self, name = "", cabinet = "", year = "", members = []):
        self.__name = name
        self.__cabinet = cabinet
        self.__year = year
        self.__members = members or []

    # setter untuk atribut-atribut yang dimiliki BEM

    def set_name(self, name):
        self.__name = name

    def set_cabinet(self, cabinet):
        self.__cabinet = cabinet

    def set_year(self, year):
        self.__year = year

    def set_members(self, members):
        self.__members.append(members)

    # getter untuk atribut-atribut yang dimiliki BEM

    def get_name(self):
        return self.__name

    def get_cabinet(self):
        return self.__cabinet

    def get_year(self):
        return self.__year

    def get_members(self):
        return self.__members



