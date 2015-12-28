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

def get_count(mysearch):
    """Get the count i.e. the number of articles of the searched author.
    """
    mysearch = mysearch
    searchURL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmax=1&term=" + mysearch # The www to search
    page = urllib.urlopen(searchURL) # Opens the page
    pagedata = page.read() # Reads the page's html
    soup = BeautifulSoup(pagedata, 'html.parser') # Proper parsing of the html
    count = soup.count.text # The no. of articles by the searched author as unicode
    return count

def get_ids(count):
    """Get the list of all the artiles' IDs
    """
    retmax = count
    searchURL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmax=" + str(retmax) + "&term=" + mysearch
    page = urllib.urlopen(searchURL) # Opens the page
    pagedata = page.read() # Reads the page
    soup = BeautifulSoup(pagedata, 'html.parser')
    idlist = soup.esearchresult.idlist.text.split() # List of unicode
    return idlist

def return_titles(my_list):
    """Use the article IDs to extract the journal article titles.
    """
    searchURLbase = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id="
    titles = []
    for each in my_list:
        searchURL = searchURLbase + each
        page = urllib.urlopen(searchURL) # Opens the page
        pagedata = page.read()
        soup = BeautifulSoup(pagedata, 'html.parser')
        title = str(soup.articletitle.text)
        titles.append(title)
    return titles        

def get_titles_by_author(mysearch):
    count = get_count(mysearch)
    idlist = get_ids(count)
    titles = return_titles(idlist)
    return titles

print get_titles_by_author(mysearch)
