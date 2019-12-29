#Александър Чаушев
#ИУ7 - 16Б
import os, platform


def clearScr():
    if platform.system() == 'Linux' or platform.system() == 'Mac':
        os.system('clear')
    elif platform.system() == 'Windows': 
        os.system('cls')


def printMenu():
    clearScr()
    print("-" * 5 + "Меню" + "-" * 5)
    print("0) Показать текст")
    print("1) Удалить заданное слово во всем тексте")
    print("2) Произвести во всем тексте замену одного слова другим")                    
    print("/- Выравниние текста по:")
    print("3)левому краю  ")
    print("4)правому краю ")
    print("5)ширине       ")
    print("6) Замену арифметических выражений состоящих из умножения и деления на результат их вычисления")
    print("7) Найти самое длинное и самое кароткое предложение в тексте")
    print()
    
    
def readOptions():
    try:
        mode = int(input())
    except ValueError:
        print("Пожалуйста, выберите число в диапазоне от 1 до 7 включительно")             
        return readOptions()
    if int(mode) > 7 or mode < 1:
        print("Пожалуйста, выберите число в диапазоне от 1 до 7 включительно")
        return readOptions()
    print("_____________________________________________\n")
    return mode



def process(mode, text):
    if mode == 1:
        word = input("Введите слово: ")
        return myRemove(text, word)
    elif mode == 2:
        word = input("Введите слово, которое будет заменено: ")
        toWord = input("Введите слово, которым будет заменено: ")           
        return myReplace(text, word, toWord)
    elif mode >= 3 and mode <= 5:
        for i in range(len(text)):
            line = text[i]
            text[i] = " ".join([x.strip() for x in line.split()])
        if mode == 3:
            for i in range(len(text)):
                text[i] = text[i].lstrip()
        else:
            for i in range(len(text)):
                text[i] = text[i].lstrip()

            lenghtestLine = 0
            for line in text:
                if len(line) > lenghtestLine:
                    lenghtestLine = len(line)
        
            if mode == 4:
                for i in range(len(text)):
                    if text[i] != "":
                        text[i] = " " * (lenghtestLine - len(text[i])) + text[i]

            elif mode == 5:
                text = (centerAlign(text, lenghtestLine))

        return text
    elif mode == 6:
         return findArithmetic(text)
    elif mode == 7:
        return findLengAndShortSent(text)   
        

def brk(listed):
    seperator = [" ", ",", ".", '"', "'", ";", ":", "[", "]", "{", "}", "=", "+", "-", "_", ")", "(", "1", "!", "/", "\\", "?", ">", "<"]
    breakedLines = []
    i = -1
    for line in listed:
        breakedLines.append([""])
        i += 1
        j = 0
        for char in line:
            if char in seperator:
                breakedLines[i].append(char)
                breakedLines[i].append("")
                j += 2
            else:
                breakedLines[i][j] += char

    return breakedLines


def myReplace(listed, word, toWord):                    
    breakedLines = brk(listed)
    for i in range(len(breakedLines)):
        for j, wrd in enumerate(breakedLines[i]):
            if wrd == word:
                breakedLines[i][j] = toWord

        breakedLines[i] = "".join(breakedLines[i])
    return breakedLines
                
def myRemove(listed, word):                                
    breakedLines = brk(listed)
    for i in range(len(breakedLines)):
        for j, wrd in enumerate(breakedLines[i]):
            if wrd == word:
                breakedLines[i][j] = ""

        breakedLines[i] = "".join(breakedLines[i])
    return breakedLines

def findArithmetic(textList):
    for line in textList:
        for str in textList:
            j = 0
            while j < len(str):
                if str[j] >= '0' and str[j] <= '9':
                    start = j
                    while j < len(str) and \
                            ((str[j] >= '0' and str[j] <= '9')
                             or (str[j] in '* / - + \( )% ^ **')):
                        j += 1
                    print(eval(str[start:j]), end=' ')
                else:
                    print(str[j], end='')
                    j += 1
        return
        
        '''
                j = 0
                while j < len(str):
                    if str[j] >= '0' and str[j] <= '9':
                        start = j
                        while j < len(str) and \
                                ((str[j] >= '0' and str[j] <= '9')
                                 or (str[j] in '* / - + \( )% ^ **')):
                            j += 1
                        print(eval(str[start:j]), end=' ')
                    else:
                        print(str[j], end='')
                        j += 1
                return
'''
def centerAlign(listed, scrWidth):            
    breakedLines = []
    i = -1
    for line in listed:
        breakedLines.append([""])
        i += 1
        j = 0
        for char in line:
            if char == " ":
                breakedLines[i].append(char)
                breakedLines[i].append("")
                j += 2
            else:
                breakedLines[i][j] += char
        if "" in breakedLines[i]:
            breakedLines[i].remove("")

    for i in range(len(breakedLines)):
        spaces = breakedLines[i].count(" ")
        if spaces != 0:
            lenLn = 0
            for j in range(len(breakedLines[i])):
                lenLn += len(breakedLines[i][j])

            differ = scrWidth - lenLn
            toAdd = differ % spaces
            for j in range(len(breakedLines[i])):
                if breakedLines[i][j] == " ":
                    breakedLines[i][j] += " " * (differ//spaces + (1 if toAdd > 0 else 0))
                    toAdd -= 1
        breakedLines[i] = "".join(breakedLines[i])
    
    return breakedLines
def findLengAndShortSent(text):
    fr = text.copy()
    sep = ["?", ".", "!"]
    text = list("".join(text))
    sentences = [""]
    i = 0
    for char in text:
        sentences[i] += char
        if char in sep:
            sentences[i] = " ".join(sentences[i].strip().split())
            sentences.append("")
            i += 1

    sentences.remove("")
    result = [sentences[0], sentences[0]]
    for i in range(1, len(sentences)):
        if len(sentences[i]) > len(result[0]):
            result[0] = sentences[i]
        if len(sentences[i]) < len(result[1]):
            result[1] = sentences[i]

    print("Самое кароткое: \n" + result[1])
    print()
    print("Самое длинное: \n" + result[0])
    return fr

def askForRep():
    ans = input("Открыт меню? y/n\n")
    if ans == "y" or ans == "Y":
        return True
    elif ans == "n" or ans == "N":
        return False
    else:
        return askForRep()


# начало кода ____________________________________

'''f = open('text.txt', 'r')

textList = f.read().split('\n');
printext = textList
f.close()
while 1:
    printMenu()
    mode = readOptions()
    textList = process(mode,textList)
    if mode != 6 and mode != 7: print("\n".join(textList))
    if not askForRep():
        break
'''
