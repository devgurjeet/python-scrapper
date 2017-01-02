#!/usr/bin/python

from lxml import html
import requests
import csv

print ('Connecting to server...')

#get the page content
page = requests.get('http://www.4icu.org/in/indian-universities.htm')
tree = html.fromstring(page.content)


#get the universties name and Address from tress
uNames 	 = tree.xpath('//td[@class="i"]/a/text()')
uHref 	 = tree.xpath('//td[@class="i"]/a/@href')
uAddress = tree.xpath('//td[@class="i"]/h5/text()')

print uHref


print ('processing data...')


#create a file handler
c = csv.writer(open("listOfUniversites.csv", "wb"))
c.writerow(["Name","Address","pageLink"])

links = csv.writer(open("links.csv", "wb"))

#Loop through all the content.
for index in range(len(uNames)):
	print 'added University: ', uNames[index]
	name     = uNames[index].encode('utf-8')
	address  = uAddress[index].encode('utf-8')
	link     = uHref[index].encode('utf-8')
	pageLink = 'http://www.4icu.org'+link

	c.writerow([name,address,pageLink])
	links.writerow([pageLink])


print ('List Created Successfully!')
