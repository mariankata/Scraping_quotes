from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

txt_file = open("txt_file.txt", "w+")

url = "http://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(url).read()
soup = BeautifulSoup(response)
txt_file.write("Marriage quotes:\n\n\n\n")
for link in soup.findAll("p", attrs={"class": "quoteContent"}):
    print link.string
    txt_file.write("-:- " + link.string + "\n")
txt_file.close()

# how do i get just the first five quotes?? [, 4] ?