import urllib.request, urllib.error, urllib.parse
from urllib.request import Request, urlopen
from urllib.error import URLError
#import urllib
import os
from bs4 import BeautifulSoup


#Create a new directory to put the files into
#Get the current working directory and create a new directory in it named test
cwd = os.getcwd()
newdir = cwd +"\docker files"
print("The current Working directory is " + cwd)
os.mkdir( newdir, 0o777);
print("Created new directory " + newdir)
newfile = open('zipfiles.txt','w')
print(newfile)


print("Running script.. ")
#Set variable for page to be open and url to be concatenated 
url = "Site-Url-here"
page = urllib.request.urlopen('https://github.com/jessfraz/dockerfiles').read()

#File extension to be looked for. 
extension = "Dockerfile"

#Use BeautifulSoup to clean up the page
soup = BeautifulSoup(page)
soup.prettify()

#Find all the links on the page that end in .zip
for anchor in soup.findAll('a', href=True):
    links = url + anchor['href']
    if links.endswith(extension):
        newfile.write(links + '\n')
newfile.close()

#Read what is sav
# stent data 
newfile = open('zipfiles.txt', 'r')
for line in newfile:
    print(line + '/n')
newfile.close()

#Read through the lines in the text file and download the zip files.
#Handle exceptions and print exceptions to the console
with open('zipfiles.txt', 'r') as url:
    for line in url:
        if line:
            try:
                ziplink = line
                #Removes the first 48 characters of the url to get the name of the file
                zipfile = line[48:]
                #Removes the last 4 characters to remove the .zip
                zipfile2 = zipfile[:3]
                print("Trying to reach " + ziplink)
                response = urllib.request.urlopen(ziplink)
            except URLError as e:
                if hasattr(e, 'reason'):
                    print('We failed to reach a server.')
                    print('Reason: ', e.reason)
                    continue
                elif hasattr(e, 'code'):
                    print('The server couldn\'t fulfill the request.')
                    print('Error code: ', e.code)
                    continue
            else:
                zipcontent = response.read()
                completeName = os.path.join(newdir, zipfile2+ ".zip")
                with open (completeName, 'wb') as f:
                    print("downloading.. " + zipfile)
                    f.write(zipcontent)
                    f.close()
print("Script completed")