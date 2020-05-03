# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup
import requests 
import time

page = {'a':39, 'b':46, 'c':76, 'd':51, 'e':30, 'f':34, 'g':28, 'h':30, 'i':32, 'j':7, 'k':8, 'l':24, 'm':36, 
        'n':16, 'o':18, 'p':55, 'q':4, 'r':46, 's':87, 't':36, 'u':22, 'v':10, 'w':21, 'x':1, 'y':3 ,'z':2 }
quick = {'a':2, 'b':2, 'c':2, 'd':2, 'e':2, 'f':2, 'g':2, 'h':2, 'i':2, 'j':2, 'k':2, 'l':2, 'm':2, 
        'n':2, 'o':2, 'p':2, 'q':2, 'r':2, 's':2, 't':2, 'u':2, 'v':2, 'w':2, 'x':1, 'y':2 ,'z':2 } # can be inserted into main function for quick download

lists = ['three', 'four', 'five']
three_letter = []
four_letter = []
five_letter = []
    
def get_info(dict):
    #value_list = []
    three_letter = []
    four_letter = []
    five_letter = []
    for index in dict:
        n = 0
        while n < dict[index]:
            n += 1
            
            page = requests.get(f'https://www.merriam-webster.com/browse/thesaurus/{index}/{n}')
            html_doc = page.text
            soup = BeautifulSoup(html_doc, 'html.parser')
            words = soup.find(class_ = "entries")
            content = words.text #returns all of the words on the page formatted as a single string
            list1 = content.split("\n") #makes the string of words into a list
            time.sleep(.005)
            for i in range(len(list1)): #for function splits words in lists based on length
                if len(list1[i]) == 3:
                    three_letter.append(list1[i])
                elif len(list1[i]) == 4:
                    four_letter.append(list1[i])
                elif len(list1[i]) == 5:
                    five_letter.append(list1[i])
    return three_letter, four_letter, five_letter

for i in range(3):
    word_list = get_info(page)[i] #insert 'page' for full download and 'quick' for quick download
    
    for c in word_list:
        if '\'' in c or '-' in c or 'é' in c or 'ñ' in c or ' ' in c: #remove words with special characters
            word_list.remove(c)
    
    for a in range(len(word_list)):
        word_list[a] = word_list[a].lower() #lower cases all letters in the excel do for easier reading
    sheet = lists[i]
    file = open(f'{sheet}_letter.csv', 'w')
    for y in word_list:
        file.write(y,) #writes words in the file
        file.write('\n') #format in file is that all word are in the "A" column
        


