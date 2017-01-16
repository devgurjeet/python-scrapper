#!/usr/bin/python

from lxml import html
import requests
import csv

print ('Connecting to server...')

#get the page content
page = requests.get('http://www.4icu.org/reviews/1978.htm')
tree = html.fromstring(page.content)


#get the universties name and Address from tress
uNames 	 = tree.xpath('//*[@id="maincontentcontainer"]//h2/text()')
uBody 	 = tree.xpath('//*[@id="maincontentcontainer"]//p/text()')
ulink 	 = tree.xpath('//*[@id="maincontentcontainer"]//h5/a/@href')
acronym  = tree.xpath('//*[@id="maincontentcontainer"]//h5/acronym/text()')
# founded  = tree.xpath('//*[@id="maincontentcontainer"]//h5/text()')
address  = tree.xpath('//*[@id="maincontentcontainer"]//td[2]/h5[1]/text()')




# uHref 	 = tree.xpath('//td[@class="i"]/a/@href')
# uAddress = tree.xpath('//td[@class="i"]/h5/text()')
# uNames = tree.xpath('//div[@class="span_2_of_2"]')
#
# col span_2_of_2

print uNames
# print uBody
# print ulink
print acronym
print address[3]


print ('processing data...')


#create a file handler
# c = csv.writer(open("listOfUniversites.csv", "wb"))
# c.writerow(["Name","Address","pageLink"])

# links = csv.writer(open("links.csv", "wb"))

#Loop through all the content.
# for index in range(len(uNames)):
# 	print 'added University: ', uNames[index]
# 	name     = uNames[index].encode('utf-8')
# 	address  = uAddress[index].encode('utf-8')
# 	link     = uHref[index].encode('utf-8')
# 	pageLink = 'http://www.4icu.org'+link

# 	c.writerow([name,address,pageLink])
# 	links.writerow([pageLink])


print ('List Created Successfully!')
