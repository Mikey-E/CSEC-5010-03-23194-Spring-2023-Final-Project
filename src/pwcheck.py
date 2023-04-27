#Author: Michael Elgin

#File to create a checked password object.
#Will encapsulate any warnings associated with it.

import password_strength as pws

class CheckedPassword:

	def __init__(self, password:str, length:int=12, uppercase:int=1, numbers:int=1, special:int=1):
		self.__password = password

		#Recommendations
		self.length = length
		self.uppercase = uppercase
		self.numbers = numbers
		self.special = special
	
		#Determined based on password and recommendations
		self.conditions = self.check(self.__password)
		self.warnings = self.user_friendly_warnings(*self.conditions)

	def check(self, password:str) -> (bool, list):
		"""
		Takes a password and returns whether or not it is secure,
		along with a list of failed conditions
		"""
		conditions = pws.PasswordPolicy.from_names(
			length = self.length,
			uppercase = self.uppercase,
			numbers = self.numbers,
			special = self.special,
		)

		return conditions.test(password)

	def user_friendly_warnings(self, *args:tuple[pws.tests_base.ATest]) -> list[str]:
		"""
		Returns user friendly string of any failed test case(s).
		"""
		mapping = {
			"length"	:	"Suggested length",
			"uppercase"	:	"Suggested uppercase characters",
			"numbers"	:	"Suggested numbers",
			"special"	:	"Suggested special characters",
		}

		return [mapping[arg.name()] + ": " + \
			(str(arg.count) if arg.name() != "length" else str(arg.length))\
			for arg in args]
