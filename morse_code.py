

morse_dict = {
	"A":".-", 
	"B":"-...", 
	"C":"-.-.",
	"D":"-..",
	"E":".",
	"F":"..-.",
	"G":"--.",
	"H":"....",
	"I":"..",
	"J":".---",
	"K":"-.-",
	"L":".-..",
	"M":"--",
	"N":"-.",
	"O":"---",
	"P":".--.",
	"Q":"--.-",
	"R":".-.",
	"S":"...",
	"T":"-",
	"U":"..-",
	"V":"...-",
	"W":".--",
	"X":"-..-",
	"Y":"-.--",
	"Z":"--..",
	###########
	".-":"A", 
	"-...":"B", 
	"-.-.":"C",
	"-..":"D",
	".":"E",
	"..-.":"F",
	"--.":"G",
	"....":"H",
	"..":"I",
	".---":"J",
	"-.-":"K",
	".-..":"L",
	"--":"M",
	"-.":"N",
	"---":"O",
	".--.":"P",
	"--.-":"Q",
	".-.":"R",
	"...":"S",
	"-":"T",
	"..-":"U",
	"...-":"V",
	".--":"W",
	"-..-":"X",
	"-.--":"Y",
	"--..":"Z",
	############
	"1":".----",
	"2":"..---",
	"3":"...--",
	"4":"....-",
	"5":".....",
	"6":"-....",
	"7":"--...",
	"8":"---..",
	"9":"----.",
	"0":"-----",
	############
	".----":"1",
	"..---":"2",
	"...--":"3",
	"....-":"4",
	".....":"5",
	"-....":"6",
	"--...":"7",
	"---..":"8",
	"----.":"9",
	"-----":"0",

	}

def is_morse(string):
	if len(string) == 0:
		return False
	for x in string:
		if x not in '-. ':
			return False
	return True

def convert_morse(string):
	result = ""
	string = string.upper()

	if is_morse(string):
		string_storage = ""
		string += " "

		for x in string:
			if x != " ":
				string_storage += x

			elif x == " ":
				if len(string_storage) > 0:
					result += morse_dict[string_storage]
				result += " "
				string_storage = ""
				continue
		
		result = result.replace("  ", "%")
		result = result.replace(" ", "")
		result = result.replace("%", " ")
		return result


	else:
		for x in string:
			if x == " ":
				result += x
				result += " "
				continue
			else:
				result += morse_dict[x]
				result += " "
				continue
		return result
