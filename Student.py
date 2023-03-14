from CivitasAcademica import CivitasAcademica

from Laptop import Laptop
from Textbook import Textbook

# Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
# Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.

#Deklarasi kelas Student, kelas Student mewarasi kelas CivitasAcademica
class Student(CivitasAcademica):
	#Student memiliki atribut dari Sivitas Akademik dan Human
	#Kemudian ada beberapa atribut tambahan dari Student
	#disini tidak perlu menambahkan nama dan jenis kelamin karena sudah diwarisi dari human

    __nim = ""
    __faculty = "" 
    __major = ""
    __laptops = [] #student dapat memiliki beberapa laptop
    __books = [] #student juga memiliki beberapa buku

    #constructor dengan parameter, # constructor dengan parameter, parameter juga diisi dengan atribut parentnya
    def __init__(self, name = "", gender = "", univ = "", email = "", nim = "", faculty = "", major = "", laptops = [], books = []):

        #fungsi super digunakan untuk memanggil construct milik parent sehingga anak mewarisi semua method dan atribut dari parentnya
        super().__init__(name, gender, univ, email)
        self.__nim = nim
        self.__faculty = faculty
        self.__major = major
        self.__laptops = laptops or []
        self.__books = books or []

    #setter untuk atribut-atribut Student
    def set_nim(self, nim):
        self.__nim = nim

    def set_faculty(self, faculty):
        self.__faculty = faculty

    def set_major(self, major):
        self.__major = major

    def set_laptops(self, laptops):
        self.__laptops.append(laptops)

    def set_books(self, books):
        self.__books.append(books)

    #getter untuk atribut-atribut Student

    def get_nim(self):
        return self.__nim

    def get_faculty(self):
        return self.__faculty

    def get_major(self):
        return self.__major

    def get_laptops(self):
        return self.__laptops

    def get_books(self):
        return self.__books

    #method untuk student yaitu studying

    def studying(self):
        print(self.get_name(), "is studying!")