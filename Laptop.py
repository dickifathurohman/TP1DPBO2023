# Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
# Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.
   
class Laptop: 

	__brand = ""
	__type = ""

	# Constructor dengan atribut sebagai parameternya
	def __init__(self, brand = "", type = ""):
		self.__brand = brand
		self.__type = type

	# setter untuk atribut-atribut yang dimiliki Laptop

	def set_brand(self, brand):
		self.__brand = brand

	def set_type(self, type):
		self.__type = type

	# getter untuk atribut-atribut yang dimiliki Laptop

	def get_brand(self):
		return self.__brand

	def get_type(self):
		return self.__type



