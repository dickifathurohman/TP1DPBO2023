# Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
# Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.
   
class Program: 

    __name = ""
    __date = ""
    __description = ""
    __status = ""

    # Constructor dengan atribut sebagai parameternya
    def __init__(self, name = "", date = "", description = "", status = ""):
        self.__name = name
        self.__date = date
        self.__description = description
        self.__status = status

    # setter untuk atribut-atribut yang dimiliki Program

    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def set_description(self, description):
        self.__description = description

    def set_status(self, status):
        self.__status = status

    # getter untuk atribut-atribut yang dimiliki Program

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status


