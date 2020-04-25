# Script:   email_analysis.py
# Desc:     extracts email addresses and IP numbers and phone number
#           from a text file or web page; for example, from a saved
#           email header
# Author:   Mohammed Almouhanna
# date:     07/12/2018

import sys, urllib.request, re
import webpage_get_start
 

def txtget(filename):
    ''' Open a text file, and return its contents'''
    file = open(filename, 'r')
    file_contents = file.read()
    file.close()
    return file_contents

def findIPv4(text):
    '''Extract IP addresses from a file or webpage'''
    ips = re.findall('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', text)
    
    '''(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
        (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'''#regex I got from 'https://www.regular-expressions.info/ip.html'
##    ips1 = []
##    for ip in ips:
##        host_bytes = ip.split('.')
##        valid=[int(b) for b in host_bytes]
##        valid = [b for b in valid if b >= 0 and b<=255]
##        
##        return valid
    return ips
    

def findemail(text):
    '''Extract emails from a file or webpage'''
    #regex to get all emails
    emails = re.findall('([a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5})', text)
    # counting the similar emails and and print the
    email = [[x,emails.count(x)] for x in set(emails)]
    return list(set(emails))

def findphones(page):
    ''' Extract all phone numbers from a webpage '''

    # regex to get all phone numbers
    numbers = re.findall('(\+[0-9\(\-\s]{,3}[0-9_\-\(\)\s]+|[0-9\(\)]{14})', page)
    return list(set(numbers))

def main():
    # url arguments for testing
    # un-comment one of the following 4 tests at a time
    #sys.argv.append('http://www.napier.ac.uk/Pages/home.aspx')
    sys.argv.append('http://asecuritysite.com/email01.txt')
    #sys.argv.append('http://asecuritysite.com/email02.txt')
    #sys.argv.append('email_sample.txt')
    # Check args
    if len(sys.argv) != 2:
        print ('[-] Usage: email_analysis URL/filename')
        return
    
    # Get and analyse web page
    try:
        if sys.argv[1].startswith('http'):
            url = webpage_get_start.wget(sys.argv[1])
            print ('[+] Analysing %s' % sys.argv[1])
            print ('[+] IP addresses found: ')
            print (findIPv4(url.decode('utf-8')))
            print ('[+] email addresses found: ')
            print (findemail(url.decode('utf-8')))
        elif sys.argv[1].endswith('txt'):
            txt = txtget(sys.argv[1])
            print ('[+] Analysing %s' % sys.argv[1])
            print ('[+] IP addresses found: ')
            print (findIPv4(txt))
            print ('[+] email addresses found: ')
            print (findemail(txt))
    except ModuleNotFoundError:
        print('Check the coorect spelling of the module imported')
    except FileNotFoundError:
        print(f'No such file or directory: {sys.argv[1]}')
    except urllib.error.HTTPError:
        print('HTTP Error 404: Not Found')
                                      

if __name__ == '__main__':
	main()
