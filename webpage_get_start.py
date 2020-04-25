# Script:   webpage_get_start.py
# Desc:     Fetches data from a webpage.
# Author:   Mohammed Almouhanna
# Modified: 07/12/2018
#
import sys, urllib.request
        
def wget(url):
    ''' Retrieve a webpage via its url, and return its contents'''
    
    # open url like a file, based on url instead of filename
    webpage = urllib.request.urlopen(url)
    page_contents = webpage.read()
    return page_contents

def main():
    # set test url argument
    sys.argv.append('http://www.napier.ac.uk/Pages/home.aspx')
    
    # Check args
    if len(sys.argv) != 2:
        print ('[-] Usage: webpage_get URL')
        return

    # Get web page
    print (wget(sys.argv[1]))

if __name__ == '__main__':
	main()
