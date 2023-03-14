# Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
# Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.
   
class Marker: 

	__brand = ""
	__color = ""

	# Constructor dengan atribut sebagai parameternya
	def __init__(self, brand = "", color = ""):
		self.__brand = brand
		self.__color = color

	# setter untuk atribut-atribut yang dimiliki Marker

	def set_brand(self, brand):
		self.__brand = brand

	def set_color(self, color):
		self.__color = color

	# getter untuk atribut-atribut yang dimiliki Marker

	def get_brand(self):
		return self.__brand

	def get_color(self):
		return self.__color



