#Author: Michael Elgin

#Test file for pytest

import sys
import os

#Importability setup
cd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.normpath(os.path.join(cd, '..', "src/")))

from CheckedPassword import CheckedPassword

def test_policy_criteria():
	cpw = CheckedPassword("asdfqmdiqlk")
	expectedWarningsAmt = 4
	assert len(cpw.warnings) == expectedWarningsAmt, "length of conditions was not " + str(expectedWarningsAmt)
	assert "Suggested length: 12" in cpw.warnings, "no warning for length of password"
	assert "Suggested numbers: 1" in cpw.warnings, "no warning for having no numbers in password"
	assert "Suggested uppercase characters: 1" in cpw.warnings, "no warning for having no uppercase characters"
	assert "Suggested special characters: 1" in cpw.warnings, "no warning for having no special characters"
	assert "One of the most common passwords" not in cpw.warnings

def test_numbers():
	cpw = CheckedPassword("asdfasdfasdfA!")
	expectedWarningsAmt = 1
	assert len(cpw.warnings) == expectedWarningsAmt, "length of conditions was not " + str(expectedWarningsAmt)
	assert "Suggested numbers: 1" in cpw.warnings, "no warning for having no numbers in password"
	assert "One of the most common passwords" not in cpw.warnings

def test_uppercase():
	cpw = CheckedPassword("asdfasdfasdf1!")
	expectedWarningsAmt = 1
	assert len(cpw.warnings) == expectedWarningsAmt, "length of conditions was not " + str(expectedWarningsAmt)
	assert "Suggested uppercase characters: 1" in cpw.warnings, "no warning for having no uppercase characters"
	assert "One of the most common passwords" not in cpw.warnings

def test_specials():
	cpw = CheckedPassword("asdfasdfasdfA1")
	expectedWarningsAmt = 1
	assert len(cpw.warnings) == expectedWarningsAmt, "length of conditions was not " + str(expectedWarningsAmt)
	assert "Suggested special characters: 1" in cpw.warnings, "no warning for having no special characters"
	assert "One of the most common passwords" not in cpw.warnings

def test_all_errors():
	cpw = CheckedPassword("sunshine")
	expectedWarningsAmt = 5
	assert len(cpw.warnings) == expectedWarningsAmt, "length of conditions was not " + str(expectedWarningsAmt)
	assert "Suggested length: 12" in cpw.warnings, "no warning for length of password"
	assert "Suggested numbers: 1" in cpw.warnings, "no warning for having no numbers in password"
	assert "Suggested uppercase characters: 1" in cpw.warnings, "no warning for having no uppercase characters"
	assert "Suggested special characters: 1" in cpw.warnings, "no warning for having no special characters"
	assert "One of the most common passwords" in cpw.warnings
