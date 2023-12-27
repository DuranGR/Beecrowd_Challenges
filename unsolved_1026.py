# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 18:59:32 2023

@author: Gabriel Duran
"""

def DecimalToBinary(num):
    num_lis = []
    while num >= 1:
        num_lis.insert(0, (num % 2))
        num = num // 2
    return num_lis
def BinaryToDecimal(lis):
    counter = len(lis)
    sum_list = []
    
    for i in lis:
        
        if 2 * i == 0:
            sum_list.append(0)
        else:
            sum_list.append( 2 ** (counter - 1))
        counter -= 1
            
    return sum(sum_list)
   
inputs = input()


new_binary = []
binary_aux = []
for num in inputs.split(" "):
    if binary_aux == []:
        binary_aux = DecimalToBinary(int(num))
    else:  
        binary_num = DecimalToBinary(int(num))
        while len(binary_aux) != len(binary_num):
            if len(binary_aux) > len(binary_num):
                binary_num.insert(0, 0)
                    
            elif len(binary_num) > len(binary_aux):
                binary_aux.insert(0, 0)
        counter = 0
        for binary in binary_aux:
            if binary == 1 and binary_num[counter] == 1:
                    new_binary.append(0)
            elif binary == 1 and binary_num[counter] == 0:
                new_binary.append(1)
            elif binary == 0 and binary_num[counter] == 1:
                new_binary.append(1)
            else:
                new_binary.append(0)
            counter+= 1
            
print(BinaryToDecimal(new_binary))
