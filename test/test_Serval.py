#Author: Michael Elgin

#Test file for pytest

import sys
import os
from cryptography.fernet import Fernet

#Importability setup
cd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.normpath(os.path.join(cd, '..', "src/")))

from Serval import Serval
from CheckedPassword import CheckedPassword

def setup_serval(func):
	"""decorator for setting up the Serval with the directory and password"""
	def wrapper():
		s = Serval()
		s.setOutputDirectory(cd)
		password = "asdfasdfasdf1!A"
		s.setCheckedPassword(password)
		func(s)
	return wrapper

def test_setOutputDirectory_not_exist():
	s = Serval()
	assert s.setOutputDirectory("asdf") == False

def test_setOutputDirectory_does_exist():
	s = Serval()
	assert s.setOutputDirectory("/") == True

def test_remove_extension():
	s = Serval()
	assert s.base_name("asdf.serval") == "asdf"

def test_remove_no_extension():
	s = Serval()
	assert s.base_name("asdf") == "asdf"

def test_create_handle_extension():
	s = Serval()
	s.setOutputDirectory(cd)
	s.create("testasdf.serval")
	assert "testasdf.serval" in os.listdir(cd)
	os.remove(cd + "/" + "testasdf.serval")
	assert "testasdf.serval" not in os.listdir(cd)

def test_create_handle_no_extension():
	s = Serval()
	s.setOutputDirectory(cd)
	s.create("testasdf")
	assert "testasdf.serval" in os.listdir(cd)
	os.remove(cd + "/" + "testasdf.serval")
	assert "testasdf.serval" not in os.listdir(cd)

def test_create_double():
	s = Serval()
	s.setOutputDirectory(cd)
	fileName = "double_create_check.serval"
	assert(s.create(fileName))
	assert fileName in os.listdir(cd)
	assert(not s.create(fileName))
	assert fileName in os.listdir(cd)
	s.delete(fileName)
	assert fileName not in os.listdir(cd)

@setup_serval
def test_create_key(s:Serval):
	key = s.create_key()
	assert len(key) == 44 #Base64 encoded 32 bytes
	assert type(key) == bytes

@setup_serval
def test_update(s:Serval):
	fileName = "test_update.serval"
	message = "This is the message to be encrypted"
	s.update(fileName, message)
	with open(cd + "/" + fileName, "rb") as f:
		contents = f.read()
	assert len(contents) > 0, "File is empty"
	fern_for_decryption = Fernet(s.create_key())
	assert message == fern_for_decryption.decrypt(contents).decode(), "encryption was not reversed to same message"
	os.remove(cd + "/" + fileName)
	assert fileName not in os.listdir(cd)

@setup_serval
def test_delete(s:Serval):
	fileName = "test_delete"
	s.create(fileName)
	assert fileName + ".serval" in os.listdir(cd)
	assert(s.delete(fileName))
	assert fileName + ".serval" not in os.listdir(cd)
	assert(not s.delete(fileName))

@setup_serval
def test_read(s:Serval):
	fileName = "test_read.serval"
	message = "This is the message to be encrypted, then read"
	s.update(fileName, message)
	assert s.read(fileName) == message
	s.delete(fileName)
	assert fileName + ".serval" not in os.listdir(cd)
