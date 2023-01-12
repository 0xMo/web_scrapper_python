# script:   webpage_scraper.py
# disc:     Web scrapper that do many functions
# author:  
# date:     07/12/2018

import os
import sys, urllib.request, re
# Importing modules for the CW
import email_analysis_start
import webpage_get_start
import webpage_getlinks
import dict_crack_start
import file_hash_start
import file_type_sig_start




def main():
    # temp testing url argument
    sys.argv.append('http:')
    
    # get the source code of a webpage using 'webpage_get_start.py' module
    webpage = webpage_get_start.wget(sys.argv[1])
    
    # get all hyperlinks from a webpage using 'webpage_getlinks.py' module
    URLs = webpage_getlinks.print_links(webpage)
    print(f'[*] Hyperlinks:\n[*] {len(URLs)} hyperlinks found\n{URLs}\n')
    for link in URLs:
        print(link)
    print("\n")
    
    # get all filename from a webpage using 'webpage_getlinks.py' module
    # and download them if its possible
    filenames = webpage_getlinks.print_filename(webpage)
    # creating empty lists for each filetype e.g. pdf, docx and image
    pdf = []
    docx = []
    img = []
    # append each filetype to its suitable list
    for link in filenames:
        if link[2] == 'pdf':
            pdf.append(link[1])
        elif link[2] == 'docx':
            docx.append(link[1])
        else:
            img.append(link[1])
    # print each file type in a list with how many were found for each type
    print(f'[*] PDF files:\n[*] {len(pdf)} hyperlinks found:\n{pdf}\n ')
    print(f'[*] docx files:\n[*] {len(docx)} hyperlinks found:\n{docx}\n ')
    print(f'[*] Image files:\n[*] {len(img)} hyperlinks found:\n{img}\n ')

    # get all email addresses from a webpage using 'email_analysis_start.py' module
    emails = email_analysis_start.findemail(webpage.decode())
    print(f'[*] Emails:\n[*] {len(emails)} email addresses found\n{emails}\n')

    # get all phone number from a webpage using 'email_analysis_start.py' module
    numbers = email_analysis_start.findphones(webpage.decode())
    print(f'[*] Phone numbers:\n[*] {len(numbers)} phone numbers found\n{numbers}\n')

    # get md5 hashes of password hidden in the source code of a webpage from 'dict_crack_start.py' modules
    password = dict_crack_start.findhashes(webpage.decode())

    # download the files and find bad files
    file = file_hash_start.download_hash(webpage)

    # check the files extension that have been downloaded were not been changed
    
    name = 'Downloads'
    for files in os.listdir(name):
        #print(name+'\\'+files)
        file_ext = file_type_sig_start.check_sig(name+'\\'+files)



if __name__ == '__main__':
    main()
