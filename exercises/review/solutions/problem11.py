r"""
The solution to problem 11.

We note that this solution is not a *true* morse code translator, but that it
achieves the instructive goals of this exercise. In real morse code, spaces
between letters and words are given three dots and seven dots of space,
respectively. Here we simply print a slash between words.
"""

# A dictionary mapping between ascii text characters and morse code. For the
# sake of this solution, a hard-coded dictionary suffices just fine. In a
# larger program, one might elect to store the mapping as a text file with two
# columns, which then gets read in with a file I/O routine to systematically
# construct this dictionary.
MORSE_CODE = {
	'A': '.-',
	'B': '-...',
	'C': '-.-.',
	'D': '-..',
	'E': '.',
	'F': '..-.',
	'G': '--.',
	'H': '....',
	'I': '..',
	'J': '.---',
	'K': '-.-',
	'L': '.-..',
	'M': '--',
	'N': '-.',
	'O': '---',
	'P': '.--.',
	'Q': '--.-',
	'R': '.-.',
	'S': '...',
	'T': '-',
	'U': '..-',
	'V': '...-',
	'W': '.--',
	'X': '-..-',
	'Y': '-.--',
	'Z': '--..',
	'1': '.----',
	'2': '..---',
	'3': '...--',
	'4': '....-',
	'5': '.....',
	'6': '-....',
	'7': '--...',
	'8': '---..',
	'9': '----.',
	'0': '-----',
	',': '--..--',
	'.': '.-.-.-',
	'?': '..--..',
	'/': '-..-.',
	'-': '-....-',
	'(': '-.--.',
	')': '-.--.-',
	' ': ' / '
}

def text_to_morse(text):
	r"""
	Converts a string to morse code.

	Parameters
	----------
	text : ``str``
		The input string of text.

	Returns
	-------
	morse : ``str``
		The input string convered to morse code via the dictionary implemented
		as a global variable in this file.
	"""
	morse_code = ''
	for char in text:
		if char.upper() in MORSE_CODE.keys():
			morse_code += MORSE_CODE[char.upper()] + ' '
	return morse_code

text = "hi pam"
morse_code = text_to_morse(text)
print(morse_code)

# Output .... ..  /  .--. .- --
