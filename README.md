# COSC-5010-03-23194-Spring-2023-Final-Project

## Usage

Notes:
- Depending on your operating system and/or settings, it may be necessary to run the terminal with adiministrator priveleges.

To launch the application:

cd src

py GUI.py

### Testing

cd test

py -m pytest

This will run all tests. If you wish to run specfic test files, name a specific file after pytest

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

### Redundancy

#### Defense in depth

In addition to being encrypted, .serval files are also made obscure by default.

### Trust and responsibility

#### Reluctance to trust

Trust is strictly password-based. There are no exceptions for accessing .serval files.

## Misc notes

- Docstrings have been omitted for functions that seemed self-documenting and needed no more context about their operation

## 5010 Extension

The extension is the addendum in the Project_Design_Document folder.
