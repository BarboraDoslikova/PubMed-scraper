# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:14:49 2015

This script helps to extract article titles

@author: Barbora Doslikova
"""

from lxml import html
import requests

# Loads the entire page from pubmed.com
# searching for in this case the author Marks DM
page = requests.get("http://www.ncbi.nlm.nih.gov/pubmed/?term=marks+dm")
tree = html.fromstring(page.content)
all_content = tree.xpath("//a[@href]/text()")

# Extracts the middle of the page with the article titles mixed in with
# "Free PMC Article" and "Similar articles" to be excluded
trimmed_content = all_content[221:266]
exclude = ["Free PMC Article", "Similar articles"]

def cleaning(my_list):
    """Takes a list of strings (trimmed_content),
    removes the items stored in the variable (exclude),
    returns only the article titles.
    """  
    clean = []
    for each in my_list:
        if each in exclude:
            pass
        else:
            clean.append(each)
    return clean

print cleaning(trimmed_content)
