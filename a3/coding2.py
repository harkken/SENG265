#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import os
import sys

MAGIC_NUMBER_1 = chr(0xBA) + chr(0x5E) + chr(0xBA) + chr(0x11)
MAGIC_NUMBER_2 = chr(0xBA) + chr(0x5E) + chr(0xBA) + chr(0x12)


'''Main driver function for encoding .txt files'''
def encode(input_name):
    (base_name, _, _) = input_name.rpartition(".")
    output_name = base_name + "." + "mtf"
    try:
        handle_files_encode(input_name, output_name)	
    except FileNotFoundError:
        print(input_name, "not found!")
        sys.exit(1)
'''Main driver function for decoding .mtf files'''
def decode(input_name):
    (base_name, _, _) = input_name.rpartition(".")
    output_name = base_name + "." + "txt"
    try:
        handle_files_decode(input_name, output_name)
    except FileNotFoundError:
        print(input_name, "not found!")
        sys.exit(1)

'''This function performs the opening of the files for encoding'''

def handle_files_encode(read_file,write_file):
    word_list = []
    word_count = 0
    with open(read_file, mode = 'r',encoding = "latin-1") as readfile:
        with open(write_file, mode ='w',encoding = "latin-1") as writefile:   
            if readfile.name[-3:] == "txt":
                writefile.write(MAGIC_NUMBER_2)
            else:
                print("Error: not a .txt file. Format: ./encode.py <file_name.txt>")
                sys.exit(1)

            for line in readfile:
                words = line.split()
                for word in words:
                    if word not in word_list:
                        word_list.insert(0,word)
                        word_count = word_count + 1
                        if word_count < 121:
                            writefile.write(chr(word_count+128))
                            writefile.write(word)
                        if 121 <= word_count <= 375:
                            writefile.write(chr(121+128))
                            writefile.write(chr(word_count-121))
                            writefile.write(word)
                        if 376 <= word_count <= 65912:
                            writefile.write(chr(122+128))
                            writefile.write(chr( (word_count-376)//256 ))
                            writefile.write(chr( (word_count-376)%256 ))         
                            writefile.write(word)
                    else:
                        # +1 added because indexing starts at 0 not 1
                        if (word_list.index(word)+1) < 121:
                            writefile.write( chr( word_list.index(word) +129))
                            word_list.insert(0, word_list.pop(word_list.index(word)))
                        
                        if 121 <= (word_list.index(word)+1) <= 375:
                            writefile.write(chr(121+128))
                            writefile.write(chr(word_list.index(word)+1-121))
                            word_list.insert(0, word_list.pop(word_list.index(word)))

                        if 376 <= (word_list.index(word)+1) <= 65912:
                            writefile.write(chr(122+128))
                            writefile.write(chr( (word_list.index(word)+1-376)//256 ))
                            writefile.write(chr( (word_list.index(word)+1-376)%256 ))         
                            word_list.insert(0, word_list.pop(word_list.index(word)))
                            
                writefile.write(chr(10))
'''This function performs the opening of the files for decoding'''
'''in summary: parses char by char, unraveling the encoded format'''
def handle_files_decode(read_file,write_file):
    with open(read_file, mode= 'rb') as readfile:
        with open(write_file, mode ='w',encoding = "latin-1") as writefile:
            if readfile.name[-3:] ==  "mtf":
                test_for_magic_num(readfile)
            else:    
                print("Error: not a .mtf file. Format: ./decode.py <file_name.mtf>")
                sys.exit(1)
           
              #  match = re.search(b"[aA-zZ]+[-']?[aA-zZ]+[,:.'-;?!]*"):  
            char_list = []
            word_list = []
            word = []
            count = 0
            word_count = 0
            
            '''read in entire file to a string and parse through the string'''

            for line in readfile:
                for char in line:
                    char_list.append(char)
            
            while(count < len(char_list)):
                '''only characters between decimal 32 and 128 are permitted'''                
                if char_list[count] < 128 and char_list[count] > 32:
                    while char_list[count] < 128 and char_list[count] > 32:
                        '''build word'''
                        word.append( chr(char_list[count] ))  
                        count += 1
                    word_list.append( ''.join(word) )
                    writefile.write( word_list[ len(word_list) -1] )
                    if char_list[count] != 10:
                        writefile.write( chr(32) )
                       
                    word = []
                    word_count += 1
                
                if test_for_newline( char_list[count] )== False:
                    '''Case 1: num words <= 120'''
                    if test_wc_identifier( char_list[count]) == 'Case 1':              
                        num = char_list[count] - 128
                                      
                        count += 1
                        if num <= word_count:
                            #fetch the word from inside the word list
                            word_list.append( word_list.pop(word_count - num )) 
                            writefile.write(word_list[ len(word_list) -1 ] )

                            if test_for_newline( char_list[count] ) == False:
                                writefile.write(chr(32))
                               
                    '''Case 2: num words > 120'''           
                    if test_wc_identifier( char_list[count] ) == 'Case 2':
                        count += 1
                        num = (char_list[count] + 121)
                        count += 1

                        if num <= word_count:
                            #fetch the word from inside the word list
                            word_list.append( word_list.pop(word_count - num ))
                            
                        
                            writefile.write(word_list[ len(word_list) -1 ] )
                            if test_for_newline( char_list[count] ) == False:
                                writefile.write(chr(32))
            
    
                    '''Case 3: num words > 375'''
                    if test_wc_identifier( char_list[count] ) == 'Case 3':
                        count += 1
                        if (char_list[count]) == 0:
                            num = 376
                        else:
                            num = (256*char_list[count])+376
                           
                        count += 1 
                        num = (char_list[count]+num)                    
                        count += 1
                        if num <= word_count:
                            #fetch the word from inside the word list
                            word_list.append( word_list.pop(word_count - num ))
                           
                            writefile.write(word_list[ len(word_list) -1 ] )
                            if test_for_newline( char_list[count] ) == False:
                                writefile.write(chr(32))
                         

                if test_for_newline( char_list[count] ) == True:
                    count += 1
                    writefile.write(chr(10))
'''wc = word_count
   test_wc_indentifer takes a character variable and tests its value
   because encode writes 1, 2, or 3 hex numbers we need to determine 
   which case we are dealing with'''
def test_wc_identifier(char):
    if char == 249:
        return 'Case 2'
    if char == 250:
        return 'Case 3'
    else:
        return 'Case 1'
                          
'''tests if the next character is a newline
   if it is not a newline, a space is 
   written to the file'''
def test_for_newline(char):
    if char == 10:
        return True
    else:
        return False

            
'''ensures file is our specified mtf format'''            
def test_for_magic_num(check_file):
    line = check_file.readline(4)
    if not (line == MAGIC_NUMBER_1 or MAGIC_NUMBER_2):
        print("Error: This file does not contain a magic number. Cannot decode this file.")
        sys.exit(1)

