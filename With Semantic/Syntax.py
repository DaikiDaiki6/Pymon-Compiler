class Syn:
    def __init__(self, LexemeTokens):
        self.LexemeTokens = LexemeTokens
        self.DictLexemeTokens = {}
        self.Terminals = []  # Initialize self.Terminals as an empty list
        self.currentTerminal = None  # Initialize currentTerminal as None
        self.position = 0
        self.currentkeys = None
        self.currentvalues = None
        self.SyntaxErrors = []
        self.lineCounter = 1
        self.SemanticSequence = []
        self.keys = []
        self.values = []

    def ListToDict(self):  # splitting all the whitespaces terminals and putting on dictionaries
        for item in self.LexemeTokens:
            key, value = item.split(" : ", 1)
            if key in ['SPACE', 'COMMENT'] or value == '"\\t"':
                pass
            else:
                self.DictLexemeTokens[key] = value
                self.Terminals.append({key: value})  # Append dictionary to self.Terminals
        self.currentTerminal = self.Terminals[0]
        self.keys = list(self.currentTerminal.keys())
        self.values = list(self.currentTerminal.values())
        self.currentkeys = self.keys[0]
        self.currentvalues = self.values[0]

    def next(self):  # character next function
        self.position += 1
        if self.position >= len(self.Terminals):  # Adjust the condition here
            self.currentTerminal = '\0'
        else:
            self.currentTerminal = self.Terminals[self.position]
            self.keys = list(self.currentTerminal.keys())
            self.values = list(self.currentTerminal.values())
            self.currentkeys = self.keys[0]
            self.currentvalues = self.values[0]
            if self.currentkeys == '"NEWLINE"':
                self.lineCounter += 1
                self.next()

    def prev(self):  # character prev function
        self.position -= 1
        if self.position < 0:
            self.currentTerminal = '\0'
        else:
            self.currentTerminal = self.Terminals[self.position]
            self.keys = list(self.currentTerminal.keys())
            self.values = list(self.currentTerminal.values())
            self.currentkeys = self.keys[0]
            self.currentvalues = self.values[0]
            if self.currentkeys == '"NEWLINE"':
                self.lineCounter -= 1
                self.prev()

    # =====================================The STRUCTURE CODE============================================================#

    def TProg_start(self):  # <program>
        if self.currentkeys == '|':
            self.SemanticSequence.insert(len(self.SemanticSequence),{"<Prog_start+>": self.position})
            self.next()  # Expected: self.currentkeys = first set of <declaration> and <body>
            if self.currentkeys in ['hint', 'flute', 'star', 'bully', 'car', 'pout', 'if', 'poor', 'checkif',
                                    'task', '|'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "hint", "flute", "star", "bully", "car", "pout", "if", "poor", "checkif", "task", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI
        else:
            print("SYNTAX ERROR 1.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "|"')  # put error in a list for viewing in GUI

    def TProg_end(self):  # <program>
        self.next()  # Expected: self.currentkeys = NULL
        if self.position == len(self.Terminals) and self.currentkeys == '|':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<Program->": self.position-1})
        else:
            print("SYNTAX ERROR 2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "NULL"')  # put error in a list for viewing in GUI

    def Tdeclaration(self):  # <declaration>
        if self.currentkeys in ['hint', 'flute', 'star', 'bully', 'car']:
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<declaration+>": self.position})
            self.Tdata_type()
            self.Tid_or_array()
            self.Tdeclare_and_initialize()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<declaration->": self.position - 1})
            self.Tdeclaration()
            if self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task', '|', 'universal', 'hint', 'flute', 'star',
                                    'car', 'bully', 'advance', '}', 'remit'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 3: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "}}", "remit", "IDENTIFIER"')  # put error in a list for viewing in GUI
        elif self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task', '|', 'universal', 'hint', 'flute',
                                  'star', 'car', 'bully', 'advance', '}', 'remit'] or 'IDENTIFIER' in self.currentkeys:
            pass # NULL <declaration>
        else:
            print("SYNTAX ERROR 3.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "hint", "flute", "star", "bully", "car", "pout", "if", "poor", "checkif", "task", "|", "universal", "advance", "}}", "remit", "IDENTIFIER"')  # put error in a list for viewing in GUI

    def Tdata_type(self):  # <data type>
        self.SemanticSequence.insert(len(self.SemanticSequence), {"<data type>": self.position})
        if self.currentkeys in ['hint', 'flute', 'star', 'bully', 'car']:
            self.next()  # Expected: self.currentkeys = follow set <data type>
            if 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 4: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "IDENTIFIER"')  # put error in a list for viewing in GUI
        else:
            print("SYNTAX ERROR 4.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "hint", "flute", "star", "bully", "car"')  # put error in a list for viewing in GUI

    def Tid_or_array(self):  # <id or array>
        self.SemanticSequence.insert(len(self.SemanticSequence), {"<id or array+>": self.position})
        if 'IDENTIFIER' in self.currentkeys:
            self.Tid()
            self.Tindex()
            if self.currentkeys in ['=', 'pout', 'if', 'poor', 'checkif', 'task', '|', 'universal',
                                    'hint', 'flute', 'star', 'car', 'bully', 'advance', 'remit', ']', 'COMMA', ')', '+',
                                    '-', '*', '/', '%', 'chill', 'goon', '}', '<', '>', '<=', '>=', '==', '!=', 'and',
                                    'or',
                                    '+=', '-=', '*=', '/=', '%='] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<id or array->": self.position-1})
            else:
                print("SYNTAX ERROR 5: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "=", "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "]", "COMMA", ")", "+", "-", "*", "/", "%", "chill", "goon", "}}", "<", ">", "<=", ">=", "==", "!=", "and", "or", "+=", "-=", "*=", "/=", "%=", "IDENTIFIER"')  # put error in a list for viewing in GUI
        else:
            print("SYNTAX ERROR 5.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "IDENTIFIER"')  # put error in a list for viewing in GUI

    def Tid(self):  # <id>
        self.SemanticSequence.insert(len(self.SemanticSequence), {"<id>": self.position})
        if 'IDENTIFIER' in self.currentkeys:
            self.next()  # Expected: self.currentkeys = follow set <id>
            if (self.currentkeys in ['[', '=', 'pout', 'if', 'poor', 'checkif', 'task', '|', 'universal', 'hint',
                                     'flute', 'star', 'car', 'bully', 'advance', 'remit', ']', 'COMMA', ')', '+', '-',
                                     '*', '/', '%', 'chill', 'goon', '}', '<', '>', '<=', '>=', '==', '!=', 'and', 'or',
                                     '+=', '-=', '*=', '/=', '%=', '(', 'in'] or 'IDENTIFIER' in self.currentkeys):
                pass
            else:
                print("SYNTAX ERROR 6: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "[", "=", "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "]", "COMMA", ")", "+", "-", "*", "/", "%", "chill", "goon", "}}", "<", ">", "<=", ">=", "==", "!=", "and", "or", "+=", "-=", "*=", "/=", "%=", "IDENTIFIER"')  # put error in a list for viewing in GUI
        else:
            print("SYNTAX ERROR 6.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "IDENTIFIER"')  # put error in a list for viewing in GUI

    def Tindex(self):  # <index>
        if self.currentkeys == '[':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<index+>": self.position})
            self.next()  # Expected: self.currentkeys = first set <hint or id value>
            self.Thint_or_id_value()
            if self.currentkeys == ']':
                self.next()  # Expected: self.currentkeys = first set <2d array> or follow set <index>
                if (self.currentkeys in ['=', 'pout', 'if', 'poor', 'checkif', 'task', '|', 'universal', 'hint',
                                         'flute', 'star', 'car', 'bully', 'advance', 'remit', ']', 'COMMA', ')', '+',
                                         '-', '*', '/', '%', 'chill', 'goon', '}', '<', '>', '<=', '>=', '==', '!=',
                                         'and', 'or', '+=', '-=', '*=', '/=',
                                         '%='] or 'IDENTIFIER' in self.currentkeys):
                    self.SemanticSequence.insert(len(self.SemanticSequence), {"<index->": self.position-1})
                else:
                    print("SYNTAX ERROR 7: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "=", "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "]", "COMMA", ")", "+", "-", "*", "/", "%", "chill", "goon", "}}", "<", ">", "<=", ">=", "==", "!=", "and", "or", "+=", "-=", "*=", "/=", "%=", "IDENTIFIER"')  # put error in a list for viewing in GUI
            else:
                print("SYNTAX ERROR 7.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "]"')  # put error in a list for viewing in GUI
        elif (self.currentkeys in ['=', 'pout', 'if', 'poor', 'checkif', 'task', '|', 'universal', 'hint',
                                   'flute', 'star', 'car', 'bully', 'advance', 'remit', ']', 'COMMA', ')', '+',
                                   '-', '*', '/', '%', 'chill', 'goon', '}', '<', '>', '<=', '>=', '==', '!=',
                                   'and', 'or', '+=', '-=', '*=', '/=',
                                   '%='] or 'IDENTIFIER' in self.currentkeys):
            pass  # NULL <index>
        else:
            print("SYNTAX ERROR 7.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "[", "=", "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "]", "COMMA", ")", "+", "-", "*", "/", "%", "chill", "goon", "}}", "<", ">", "<=", ">=", "==", "!=", "and", "or", "+=", "-=", "*=", "/=", "%=", "IDENTIFIER"')  # put error in a list for viewing in GUI

    def Thint_or_id_value(self):  # <hint or id value>
        if self.currentkeys == 'HINTLIT':
            self.next()  # Expected: self.currentkeys = follow set <hint or id value>
            if self.currentkeys in [']', 'COMMA', ')']:
                pass
            else:
                print("SYNTAX ERROR 8: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "]", "COMMA", ")"')  # put error in a list for viewing in GUI
        elif "IDENTIFIER" in self.currentkeys:
            self.Tid_or_array()
            if self.currentkeys in [']', 'COMMA', ')']:
                pass
            else:
                print("SYNTAX ERROR 8.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "]", "COMMA", ")"')  # put error in a list for viewing in GUI
        else:
            print("SYNTAX ERROR 8.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "HINTLIT", "IDENTIFIER"')  # put error in a list for viewing in GUI

    def Tdeclare_and_initialize(self):  # <declare and initialize>
        if self.currentkeys == '=':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<assignment operator>": self.position})
            self.next()  # Expected: self.currentkeys = first set <allowed value>
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<allowed value+>": self.position})
            self.Tallowed_value()
            if (self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task', '|', 'universal', 'hint', 'flute', 'star',
                                     'car', 'bully', 'advance', 'remit', '}'] or 'IDENTIFIER' in self.currentkeys):
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<allowed value->": self.position-1})
            else:
                print("SYNTAX ERROR 10: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI
        elif (self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task', '|', 'universal', 'hint', 'flute', 'star',
                                   'car', 'bully', 'advance', 'remit', '}'] or 'IDENTIFIER' in self.currentkeys):
            pass
        else:
            print("SYNTAX ERROR 10.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "=", "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI

    def Tallowed_value(self):  # <allowed value>
        if self.currentkeys == 'pin':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<input+>": self.position})
            self.next()  # Expected: self.currentkeys = first set <parameter>
            if self.currentkeys == '(':
                self.next()  # Expected: self.currentkeys = first set <return value>
                self.Treturn_value()
                if self.currentkeys == ')':
                    self.next()  # Expected: self.currentkeys = follow set <allowed value>
                    if (self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task', '|', 'universal', 'hint', 'flute',
                                             'star', 'car', 'bully', 'advance', 'remit', 'chill',
                                             'goon', '}'] or 'IDENTIFIER' in self.currentkeys):
                        self.SemanticSequence.insert(len(self.SemanticSequence), {"<input->": self.position-1})
                    else:
                        print("SYNTAX ERROR 11: Unexpected", self.currentvalues, self.lineCounter)
                        self.SyntaxErrors.append(
                            f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI
                else:
                    print("SYNTAX ERROR 11.1: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI
            else:
                print("SYNTAX ERROR 11.2: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "("')  # put error in a list for viewing in GUI
        elif self.currentkeys == '[':
            self.Tarray_value()
            if (self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task', '|', 'universal', 'hint', 'flute',
                                     'star', 'car', 'bully', 'advance', 'remit', 'chill',
                                     'goon', '}'] or 'IDENTIFIER' in self.currentkeys):
                pass
            else:
                print("SYNTAX ERROR 11.3: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", "}}",  "IDENTIFIER"')  # put error in a list for viewing in GUI
        elif self.currentkeys == 'CARLIT':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<carlit>": self.position})
            self.next()  # Expected: self.currentkeys = follow set <allowed value>
            if (self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task', '|', 'universal', 'hint', 'flute',
                                     'star', 'car', 'bully', 'advance', 'remit', 'chill',
                                     'goon', '}'] or 'IDENTIFIER' in self.currentkeys):
                pass
            else:
                print("SYNTAX ERROR 11.4: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", "}}",  "IDENTIFIER"')  # put error in a list for viewing in GUI
        elif self.currentkeys in ['cap', 'nocap']:
            self.Tbully_value()
            if (self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task', '|', 'universal', 'hint', 'flute',
                                     'star', 'car', 'bully', 'advance', 'remit', 'chill',
                                     'goon', '}'] or 'IDENTIFIER' in self.currentkeys):
                pass
            else:
                print("SYNTAX ERROR 11.5: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", "}}",  "IDENTIFIER"')  # put error in a list for viewing in GUI
        elif self.currentkeys in ['(', 'FLUTELIT', 'HINTLIT', 'STARLIT'] or 'IDENTIFIER' in self.currentkeys:
            self.Tmath_expression()
            if (self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task', '|', 'universal', 'hint', 'flute',
                                     'star', 'car', 'bully', 'advance', 'remit', 'chill',
                                     'goon', '}'] or 'IDENTIFIER' in self.currentkeys):
                pass
            else:
                print("SYNTAX ERROR 11.6: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", "}}",  "IDENTIFIER"')  # put error in a list for viewing in GUI
        else:
            print("SYNTAX ERROR 11.7: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pin", "[", "CARLIT", "cap", "nocap", "(", "HINTLIT", "FLUTELIT", "STARLIT", "IDENTIFIER"')  # put error in a list for viewing in GUI
        if "NEWLINE" in self.currentkeys:
            self.lineCounter += 1
            self.next()

    def Treturn_value(self):
        if (self.currentkeys in ['[', 'CARLIT', 'cap', 'nocap', '(', 'HINTLIT', 'FLUTELIT',
                                 'STARLIT'] or 'IDENTIFIER' in self.currentkeys):
            self.Tdata_value()
            if self.currentkeys == ')':
                pass
            else:
                print("SYNTAX ERROR 12: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI
        elif self.currentkeys == ')':
            pass  # NULL <return value>
        else:
            print("SYNTAX ERROR 12.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pin", "[", "CARLIT", "cap", "nocap", "(", "HINTLIT", "FLUTELIT", "STARLIT", "IDENTIFIER", ")"')  # put error in a list for viewing in GUI

    def Tdata_value(self):
        if self.currentkeys in ['FLUTELIT', 'HINTLIT', 'STARLIT', 'CARLIT', 'cap',
                                '(','nocap'] or 'IDENTIFIER' in self.currentkeys:
            self.Tdata_value_no_array()
            if self.currentkeys in [')', 'COMMA', ']']:
                pass
            else:
                print("SYNTAX ERROR 13: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "COMMA", "]"')  # put error in a list for viewing in GUI
        elif self.currentkeys == '[':
            self.Tarray_value()
            if self.currentkeys in [')', 'COMMA', ']']:
                pass
            else:
                print("SYNTAX ERROR 13.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "COMMA", "]"')  # put error in a list for viewing in GUI
        else:
            print("SYNTAX ERROR 13.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "FLUTELIT", "HINTLIT", "STARLIT", "CARLIT", "cap", "nocap", "IDENTIFIER", "["')  # put error in a list for viewing in GUI

    def Tdata_value_no_array(self):
        if self.currentkeys in ['cap', 'nocap']:
            self.Tbully_value()
            if (self.currentkeys in [')', 'COMMA', ']', '<', '>', '<=', '>=', '==', '!=', 'and', 'or']):
                pass
            else:
                print("SYNTAX ERROR 14: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "COMMA", "]", "<", ">", "<=", ">=", "==", "!=", "and", "or"')  # put error in a list for viewing in GUI
        elif self.currentkeys == 'CARLIT':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<carlit+>": self.position})
            self.next()  # Expected: self.currentkeys = follow set <data value no array>
            if (self.currentkeys in [')', 'COMMA', ']', '<', '>', '<=', '>=', '==', '!=', 'and', 'or']):
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<carlit->": self.position-1})
            else:
                print("SYNTAX ERROR 14.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "COMMA", "]", "<", ">", "<=", ">=", "==", "!=", "and", "or"')  # put error in a list for viewing in GUI
        elif self.currentkeys in ['(', 'FLUTELIT', 'HINTLIT', 'STARLIT'] or 'IDENTIFIER' in self.currentkeys:
            self.Tmath_expression()
            if (self.currentkeys in [')', 'COMMA', ']', '<', '>', '<=', '>=', '==', '!=', 'and', 'or']):
                pass
            else:
                print("SYNTAX ERROR 14.2: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "COMMA", "]", "<", ">", "<=", ">=", "==", "!=", "and", "or"')  # put error in a list for viewing in GUI
        else:
            print("SYNTAX ERROR 14.3: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "cap", "nocap", "CARLIT", "(", "FLUTELIT", "HINTLIT", "STARLIT", "IDENTIFIER"')  # put error in a list for viewing in GUI

    def Tbully_value(self):
        if self.currentkeys in ['cap', 'nocap']:
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<bully value>": self.position})
            self.next()  # Expected: self.currentkeys = follow set <bully value>
            if (self.currentkeys in [')', 'COMMA', ']', '==', '!=', 'and', 'or', 'hint', 'star', 'car', 'bully',
                                     'flute', '}', '|', 'pout', 'if', 'poor', 'checkif', 'task', 'advance', 'chill',
                                     'goon'] or 'IDENTIFIER' in self.currentkeys):
                pass
            else:
                print("SYNTAX ERROR 15: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "COMMA", "]", "==", "!=", "and", "or", "hint", "star", "car", "bully", "flute", "}}", "|", "pout", "if", "poor", "checkif", "task", "advance", "chill", "goon", "IDENTIFIER"')  # put error in a list for viewing in GUI

        else:
            print("SYNTAX ERROR 15.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "cap", "nocap"')  # put error in a list for viewing in GUI

    def Tmath_expression(self):
        self.SemanticSequence.insert(len(self.SemanticSequence), {"<math expression+>": self.position})
        if self.currentkeys == '(':
            self.next()  # Expected: self.currentkeys = first set <math expression>
            self.Tmath_expression()
            if self.currentkeys == ')':
                self.next()  # Expected: self.currentkeys = first set <arithmetic tail> or follow set <math expression>
                self.Tarithmetic_tail()
                if (self.currentkeys in [')', 'pout', 'if', 'poor', 'checkif', 'task', '|', 'universal',
                                         'hint', 'flute', 'star', 'car', 'bully', 'advance', 'remit', 'chill', 'goon',
                                         'COMMA', ']', '<', '>', '<=', '>=', '==', '!=', 'and', 'or',
                                         '}'] or 'IDENTIFIER' in self.currentkeys):
                    self.SemanticSequence.insert(len(self.SemanticSequence), {"<math expression->": self.position-1})
                else:
                    print("SYNTAX ERROR 16: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", "COMMA", "]", "<", ">", "<=", ">=", "==", "!=", "and", "or", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI
            else:
                print("SYNTAX ERROR 16.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI
        elif self.currentkeys in ['HINTLIT', 'FLUTELIT']:
            self.Tnumber_value()
            self.Tarithmetic_tail()
            if (self.currentkeys in [')', 'pout', 'if', 'poor', 'checkif', 'task', '|', 'universal',
                                     'hint', 'flute', 'star', 'car', 'bully', 'advance', 'remit', 'chill', 'goon',
                                     'COMMA', ']', '<', '>', '<=', '>=', '==', '!=', 'and',
                                     'or', '}'] or 'IDENTIFIER' in self.currentkeys):
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<math expression->": self.position-1})
            else:
                print("SYNTAX ERROR 16.2: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", "COMMA", "]", "<", ">", "<=", ">=", "==", "!=", "and", "or", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI
        elif self.currentkeys == 'STARLIT':
            self.next()  # Expected: self.currentkeys = first set <arithmetic tail> or follow set <math expression>
            if self.currentkeys == '+':
                self.Tarithmetic_tail()
                if (self.currentkeys in [')', 'pout', 'if', 'poor', 'checkif', 'task', '|', 'universal',
                                         'hint', 'flute', 'star', 'car', 'bully', 'advance', 'remit', 'chill', 'goon',
                                         'COMMA', ']', '==', '!=', 'and',
                                         'or', '}'] or 'IDENTIFIER' in self.currentkeys):
                    self.SemanticSequence.insert(len(self.SemanticSequence), {"<math expression->": self.position-1})
                else:
                    print("SYNTAX ERROR 16.3: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", "COMMA", "]", "==", "!=", "and", "or", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI
            elif (self.currentkeys in [')', 'pout', 'if', 'poor', 'checkif', 'task', '|', 'universal',
                                       'hint', 'flute', 'star', 'car', 'bully', 'advance', 'remit', 'chill', 'goon',
                                       'COMMA', ']', '==', '!=', 'and',
                                       'or', '}'] or 'IDENTIFIER' in self.currentkeys):
                    self.SemanticSequence.insert(len(self.SemanticSequence), {"<math expression->": self.position-1})
            else:
                print("SYNTAX ERROR 16.3: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", "COMMA", "]", "==", "!=", "and", "or", "}}", "IDENTIFIER", "+"')  # put error in a list for viewing in GUI

        elif 'IDENTIFIER' in self.currentkeys:
            self.Tid_or_array()
            self.Tarithmetic_tail()
            if (self.currentkeys in [')', 'pout', 'if', 'poor', 'checkif', 'task', '|', 'universal',
                                     'hint', 'flute', 'star', 'car', 'bully', 'advance', 'remit', 'chill', 'goon',
                                     'COMMA', ']', '<', '>', '<=', '>=', '==', '!=', 'and',
                                     'or', '}'] or 'IDENTIFIER' in self.currentkeys):
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<math expression->": self.position-1})
            else:
                print("SYNTAX ERROR 16.4: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", "COMMA", "]", "<", ">", "<=", ">=", "==", "!=", "and", "or", "}}" "IDENTIFIER"')  # put error in a list for viewing in GUI
        else:
            print("SYNTAX ERROR 16.5: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "(", "HINTLIT", "FLUTELIT", "STARLIT", "IDENTIFIER"')  # put error in a list for viewing in GUI

    def Tarithmetic_tail(self):
        if self.currentkeys in ['+', '-', '*', '/', '%']:
            self.Tarithmetic()
            self.Tmath_expression()
            if (self.currentkeys in [')', 'pout', 'if', 'poor', 'checkif', 'task', '|', 'universal',
                                     'hint', 'flute', 'star', 'car', 'bully', 'advance', 'remit', 'chill', 'goon',
                                     'COMMA', ']', '<', '>', '<=', '>=', '==', '!=', 'and',
                                     'or', '}'] or 'IDENTIFIER' in self.currentkeys):
                pass
            else:
                print("SYNTAX ERROR 17: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", "COMMA", "]", "<", ">", "<=", ">=", "==", "!=", "and", "or", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI
        elif (self.currentkeys in [')', 'pout', 'if', 'poor', 'checkif', 'task', '|', 'universal',
                                   'hint', 'flute', 'star', 'car', 'bully', 'advance', 'remit', 'chill', 'goon',
                                   'COMMA', ']', '<', '>', '<=', '>=', '==', '!=', 'and',
                                   'or', '}'] or 'IDENTIFIER' in self.currentkeys):
            pass  # NULL <arithmetic tail>
        else:
            print("SYNTAX ERROR 17.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "+", "-", "*", "/", "%", ")", "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", "COMMA", "]", "<", ">", "<=", ">=", "==", "!=", "and", "or", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI

    def Tarithmetic(self):
        if self.currentkeys in ['+', '-', '*', '/', '%']:
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<arithmetic>": self.position})
            self.next()  # Expected: self.currentkeys = follow set <arithmetic>
            if self.currentkeys in ['(', 'HINTLIT', 'FLUTELIT', 'STARLIT'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 17.2: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "(", "HINTLIT", "FLUTELIT", "STARLIT", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 17.3: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "+", "-", "*", "/", "%"')  # put error in a list for viewing in GUI:

    def Tnumber_value(self):
        if self.currentkeys in ['FLUTELIT', 'HINTLIT']:
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<number value>": self.position})
            self.next()  # Expected: self.currentkeys = follow set <number value>
            if self.currentkeys in ['+', '-', '*', '/', '%', ')', 'pout', 'if', 'poor', 'checkif', 'task',
                                    '|', 'universal', 'hint', 'flute', 'star', 'car', 'bully', 'advance', 'remit',
                                    'chill', 'goon', 'COMMA', ']', '<', '>', '<=', '>=', '==', '!=', 'and', 'or',
                                    '}'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 18: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "+", "-", "*", "/", "%", ")", "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", "COMMA", "]", "<", ">", "<=", ">=", "==", "!=", "and", "or", "IDENTIFIER", "}}"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 18.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "FLUTELIT", "HINTLIT"')  # put error in a list for viewing in GUI:

    def Tarray_value(self):
        if self.currentkeys == '[':
            self.next()  # Expected: self.currentkeys = first set <parameter values>
            self.Tarray_parameter_values()
            if self.currentkeys == ']':
                self.next()  # Expected: self.currentkeys = follow set <array value>
                if self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task', '|', 'universal', 'hint',
                                        'flute', 'star', 'car', 'bully', 'advance', 'remit', 'chill', 'goon', ')',
                                        'COMMA', ']', '}'] or 'IDENTIFIER' in self.currentkeys:
                    pass
                else:
                    print("SYNTAX ERROR 19: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "task", "|", "universal", "hint", "flute", "star", "car", "bully", "advance", "remit", "chill", "goon", ")", "COMMA", "]", "IDENTIFIER"')  # put error in a list for viewing in GUI:
            else:
                print("SYNTAX ERROR 19.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "]"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 19.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "["')  # put error in a list for viewing in GUI:

    def Tarray_parameter_values(self):
        if self.currentkeys in ['[', 'cap', 'nocap', 'CARLIT', 'STARLIT', 'HINTLIT',
                                'FLUTELIT'] or 'IDENTIFIER' in self.currentkeys:
            self.Tarray_data_value()
            self.Tarray_parameter_tail()
            if self.currentkeys == ']':
                pass
            else:
                print("SYNTAX ERROR 20: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "]"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 20.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "[", "cap", "nocap", "CARLIT", "STARLIT", "HINTLIT", "FLUTELIT"')  # put error in a list for viewing in GUI:

    def Tarray_data_value(self):
        if self.currentkeys in ['cap', 'nocap', 'CARLIT', 'STARLIT', 'HINTLIT', 'FLUTELIT'] or 'IDENTIFIER' in self.currentkeys:
            self.Tdata_value()
            if self.currentkeys in ['COMMA', ']']:
                pass
            else:
                print("SYNTAX ERROR 21: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "COMMA", "]"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 21.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "cap", "nocap", "CARLIT", "STARLIT", "HINTLIT", "FLUTELIT", "IDENTIFIER", "["')  # put error in a list for viewing in GUI:

    def Tdata_value_tail(self):
        if self.currentkeys == 'COMMA':
            self.next()
            self.Tdata_value_no_array()
            self.Tdata_value_tail()
            if self.currentkeys == ']':
                pass
            else:
                print("SYNTAX ERROR 23: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "]"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == ']':
            pass  # NULL <data value tail>
        else:
            print("SYNTAX ERROR 23.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "COMMA", "]"')  # put error in a list for viewing in GUI:

    def Tarray_parameter_tail(self):
        if self.currentkeys == 'COMMA':
            self.next()
            self.Tarray_data_value()
            self.Tarray_parameter_tail()
            if self.currentkeys == ']':
                pass
            else:
                print("SYNTAX ERROR 24: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "]"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == ']':
            pass  # NULL <array parameter tail>
        else:
            print("SYNTAX ERROR 24.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "COMMA", "]"')  # put error in a list for viewing in GUI:

    def Tbody(self):
        if self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task'] or 'IDENTIFIER' in self.currentkeys:
            self.Tstatement()
            if self.currentkeys == '|':
                pass
            else:
                print("SYNTAX ERROR 25: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ |')  # put error in a list for viewing in GUI:
        elif self.currentkeys == '|':
            pass  # NULL <body>
        else:
            print("SYNTAX ERROR 25.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "task", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tstatement(self):
        if self.currentkeys in ['pout', 'if', 'poor', 'checkif'] or 'IDENTIFIER' in self.currentkeys:
            self.Tbody_no_task()
            self.Tstatement()
            if self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task', '|'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 26: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "task", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == 'task':
            self.Tfunction()
            self.Tstatement()
            if self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task', '|'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 26.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "task", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task', '|'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <statement>
        else:
            print("SYNTAX ERROR 26.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "IDENTIFIER", "task", "|"')  # put error in a list for viewing in GUI:

    def Tbody_no_task(self):
        if self.currentkeys in ['pout', 'poor', 'checkif'] or 'IDENTIFIER' in self.currentkeys:
            self.Tbody_no_if_task()
            if self.currentkeys in ['advance', 'pout', 'if', 'poor', 'checkif', 'task',
                                    '}', '|'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 27: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "advance", "pout", "if", "poor", "checkif", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == 'if':
            self.Tcondition_statement()
            if self.currentkeys in ['advance', 'pout', 'if', 'poor', 'checkif', 'task',
                                    '}', '|'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 27.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "advance", "pout", "if", "poor", "checkif", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['advance', 'pout', 'if', 'poor', 'checkif', 'task',
                                  '}', '|'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <body no task>
        else:
            print("SYNTAX ERROR 27.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "advance", "pout", "if", "poor", "checkif", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tbody_no_if_task(self):
        if self.currentkeys == 'pout' or 'IDENTIFIER' in self.currentkeys:
            if self.currentkeys == 'pout':
                self.Tbody_no_if_loop_task()
                if self.currentkeys in ['if', 'advance', 'chill', 'goon', 'pout', 'poor', 'checkif', 'task',
                                        '}', '|'] or 'IDENTIFIER' in self.currentkeys:
                    pass
            elif 'IDENTIFIER' in self.currentkeys:
                self.next()  # Expected: self.currentkeys = '(' if in <function call statement>
                if self.currentkeys == '(':
                    self.prev()
                    self.Tfunction_call_statement()
                    if self.currentkeys in ['if', 'advance', 'chill', 'goon', 'pout', 'poor', 'checkif', 'task',
                                            '}', '|'] or 'IDENTIFIER' in self.currentkeys:
                        pass
                    else:
                        print("SYNTAX ERROR 29: Unexpected", self.currentvalues, self.lineCounter)
                        self.SyntaxErrors.append(
                            f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "chill", "goon", "|", "pout", "task", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
                else:
                    self.prev()  # if IDENTIFIER but not for <function call statement>
                    self.Tbody_no_if_loop_task()
                    if self.currentkeys in ['if', 'advance', 'chill', 'goon', 'pout', 'poor', 'checkif', 'task',
                                            '}', '|'] or 'IDENTIFIER' in self.currentkeys:
                        pass
                    else:
                        print("SYNTAX ERROR 29.1: Unexpected", self.currentvalues, self.lineCounter)
                        self.SyntaxErrors.append(
                            f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "chill", "goon", "|", "pout", "task", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:

            else:
                print("SYNTAX ERROR 28: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "advance", "chill", "goon", "pout", "poor", "checkif", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['poor', 'checkif']:
            self.Tloop_statement()
            if self.currentkeys in ['if', 'advance', 'chill', 'goon', 'pout', 'poor', 'checkif', 'task',
                                    '}', '|'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 28.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "advance", "chill", "goon", "pout", "poor", "checkif", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['if', 'advance', 'chill', 'goon', 'pout', 'poor', 'checkif', 'task',
                                  '}', '|'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <body no if-task>
        else:
            print("SYNTAX ERROR 28.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "advance", "chill", "goon", "pout", "poor", "checkif", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tbody_no_if_loop_task(self):
        if 'IDENTIFIER' in self.currentkeys:
            self.Tinitialization_statement()
            if self.currentkeys in ['if', 'poor', 'checkif', 'advance', 'remit', 'chill', 'goon', '|',
                                    'pout', 'task', '}'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 29.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "chill", "goon", "|", "pout", "task", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == 'pout':
            self.Toutput_statement()
            if self.currentkeys in ['if', 'poor', 'checkif', 'advance', 'remit', 'chill', 'goon', '|',
                                    'pout', 'task', '}'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 29.2: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "chill", "goon", "|", "pout", "task", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        if self.currentkeys in ['if', 'poor', 'checkif', 'advance', 'remit', 'chill', 'goon', '|',
                                'pout', 'task', '}'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <body no if-loop-task>
        else:
            print("SYNTAX ERROR 29.3: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "chill", "goon", "|", "pout", "task", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tfunction_call_statement(self):
        if 'IDENTIFIER' in self.currentkeys:
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function call statement+>": self.position})
            self.Tid()
            self.Tparameter()
            if self.currentkeys in ['if', 'poor', 'checkif', 'advance', 'remit', 'chill', 'goon', '|',
                                    'pout', 'task', '}'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<function call statement->": self.position - 1})
            else:
                print("SYNTAX ERROR 29.4: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "chill", "goon", "|", "pout", "task", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 29.5: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tparameter(self):
        self.SemanticSequence.insert(len(self.SemanticSequence), {"<parameter+>": self.position})
        if self.currentkeys == '(':
            self.next()
            self.Tparameter_values()
            if self.currentkeys == ')':
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<parameter->": self.position})
                self.next()
                if self.currentkeys in ['if', 'poor', 'checkif', 'advance', 'remit', 'chill', 'goon', '|',
                                        'pout', 'task', '}'] or 'IDENTIFIER' in self.currentkeys:
                    pass
                else:
                    print("SYNTAX ERROR 30: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "chill", "goon", "|", "pout", "task", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
            else:
                print("SYNTAX ERROR 30.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 30.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "("')  # put error in a list for viewing in GUI:

    def Tparameter_values(self):
        if self.currentkeys in ['FLUTELIT', 'HINTLIT', 'STARLIT', 'CARLIT', 'cap', 'nocap',
                                '(','['] or 'IDENTIFIER' in self.currentkeys:
            self.Tdata_value()
            self.Tparameter_tail()
            if self.currentkeys == ')':
                pass
            else:
                print("SYNTAX ERROR 31: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == ')':
            pass  # NULL <parameter values>
        else:
            print("SYNTAX ERROR 31.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "FLUTELIT", "HINTLIT", "STARLIT", "CARLIT", "cap", "nocap", "[", "IDENTIFIER", ")"')  # put error in a list for viewing in GUI:

    def Tparameter_tail(self):
        if self.currentkeys == 'COMMA':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<comma>": self.position})
            self.next()
            self.Tparameter_values()
            if self.currentkeys == ')':
                pass
            else:
                print("SYNTAX ERROR 32: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == ')':
            pass
        else:
            print("SYNTAX ERROR 32.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "COMMA", ")"')  # put error in a list for viewing in GUI:

    def Toutput_statement(self):
        self.SemanticSequence.insert(len(self.SemanticSequence), {"<output statement+>": self.position})
        if self.currentkeys == 'pout':
            self.next()
            self.Tparameter()
            if self.currentkeys in ['if', 'poor', 'checkif', 'advance', 'remit', 'chill', 'goon', '|',
                                    'pout', 'task', '}'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<output statement->": self.position - 1})
            else:
                print("SYNTAX ERROR 33: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "chill", "goon", "|", "pout", "task", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 33.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout"')  # put error in a list for viewing in GUI:

    def Tinitialization_statement(self):
        if 'IDENTIFIER' in self.currentkeys:
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<initialization statement+>": self.position})
            self.Tid_or_array()
            self.Tassignment_operator()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<allowed value+>": self.position})
            self.Tallowed_value_initialize()
            if self.currentkeys in ['if', 'poor', 'checkif', 'advance', 'remit', 'chill', 'goon', '|',
                                    'pout', 'task', '}'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<allowed value->": self.position-1})
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<initialization statement->": self.position - 1})
            else:
                print("SYNTAX ERROR 34: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "chill", "goon", "|", "pout", "task", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 34.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tassignment_operator(self):
        if self.currentkeys in ['=', '+=', '-=', '*=', '/=', '%=']:
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<assignment operator>": self.position})
            self.next()
            if self.currentkeys in ['pin', '[', 'CARLIT', 'cap', 'nocap', '(', 'HINTLIT', 'STARLIT',
                                    'FLUTELIT'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 35: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pin", "[", "CARLIT", "cap", "nocap", "(", "HINTLIT", "STARLIT", "FLUTELIT", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 35.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "=", "+=", "-=", "*=", "/=", "%="')  # put error in a list for viewing in GUI:

    def Tallowed_value_initialize(self):
        if 'IDENTIFIER' in self.currentkeys:
            self.next()  # Expected: self.currentkeys = '(' if in <function call statement>
            if self.currentkeys == '(':
                self.prev()
                self.Tfunction_call_statement()
            else:
                self.prev()  # if IDENTIFIER but not for <function call statement>
                if 'IDENTIFIER' in self.currentkeys:
                    self.Tallowed_value()
                    if self.currentkeys in ['if', 'poor', 'checkif', 'advance', 'remit', 'chill', 'goon',
                                            'pout', 'task', '}', '|'] or 'IDENTIFIER' in self.currentkeys:
                        pass
                    else:
                        print("SYNTAX ERROR 36: Unexpected", self.currentvalues, self.lineCounter)
                        self.SyntaxErrors.append(
                            f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "chill", "goon", "pout", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['pin', '[', 'CARLIT', 'cap', 'nocap', '(', 'HINTLIT', 'FLUTELIT', 'STARLIT']:
            self.Tallowed_value()
            if self.currentkeys in ['if', 'poor', 'checkif', 'advance', 'remit', 'chill', 'goon',
                                    'pout', 'task', '}', '|'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 36.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "chill", "goon", "pout", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 36.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "IDENTIFIER", "pin", "[", "CARLIT", "cap", "nocap", "(", "HINTLIT", "FLUTELIT", "STARLIT"')  # put error in a list for viewing in GUI:
        if "NEWLINE" in self.currentkeys:
            self.lineCounter += 1
            self.next()

    def Tloop_statement(self):
        if self.currentkeys == 'poor':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<poor loop+>": self.position})
            self.Tfor()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<loop body+>": self.position})
            self.Tloop_body()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<loop body->": self.position - 1})
            if self.currentkeys in ['|', 'pout', 'if', 'poor', 'checkif', 'task', 'advance', 'remit', '}',
                                    'chill', 'goon'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<poor loop->": self.position-1})
            else:
                print("SYNTAX ERROR 37: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "|", "pout", "if", "poor", "checkif", "task", "advance", "remit", "}}", "chill", "goon", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == 'checkif':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<checkif loop+>": self.position})
            self.Tcheckif()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<loop body+>": self.position})
            self.Tloop_body()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<loop body->": self.position - 1})
            if self.currentkeys in ['|', 'pout', 'if', 'poor', 'checkif', 'task', 'advance', 'remit', '}',
                                    'chill', 'goon'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<checkif loop->": self.position - 1})
            else:
                print("SYNTAX ERROR 37.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "|", "pout", "if", "poor", "checkif", "task", "advance", "remit", "}}", "chill", "goon", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 37.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "poor", "checkif"')  # put error in a list for viewing in GUI:

    def Tfor(self):
        if self.currentkeys == 'poor':
            self.next()
            self.Tid()
            if self.currentkeys == 'in':
                self.next()
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<range+>": self.position})
                if self.currentkeys == 'range':
                    self.next()
                    if self.currentkeys == '(':
                        self.next()
                        self.Thint_or_id_value()
                        self.Trange()
                        if self.currentkeys == ')':
                            self.SemanticSequence.insert(len(self.SemanticSequence), {"<range->": self.position})
                            self.next()
                            if self.currentkeys == '{':
                                pass
                            else:
                                print("SYNTAX ERROR 38: Unexpected", self.currentvalues, self.lineCounter)
                                self.SyntaxErrors.append(
                                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "{{"')  # put error in a list for viewing in GUI:
                        else:
                            print("SYNTAX ERROR 38.1: Unexpected", self.currentvalues, self.lineCounter)
                            self.SyntaxErrors.append(
                                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
                    else:
                        print("SYNTAX ERROR 38.2: Unexpected", self.currentvalues, self.lineCounter)
                        self.SyntaxErrors.append(
                            f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "("')  # put error in a list for viewing in GUI:
                else:
                    print("SYNTAX ERROR 38.3: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "range"')  # put error in a list for viewing in GUI:
            else:
                print("SYNTAX ERROR 38.4: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "in"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 38.5: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "poor"')  # put error in a list for viewing in GUI:

    def Trange(self):
        if self.currentkeys == 'COMMA':
            self.next()
            self.Thint_or_id_value()
            self.Trange_tail()
            if self.currentkeys == ')':
                pass
            else:
                print("SYNTAX ERROR 39: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == ')':
            pass  # NULL <range>
        else:
            print("SYNTAX ERROR 39.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "COMMA", ")"')  # put error in a list for viewing in GUI:

    def Trange_tail(self):
        if self.currentkeys == 'COMMA':
            self.next()
            self.Thint_or_id_value()
            if self.currentkeys == ')':
                pass
            else:
                print("SYNTAX ERROR 40: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == ')':
            pass  # NULL <range tail>
        else:
            print("SYNTAX ERROR 40.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "COMMA", ")"')  # put error in a list for viewing in GUI:

    def Tloop_body(self):
        if self.currentkeys == '{':
            self.next()
            self.Tloop_content()
            if self.currentkeys == '}':
                self.next()
                if self.currentkeys in ['if', 'advance', 'chill', 'goon', 'pout', 'poor', 'checkif',
                                        'task', '}', '|', 'elib', 'elsa'] or 'IDENTIFIER' in self.currentkeys:
                    pass
                else:
                    print("SYNTAX ERROR 41: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "advance", "chill", "goon", "pout", "poor", "checkif", "task", "}}", "|", "elib", "elsa", "IDENTIFIER"')  # put error in a list for viewing in GUI:
            else:
                print("SYNTAX ERROR 41.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "}}"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 41.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "{{"')  # put error in a list for viewing in GUI:

    def Tloop_content(self):
        if self.currentkeys in ['poor', 'checkif', 'pout', 'if', 'advance', 'chill',
                                'goon'] or 'IDENTIFIER' in self.currentkeys:
            self.Tbody_no_if_task()
            self.Tloop_condition()
            self.Tcontrol_flow()
            self.Tloop_content()
            if self.currentkeys == '}':
                pass
            else:
                print("SYNTAX ERROR 42: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "}}"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == '}':
            pass
        else:
            print("SYNTAX ERROR 42.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "poor", "checkif", "pout", "if", "advance", "chill", "goon", "IDENTIFIER", "}}"')  # put error in a list for viewing in GUI:

    def Tloop_condition(self):
        if self.currentkeys == 'if':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<loop condition+>": self.position})
            self.Tloop_if()
            self.Tloop_elif()
            self.Tloop_else()
            if self.currentkeys in ['if', 'advance', 'chill', 'goon', 'pout', 'poor', 'checkif',
                                    '}'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<loop condition->": self.position-1})
            else:
                print("SYNTAX ERROR 43: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "advance", "chill", "goon", "pout", "poor", "checkif", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['if', 'advance', 'chill', 'goon', 'pout', 'poor', 'checkif',
                                  '}'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <loop condition>
        else:
            print("SYNTAX ERROR 43.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "advance", "chill", "goon", "pout", "poor", "checkif", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tloop_if(self):
        if self.currentkeys == 'if':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<loop if+>": self.position})
            self.Tif()
            self.Tloop_body()
            if self.currentkeys in ['elib', 'elsa', 'if', 'advance', 'chill', 'goon', 'pout', 'poor', 'checkif',
                                    '}'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<loop if->": self.position-1})
            else:
                print("SYNTAX ERROR 44: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elib", "elsa", "if", "advance", "chill", "goon", "pout", "poor", "checkif", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 44.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if"')  # put error in a list for viewing in GUI:

    def Tif(self):
        if self.currentkeys == 'if':
            self.next()
            self.Tcondition()
            if self.currentkeys == '{':
                pass
            else:
                print("SYNTAX ERROR 45: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "{{"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 45.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if"')  # put error in a list for viewing in GUI:

    def Tcondition(self):
        self.SemanticSequence.insert(len(self.SemanticSequence), {"<condition+>": self.position})
        if self.currentkeys == '(':
            self.next()
            self.Tlogical_expression()
            if self.currentkeys == ')':
                self.next()
                if self.currentkeys == '{':
                    self.SemanticSequence.insert(len(self.SemanticSequence), {"<condition->": self.position-1})
                else:
                    print("SYNTAX ERROR 46: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "{{"')  # put error in a list for viewing in GUI:
            else:
                print("SYNTAX ERROR 46.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 46.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "("')  # put error in a list for viewing in GUI:

    def Tlogical_expression(self):
        if self.currentkeys == '(':
            self.next()
            self.Tlogical_expression()
            if self.currentkeys == ')':
                self.next()
                self.Tlogic_or_relational_tail()
                if self.currentkeys == ')':
                    pass
                else:
                    print("SYNTAX ERROR 47: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
            else:
                print("SYNTAX ERROR 47.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == 'not':
            self.Tnot_logic()
            self.Tlogic_or_relational_tail()
            if self.currentkeys == ')':
                pass
            else:
                print("SYNTAX ERROR 47.2: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['cap', 'nocap', 'CARLIT', 'STARLIT', 'HINTLIT',
                                  'FLUTELIT'] or 'IDENTIFIER' in self.currentkeys:
            self.Trelational_expression()
            self.Tlogic_tail()
            if self.currentkeys == ')':
                pass
            else:
                print("SYNTAX ERROR 47.3: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 47.4: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "(", "cap", "nocap", "CARLIT", "STARLIT", "HINTLIT", "FLUTELIT", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tlogic_tail(self):
        if self.currentkeys in ['and', 'or']:
            self.Tlogical_operator()
            self.Tlogical_expression()
            if self.currentkeys == ')':
                pass
            else:
                print("SYNTAX ERROR 48: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == ')':
            pass  # NULL <logic tail>
        else:
            print("SYNTAX ERROR 48.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "and", "or", ")"')  # put error in a list for viewing in GUI:

    def Tlogical_operator(self):
        if self.currentkeys in ['and', 'or']:
            self.next()
            if self.currentkeys in ['(', 'not', 'cap', 'nocap', 'CARLIT', 'STARLIT', 'HINTLIT', 'FLUTELIT',
                                    ] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 49: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "(", "not", "cap", "nocap", "CARLIT", "STARLIT", "HINTLIT", "FLUTELIT", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 49.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "and", "or"')  # put error in a list for viewing in GUI:

    def Tnot_logic(self):
        if self.currentkeys == 'not':
            self.next()
            if self.currentkeys == '(':
                self.next()
                self.Tlogical_expression()
                if self.currentkeys == ')':
                    self.next()
                    if self.currentkeys in ['and', 'or', '==', '!=', ')']:
                        pass
                    else:
                        print("SYNTAX ERROR 50: Unexpected", self.currentvalues, self.lineCounter)
                        self.SyntaxErrors.append(
                            f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "and", "or", "==", "!="')  # put error in a list for viewing in GUI:
                else:
                    print("SYNTAX ERROR 50.1: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
            else:
                print("SYNTAX ERROR 50.2: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "("')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 50.3: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "not"')  # put error in a list for viewing in GUI:

    def Tlogic_or_relational_tail(self):
        if self.currentkeys in ['and', 'or']:
            self.Tlogic_tail()
            if self.currentkeys == ')':
                pass
            else:
                print("SYNTAX ERROR 51: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['<', '>', '<=', '>=', '==', '!=']:
            self.Trelational_tail()
            if self.currentkeys == ')':
                pass
            else:
                print("SYNTAX ERROR 51.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == ')':
            pass
        else:
            print("SYNTAX ERROR 51.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "and", "or", "==", "!=", ")"')  # put error in a list for viewing in GUI:

    def Trelational_expression(self):
        if self.currentkeys == '(':
            self.next()
            self.Tlogic_or_relational_tail()
            if self.currentkeys == ')':
                self.next()
                if self.currentkeys in [')', 'and', 'or']:
                    pass
                else:
                    print("SYNTAX ERROR 52: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "and", "or"')  # put error in a list for viewing in GUI:
            else:
                print("SYNTAX ERROR 52.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['cap', 'nocap', 'CARLIT', 'STARLIT', 'HINTLIT',
                                  'FLUTELIT'] or 'IDENTIFIER' in self.currentkeys:
            self.Tdata_value_no_array()
            self.Tlogic_or_relational_tail()
            if self.currentkeys in [')', 'and', 'or']:
                pass
            else:
                print("SYNTAX ERROR 52.2: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "and", "or"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 52.3: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "(", "cap", "nocap", "CARLIT", "STARLIT", "HINTLIT", "FLUTELIT", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Trelational_tail(self):
        if self.currentkeys in ['<', '>', '<=', '>=', '==', '!=']:
            self.Trelational_operator()
            self.Trelational_expression()
            if self.currentkeys in [')', 'and', 'or']:
                pass
            else:
                print("SYNTAX ERROR 53: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")", "and", "or"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in [')', 'and', 'or']:
            pass  # NULL <relational tail>
        else:
            print("SYNTAX ERROR 53.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "<", ">", "<=", ">=", "==", "!=", ")", "and", "or"')  # put error in a list for viewing in GUI:

    def Trelational_operator(self):
        if self.currentkeys in ['<', '>', '<=', '>=', '==', '!=']:
            self.next()
            if self.currentkeys in ['(', 'not', 'cap', 'nocap', 'CARLIT', 'STARLIT', 'HINTLIT', 'FLUTELIT',
                                    ] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 54: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "(", "not", "cap", "nocap", "CARLIT", "STARLIT", "HINTLIT", "FLUTELIT", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 54.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "<", ">", "<=", ">=", "==", "!="')  # put error in a list for viewing in GUI:

    def Tloop_elif(self):
        if self.currentkeys == 'elib':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<loop elif+>": self.position})
            self.Telif()
            self.Tloop_body()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<loop elif->": self.position - 1})
            self.Tloop_elif()
            if self.currentkeys in ['elsa', 'advance', 'chill', 'goon', 'if', 'pout', 'poor', 'checkif',
                                    '}'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 55: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elsa", "advance", "chill", "goon", "if", "pout", "poor", "checkif", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['elsa', 'advance', 'chill', 'goon', 'if', 'pout', 'poor', 'checkif',
                                  '}'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <loop elif>
        else:
            print("SYNTAX ERROR 55.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elib", "elsa", "advance", "chill", "goon", "if", "pout", "poor", "checkif", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Telif(self):
        if self.currentkeys == 'elib':
            self.next()
            self.Tcondition()
            if self.currentkeys == '{':
                pass
            else:
                print("SYNTAX ERROR 56: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "{{"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 56.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elib"')  # put error in a list for viewing in GUI:

    def Tloop_else(self):
        if self.currentkeys == 'elsa':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<loop else+>": self.position})
            self.next()
            self.Tloop_body()
            if self.currentkeys in ['advance', 'chill', 'goon', 'if', 'pout', 'poor', 'checkif',
                                    '}'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<loop else->": self.position-1})
            else:
                print("SYNTAX ERROR 57: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "advance", "chill", "goon", "if", "pout", "poor", "checkif", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['advance', 'chill', 'goon', 'if', 'pout', 'poor', 'checkif',
                                  '}'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <loop else>
        else:
            print("SYNTAX ERROR 57.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "advance", "chill", "goon", "if", "pout", "poor", "checkif", "}}", "elsa", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tcontrol_flow(self):
        if self.currentkeys in ['advance', 'chill', 'goon']:
            if self.currentvalues == 'advance':
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<pass>": self.position})
            elif self.currentvalues == 'chill':
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<break>": self.position})
            elif self.currentvalues == 'goon':
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<continue>": self.position})
            self.next()
            if self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'advance', 'chill', 'goon',
                                    '}', 'remit'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 58: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "advance", "chill", "goon", "}}", "remit", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'advance', 'chill', 'goon',
                                  '}', 'remit'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <control flow>
        else:
            print("SYNTAX ERROR 58.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "advance", "chill", "goon", "}}", "remit", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tcheckif(self):
        if self.currentkeys == 'checkif':
            self.next()
            self.Tcondition()
            if self.currentkeys == '{':
                pass
            else:
                print("SYNTAX ERROR 59: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "{{"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 59.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "checkif"')  # put error in a list for viewing in GUI:

    def Tcondition_statement(self):
        if self.currentkeys == 'if':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<condition statement+>": self.position})
            self.Tif_with_body()
            self.Telif_with_body()
            self.Telse_with_body()
            if self.currentkeys in ['|', 'pout', 'if', 'poor', 'checkif', 'task', 'advance',
                                    '}', 'remit', 'chill', 'goon'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<condition statement->": self.position - 1})
            else:
                print("SYNTAX ERROR 60: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "|", "pout", "if", "poor", "checkif", "task", "advance", "}}", "remit", "chill", "goon", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 60.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if"')  # put error in a list for viewing in GUI:

    def Tif_with_body(self):
        self.SemanticSequence.insert(len(self.SemanticSequence), {"<if with body+>": self.position})
        if self.currentkeys == 'if':
            self.Tif()
            self.Tcondition_body()
            if self.currentkeys in ['elib', 'elsa', 'pout', 'if', 'poor', 'checkif', 'advance', 'task',
                                    '}', '|'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<if with body->": self.position - 1})
            else:
                print("SYNTAX ERROR 61: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elib", "elsa", "pout", "if", "poor", "checkif", "advance", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 61.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if"')  # put error in a list for viewing in GUI:

    def Tcondition_body(self):
        self.SemanticSequence.insert(len(self.SemanticSequence), {"<condition body+>": self.position})
        if self.currentkeys == '{':
            self.next()
            self.Tcondition_content()
            if self.currentkeys == '}':
                self.next()
                if self.currentkeys in ['elib', 'elsa', 'pout', 'if', 'poor', 'checkif', 'advance', 'task',
                                        '}', '|'] or 'IDENTIFIER' in self.currentkeys:
                    self.SemanticSequence.insert(len(self.SemanticSequence), {"<condition body->": self.position -1})
                else:
                    print("SYNTAX ERROR 62: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elib", "elsa", "pout", "if", "poor", "checkif", "advance", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
            else:
                print("SYNTAX ERROR 62.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "}}"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 62.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "{{"')  # put error in a list for viewing in GUI:

    def Tcondition_content(self):
        if self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'advance'] or 'IDENTIFIER' in self.currentkeys:
            self.Tbody_no_task()
            self.Tpass()
            self.Tcondition_content()
            if self.currentkeys == '}':
                pass
            else:
                print("SYNTAX ERROR 63: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "}}"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == '}':
            pass  # NULL <condition content>
        else:
            print("SYNTAX ERROR 63.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "advance", "IDENTIFIER", "}}"')  # put error in a list for viewing in GUI:

    def Tpass(self):
        if self.currentkeys == 'advance':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<pass>": self.position})
            self.next()
            if self.currentkeys in ['pout', 'if', 'checkif', 'poor', 'advance', 'remit',
                                    '}'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 64: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "checkif", "poor", "advance", "remit", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['pout', 'if', 'checkif', 'poor', 'advance',
                                  'remit', '}'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <pass>
        else:
            print("SYNTAX ERROR 64.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "advance", "pout", "if", "checkif", "poor", "advance", "remit", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Telif_with_body(self):
        if self.currentkeys == 'elib':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<elif with body+>": self.position})
            self.Telif()
            self.Tcondition_body()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<elif with body->": self.position - 1})
            self.Telif_with_body()
            if self.currentkeys in ['elsa', 'pout', 'if', 'poor', 'checkif', 'advance', 'task',
                                    '}', '|'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 65: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elsa", "pout", "if", "poor", "checkif", "advance", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['elsa', 'pout', 'if', 'poor', 'checkif', 'advance', 'task',
                                  '}', '|'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <elif with body>
        else:
            print("SYNTAX ERROR 65.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elib", "elsa", "pout", "if", "poor", "checkif", "advance", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Telse_with_body(self):
        if self.currentkeys == 'elsa':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<else with body+>": self.position})
            self.next()
            self.Tcondition_body()
            if self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'advance', 'task',
                                    '}', '|'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<else with body->": self.position-1})
            else:
                print("SYNTAX ERROR 66: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "advance", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'advance', 'task',
                                  '}', '|'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <else with body>
        else:
            print("SYNTAX ERROR 66.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elsa", "pout", "if", "poor", "checkif", "advance", "task", "}}", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tfunction(self):
        self.SemanticSequence.insert(len(self.SemanticSequence), {"<function+>": self.position})
        if self.currentkeys == 'task':
            self.next()
            self.Tid()
            if self.currentkeys == '(':
                self.next()
                self.Tfunction_parameter()
                if self.currentkeys == ')':
                    self.next()
                    self.Tfunction_body()
                    if self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'advance', 'task',
                                            '|'] or 'IDENTIFIER' in self.currentkeys:
                        self.SemanticSequence.insert(len(self.SemanticSequence), {"<function->": self.position-1})
                    else:
                        print("SYNTAX ERROR 67: Unexpected", self.currentvalues, self.lineCounter)
                        self.SyntaxErrors.append(
                            f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "advance", "task", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
                else:
                    print("SYNTAX ERROR 67.1: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
            else:
                print("SYNTAX ERROR 67.2: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "("')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 67.3: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "task"')  # put error in a list for viewing in GUI:

    def Tfunction_parameter(self):
        if 'IDENTIFIER' in self.currentkeys:
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function parameter+>": self.position})
            self.Tid()
            self.Tid_tail()
            if self.currentkeys == ')':
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<function parameter->": self.position-1})
            else:
                print("SYNTAX ERROR 68: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == ')':
            pass  # NULL <function parameter>
        else:
            print("SYNTAX ERROR 68.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "IDENTIFIER", ")"')  # put error in a list for viewing in GUI:

    def Tid_tail(self):
        if self.currentkeys == 'COMMA':
            self.next()
            self.Tfunction_parameter()
            if self.currentkeys == ')':
                pass
            else:
                print("SYNTAX ERROR 69: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == ')':
            pass  # NULL <id tail>
        else:
            print("SYNTAX ERROR 69.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "COMMA", ")"')  # put error in a list for viewing in GUI:

    def Tfunction_body(self):
        if self.currentkeys == '{':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function body+>": self.position})
            self.next()
            self.Tfunction_declaration()
            self.Tfunction_content()
            if self.currentkeys == '}':
                self.next()
                if self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task',
                                        '|'] or 'IDENTIFIER' in self.currentkeys:
                    self.SemanticSequence.insert(len(self.SemanticSequence), {"<function body->": self.position-1})
                else:
                    print("SYNTAX ERROR 70: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "task", "|", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 70.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "{{"')  # put error in a list for viewing in GUI:

    def Tfunction_declaration(self):
        if self.currentkeys == 'universal':
            self.Tuniversal()
            self.Tfunction_declaration()
            if self.currentkeys in ['pout', 'if', 'poor', 'checkif', '}', 'advance',
                                    'remit'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 71: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "}}", "remit", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['hint', 'flute', 'star', 'car', 'bully']:
            self.Tdeclaration()
            self.Tfunction_declaration()
            if self.currentkeys in ['pout', 'if', 'poor', 'checkif', '}', 'remit'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 71.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "pout", "if", "poor", "checkif", "}}", "remit", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['pout', 'if', 'poor', 'checkif', '}', 'advance',
                                  'remit'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <function declaration>
        else:
            print("SYNTAX ERROR 71.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "universal", "hint", "flute", "star", "car", "bully", "pout", "if", "poor", "checkif", "}}" , "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tuniversal(self):
        if self.currentkeys == 'universal':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<universal+>": self.position})
            self.next()
            self.Tdata_type()
            self.Tid_or_array()
            if self.currentkeys in ['universal', 'hint', 'flute', 'star', 'car', 'bully', 'pout', 'if',
                                    'poor', 'checkif', '}', 'advance'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<universal->": self.position})
            else:
                print("SYNTAX ERROR 72: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "universal", "hint", "flute", "star", "car", "bully", "pout", "if", "poor", "checkif", "}}", "advance", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['universal', 'hint', 'flute', 'star', 'car', 'bully', 'pout', 'if',
                                  'poor', 'checkif', '}', 'advance'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <universal>
        else:
            print("SYNTAX ERROR 72.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "universal", "hint", "flute", "star", "car", "bully", "pout", "if", "poor", "checkif", "}}", "advance", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tfunction_content(self):
        if self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'advance',
                                'remit'] or 'IDENTIFIER' in self.currentkeys:
            self.Tbody_no_if_loop_task()
            self.Tfunction_condition()
            self.Tfunction_loop()
            self.Tpass()
            self.Treturn()
            self.Tfunction_content()
            if self.currentkeys == '}':
                pass
            else:
                print("SYNTAX ERROR 73: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "}}"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == '}':
            pass  # NULL <function content>
        else:
            print("SYNTAX ERROR 73.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "pout", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tfunction_condition(self):
        if self.currentkeys == 'if':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function condition+>": self.position})
            self.Tfunction_if()
            self.Tfunction_elif()
            self.Tfunction_else()
            if self.currentkeys in ['poor', 'checkif', 'advance', 'remit', 'pout', 'if',
                                    '}'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<function condition->": self.position})
            else:
                print("SYNTAX ERROR 74: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "pout", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        if self.currentkeys in ['poor', 'checkif', 'advance', 'remit', 'pout', 'if',
                                '}'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <function condition>
        else:
            print("SYNTAX ERROR 74.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "remit", "pout", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tfunction_if(self):
        if self.currentkeys == 'if':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function if+>": self.position})
            self.Tif()
            self.Tfunction_condition_body()
            if self.currentkeys in ['elib', 'elsa', 'poor', 'checkif', 'advance', 'remit', 'pout', 'if',
                                    '}'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<function if->": self.position-1})
            else:
                print("SYNTAX ERROR 75: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elib", "elsa", "poor", "checkif", "advance", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 75.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if"')  # put error in a list for viewing in GUI:

    def Tfunction_condition_body(self):
        self.SemanticSequence.insert(len(self.SemanticSequence), {"<function condition body+>": self.position})
        if self.currentkeys == '{':
            self.next()
            self.Tfunction_content()
            if self.currentkeys == '}':
                self.next()
                if self.currentkeys in ['elib', 'elsa', 'poor', 'checkif', 'advance', 'remit', 'pout', 'if',
                                        '}'] or 'IDENTIFIER' in self.currentkeys:
                    self.SemanticSequence.insert(len(self.SemanticSequence), {"<function condition body->": self.position - 1})
                else:
                    print("SYNTAX ERROR 76: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elib", "elsa", "poor", "checkif", "advance", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
            else:
                print("SYNTAX ERROR 76.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "}}"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 76.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "{{"')  # put error in a list for viewing in GUI:

    def Tfunction_elif(self):
        if self.currentkeys == 'elib':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function elif+>": self.position})
            self.Telif()
            self.Tfunction_condition_body()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function elif->": self.position - 1})
            self.Tfunction_elif()
            if self.currentkeys in ['elsa', 'poor', 'checkif', 'advance', 'remit', 'pout', 'if',
                                    '}'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 77: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elsa", "poor", "checkif", "advance", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['elsa', 'poor', 'checkif', 'advance', 'remit', 'pout', 'if',
                                  '}'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <function elif>
        else:
            print("SYNTAX ERROR 77.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elib", ')  # put error in a list for viewing in GUI:

    def Tfunction_else(self):
        if self.currentkeys == 'elsa':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function else+>": self.position})
            self.next()
            self.Tfunction_condition_body()
            if self.currentkeys in ['poor', 'checkif', 'advance', 'remit', 'pout', 'if',
                                    '}'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<function else->": self.position - 1})
            else:
                print("SYNTAX ERROR 78: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "poor", "checkif", "advance", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['poor', 'checkif', 'advance', 'remit', 'pout', 'if',
                                  '}'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <function else>
        else:
            print("SYNTAX ERROR 78.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elsa", "poor", "checkif", "advance", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tfunction_loop(self):
        if self.currentkeys == 'poor':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function poor loop+>": self.position})
            self.Tfor()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function loop body+>": self.position})
            self.Tfunction_loop_body()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function loop body->": self.position - 1})
            if self.currentkeys in ['advance', 'remit', 'pout', '}', 'chill', 'goon', 'poor', 'checkif',
                                    'if'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<function poor loop->": self.position - 1})
            else:
                print("SYNTAX ERROR 79: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "advance", "remit", "pout", "}}", "chill", "goon", "poor", "checkif", "if", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == 'checkif':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function checkif loop+>": self.position})
            self.Tcheckif()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function loop body+>": self.position})
            self.Tfunction_loop_body()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function loop body->": self.position - 1})
            if self.currentkeys in ['advance', 'remit', 'pout', '}', 'chill', 'goon', 'poor', 'checkif',
                                    'if'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<function checkif loop->": self.position - 1})
            else:
                print("SYNTAX ERROR 79.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "advance", "remit", "pout", "}}", "chill", "goon", "poor", "checkif", "if", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['advance', 'remit', 'pout', '}', 'chill', 'goon', 'poor', 'checkif',
                                  'if'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <function loop>
        else:
            print("SYNTAX ERROR 79.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "poor", "checkif", "advance", "remit", "pout", "}}", "chill", "goon", "poor", "checkif", "if", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tfunction_loop_body(self):
        if self.currentkeys == '{':
            self.next()
            self.Tfunction_loop_content()
            if self.currentkeys == '}':
                self.next()
                if self.currentkeys in ['advance', 'remit', 'pout', '}', 'chill', 'goon', 'poor',
                                        'checkif', 'if', 'elib', 'elsa'] or 'IDENTIFIER' in self.currentkeys:
                    pass
                else:
                    print("SYNTAX ERROR 80: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "advance", "remit", "pout", "}}", "chill", "goon", "poor", "checkif", "if", "elib", "elsa", "IDENTIFIER"')  # put error in a list for viewing in GUI:
            else:
                print("SYNTAX ERROR 80.1: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "}}"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 80.2: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "{{"')  # put error in a list for viewing in GUI:

    def Tfunction_loop_content(self):
        if self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'advance', 'chill', 'goon',
                                'remit'] or 'IDENTIFIER' in self.currentkeys:
            self.Tbody_no_if_loop_task()
            self.Tfunction_loop_condition()
            self.Tfunction_loop()
            self.Tcontrol_flow()
            self.Treturn()
            self.Tfunction_loop_content()
            if self.currentkeys == '}':
                pass
            else:
                print("SYNTAX ERROR 81: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "}}"')  # put error in a list for viewing in GUI:
        elif self.currentkeys == '}':
            pass  # NULL <function loop content>
        else:
            print("SYNTAX ERROR 81.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "poor", "checkif", "advance", "chill", "goon", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tfunction_loop_condition(self):
        if self.currentkeys == 'if':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function loop condition+>": self.position})
            self.Tfunction_loop_if()
            self.Tfunction_loop_elif()
            self.Tfunction_loop_else()
            if self.currentkeys in ['poor', 'checkif', 'advance', 'chill', 'goon', 'remit', 'pout',
                                    'if', '}'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<function loop condition->": self.position-1})
            else:
                print("SYNTAX ERROR 82: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "poor", "checkif", "advance", "chill", "goon", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['poor', 'checkif', 'advance', 'chill', 'goon', 'remit', 'pout',
                                  'if', '}'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <function loop condition>
        else:
            print("SYNTAX ERROR 82.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if", "poor", "checkif", "advance", "chill", "goon", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tfunction_loop_if(self):
        if self.currentkeys == 'if':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function loop if+>": self.position})
            self.Tif()
            self.Tfunction_loop_body()
            if self.currentkeys in ['elib', 'elsa', 'poor', 'checkif', 'advance', 'chill', 'goon', 'remit', 'pout',
                                    'if', '}'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<function loop if->": self.position-1})
            else:
                print("SYNTAX ERROR 83: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elib", "elsa", "poor", "checkif", "advance", "chill", "goon", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        else:
            print("SYNTAX ERROR 83.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "if"')  # put error in a list for viewing in GUI:

    def Tfunction_loop_elif(self):
        if self.currentkeys == 'elib':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function loop elif+>": self.position})
            self.Telif()
            self.Tfunction_loop_body()
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function loop elif->": self.position - 1})
            self.Tfunction_loop_elif()
            if self.currentkeys in ['elsa', 'poor', 'checkif', 'advance', 'chill', 'goon', 'remit', 'pout',
                                    'if', '}'] or 'IDENTIFIER' in self.currentkeys:
                pass
            else:
                print("SYNTAX ERROR 84: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elsa", "poor", "checkif", "advance", "chill", "goon", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['elsa', 'poor', 'checkif', 'advance', 'chill', 'goon', 'remit', 'pout',
                                  'if', '}'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <function loop elif>
        else:
            print("SYNTAX ERROR 84.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elib", "elsa", "poor", "checkif", "advance", "chill", "goon", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Tfunction_loop_else(self):
        if self.currentkeys == 'elsa':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<function loop else+>": self.position})
            self.next()
            self.Tfunction_loop_body()
            if self.currentkeys in ['poor', 'checkif', 'advance', 'chill', 'goon', 'remit', 'pout',
                                    'if', '}'] or 'IDENTIFIER' in self.currentkeys:
                self.SemanticSequence.insert(len(self.SemanticSequence), {"<function loop else->": self.position-1})
            else:
                print("SYNTAX ERROR 85: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elsa", "poor", "checkif", "advance", "chill", "goon", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['poor', 'checkif', 'advance', 'chill', 'goon', 'remit', 'pout',
                                  'if', '}'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <function loop else>
        else:
            print("SYNTAX ERROR 85.1: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "elsa", "poor", "checkif", "advance", "chill", "goon", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    def Treturn(self):
        if self.currentkeys == 'remit':
            self.SemanticSequence.insert(len(self.SemanticSequence), {"<return+>": self.position})
            self.next()
            if self.currentkeys == '(':
                self.next()
                self.Treturn_value()
                if self.currentkeys == ')':
                    self.next()
                    if self.currentkeys in ['poor', 'checkif', 'advance', 'chill', 'goon', 'remit', 'pout',
                                            'if', '}'] or 'IDENTIFIER' in self.currentkeys:
                        self.SemanticSequence.insert(len(self.SemanticSequence), {"<return->": self.position-1})
                    else:
                        print("SYNTAX ERROR 86: Unexpected", self.currentvalues, self.lineCounter)
                        self.SyntaxErrors.append(
                            f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "poor", "checkif", "advance", "chill", "goon", "remit", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:
                else:
                    print("SYNTAX ERROR 86.1: Unexpected", self.currentvalues, self.lineCounter)
                    self.SyntaxErrors.append(
                        f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ ")"')  # put error in a list for viewing in GUI:
            else:
                print("SYNTAX ERROR 86.2: Unexpected", self.currentvalues, self.lineCounter)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "("')  # put error in a list for viewing in GUI:
        elif self.currentkeys in ['poor', 'checkif', 'advance', 'chill', 'goon', 'remit', 'pout',
                                  'if', '}'] or 'IDENTIFIER' in self.currentkeys:
            pass  # NULL <return>
        else:
            print("SYNTAX ERROR 86.3: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "remit", "poor", "checkif", "advance", "chill", "goon", "pout", "if", "}}", "IDENTIFIER"')  # put error in a list for viewing in GUI:

    # =====================================The STRUCTURE CODE============================================================#

    def GetNextTerminal(self):  # <program> and <program content>
        terminator = 0
        ctr = 0
        if self.currentkeys == '"NEWLINE"':
            print("SYNTAX ERROR 87: Unexpected", self.currentvalues, self.lineCounter)
            self.SyntaxErrors.append(
                f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}" \n\nExpected ⏵ "|"')  # put error in a list for viewing in GUI
        if self.currentkeys == '|':
            terminator += 1
        self.TProg_start()
        while self.position < len(self.Terminals) and ctr != len(self.Terminals) and terminator != 0:
            if self.currentkeys == '|':
                break
            elif self.currentkeys in ['hint', 'flute', 'star', 'bully', 'car']:
                self.Tdeclaration()
            elif self.currentkeys in ['pout', 'if', 'poor', 'checkif', 'task'] or "IDENTIFIER" in self.currentkeys:
                self.Tbody()
            else:
                print("SYNTAX ERROR X:", self.currentvalues)
                self.SyntaxErrors.append(
                    f'LINE #{self.lineCounter} : Unexpected ⏵ "{self.currentvalues}"')  # put error in a list for viewing in GUI
                break
            ctr += 1
        self.TProg_end()
        if len(self.SyntaxErrors) == 0:
            print("SYNTAX COMPILE SUCCESSFUL", self.lineCounter)
            self.SyntaxErrors.append("               SYNTAX COMPILE SUCCESSFUL\n-------------------------------------------------------------\n\n")  # put in a list for viewing in GUI
            print(self.SemanticSequence)
        else:
            print("ERRORS FOUND", self.lineCounter)
        return self.SyntaxErrors

