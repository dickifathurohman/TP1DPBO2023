# Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
# Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.
   
class Textbook: 

	__title = ""
	__author = ""

	# Constructor dengan atribut sebagai parameternya
	def __init__(self, title = "", author = ""):
		self.__title = title
		self.__author = author

	# setter untuk atribut-atribut yang dimiliki Textbook

	def set_title(self, title):
		self.__title = title

	def set_author(self, author):
		self.__author = author

	# getter untuk atribut-atribut yang dimiliki Textbook

	def get_title(self):
		return self.__title

	def get_author(self):
		return self.__author



