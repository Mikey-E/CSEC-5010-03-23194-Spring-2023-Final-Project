#Author: Michael Elgin

#Middleware to connect all software components together.

import os
from getpass import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from base64 import b64encode

from pwcheck import CheckedPassword

class Serval:

	def __init__(self):
		self.outputDirectory = "."

	def setCheckedPassword(self, password:str=None):
		self.checkedPassword = CheckedPassword(password if password != None else getpass())
		self.display_warnings()
		self.fernet = Fernet(self.create_key())

	def setOutputDirectory(self, path:str=".") -> bool:
		"""Changes where the .serval files are to be operated on"""
		if not os.path.exists(path):
			return False
		self.outputDirectory = path
		return True

	def display_warnings(self):
		if len(self.checkedPassword.warnings) > 0:
			print("\nWARNING - Password is insecure - suggested improvements below\n")
			for warning in self.checkedPassword.warnings:
				print(warning)
			print("\nHighly consider using a different password")

	def remove_serval_extension(self, fileName:str) -> str:
		"""removes .serval extension if it exists"""
		try:
			if fileName[-7:] == ".serval":
				return fileName.replace(".serval", "")
			return fileName
		except IndexError:
			return fileName

	def create_key(self):
		digest = hashes.Hash(hashes.SHA256())
		digest.update(self.checkedPassword.password.encode())
		return b64encode(digest.finalize())

	#CRUD functions follow
	def create(self, fileName:str):
		"""create an empty new .serval file"""
		with open(self.outputDirectory + "/" + self.remove_serval_extension(fileName) + ".serval", "wb") as f:
			f.write(bytes())

	def read(self, fileName:str):
		with open(self.outputDirectory + "/" + self.remove_serval_extension(fileName) + ".serval", "rb") as f:
			return self.fernet.decrypt(f.read()).decode()

	def update(self, fileName:str, string:str):
		"""writes an encrypted message to a .serval file"""
		with open(self.outputDirectory + "/" + self.remove_serval_extension(fileName) + ".serval", "wb") as f:
			f.write(self.fernet.encrypt(string.encode()))

	def delete(self, fileName:str):
		os.remove(self.outputDirectory + "/" + self.remove_serval_extension(fileName) + ".serval")

def main():
	pass

if __name__ == "__main__":
	main()
