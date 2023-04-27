# CSEC-5010-03-23194-Spring-2023-Final-Project

## Usage

To launch the application:

py src/serval.py

### Testing

py -m pytest test

This will run all tests. If you wish to run specfic test files, replace "test" with test/path/to/test_file.py

Test cases are largely self-documenting.

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

## 5010 Extension

The extension is the addendum in the Project_Design_Document folder.
