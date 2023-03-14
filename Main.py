# Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
# Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.

#import classes
from Laptop import Laptop
from Marker import Marker
from Textbook import Textbook
from Modul import Modul
from Program import Program
from Student import Student
from Assistant import Assistant
from ECMember import ECMember
from BEMMember import BEMMember
from BEM import BEM
from Lecturer import Lecturer

#membuat objek laptop dan mengisi atributnya
laptop1 = Laptop("Asus", "Vivobook X505Z")
laptop2 = Laptop("Asus", "Zenbook X666X")
laptop3 = Laptop("Apple", "Macbook Pro M2")
laptop4 = Laptop("Lenovo", "Legion 64M1N6")
laptop5 = Laptop("Lenovo", "Thinkpad 12345")

#membuat objek Marker dan mengisi atributnya
marker1 = Marker("Snowman", "Black")
marker2 = Marker("Snowman", "Blue")
marker3 = Marker("Snowman", "Red")

#membuat objek Textbook dan mengisi atributnya
book1 = Textbook("Get to know Artificial Intelligence", "Yaya")
book2 = Textbook("Study Programming Algorithm", "Rosa")
book3 = Textbook("Inside Operating System", "Hendrick")
book4 = Textbook("The Growth of Big Data", "Argus")

#membuat objek Modul dan mengisi atributnya
modul1 = Modul("DPBO", "Inheritance part 1")
modul2 = Modul("DPBO", "Inheritance part 2")
modul3 = Modul("Basis Data", "Generalization")

#membuat program
ECprogram = Program("Speaking session", "20-07-2023", "Everyone need to speak about their dream", "")
BEMprogram = Program("P2M", "12-05-2023", "to implement tri dharma", "")

#membuat objek student, assistant, EC member juga BEM Member
resyad = Student("Resyad", "Male", "UPI", "resyad@upi.edu", "2106543", "FPMIPA", "Computer Science", laptops=[laptop5, laptop1], books=[book2, book3])

mila = Assistant("Mila", "Female", "UPI", "mila@upi.edu", "2101234", "FPMIPA", "Computer Science", laptops=[laptop5], books=[book2], moduls=[modul1, modul2, modul3])

angga = ECMember("Angga", "Male", "UPI", "angga@upi.edu", "2104321", "FPMIPA", "Computer Science", laptops=[laptop2, laptop3], books=[book2, book3], role="staff", program=ECprogram)
gatsby = ECMember("Getsby", "Male", "UPI", "getsby@upi.edu", "2103842", "FPMIPA", "Computer Science", laptops=[laptop4, laptop1], books=[book1, book4], role="staff", program=None)

pahri = BEMMember("Pahri", "Male", "UPI", "pahri@upi.edu", "2106789", "FPMIPA", "Computer Science", laptops=[laptop3], books=[book1, book2], division="Divadsospol", position="Head of Division", program=None)

#membuat objek BEM yang mempunyai members
kemakom = BEM("Kemakom", "Abakadabra", "2023/2024", members=[pahri])

#membuat lecturert yang memiliki assistant
dosen = Lecturer("Rose", "Female", "UPI", "rose@upi.edu", "123456789", "FPMIPA", "Comp Science Education Department", laptops=[laptop4, laptop2], markers=[marker1, marker2, marker3], assistants=[mila])


#menampilkan data student regular (resyad)
print("In University there is a regular student :")

print(resyad.get_name(), " | ", resyad.get_gender(), " | ", resyad.get_nim(), " | ", resyad.get_univ(), " | ", resyad.get_faculty(), " | ", resyad.get_major(), " | ", resyad.get_email())
print("\nStudent has laptops :")
for laptop in resyad.get_laptops():
    print(laptop.get_brand(), " | ", laptop.get_type())
print("Student also has books:")

for buku in resyad.get_books():
    print("Title : ", buku.get_title(), " | Author : ", buku.get_author())

print("\nAs a human being, student can do :")
resyad.eat()
resyad.drink()
resyad.sleep()
print("And a student need to study!")
resyad.studying()

#menampilkan data BEM

print("\nIn University there is student Organization or BEM :")
print("BEM : ", kemakom.get_name(), " | ", kemakom.get_cabinet(), " | ", kemakom.get_year())

#data member bem dan programnya
print("There are students that is a Bem member : ")
for member in kemakom.get_members():
    print(member.get_name(), " | ", member.get_gender(), " | ", member.get_nim(), " | ", member.get_univ(), " | ", member.get_faculty(), " | ", member.get_major(), " | ", member.get_email())

    print("\nOther than what human and student can do, BEM Member can planning and implementing program, and attending evaluation")
    member.planning_program(BEMprogram)
    member.attending_evaluation()
    member.implementing_program()
    member.attending_evaluation()

#data english club
print("\nStudent can join a club or community, for example english club :")
print(angga.get_name(), " | ", angga.get_gender(), " | ", angga.get_nim(), " | ", angga.get_univ(), " | ", angga.get_faculty(), " | ", angga.get_major(), " | ", angga.get_email())
angga.advancing_language()
angga.planning_program(ECprogram)
print("")
print(gatsby.get_name(), " | ", gatsby.get_gender(), " | ", gatsby.get_nim(), " | ", gatsby.get_univ(), " | ", gatsby.get_faculty(), " | ", gatsby.get_major(), " | ", gatsby.get_email())
gatsby.advancing_language()
gatsby.planning_program(ECprogram)

#data dosen
print("\nOther than student, there is also a lecturer:")
print(dosen.get_name(), " | ", dosen.get_gender(), " | ", dosen.get_nip(), " | ", dosen.get_univ(), " | ", dosen.get_faculty(), " | ", dosen.get_department(), " | ", dosen.get_email())

print("Lecturer can teach the class and give the students their score:")
dosen.teaching()
dosen.give_score()

print("\nLecturer has laptops :")
for laptop in dosen.get_laptops():
    print(laptop.get_brand(), " | ", laptop.get_type())

print("Lecturer has markers:")
for spidol in dosen.get_markers():
    print("Brand : ", spidol.get_brand(), " | Color : ", spidol.get_color())

#data assistant
print("\nLecturer has assistant that helped them, a student can be an assistant :")
print(mila.get_name(), " | ", mila.get_gender(), " | ", mila.get_nim(), " | ", mila.get_univ(), " | ", mila.get_faculty(), " | ", mila.get_major(), " | ", mila.get_email())

print("\nAn assistant had a material for teaching")

for modul in mila.get_moduls():
    print("Course : ", modul.get_matkul(), " | Subject Matterial : ", modul.get_materi())

print("\nOther than what human and student can do, assistant can teach and give homework")
mila.teaching()
mila.giving_homework()