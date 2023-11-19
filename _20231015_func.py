from typing import List
from math import log10, sqrt, modf
import time
from string import ascii_lowercase




def countDown(numOfStartCoundown: int):
    """Эта фуккция выводит обратный отсчет на экран."""

    print(numOfStartCoundown)
    if (numOfStartCoundown <= 1):
        return
    else:
        countDown(numOfStartCoundown - 1)

def sumArray(arr: list[int]):
    """Суммирует  числа в массиве"""

    total = 0
    for x in arr:
        total += x
    return float(total)

def validatePIN_old(pin):
    """Проверяем PIN на соотвествие: Чтобыба был только из чисел,
      и равнялся 4 или 6 цифер"""
    
    if pin.isdigit():
        lenghtPIN = len(pin)
        if  lenghtPIN == 4 or lenghtPIN == 6:
            return True
        else:
            return False
    else:
        return False
    

def validatePIN_old1(pin):
    """Проверяем PIN на соотвествие: Чтобыба был только из чисел,
      и был равен  4 или 6 разрядам"""
    
    if isinstance(pin,str):  
        lenghtPIN = len(pin)
        if pin.isdigit() and (lenghtPIN == 4 or lenghtPIN == 6):
            return True
        else:
            return False
    elif isinstance(pin,int):
        digits = int(log10(pin) + 1)
        if (digits == 4) or (digits == 6):
            return True
        else:
            return False
        
def validatePIN(pin):
    """Проверяем PIN на соотвествие: Чтобыба был только из чисел,
      и был равен  4 или 6 разрядам"""
    if isinstance(pin,str):  
        lenghtPIN = len(pin)
        if pin.isdigit() and (lenghtPIN == 4 or lenghtPIN == 6):
            return True
        else:
            return False
    elif isinstance(pin,int):
        if (0 <= pin <= 9999) or (100000 <= pin <= 999999):
            return True
        else:
            return False

        
def isSqare(isSqareNum: int):
    """Проверяем, является ли число возведением
      в квардат какого-то ровного числа, допустим 5 или 6"""
    if isSqareNum > 0:
        x = modf(sqrt(isSqareNum))
        if x[0]:
            return False
        else:
            return True
    else:
        return False
    
def is_qwadre(s):
 # не мое решение, но интересное
 x = s ** 0.5
 return x == int(x) if s >= 0 else False

def deleteVowels_old(stringWithVowels : str):
    """Удаляем все гласные буквы из строки"""
    
    stringNoneVowels_list = [letter for letter in stringWithVowels
                         if letter not in ['а', 'А', 'о', 'О','у', 'У', 'ы', 'Ы', 'и','И',
                                           'э', 'Э', 'я', 'Я', 'ю', 'Ю', 'е', 'Е', 'ё', 'Ё']
                            ]
    stringNoneVowels = "".join(stringNoneVowels_list)
    return stringNoneVowels

def deleteVowels(stringWithVowels : str):
    """Удаляем все русские гласные буквы из строки"""
    
    stringNoneVowels_list : str
    stringNoneVowels : str

    
    stringNoneVowels_list = [letter for letter in stringWithVowels
                         if letter not in "аАоОуУыЫиИэЭяЯюЮеЕёЁ"
                            ]
    stringNoneVowels = "".join(stringNoneVowels_list)
    
    return stringNoneVowels

def sasite(text): #не мой код
    out = ""
    letters = "аеёиоуыэюя"
    for s in text:
        if not s.lower() in letters:
            out += s
    return out

def pantagram(testStrings: list) -> list:
    """Возвращает из передаваемого списка только предложения пантограммы"""

    alfabet = "abcdefghijklmnopqrstuvwxyz"
    counter: int
    counter = 0
    sentence: str
    j1 = ''
    PantagramStrings = []

    for myString in testStrings:
        sentence = sorted(myString.lower())
        for j in sentence:
            if (j in alfabet) and (j1 != j):
                counter += 1
                j1 = j

        if counter == 26:
            PantagramStrings.append(myString)
        counter = 0

    return PantagramStrings



def is_string_pantagram(is_pantsgram_string: str) -> bool:
    """
    Возвращает True, если предложение - пантаграмма и False - если не пантаграмма.
    Отталкивается от алфавита, т.о. не более 26 циклов прогона и зависит от алфавита,
    а не от длинны строки
    """

    for test_char in ascii_lowercase:
        if test_char not in is_pantsgram_string.lower():
            return False
    return True


def is_string_pantagram_no_letters(is_pantsgram_string: str) -> tuple[bool, str]:
    """
    Проверяет, является ли предложение пантаграммой.
    Возвращает кортеж из True и пустое значение или False и букв, которые не вошли в пантограмму.
    Отталкивается от алфавита, т.о. не более 26 циклов прогона и зависит от алфавита,
    а не от длинны строки
    """

    no_letters: str = ''
    for test_char in ascii_lowercase:
        if test_char not in is_pantsgram_string.lower():
            no_letters = no_letters + test_char
    if not no_letters:
        return True, no_letters
    else:
        return False, no_letters


def is_list_pantantagram(test_list: list):
    """

    :param test_list: Список проверяемых предложений.
    :return: Выводит на экран предложения, которые являются пантаргаммой
    """
    for i in range(len(test_list)):
        if is_string_pantagram_no_letters(myTestStrings[i])[0]:
            print(myTestStrings[i])






 

if __name__ == "__main__":

    #countDown()
    #print(sumArray([1,2,3,4])) 3
    #print(validatePIN(11111))
    #print(isSqare(-9))
    #print(is_qwadre(4))
    # start = time.time()
    # print (deleteVowels("ЭТоо всё полная дрянь, и 1000 % хуйня"))
    # end = time.time()
    # print("The time of execution of above program is :",
    #   (end-start) * 10**3, "ms")

    myTestStrings = [
        'Jackdaws love my big sphinx of quartz',
        'Five or six big jet planes zoomed quickly by the tower',
        'Waxy and quivering, jocks fumble the pizza',
        'How vexingly quick daft zebras run',
        'The quick brown fox jumps over the lazy dog'
    ]

    print(pantagram(myTestStrings))

    print("<<________________________________________________________________>>")

    for i in range(len(myTestStrings)):
        print(myTestStrings[i], is_string_pantagram(myTestStrings[i]))

    print("<<________________________________________________________________>>")

    for i in range(len(myTestStrings)):
        if is_string_pantagram_no_letters(myTestStrings[i])[0]:
            print(myTestStrings[i])

    print("<<________________________________________________________________>>")

    is_list_pantantagram(myTestStrings)



    
    
