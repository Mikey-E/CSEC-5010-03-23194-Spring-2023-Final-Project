#Author: Michael Elgin

#Test file for pytest

import sys
import os

#Importability setup
cd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.normpath(os.path.join(cd, '..', '..', "src/")))

from serval import Serval
from pwcheck import CheckedPassword

def test_setOutputDirectory_not_exist():
	s = Serval()
	assert s.setOutputDirectory("asdf") == False

def test_setOutputDirectory_does_exist():
	s = Serval()
	assert s.setOutputDirectory("/") == True

def test_remove_extension():
	s = Serval()
	assert s.remove_serval_extension("asdf.serval") == "asdf"

def test_remove_no_extension():
	s = Serval()
	assert s.remove_serval_extension("asdf") == "asdf"

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

def test_create_key():
	s = Serval()
	s.setOutputDirectory(cd)
	password = "asdfasdfasdf1!A"
	s.setCheckedPassword(password)
	key = s.create_key()
	assert len(key) == 44 #Base64 encoded 32 bytes
	assert type(key) == bytes
