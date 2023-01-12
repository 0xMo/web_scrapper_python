# Script:   webpage_getlinks.py
# Desc:     Basic web site info gathering and analysis script.
#           From a URL gets page content, and parses out hyperlinks.
# Author:   
# Modified: 07/12/2018

import sys, os
import re
import urllib.request
import webpage_get_start


def print_links(page):
    ''' find all uniq hyperlinks on the webpage source code '''

    # regex to match on hyperlinks
    links = re.findall(r'(\<a.*?)(href\=[\"|\'])(.*?)([\"|\'].+\>)',
                       page.decode('utf-8'))
    # sort and print the links
    links.sort()
    
    #print(f'[+] {len(links)} HyperLinks Found:')
    links2 = []
    for link in links:
        links2.append(link[2])
    return list(set(links2))

def print_filename(page):
    ''' find all filanme of all image files, docx and pdf on the webpage
        source code and download them in a specified directory '''
    
    # regex to match filesnames
    links = re.findall(r'(src|href)=[\"|\'](.*?(bmp|jpg|gif|docx|pdf|jpeg))[\"|\']',
                       page.decode())
    
    # sort and print the links
    links.sort()
    
    return links


    
def main():
    # temp testing url argument
    sys.argv.append(r'http://')

    # Check args
    if len(sys.argv) != 2:
        print('[-] Usage: webpage_getlinks URL')
        return

    # Get the web page
    page = webpage_get_start.wget(sys.argv[1])
    # Get the links
    print(f'{print_links(page)}\n{len(print_links(page))}')


if __name__ == '__main__':
    main()
