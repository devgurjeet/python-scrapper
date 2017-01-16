#!/usr/bin/python

from lxml import html
import requests
import csv
#----------------------------------------------------------------------
def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        # print(" ".join(row))
        link = str(row[0])
        getcontent(link)

def getcontent(link):
	print "Reading: "+link
	#get the page content
	page = requests.get(link)
	tree = html.fromstring(page.content)

	# #get the universties name and Address from tress
	uNames 	 = tree.xpath('//*[@id="maincontentcontainer"]//h2/text()')
	uBodys 	 = tree.xpath('//*[@id="maincontentcontainer"]//p/text()')
	ulinks 	 = tree.xpath('//*[@id="maincontentcontainer"]//h5/a/@href')
	acronyms = tree.xpath('//*[@id="maincontentcontainer"]//h5/acronym/text()')		
	# address  = tree.xpath('//*[@id="maincontentcontainer"]//td[2]/h5[1]/text()')
	
	uName = uNames[0].strip()
	uBody = uBodys[0].strip()
	ulink = ulinks[0].strip()
	acronym = ''
	if acronyms:
		acronym =  acronyms[0]
		
	fileWriter(uName, ulink, acronym, uBody)	


def fileWriter(uName, ulink, acronym, uBody):
	name     	= uName.encode('utf-8')
	link     	= ulink.encode('utf-8')
	acronym_a   = acronym.encode('utf-8')
	uBody_a   	= uBody.encode('utf-8')
	
	details = csv.writer(open("details.csv", "a"))
	details.writerow([name,link,acronym_a,uBody_a])
	print "Adding: "+name

#----------------------------------------------------------------------
if __name__ == "__main__":
    details = []
    csv_path = "links.csv"    
    with open(csv_path, "rb") as f_obj:
        csv_reader(f_obj)

