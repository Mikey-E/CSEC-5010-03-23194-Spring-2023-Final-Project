#Author: Michael Elgin

#Middleware to connect all software components together.

import os
from getpass import getpass
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from base64 import b64encode

from CheckedPassword import CheckedPassword

class Serval:

	def __init__(self):
		self.outputDirectory = "."

	def setCheckedPassword(self, password:str=None):
		self.__checkedPassword = CheckedPassword(password if password != None else getpass())
		self.display_warnings()
		self.fernet = Fernet(self.create_key())

	def setOutputDirectory(self, path:str=".") -> bool:
		"""Changes where the .serval files are to be operated on"""
		if not os.path.exists(path):
			return False
		self.outputDirectory = path
		return True

	def display_warnings(self):
		if len(self.__checkedPassword.warnings) > 0:
			print("\nWARNING - Password is insecure - suggested improvements below\n")
			for warning in self.__checkedPassword.warnings:
				print(warning)
			print("\nHighly consider using a different password")

	def base_name(self, fileName:str) -> str:
		"""removes .serval extension if it exists"""
		try:
			if fileName[-7:] == ".serval":
				return fileName.replace(".serval", "")
			return fileName
		except IndexError:
			return fileName

	def create_key(self):
		digest = hashes.Hash(hashes.SHA256())
		digest.update(self.__checkedPassword.password.encode())
		return b64encode(digest.finalize())

	#CRUD functions follow
	def create(self, fileName:str) -> bool:
		"""create an empty new .serval file"""
		fileName = self.base_name(fileName)
		if fileName + ".serval" in os.listdir(self.outputDirectory):
			return False
		with open(self.outputDirectory + "/" + fileName + ".serval", "wb") as f:
			f.write(bytes())
		return True

	def read(self, fileName:str) -> str:
		try:
			with open(self.outputDirectory + "/" + self.base_name(fileName) + ".serval", "rb") as f:
				contents = f.read()
				if len(contents) == 0:
					return ""
				try:
					return self.fernet.decrypt(contents).decode()
				except InvalidToken:
					return None
		except FileNotFoundError:
			return ""

	def update(self, fileName:str, string:str):
		"""writes an encrypted message to a .serval file"""
		with open(self.outputDirectory + "/" + self.base_name(fileName) + ".serval", "wb") as f:
			f.write(self.fernet.encrypt(string.encode()))

	def delete(self, fileName:str) -> bool:
		try:
			os.remove(self.outputDirectory + "/" + self.base_name(fileName) + ".serval")
			return True
		except FileNotFoundError:
			return False
	def get_warnings():
		return self.__checkedPassword.warnings

def main():
	pass

if __name__ == "__main__":
	main()
