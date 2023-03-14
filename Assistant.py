from Student import Student

from Modul import Modul

# Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
# Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.

#Deklarasi kelas Assistant, kelas Assistant mewarasi kelas Student
class Assistant(Student):

    __moduls = [] #asistanst memiliki beberapa modul untuk bahan mengajarnya dikelas

    #constructor dengan parameter, # constructor dengan parameter, parameter juga diisi dengan atribut parentnya
    def __init__(self, name = "", gender = "", univ = "", email = "", nim = "", faculty = "", major = "", laptops = [], books = [], moduls = []):

        #fungsi super digunakan untuk memanggil construct milik parent sehingga anak mewarisi semua method dan atribut dari parentnya
        super().__init__(name, gender, univ, email, nim, faculty, major, laptops, books)
        self.__moduls = moduls or []

    #setter untuk atribut-atribut Assistant

    def set_moduls(self, moduls):
        self.__moduls.append(moduls)

    #getter untuk atribut-atribut Assistant

    def get_moduls(self):
        return self.__moduls

    #method / kegiatan yang bisa dilakukan oleh assistant

    def teaching(self):
        print(self.get_name(), "is teaching the freshman!")
    
    def giving_homework(self):
        print(self.get_name(), "is giving the freshman a Homework!")