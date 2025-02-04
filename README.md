# Notepad-Secure

Final project for COSC-5010-03-23194, spring 2023.

This software stores any information in encrypted files. It can be thought of as like Notepad, but "Notepad *secure*" because
it does not leave plaintext .txt files but rather encrypted files called .serval files, named after the African cat. Informally, this is an acronym for
**s**ecure **e**ncrypted **r**epository (of) **v**aluable **a**sset **l**anguage.

In the interest of usability, this final version allows users to use any password they want, even if it is possibly insecure,
however it still makes sure to warn them on both the GUI and terminal if they are doing so.

## Usage

Depending on your operating system and/or settings, it may be necessary to run the terminal with adiministrator priveleges.

To launch the application, run the following command:

py src/GUI.py

The application will start with a field in which to designate a working directory, and a field to type a password.
This password can be anything, even nothing (which is of course not recommended, but still results in files being
encrypted with an empty string as the basis for the encryption. One might do this to make a .serval file easily
available to anyone using the software).

Once these 2 fields have been chosen, click Refresh Files and Password. Now you will see a list of files in the working
directory for which you have access based on your password. You can read data from a selected file into the text box on the
right with the Read button, make edits, and update the selected file with the Update button.
The Delete button will delete the selected file from the file system. Create will create a file if it does not already exist,
and that new file will be accessible only with the supplied password once some content has been updated to it.

Open up a .serval file with another editor on the filesystem, and you will see the contents securely encrypted.

### Testing

py -m pytest test

This will run all tests. If you wish to run specific test files, name a specific file after pytest e.g.

py -m pytest test/\<file\>.py

Test cases are largely self-documenting.

## Dependencies

- Python 3.11.2
- PySimpleGUI 4.60.4
- cryptography 39.0.0
- password_strength 0.0.3.post2
- pytest 7.3.1

## Secure design patterns

### Design attributes

#### Transparent design

This software is open-source. Furthermore, it adhere's to Kerckhoff's principle because the cryptography only relies on the
key being secret.

### Exposure minimization

#### Fail securely

The software is designed so that only encrypted data is ever written to non-volatile storage. This way, if a crash were
to occur, there would not be an unencrypted file left out in the open.

#### Least information

No information about the user is required except for their password, which is used to determine their cryptographic key.

#### Secure by default

No sensitive data or other security hazards pre-exist usage.

### Strong enforcement

#### Complete mediation

The protected assets (.serval files) are accessible only by password. Nothing else need be mediated.

#### Least common mechanism

All software components are mediated by a single piece of middleware, serval.py

### Trust and responsibility

#### Reluctance to trust

Trust is strictly password-based. There are no exceptions for accessing .serval files.

## Miscellaneous notes

- Docstrings have been omitted for functions that seemed self-documenting and needed no more context about their operation
- Modified (tampered) .serval files are considered corrupt and not loaded into the list of files.
- An empty .serval file is considered available for anyone to write to (not yet password protected).

## 5010 Extension

The extension is the addendum in the Project_Design_Document folder of Michael_Elgin_Project_Design_Document.pdf
