#input_string = ""
#position = 0      #position of current character
current_char = '' #current character
IdentifierCTR = 0 #counter of how many Identifiers are there
unknownCharacters = ['@', '$', '^', '&', '_', '?', '|', ';', '-', '|', '\\', ':', ';', 'q', 'd', 'j', 'k', 'l', 'm', 'w', 'v', 'x', 'y', 'z', "'"] + [chr(ord('A') + i) for i in range(26)]
# reservedKeywords = ["and", "pin", "pout", "hint", "flute", "star", "bully", "if", "elsa", "elib", "in", "and", "or", "not", "poor", "checkif", "chill", "goon", "task", "remit", "nocap", "cap", "universal", "advance", "range"]

# delim1 = [" ", "#", "~", "\n", "}", "\0"]
# delim2 = [" ", "("]
# delim3 = [" "]
# delim4 = [" ", ")", "]", "}", "#", "~", "=", "!", "<", ">", "\n", "\0"]
# delim5 = ["("]
# delim6 = ["{"]
# delim7 = [" ", "`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", '"', "c", "n", "(", "_"]
# delim8 = [" ", "`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", '"', "(", "_"]
# delim9 = [" ", "`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", "_", "\0"]
# delim10 = [" ", "+", "-", "*", "/", "%", ")", "<", ">", "=", "!", ",", "#", "~", "\n", "\0", "}", "]"]
# delim11 = ["}", "#", "~", "`", " ", "\0", "\n", "a", "b", "c", "f", "g", "h", "i", "p", "r", "s", "u"]
# delim12 = ["#", "~", " ", "\0", "\n", "`", "a", "b", "c", "e", "f", "g", "h", "i", "p", "r", "s", "t", "u", "]"]
# delim13 = [" ", "\0", "\n", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "`", "c", "n", '"', "(", "_"]
# delim14 = [" ", "\0", "\n", "a", "o", "#", "~", "+", "-", "*", "/", "%", "!", "=", "<", ">", ",", "]", "}", ")", "{"]
# delim15 = [" ", "\n", "\0", "b", "c", "f", "h", "i", "p", "s", "t", "u", "#", "~"]
# delim16 = ["\0"]
# delim17 = [" ", "+", "=", "!", "<", ">", ",", "#", "~", "]", ")", "}", "\n", "\0"]
# delim18 = [" ", "+", "-", "*", "/", "%", ")", "(", "<", ">", "=", "!", ",", "#", "~", "\n", "\0", "}", "]"]
# delim19 = ["]", "\n", "\0"]
# delim20 = [" ", "\n", "\0", "}", "]"]
# delim21 = [" ", "`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", '"', "c", "n", "(", "_"]

