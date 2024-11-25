"""
A collection of functions for encrypting and decrypting text using TYPE13 codes.

This module provides the following functions:

- `encrypter(string)`: Encrypts a string using TYPE13 codes.
- `decrypter(encoded_str)`: Decrypts a string encoded with TYPE13 codes.
- `validate_dc(data, dc)`: Validates whether two strings are equal.
"""
defs = {
	"A" : "&00;",
	"B" : "&01;",
	"C" : "&02;",
	'D' : "&03;",
	'E' : "&04;",
	'F' : "&05;",
	'G' : "&06;",
	'H' : "&07;",
	'I' : "&08;",
	'J' : "&09;",
	'K' : "&10;",
	'L' : "&11;",
	'M' : "&12;",
	'N' : "&13;",
	'O' : "&14;",
	'P' : "&15;",
	'Q' : "&16;",
	'R' : "&17;",
	'S' : "&18;",
	'T' : "&19;",
	'U' : "&20;",
	'V' : "&21;",
	'W' : "&22;",
	'X' : "&23;",
	'Y' : "&24;",
	'Z' : "&25;",
	"a" : "&001;",
	"b" : "&002;",
	'c' : "&003;",
	'd' : "&004;",
	'e' : "&005;",
	'f' : "&006;",
	'g' : "&007;",
	'h' : "&008;",
	'i' : "&009;",
	'j' : "&010;",
	'k' : "&011;",
	'l' : "&012;",
	'm' : "&013;",
	'n' : "&014;",
	'o' : "&015;",
	'p' : "&016;",
	'q' : "&017;",
	'r' : "&018;",
	's' : "&019;",
	't' : "&020;",
	'u' : "&021;",
	'v' : "&022;",
	'w' : "&023;",
	'x' : "&024;",
	'y' : "&025;",
	'z' : "&026;",
	"{" : "&co;",
	"}" : "&cc;",
	"#" : "&hs;",
	"@" : "&at;",
	"." : "&st;",
	"," : "&cm;",
	"/" : "&fs;",
	"\\": "&bs;",
	"%" : "&pc;",
	"'" : "&sq;",
	'"' : "&dq;",
	"(" : "&bo;",
	")" : "&bc;",
	"[" : "&so;",
	"]" : "&sc;",
	":" : "&fc;",
	";" : "&sm;",
	" " : "&ws;",
	".com" : "&com;",
	"$" : "&dl;",
	"-" : "&hyph;",
	"_" : "&und;",
	"=" : "&equ;",
	"+" : "&plus;",
	"|" : "&orsign;",
	"&" : "&amp;",
	"*" : "&ast;",
	"^" : "&pow;",
	"~" : "&crt;",
	"?" : "%qa;",
	"" : "&nt;",
	"<" : "&gt;",
	">" : "&lt;",
	"\n": "&nl;",
	"\t": "&tbsp;",
	"`": "&bctk;"
}
for n in list(range(1000)):
	defs[f"{n}"] = f"&&{n};"

# print(defs)
def encrypter(string):
	"""Encrypts a string using TYPE13 codes.

    Args:
        string (str): The string to be encrypted.

    Returns:
        str: The encrypted string.
    """
	re = []
	slist = {}
	for k, v in defs.items():
		for s in string:
			if k == s:
				slist[s] = v
	encoded = []

	for stri in string:
		for s, v in slist.items():
			if s == stri:
				encoded.append(slist[s])
	
	return "".join(encoded)

def decrypter(encoded_str):
	"""Decrypts a string encoded with TYPE13 codes.

    Args:
        encoded_str (str): The encoded string.

    Returns:
        str: The decrypted string.
    """
	en_list = encoded_str.split(";")
	en_list_new = []
	for en_item in en_list:
		en_list_new.append(en_item + ";")

	dc_list = []
	for item in en_list_new:
		for k, v in defs.items():
			if item == v:
				dc_list.append(k)


	decoded_str = "".join(dc_list)

	return decoded_str

def validate_dc(data, dc):
	"""Validates whether two strings are equal.

    Args:
        data (str): The first string to compare.
        dc (str): The second string to compare.

    Returns:
        bool: True if the strings are equal, False otherwise.
    """
	if data == dc:
		return True
	else:
		return False

# print(encrypter("['https://youtu.be/O5O3yK8DJCc', 'https://youtu.be/K4TOrB7at0Y']"))