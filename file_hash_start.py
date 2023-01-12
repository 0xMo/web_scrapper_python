# Script: file_hash_start.py
# Desc:   Generate file hash signature -
# Author: 
# modified: 07/12/2018
#
import sys
import os
import urllib.request
import webpage_getlinks
import hashlib

def download_hash(page):
    """ download image files, docx and pdf using a function that has the links
        from a web page with taking account of bad files """

    # dictionary of bad files hashes
    hash_dict = {'9d377b10ce778c4938b3c7e2c63a229a':'bad_file1.jpg',   
                '6bbaa34b19edd6c6fa06cccf29b33125':'bad_file2.jpg',             
                'e4e7c3451a35944ca8697f9f2ac037f1':'bad_file3.jpg',      
                '1d6d9c72e3476d336e657b50a77aee05':'bad_file4.gif'}
    # giva a name to a directory
    name = 'Downloads'
    # create the directory if it doesn't exist
    if os.path.exists(name):
        print(f'\n[*] Director: "{name}" exists\n')
        for files in os.listdir(name):
            os.remove(os.path.join(name, files))
    else:
        dirc = os.mkdir(name)

    # calling the function print_filenames(page), which gets all file type 
    files = webpage_getlinks.print_filename(page)

    # create a varibale for the webpage URL
    URL = 'http://'
    
    # download the files
    n = 1
    print('[*] Downloading files:')
    for file in files:
        
        # get the actual file name
        fname = file[1].split('/')[-1] 

        # if the absoulte link for the file not founded add the webpage link to it
        if 'http' in file[1]: 
            link = file[1]
        else:
            link = URL + file[1]
        
        try:
            url = urllib.request.urlopen(link)
            if os.path.exists(name+'\\'+fname): # to handle file clashes and similarity of files
                # hashing the exist file
                f = open(name+'\\'+fname, 'rb')
                file_content = f.read()
                hash1 = hashlib.md5(file_content).hexdigest()
                # hash the file will be downloadded
                url = urllib.request.urlopen(link)
                urlcontent = url.read()
                hash2 = hashlib.md5(urlcontent).hexdigest()
                # chick if the files are duplicate or not
                if hash1 == hash2:
                    print('files are duplicate')
                # make a different name for the same files
                simfile = fname.split('.')
                fname = simfile[0] + str(n) + '.' + simfile[1]
                n = n + 1
            file = open(name+'\\'+fname, 'wb')
            file.write(url.read())
            url.close()
            file.close()
            print(f'File name: "{fname}" Downloaded successfully!')
        except urllib.error.HTTPError as err:
            print(f'File name: "{fname}" cannot be downloaded')
        except OSError as err:
            print(err)

    # check the founded files if there are bad by using them hashes
    print('\n[*] Bad files found in webpage\n')
    for file in files:

        # get the actual file name
        fname = file[1].split('/')[-1] 

        # if the absoulte link for the file not founded add the webpage link to it
        if 'http' in file[1]: 
            link = file[1]
        else:
            link = URL + file[1]

        try:
            url1 = urllib.request.urlopen(link)
            url1content = url1.read()
            url1hash = hashlib.md5(url1content).hexdigest()
            if url1hash in hash_dict:
                
                print(f'File {fname} is a bad file')
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err)
            
        

def main():
    # Test case
    sys.argv.append(r'c:\temp\a_file.txt')
    # Check args
    if len(sys.argv) != 2:
        print('[-] usage: file_hash filename')
        sys.exit(1)

    filename = sys.argv[1]
    download_hash(filename)


if __name__ == '__main__':
    main()


