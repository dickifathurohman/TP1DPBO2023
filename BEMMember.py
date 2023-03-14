from Student import Student

from Program import Program

# Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
# Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.

#Deklarasi kelas BEMMember, kelas BEMMember mewarasi kelas Student
class BEMMember(Student):

    __division = "" #divisinya
    __position = "" #posisinya
    __program = Program() #diasumsikan satu anggota bem memiliki satu proker

    #constructor dengan parameter, # constructor dengan parameter, parameter juga diisi dengan atribut parentnya
    def __init__(self, name = "", gender = "", univ = "", email = "", nim = "", faculty = "", major = "", laptops = [], books = [], division = "", position = "", program = Program()):

        #fungsi super digunakan untuk memanggil construct milik parent sehingga anak mewarisi semua method dan atribut dari parentnya
        super().__init__(name, gender, univ, email, nim, faculty, major, laptops, books)
        self.__division = division
        self.__position = position
        self.__program = program

    #setter untuk atribut-atribut BEMMember

    def set_division(self, division):
        self.__division = division

    def set_position(self, position):
        self.__position = position

    def set_program(self, program):
        self.__program = program
    

    #getter untuk atribut-atribut BEMMember

    def get_division(self):
        return self.__division

    def get_position(self):
        return self.__position

    def get_program(self):
        return self.__program

    #method
    
    #merencanakan program
    def planning_program(self, data):
        if self.__program == None: #jika belum memiliki program
            self.__program = data #tambahkan program
            print(self.get_name(), "successfully planning a program which is:")
            print(self.__program.get_name(), " | ", self.__program.get_description(), " | ", self.__program.get_date(), " | ", self.__program.get_status())
        else: #jika sudah
            #print langsung program yang sudah ada
            print(self.get_name(), "has planned a program which is:")
            print(self.__program.get_name(), " | ", self.__program.get_description(), " | ", self.__program.get_date(), " | ", self.__program.get_status())
    
    #mengimplementasikan program
    def implementing_program(self):
        if self.__program != None: #jika programnya ada
            self.__program.set_status("Done") #maka ganti status program menjadi done atau sudah dilaksanakan
            print(self.get_name(), "succesfully implemented a program! program status is ", self.__program.get_status())
        else:
            print(self.get_name(), "Can't implementing a program because is not yet planned!")

    #menghadiri evaluasi
    def attending_evaluation(self):
        if self.__program.get_status() == "": #jika statusnya masih kosong
            print(self.get_name(), "can't attend evaluation because ", self.__program.get_name(), "program is not yet implemented!")
        else: #jika statusnya sudah done
            print(self.get_name(), "is attending evaluation!")
