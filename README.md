# TP1DPBO2023

## Janji
Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO, untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.

## Desain
![image](https://user-images.githubusercontent.com/100754802/225044584-bedfb954-52a2-428d-898c-05962dfc10e6.png)



Pada desain ini Student dan Lecturer merupakan child dari CivitasAcademica, dan SivitasAcademica merupakan child dari Human. Alasan dari pewarisan seperti ini yaitu karena Mahasiswa dan Dosen itu termasuk kedalam sivitas akademik karena Sivitas Akademik dapat berisi mahasiswa dan dosen bukan hanya mahasiswa/dosen saja sehingga Sivitas Akademik dijadikan Parent. Kemudian sivitas akademik itu merupakan Manusia sehingga menjadi Child dari Class Manusia.

Student memiliki child yaitu BEMMember, ECMember, dan Assistant karena anggota bem, club ataupun assistant adalah mahasiswa. 

Lecturer dapat memiliki banyak assistant yang membantunya.
BEM dapat mempunyai beberapa anggota, dan anggota (BEMMember) diasumsikan memiliki 1 program kerja tiap orangnya. Begitupun dengan ECMember yang juga dapat memiliki 1 program atau tidak memiliki program. Sementara itu assistant memiliki modul untuk bahan ajarnya dikelas

Penjelasan detail mengenai class :
1) Class Human
Merupakan Base/Super Class, class ini tidak mewarisi atribut dari kelas manapun. Dalam kelas ini terdiri 2 atribut yang pasti dimiliki oleh setiap Human yaitu Name dan Gender. Human memiliki method eat, drink dan sleep.
2) Class CivitasAcademica
Class ini merupakan child dari Human, karena sivitas akademik itu merupakan manusia. Maka dia mewarisi atribut dari parentnya sehingga tidak perlu membuat lagi atribut nama dan gender untuk dirinya. Sivitas Akademik memiliki dua atribut baru yaitu univ yang menandakan asal universitas, dan email yaitu email universitas.
3) Class Student
Student merupakan child dari CivitasAcademica, karena termasuk kedalamnya. Class ini memiliki atribut tambahan yaitu nim, fakultas dan prodi. Student dapat memiliki beberapa laptop dan textbook untuk menunjang kegiatan perkuliahannya (composite). Student menjadi parent bagi BEMMember, ECMember dan Assistant. Student memiliki method tambahan yaitu studying.
4) Assistant
Assistant memiliki beberapa modul untuk bahan mengajar dikelas (composite). Assistant memiliki method teaching dan giving_homework.
5) ECMember
ECMember dpat memiliki satu program per membernya. EC Member memiliki method advancing_language, dan planning_program
6) BEM
BEM memiliki beberapa BEMMember didalamnya, karena BEM pasti memiliki banyak anggota.
7) BEMMember
diasumsikan bahwa satu BEMMember hanya memegang satu program kerja yang menjadi tanggung jawabnya (Ketua pelaksana proker). Ada beberapa method yang dapat dilakukan oleh BEMMember, yaitu planning_program, implementing_program (hanya bisa dilakukan jika ada program yang dibuat), attending_evaluation (bisa dilakukan jika status program "done")
8) Class Lecturer (Dosen)
Dosen merupakan child dari CivitasAcademica, karena merupakan bagian dari sivitas akademik sama halnya dengan mahasiswa. Lecturer memiliki atribut tambahan yaitu nip, fakultas dan departemen dimana dia mengajar. Lecturer dapat memiliki beberapa laptop dan marker untuk kegiatan mengajarnya, dan beberapa assistant yang dapat membantunya. Lecturer memiliki method teaching dan give_score.


## Alur Program
Pada program Main yang dibuat dengan hardcode, hal pertama yang dilakukan yaitu membuat, mengisi attribut untuk laptop, textbook, marker dan modul yang nantinya akan dimiliki oleh Student, BEMMember / ECMember / Assistant / Lecturer. Kemudian membuat objek program untuk BEMMember dan ECMember. Selanjutnya membuat objek resyad yang merupakan mahasiswa, mila yang merupakan assistant, angga dan gatsby yang merupakan ECMember, dan pahri yang merupakan BEMMember. Kemudian membuat objek BEM yang memiliki member pahri didalamnya. Dan membuat dosen yang memiliki mila sebagai assistantnya.

Data kemudian ditampilkan, dengan urutan :
1) Regular Student (Resyad) lengkap dengan data laptop, textbooks dan method yang bisa Human dan Student lakukan.
2) Menampilkan data BEM dan Membernya. Kemudian ditampilkan juga method dan interaksinya ketika planning implementing program dan attending evaluatioan
3) Menampilkan data EC Member dan method yang dilakukannya
4) Menampilkan data dosen beserta asisstantnya dan juga method tambahan yang dapat dilakukan

## Dokumentasi
![image](https://user-images.githubusercontent.com/100754802/225044240-2728f1f7-9d76-49fd-88ba-f3bdac309ef7.png)
![image](https://user-images.githubusercontent.com/100754802/225044353-e977698e-a8a4-4d57-b9b8-30dad5d0ab84.png)
