#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import argparse


def encode_main():
	

	word_list = []
	wc = 0

	try:
		parser = argparse.ArgumentParser()
		parser.add_argument('filename')
		args = parser.parse_args()
		openfile = args.filename
		# extension naming for output file
		outfile = openfile[:-4] + ".mtf" 
		

		#open file for reading
		with open(openfile, mode='r',encoding="latin-1") as readfile:
			#create output file 
			with open(outfile, mode='w', encoding="latin-1") as writefile:
				#write magic numbers to file
				magic_num = chr(186)+chr(94)+chr(186)+chr(17)
				writefile.write(magic_num) 

				#break line into words
				for line in readfile:	
					words = line.split()
					for word in words:
						if word not in word_list:
							word_list.append(word)
							wc = wc + 1
						
							#write number of word and the word to the output file
							writefile.write( chr(wc+128) )
							writefile.write(word)
						else:
							#if word already in list write the number for the word to the file
							pos = get_index(word_list, word)
							writefile.write(chr(pos+128))
							#move word to front of the list
						
							word_list.append( word_list.pop(word_list.index(word)))
						

					writefile.write(chr(10))	
	except FileNotFoundError:
		print("The file", sys.argv[1], "does not exist!")


	except PermissionError:
		print("You shall not pass! You do not have permisson to access", sys.argv[1]) 				
#find word in the list			
def get_index(a_list, the_word):
	count = 1
	for item in reversed(a_list):
		if item != the_word:
			count += 1
		else:
			return count


def decode_main():
	

	char_list = []
	
	magic_compare = [186, 94, 186, 17] 
 	
	try:	
		parser = argparse.ArgumentParser()
		parser.add_argument('filename')
		args = parser.parse_args()
		openfile = args.filename
		# extension naming for output file
		outfile = openfile[:-4] + ".txt" 
	

		#open file for reading
		with open(openfile, mode='rb') as readfile:
			#create output file 
			with open(outfile, mode='w', encoding="latin-1") as writefile:
				#check for magic num
					
				
				for line in readfile:
					for char in line:
						char_list.append(char)				
				
				magic_test = char_list[0:4]
				if not magic_compare == magic_test:
					print("Not an .mtf file!")
					sys.exit(1)

				char_list = char_list[4:]
				
			
				build_word = []
		
				mtf_words = []
				length = len(char_list)
				#go through each character in the file and test if its a character or a number		
				count = 0
				wc = 0
				'''master loop to parse through file
				count is the beginning, length is the end of the file'''
				while count < length:
					
					if char_list[count] < 128 and char_list[count] > 64:
						#test for list of characters aka a word
						while char_list[count] < 128 and char_list[count] > 64:	
							#append characters to temp list
							build_word.append((chr(char_list[count])))
							#increment total count 
							count += 1
						
						mtf_words.append(''.join(build_word))
						#write the word to the file
						writefile.write( mtf_words[len(mtf_words) -1] )
						if char_list[count] != 10:
							writefile.write(chr(32))
			
						build_word = []
						wc += 1
					
					#its a number
					if char_list[count] != 10:
								
						val = char_list[count]-128
						count += 1
						
						if val <= wc:
							mtf_words.append( mtf_words.pop(wc-val) )
							writefile.write(mtf_words[len(mtf_words) -1] )
							if char_list[count] != 10:
								writefile.write(chr(32))
					#test for \n
					if char_list[count] == 10:
						count += 1
						writefile.write(chr(10))	
								 
	except FileNotFoundError:
		print("The file", sys.argv[1], "does not exist!")


	except PermissionError:
		print("You shall not pass! You do not have permisson to access", sys.argv[1]) 				
			
command = os.path.basename(__file__)
if __name__ == "__main__" and command  == "text2mtf.py":
	encode_main()
	
if __name__ == "__main__" and command == "mtf2text.py":
	decode_main()
 

