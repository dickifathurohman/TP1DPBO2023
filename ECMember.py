from Student import Student

from Program import Program

# Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
# Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.

#Deklarasi kelas ECMember, kelas ECMember mewarasi kelas Student
class ECMember(Student):
	
    __role = "" #member atau staff
    __program = Program() #satu mahasiswa bisa memiliki satu program untuk diimplementasikan

    #constructor dengan parameter, # constructor dengan parameter, parameter juga diisi dengan atribut parentnya
    def __init__(self, name = "", gender = "", univ = "", email = "", nim = "", faculty = "", major = "", laptops = [], books = [], role = "", program = Program()):

        #fungsi super digunakan untuk memanggil construct milik parent sehingga anak mewarisi semua method dan atribut dari parentnya
        super().__init__(name, gender, univ, email, nim, faculty, major, laptops, books)
        self.__role = role
        self.__program = program

    #setter untuk atribut-atribut ECMember

    def set_role(self, role):
        self.__role = role

    def set_program(self, program):
        self.__program = program

    #getter untuk atribut-atribut ECMember

    def get_role(self):
        return self.__role

    def get_program(self):
        return self.__program

    #method

    #melatih kemampuan berbahasa asing
    def advancing_language(self):
        print(super().get_name(), "is advancing language!")
    
    #membuat / merencanakan program
    def planning_program(self, data):
        if self.__program != None: #jika sudah memiliki program
            print(self.get_name(), "has planned a program which is:")
            print(self.__program.get_name(), " | ", self.__program.get_description(), " | ", self.__program.get_date(), " | ", self.__program.get_status())
        else: #jika belum
            self.__program = data #tambahkan program
            print(self.get_name(), "succesfully planning a program which is:")
            print(self.__program.get_name(), " | ", self.__program.get_description(), " | ", self.__program.get_date(), " | ", self.__program.get_status())