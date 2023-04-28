#Author: Michael Elgin

#Test file for pytest

import sys
import os

#Importability setup
cd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.normpath(os.path.join(cd, '..', '..', "src/")))

from serval import Serval

def test_setCurrentDirectory_not_exist():
	s = Serval()
	assert s.setCurrentDirectory("asdf") == False

def test_setCurrentDirectory_does_exist():
	s = Serval()
	assert s.setCurrentDirectory("/") == True

def test_create_handle_extension():
	s = Serval()
	s.setCurrentDirectory(cd)
	s.create("testasdf.serval")
	assert "testasdf.serval" in os.listdir()
	os.remove("testasdf.serval")
	assert "testasdf.serval" not in os.listdir()

def test_create_handle_no_extension():
	s = Serval()
	s.setCurrentDirectory(cd)
	s.create("testasdf")
	assert "testasdf.serval" in os.listdir()
	os.remove("testasdf.serval")
	assert "testasdf.serval" not in os.listdir()
