#Author: Michael Elgin

#Middleware to connect all software components together.

import os
from getpass import getpass
from cryptography.fernet import Fernet

from pwcheck import CheckedPassword

class Serval:

	def __init__(self):
		self.currentDirectory = "."

	def setCheckedPassword(self, password:str=None):
		self.checkedPassword = CheckedPassword(password if password != None else getpass())
		self.display_warnings()

	def setCurrentDirectory(self, path:str=".") -> bool:
		"""Changes where the .serval files are to be operated on"""
		try:
			os.chdir(path)
		except FileNotFoundError:
			return False
		self.currentDirectory = path
		return True

	def display_warnings(self):
		if len(self.checkedPassword.warnings) > 0:
			print("\nWARNING - Password is insecure - suggested improvements below\n")
			for warning in self.checkedPassword.warnings:
				print(warning)
			print("\nHighly consider using a different password")

	def create(self, fileName:str):
		"""create an empty new .serval file"""
		try:
			if fileName[-7:] == ".serval":
				fileName = fileName.replace(".serval", "")
		except IndexError:
			pass
		with open(fileName + ".serval", "wb") as f:
			f.write(bytes())

	def read(self, fileName:str):
		pass

	def update(self, fileName:str, string:str):
		pass

	def delete(self, fileName:str):
		pass

def main():
	pass

if __name__ == "__main__":
	main()
