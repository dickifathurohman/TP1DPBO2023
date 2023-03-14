# Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
# Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.
   
class Modul: 

	__matkul = ""
	__materi = ""

	# Constructor dengan atribut sebagai parameternya
	def __init__(self, matkul = "", materi = ""):
		self.__matkul = matkul
		self.__materi = materi

	# setter untuk atribut-atribut yang dimiliki Modul

	def set_matkul(self, matkul):
		self.__matkul = matkul

	def set_materi(self, materi):
		self.__materi = materi

	# getter untuk atribut-atribut yang dimiliki Modul

	def get_matkul(self):
		return self.__matkul

	def get_materi(self):
		return self.__materi



