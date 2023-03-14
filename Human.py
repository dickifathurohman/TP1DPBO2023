# Dicki Fathurohman_2103842_Ilmu Komputer TP1 DPBO2023
# Saya Dicki Fathurohman [2103842] mengerjakan TP1 DPBO2023 dalam mata kuliah DPBO
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin.
   
class Human: #Deklarasi untuk kelas Human

	# Atribut yang dimiliki oleh Human, ada name, dan gender
	# atribut ini nantinya akan dimiliki oleh anak atau turunan dari human
	__name = ""
	__gender = ""

	# Constructor dengan atribut sebagai parameternya
	def __init__(self, name = "", gender = ""):
		self.__name = name
		self.__gender = gender

	# setter untuk atribut-atribut yang dimiliki Human
	def set_name(self, name):
		self.__name = name

	def set_gender(self, gender):
		self.__gender = gender

	# getter untuk atribut-atribut yang dimiliki Human

	def get_name(self):
		return self.__name

	def get_gender(self):
		return self.__gender

	#method untuk human yaitu eat, drink dan sleep (kegiatan yang bisa dilakukan semua manusia)

	def eat(self):
		print(self.__name, "is eating!")

	def drink(self):
		print(self.__name, "is drinking!")

	def sleep(self):
		print(self.__name, "is sleeping!")



