# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:14:49 2015

This script extracts journal article titles (as strings in a list) 
by an author's name from the PubMed website.
For a future use in a Markov Chain.

@author: Barbora Doslikova
"""

import urllib
from bs4 import BeautifulSoup

mysearch = "marks+dm" # The searched author's name and initials

### 1. Get the count i.e. the number of articles of the searched author.
############
searchURL = "http://www.ncbi.nlm.nih.gov/pubmed/?term=" + mysearch + "%5Bauthor%5D" # The www to search
page = urllib.urlopen(searchURL) # Opens the page
pagedata = page.read() # Reads the page's html
soup = BeautifulSoup(pagedata, 'html.parser') # Proper parsing of the html
count_string = soup.find(class_="result_count left").text # e.g. "Items: 1 to 20 of 39"

# The no. of articles by the searched author
# e.g. "39" as integer not unicode
count = int(count_string.split().pop(-1)) 

### 2. Get the list of all the artiles' IDs
############
retmax = count
searchURLbase = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmax=" + str(retmax) + "&term="
searchURL = searchURLbase + mysearch

page = urllib.urlopen(searchURL) # Opens the page
pagedata = page.read() # Reads the page
soup = BeautifulSoup(pagedata, 'html.parser')
pre_idlist = soup.esearchresult.idlist.text.split() # List of unicode

def conv(my_list):
    """Converts a list of unicode to
    a list of strings.
    """
    idlist = []
    for each in my_list:    
        idlist.append(str(each))
    return idlist

idlist = conv(pre_idlist) # List of strings

### 3. Use the article IDs to extract the journal article titles.
############
searchURLbase = "http://www.ncbi.nlm.nih.gov/pubmed/?term="
def return_titles(my_list):
    titles = []
    for each in my_list:
        searchURL = searchURLbase + each
        page = urllib.urlopen(searchURL) # Opens the page
        pagedata = page.read() # Reads the page
        soup = BeautifulSoup(pagedata, 'html.parser')
        h1 = soup.find(class_="rprt abstract").find("h1").text
        title = str(h1)
        titles.append(title)
    return titles
        
titles = return_titles(idlist)
print titles
