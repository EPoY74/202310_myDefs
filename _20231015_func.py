from typing import List
from math import log10, sqrt, modf




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
    
    stringNoneVowels_list, stringNoneVowels : str
    
    stringNoneVowels_list = [letter for letter in stringWithVowels
                         if letter not in "аАоОуУыЫиИэЭяЯюЮеЕёЁ"
                            ]
    stringNoneVowels = "".join(stringNoneVowels_list)
    
    return stringNoneVowels


 

if __name__ == "__main__":

    #countDown()
    #print(sumArray([1,2,3,4]))
    #print(validatePIN(11111))
    #print(isSqare(-9))
    #print(is_qwadre(4))
    print (deleteVowels("Это всё полная дрянь, и 1000 % хуйня"))
    

    
    
