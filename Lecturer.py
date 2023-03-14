from CivitasAcademica import CivitasAcademica

from Laptop import Laptop
from Marker import Marker
from Assistant import Assistant

# Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
# Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.

#Deklarasi kelas Lecturer, kelas Lecturer mewarasi kelas CivitasAcademica
class Lecturer(CivitasAcademica):

    __nip = ""
    __faculty = "" 
    __department = ""
    __laptops = [] 
    __markers = []
    __assistants = [] #satu dosen dapat memiliki banyak asisten

    #constructor dengan parameter, # constructor dengan parameter, parameter juga diisi dengan atribut parentnya
    def __init__(self, name = "", gender = "", univ = "", email = "", nip = "", faculty = "", department = "", laptops = [], markers = [], assistants = []):

        #fungsi super digunakan untuk memanggil construct milik parent sehingga anak mewarisi semua method dan atribut dari parentnya
        super().__init__(name, gender, univ, email)
        self.__nip = nip
        self.__faculty = faculty
        self.__department = department
        self.__laptops = laptops or []
        self.__markers = markers or []
        self.__assistants = assistants or []

    #setter untuk atribut-atribut lecturer
    def set_nip(self, nip):
        self.__nip = nip

    def set_faculty(self, faculty):
        self.__faculty = faculty

    def set_department(self, department):
        self.__department = department

    def set_laptops(self, laptops):
        self.__laptops.append(laptops)

    def set_markers(self, markers):
        self.__markers.append(markers)

    def set_assistants(self, assistants):
        self.__assistants.append(assistants)

    #getter untuk atribut-atribut lecturer

    def get_nip(self):
        return self.__nip

    def get_faculty(self):
        return self.__faculty

    def get_department(self):
        return self.__department

    def get_laptops(self):
        return self.__laptops

    def get_markers(self):
        return self.__markers

    def get_assistants(self):
        return self.__assistants

    #method mengajar dan memberikan skor

    def teaching(self):
        print(self.get_name(), "is teaching the class!")

    def give_score(self):
        print(self.get_name(), "is giving the students scores!")