delim1 = ["("]
delim2 = [" "]
delim3 = ["{"]
delim4 = [" ", "(" ]
delim5 = [" ", "#", "~", "\n", "}", "\0"]
delim6 = [" ", ")", "]", "}", "#", "~", "=", "!", "\n", "\0", "|", ',']
delim7 = [" ", "`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", '"', "p", "c", "n", "(", "_", "'", "["]
delim8 = [" ", "`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", '"', "p", "(", "_"]
delim9 = [" ", "`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "p", "(", "_"]
delim10 = [" ", "`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", '"', "c", "n", "(", "_", "'"]
delim11 = [" ", "`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", "_"]
delim12 = [" ", "`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", '"', "(", "_"]
delim13 = ["#", "~", "`", " ", "\0", "\n", "a", "b", "c", "f", "g", "h", "i", "p", "r", "s", "u", "}"]
delim14 = ["#", "~", " ", "\0", "\n", "`", "a", "b", "c", "e", "f", "g", "h", "i", "p", "r", "s", "t", "u", "|", "}"]
delim15 = [" ", "\0", "\n", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "`", "c", "n", '"', "(", "_", "'", ')', '[']
delim16 = [" ", "\0", "\n", "a", "o", "#", "~", "+", "-", "*", "/", "%", "!", "=", "<", ">", ",", "|", "}", ")", "{"]
delim17 = ["`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" , '[', ']', 'c', 'n', "'", '"', '_']
delim18 = [" ", "+", "-", "*", "/", "%", ")", "<", ">", "=", "!", ",", "#", "~", "\n", "\0", "}", "|", "[", ']', ',']
delim19 = [" ", "+", "=", "!", ",", "#", "~", "|", ")", "}", "\n", "\0", ',', "]"]
delim20 = [" ", "`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", '"', 'c', 'n', "(", "_", "'", '[']
delim21 = [" ", "\n", "\0", "}", "|", "p", "h", "f", "s", "b" , "c", "i", "e", "i", "g", "t", "r", "n", "u", "a", "`", "#", "~"]
delim22 = ["|", "\n", "\0"]
delim23 = [" ", "+", "-", "*", "/", "%", ")", "(", "<", ">", "=", "!", ",", "#", "~", "\n", "\0", "}", "|", "[", "]"]
delim24 = [" ", "\n", "\0", "b", "c", "f", "h", "i", "p", "s", "t", "#", "~", "|" ]
delim25 = [" ", "=", "!", ",", "#", "~", "|", ")", "}", "\n", "\0", "COMMA", ']']
delim26 = [" ", "+", "-", "*", "/", "%", ")", "<", ">", "=", "!", ",", "#", "~", "\n", "\0", "}", "]", "|", "COMMA"]



class Lexer:
    def __init__(self, lexeme):         #local declarations inside the class
        self.lexeme = lexeme
        self.currentChar = lexeme[0]
        self.position = 0
        self.value_ = None
        self.type_ = None
        self.fullResult = None
        self.tokens = []
        self.IDcounter = 0
        self.tokensForUnknown = []
        self.lineCounter = 1

    def next(self):                     #character next function
        self.position += 1
        if self.position > len(self.lexeme) - 1:
            self.currentChar = '\0'
        else:
            self.currentChar = self.lexeme[self.position]

    def AToken(self):  # Tokens that start with A
        result = ""

        result += self.currentChar
        self.next()


        if self.currentChar == "d":  # advance token
            result += self.currentChar
            self.next()
            for char in "vance":
                if self.currentChar != char:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "advance"'
                result += self.currentChar
                self.next()
            if self.currentChar not in delim5:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim5])}'

            return "advance", result


        elif self.currentChar == "n":  # and token
            result += self.currentChar
            self.next()
            if self.currentChar == 'd':
                result += self.currentChar
                self.next()
                if self.currentChar not in delim4:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim4])}'

                return "and", result

            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "and"'

        else:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "and"'

    def BToken(self):  # Tokens that start with B
        result = ""

        for char in "bully":  # bully token
            if self.currentChar != char:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "bully"'
            result += self.currentChar
            self.next()
        if self.currentChar not in delim2:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim2])}'

        return "bully", result

    def CToken(self):  # Tokens that start with C
        result = ""

        result += self.currentChar # c
        self.next()

        if self.currentChar == "a":  # cap token
            result += self.currentChar # ca
            self.next()
            if self.currentChar == 'p':
                result += self.currentChar
                self.next()
                if self.currentChar not in delim6:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim6])}'

                return "cap", result

            if self.currentChar == 'r':
                result += self.currentChar
                self.next()
                if self.currentChar not in delim2:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim2])}'

                return "car", result

            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "cap", "car"'

        elif self.currentChar == 'h':  # checkif token
            result += self.currentChar
            self.next()
            if self.currentChar == 'e':
                result += self.currentChar
                self.next()
                for char in "ckif":
                    if self.currentChar != char:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "checkif'
                    result += self.currentChar
                    self.next()
                if self.currentChar not in delim1:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim1])}'

                return "checkif", result

            elif self.currentChar == 'i': # chill token
                result += self.currentChar
                self.next()
                for char in "ll":
                    if self.currentChar != char:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "chill"'
                    result += self.currentChar
                    self.next()
                if self.currentChar not in delim5:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim5])}'

                return "chill", result

            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "checkif", "chill"'

        else:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "cap", "car", "checkif", "chill"'

    def EToken(self):  # Tokens that start with E
        result = ""

        result += self.currentChar
        self.next()

        if self.currentChar == 'l':  # elsa token
            result += self.currentChar
            self.next()
            if self.currentChar == 's':
                result += self.currentChar
                self.next()
                if self.currentChar == 'a':
                    result += self.currentChar
                    self.next()
                    if self.currentChar not in delim3:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim3])}'
                    return "elsa", result

                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "elsa"'


            elif self.currentChar == 'i': # elib token
                result += self.currentChar
                self.next()
                if self.currentChar == 'b':
                    result += self.currentChar
                    self.next()
                    if self.currentChar not in delim1:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim1])}'

                    return "elib", result

                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "elib"'

            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "elib", "elsa"'

        else:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "elib", "elsa"'

    def FToken(self):  # Tokens that start with F
        result = ""

        for char in "flute":  # flute token
            if self.currentChar != char:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "flute"'
            result += self.currentChar
            self.next()
        if self.currentChar not in delim2:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim2])}'

        return "flute", result

    def GToken(self):  # Tokens that start with G
        result = ""

        for char in "goon":  # goon token
            if self.currentChar != char:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "goon"'
            result += self.currentChar
            self.next()
        if self.currentChar not in delim5:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim5])}'

        return "goon", result

    def HToken(self):  # Tokens that start with H
        result = ""

        for char in "hint":  # hint token
            if self.currentChar != char:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "hint"'
            result += self.currentChar
            self.next()
        if self.currentChar not in delim2:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim2])}'

        return "hint", result

    def IToken(self):  # Tokens that start with I
        result = ""

        result += self.currentChar
        self.next()

        if self.currentChar == 'f':
            result += self.currentChar
            self.next()
            if self.currentChar not in delim1:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim1])}'

            return "if", result

        if self.currentChar == 'n':
            result += self.currentChar
            self.next()
            if self.currentChar not in delim2:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim2])}'

            return "in", result


        else:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "if", "in"'

    def NToken(self):  # Tokens that start with N
        result = ""

        result += self.currentChar
        self.next()

        if self.currentChar == 'o':
            result += self.currentChar
            self.next()
            if self.currentChar == "c":  # nocap token
                result += self.currentChar
                self.next()
                for char in "ap":
                    if self.currentChar != char:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "nocap"'
                    result += self.currentChar
                    self.next()
                if self.currentChar not in delim6:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim6])}'

                return "nocap", result

            elif self.currentChar == "t":  # not token
                result += self.currentChar
                self.next()
                if self.currentChar not in delim1:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim1])}'

                return "not", result

            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "nocap", "not"'

        else:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "nocap", "not"'

    def OToken(self):  # Tokens that start with O
        result = ""

        for char in "or":  # or token
            if self.currentChar != char:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "or"'
            result += self.currentChar
            self.next()
        if self.currentChar not in delim4:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim4])}'

        return "or", result

    def PToken(self):  # Tokens that start with P
        result = ""

        result += self.currentChar
        self.next()

        if self.currentChar == 'i':  # pin token
            result += self.currentChar
            self.next()
            if self.currentChar == 'n':
                result += self.currentChar
                self.next()
                if self.currentChar not in delim1:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim1])}'

                return "pin", result
            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "pin"'

        elif self.currentChar == 'o':  # poor token
            result += self.currentChar
            self.next()
            if self.currentChar == 'o':
                result += self.currentChar
                self.next()
                if self.currentChar == 'r':
                    result += self.currentChar
                    self.next()
                    if self.currentChar not in delim2:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim2])}'

                    return "poor", result
                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "poor"'

            if self.currentChar == 'u':
                result += self.currentChar
                self.next()
                if self.currentChar == 't':
                    result += self.currentChar
                    self.next()
                    if self.currentChar not in delim1:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim1])}'

                    return "pout", result

                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "pout"'

            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "poor", "pout"'

        else:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "pin", "poor", "pout"'

    def RToken(self):                       # Tokens that start with R
        result = ""

        result += self.currentChar
        self.next()
        # result += self.currentChar
        # self.next()

        if self.currentChar == 'a':                  #range token
            result += self.currentChar
            self.next()
            for char in "nge":
                if self.currentChar != char:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "range"'
                result += self.currentChar
                self.next()
            if self.currentChar not in delim1:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim1])}'

            return "range", result

        elif self.currentChar == 'e':                 #remit token
            result += self.currentChar
            self.next()
            for char in "mit":
                if self.currentChar != char:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "remit"'
                result += self.currentChar
                self.next()
            if self.currentChar not in delim1:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim1])}'

            return "remit", result

        else:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "range", "remit"'

    def SToken(self):                       # Tokens that start with S
        result = ""

        for char in "star":                 #star token
            if self.currentChar != char:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "star"'
            result += self.currentChar
            self.next()
        if self.currentChar not in delim2:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim2])}'

        return "star", result

    def TToken(self):                       # Tokens that start with T
        result = ""

        for char in "task":                 #task token
            if self.currentChar != char:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "task"'
            result += self.currentChar
            self.next()
        if self.currentChar not in delim2:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim2])}'

        return "task", result

    def UToken(self):                       # Tokens that start with U
        result = ""

        for char in "universal":            #universal token
            if self.currentChar != char:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "universal"'
            result += self.currentChar
            self.next()
        if self.currentChar not in delim2:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim2])}'

        return "universal", result

    def RelationalToken(self):                 #Tokens for Relational Operators
        result = ""

        result += self.currentChar
        self.next()

        if result[0] == "<":                    #< token
            if self.currentChar == "=":
                result += self.currentChar
                self.next()
                if self.currentChar in delim11:  #<= token
                    return "<=", result
                else:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim11])}'
            if self.currentChar in delim11:
                return "<", result
            else:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim11])}'

        elif result[0] == ">":                  #> token
            if self.currentChar == "=":
                result += self.currentChar
                self.next()
                if self.currentChar in delim11:  #>= token
                    return ">=", result
                else:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim11])}'
            if self.currentChar in delim11:
                return ">", result
            else:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim11])}'

        elif result[0] == "=":                  #= token
            if self.currentChar == "=":
                result += self.currentChar
                self.next()

                if self.currentChar in delim10:  #== token
                    return "==", result
                else:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim10])}'
            if self.currentChar in delim7:    # = token
                return "=", result
            else:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim7])}'
        elif result[0] == "!":                  #!= token
            if self.currentChar == "=":
                result += self.currentChar
                self.next()

                if self.currentChar in delim10:
                    return "!=", result
                else:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim10])}'
            else:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected ⏵ "!="'

        return "UNKNOWN LEXEME ⏵", f'"{result}" \n ERROR: Incorrect Delimiter'

    def operatorToken(self):                    #Tokens for Arithmetic Operators
        result = ""

        if self.currentChar == "+":             #+ Token
            result += self.currentChar
            self.next()

            if self.currentChar in delim12:
                return "+", result

            if self.currentChar == "=":
                result += self.currentChar
                self.next()

                if self.currentChar in delim8:  #+= Token
                    return "+=", result
                else:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim8])}'

            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim12])}'

        elif self.currentChar == "-":           #- Token
            result += self.currentChar
            self.next()

            if self.currentChar in delim11:
                return "-", result

            if self.currentChar == "=":         #-= Token
                result += self.currentChar
                self.next()

                if self.currentChar in delim9:
                    return "-=", result
                else:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim9])}'

            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim11])}'

        elif self.currentChar == "*":
            result += self.currentChar
            self.next()

            if self.currentChar in delim11:      #*Token
                return "*", result

            if self.currentChar == "=":
                result += self.currentChar
                self.next()

                if self.currentChar in delim9:  #*= Token
                    return "*=", result
                else:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim9])}'

            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim11])}'

        elif self.currentChar == "/":
            result += self.currentChar
            self.next()

            if self.currentChar in delim11:      #/ Token
                return "/", result

            if self.currentChar == "=":
                result += self.currentChar
                self.next()

                if self.currentChar in delim9:  #/= Token
                    return "/=", result
                else:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim9])}'

            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim11])}'

        elif self.currentChar == "%":
            result += self.currentChar
            self.next()

            if self.currentChar in delim11:      #% Token
                return "%", result

            if self.currentChar == "=":
                result += self.currentChar
                self.next()

                if self.currentChar in delim9:  #%= Token
                    return "%=", result
                else:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim9])}'

            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim11])}'

        else:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "+", "-", "*", "/", "%", "+=", "-=", "*=", "/=", "%="'

    def SpecialToken(self):
        result = ""

        if self.currentChar == "{":         #{ Token
            result += self.currentChar
            self.next()

            if self.currentChar in delim13:
                return "{", result
            else:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim13])}'
        elif self.currentChar == "}":         #} Token
            result += self.currentChar
            self.next()

            if self.currentChar in delim14:
                return "}", result
            else:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim14])}'
        elif self.currentChar == "(":         #(Token
            result += self.currentChar
            self.next()

            if self.currentChar in delim15:
                return "(", result
            else:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim15])}'
        elif self.currentChar == ")":         #) Token
            result += self.currentChar
            self.next()

            if self.currentChar in delim16:
                return ")", result
            else:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim16])}'
        elif self.currentChar == "[":         #[Token
            result += self.currentChar
            self.next()

            if self.currentChar in delim17:
                return "[", result
            else:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim17])}'
        elif self.currentChar == "]":         #] Token
            result += self.currentChar
            self.next()

            if self.currentChar in delim18:
                return "]", result
            else:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim18])}'
        elif self.currentChar == "|":  # | Token
            result += self.currentChar
            self.next()

            if self.currentChar in delim24:
                return "|", result
            else:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim24])}'
        elif self.currentChar == "'":  # ' Token
            result += self.currentChar
            self.next()
            print(result, self.currentChar)
            if self.currentChar == "\0":
                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "\'\'"'
            if self.currentChar == "'":
                result += self.currentChar
                self.next()
                return "CARLIT", result
            result += self.currentChar
            self.next()
            print(result, self.currentChar)
            if self.currentChar == "'":
                result += self.currentChar
                self.next()
                print(result, self.currentChar)
                if self.currentChar in delim25:
                    return "CARLIT", result
                else:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim25])}'
            else:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "\'\'"'

        else:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \n ERROR: Incorrect Delimiter'

    def StringLitToken(self):               #Token for STARLIT
        result = ""

        if self.currentChar == '"':
            while True:
                result += self.currentChar
                self.next()

                if self.currentChar == '"':
                    result += self.currentChar
                    self.next()

                    if self.currentChar in delim19:
                        return "STARLIT", result
                    else:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim19])}'

                if self.currentChar == '\n' or self.currentChar == '\0':
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ (\" \")'

    def CommentToken(self):
        result = ""
        if self.currentChar == "~":
            print(14)
            result += self.currentChar
            self.next()

            while self.currentChar not in delim22:
                result += self.currentChar
                self.next()

                if self.currentChar == '\0':
                    break

            return "COMMENT", result

        elif self.currentChar == "#":
            result += self.currentChar

            while True:
                self.next()
                result += self.currentChar

                if self.currentChar == "#":
                    self.next()

                    if self.currentChar in delim21:
                        return "COMMENT", result
                    else:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim21])}'
                        #break

                elif self.currentChar == '\0':
                    print("1", result)
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "##"'

        else:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \nExpected ⏵ "##", "~"'

    def SeparatorToken(self):
        result = ""
        result += self.currentChar
        self.next()

        if self.currentChar in delim20:
            return "COMMA", result
        else:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim20])}'

    def digits(self):
        result = ""

        hintctr = 0  # checker of hint
        flutectr = 0  # checker of flute
        lead = 1  # checker of leading zeros

        if self.currentChar == "_":
            result += self.currentChar
            self.next()
            if self.currentChar == ".":
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected ⏵ "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"'
            while True:
                while self.currentChar in "0123456789" and self.currentChar != '\0':
                    if hintctr > 9 or flutectr > 9:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \n ERROR: Out of range'
                    result += self.currentChar
                    self.next()
                    hintctr += 1

                if self.currentChar == ".":
                    result += self.currentChar
                    self.next()
                    while self.currentChar in "0123456789" and self.currentChar != '\0':
                        if flutectr > 9:
                            return "UNKNOWN LEXEME ⏵", f'"{result}" \n ERROR: Out of range'
                        result += self.currentChar
                        self.next()
                        flutectr += 1

                        if self.currentChar == ".":
                            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim26])}'

                        if self.currentChar in delim26:  # 00.1
                            if len(result) > 2:
                                if result[1] == "0":
                                    while result[lead] not in delim26:
                                        if result[lead] in "123456789":
                                            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim26])}'
                                        if result[lead] == "0":
                                            lead += 1
                                        if result[lead] == ".":
                                            break

                            return "FLUTELIT", result

                    if flutectr == 0:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim26])}'

                elif self.currentChar in delim26:
                    if len(result) > 1:
                        if result[1] == "0":
                            if result[2] in "0123456789":
                                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim26])}'
                    elif len(result) == 1:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim26])}'
                    return "HINTLIT", result

                else:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"'

        elif self.currentChar in "0123456789":
            while True:
                while self.currentChar in "0123456789" and self.currentChar != '\0':
                    if hintctr > 9 or flutectr > 9:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim26])}'
                    result += self.currentChar
                    self.next()
                    hintctr += 1

                if self.currentChar == ".":
                    result += self.currentChar
                    self.next()

                    while self.currentChar in "0123456789" and self.currentChar != '\0':
                        if flutectr > 9:
                            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim26])}'
                        result += self.currentChar
                        self.next()
                        flutectr += 1
                        if self.currentChar == ".":
                            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim26])}'

                        if self.currentChar in delim26:
                            return "FLUTELIT", result

                    if flutectr == 0:
                        return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim26])}'

                elif self.currentChar in delim26:
                    if len(result) > 1:
                        if result[0] == "0":
                            if result[1] in "0123456789":
                                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim26])}'

                    return "HINTLIT", result

                else:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim26])}'
        else:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim26])}'

    def IdentifierToken(self):
        result = ""
        result += self.currentChar
        self.next()

        if self.currentChar in "abcdefghijklmnopqrstuvwxyz":
            result += self.currentChar
            self.next()

            while(self.currentChar in "abcdefghijklmnopqrstuvwxyz" or self.currentChar in "0123456789"):
                if self.currentChar == "`" or self.currentChar in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or not(len(result) <= 16)or self.currentChar in delim23:
                    return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim23])}'

                result += self.currentChar
                self.next()

                if self.currentChar == '\0':
                    break

            if self.currentChar in delim23:
                self.IDcounter += 1

                return f"IDENTIFIER{self.IDcounter}", result
            else:
                return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected Delimiter⏵ {", ".join([repr(x) for x in delim23])}'

        else:
            return "UNKNOWN LEXEME ⏵", f'"{result}" \n Expected ⏵ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"'

    def SpaceToken(self):
        result = ""
        result += self.currentChar
        self.next()

        if self.currentChar != " ":
            pass
        return "SPACE", "[ ]"

    def UnknownToken(self):
        result= ""
        result += self.currentChar
        self.next()

        return "UNKNOWN LEXEME ⏵", f'"{result}" \n ERROR: No Token'

    def getNextTokens(self):
        counter = 0
        error = "UNKNOWN LEXEME ⏵"

        while True:
            if counter >= len(self.lexeme):
                break

            if self.currentChar == "a":
                self.type_, self.value_ = self.AToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "b":
                self.type_, self.value_ = self.BToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "c":
                self.type_, self.value_ = self.CToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "e":
                self.type_, self.value_ = self.EToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "f":
                self.type_, self.value_ = self.FToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "g":
                self.type_, self.value_ = self.GToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "h":
                self.type_, self.value_ = self.HToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "i":
                self.type_, self.value_ = self.IToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "n":
                self.type_, self.value_ = self.NToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "o":
                self.type_, self.value_ = self.OToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "p":
                self.type_, self.value_ = self.PToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "r":
                self.type_, self.value_ = self.RToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "s":
                self.type_, self.value_ = self.SToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "t":
                self.type_, self.value_ = self.TToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar == "u":
                self.type_, self.value_ = self.UToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f"line #{self.lineCounter} : {self.type_} : {self.value_}")
                else:
                    self.tokens.append(f"{self.type_} : {self.value_}")
                continue

            elif self.currentChar in "<>!=":
                self.type_, self.value_ = self.RelationalToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f'line #{self.lineCounter} : {self.type_} : {self.value_}')
                else:
                    self.tokens.append(f'{self.type_} : {self.value_}')
                continue

            elif self.currentChar in "+-*/%":
                self.type_, self.value_ = self.operatorToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f'line #{self.lineCounter} : {self.type_} : {self.value_}')
                else:
                    self.tokens.append(f'{self.type_} : {self.value_}')
                continue

            elif self.currentChar in "([{}])|'":
                self.type_, self.value_ = self.SpecialToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f'line #{self.lineCounter} : {self.type_} : {self.value_}')
                else:
                    self.tokens.append(f'{self.type_} : {self.value_}')
                continue

            elif self.currentChar == '"':
                self.type_, self.value_ = self.StringLitToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f'line #{self.lineCounter} : {self.type_} : {self.value_}')
                else:
                    self.tokens.append(f'{self.type_} : {self.value_}')
                continue

            elif self.currentChar in "~#":
                self.type_, self.value_ = self.CommentToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f'line #{self.lineCounter} : {self.type_} : {self.value_}')
                else:
                    self.tokens.append(f'{self.type_} : {self.value_}')
                continue

            elif self.currentChar == ',':
                self.type_, self.value_ = self.SeparatorToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f'line #{self.lineCounter} : {self.type_} : {self.value_}')
                else:
                    self.tokens.append(f'{self.type_} : {self.value_}')
                continue

            elif '0' <= self.currentChar <= '9' or self.currentChar == "_":
                self.type_, self.value_ = self.digits()

                if self.type_ in error:
                    self.tokensForUnknown.append(f'line #{self.lineCounter} : {self.type_} : {self.value_}')
                else:
                    self.tokens.append(f'{self.type_} : {self.value_}')
                continue

            elif self.currentChar == '`':
                self.type_, self.value_ = self.IdentifierToken()

                if self.type_ in error:
                    self.tokensForUnknown.append(f'line #{self.lineCounter} : {self.type_} : {self.value_}')
                else:
                    self.tokens.append(f'{self.type_} : {self.value_}')
                continue

            elif self.currentChar == ' ':
                self.type_, self.value_ = self.SpaceToken()
                self.tokens.append(f'{self.type_} : {self.value_}')
                continue

            if self.currentChar == "\n":
                self.tokens.append(f'"NEWLINE" : "\\n"')
                self.lineCounter += 1
                self.next()
                continue

            if self.currentChar == "\t":
                self.tokens.append(f'"TAB" : "\\t"')
                self.lineCounter += 1
                self.next()
                continue

            elif self.currentChar in unknownCharacters or self.currentChar == ".":
                self.type_, self.value_ = self.UnknownToken()
                self.tokensForUnknown.append(f'line #{self.lineCounter} : {self.type_} : {self.value_}')
                continue

            counter += 1

def main():
    while True:
        lexeme = input("Enter lexeme: ")
        lexer = Lexer(lexeme)
        print("Token: Lexeme")
        lexer.getNextTokens()
        print(lexer.tokens)
        print(lexer.tokensForUnknown)
        if lexeme == "|":
            break


if __name__ == "__main__":
    main()













