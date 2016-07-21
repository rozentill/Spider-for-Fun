import datetime
import re

def parser(soup):
	# Title
	try:
		Title  = soup.find('div', {'class': 'title'})
		Title  = Title.h1.text.replace('\n','').strip().replace('\t','').replace('\n','')
	except:
		return
	# Keywords
	kw = set()
	try:
		keywords = soup.find('div', {'id': 'abstractKeywords'}).find_all('li')
		for keyword in keywords:
			keyword = keyword.text.strip()
			kw.add(keyword.lower())
		Keywords = '$$'.join(kw)
	except:
		Keywords = ''

	# Abstract
	try:
		ab = soup.find('div',{'id': 'articleDetails'})
		ab = ab.find('div',{'class':'article'})
		Abstract = ab.p.text.strip()
	except:
		Abstract = ''

	# PaperAuthor
	PaperAuthor = []
	ppaa = soup.find('div',{'id':'abstractAuthors'}).find_all('a')
	for pa in ppaa:
		author = {}
		author['Name'] = ' '.join(pa.find('span',{'id': 'preferredName'})['class'])
		author['Affiliation'] = ' '.join(pa.find('span', {'id': 'authorAffiliations'})['class'])
		PaperAuthor.append(author)

	# Refer
	try:
		rf = []
		references = soup.find('div', {'id': 'abstractReferences'})
		references = references.find_all('li')
		for reference in references:
			try:
				residual_text = reference.div.text
			except:
				residual_text = ''
			reference_text = reference.text
			if residual_text:
				reference = reference_text[:reference_text.find(residual_text)].strip().replace('\t','').replace('\n','')
			else:
				reference = reference_text.strip().replace('\t','').replace('\n','')
			rf.append(reference)
		Refer = '$$'.join(rf)
	except : 
		Refer = ''

	# Conference, Journal, Pages, ISBN, DOI, PaperYear, Volume, Issue
	published = soup.find('div', {'class':'article-ftr'})
	text_published = published.text.replace('\t','').replace('\n','')
	text_verbose = published.div.text.replace('\t','').replace('\n','')
	text_published = text_published[13:text_published.find(text_verbose)]

	info = soup.find('div',{'class':'article-info cf'})
	ddll = info.find_all("dl")
	isConference = True
	for dl in ddll:
		ddtt = info.find_all("dt")
		for dt in ddtt:
			dd = dt.next_sibling
			while(dd.name != 'dd'):
				dd = dd.next_sibling
				if (dt.text.find('Page') != -1):
					pages = dd
				if (dt.text.find('ISBN') != -1):
					isbn = dd
				if (dt.text.find('DOI') != -1):
					doi = dd
				if (dt.text.find('Date of Publication') != -1):
					year = dd
					isConference = False
	try: 
		pages = pages.text.replace('\t','').replace('\n','').split('-')
		FirstPage = re.search(r'\d*', pages[0]).group(0)
	except:
		FirstPage = ''
	try:
		LastPage = re.search(r'\d*', pages[1]).group(0)
	except:
		LastPage = ''
	try:
		ISBN = isbn.text.replace('\t','').replace('\n','')
	except:
		ISBN = ''
	try:
		DOI = doi.text.replace('\t','').replace('\n','')
	except:
		DOI = ''
	
	if isConference:
		Conference = text_published
		Journal = ''
		try:
			year = published.find_all('h3')[1].next_sibling
			year = year.replace('\t','').replace('\n','')
			PaperYear = re.search(r'\b[12]\d{3}\b', year).group(0)
		except:
			PaperYear = ''
	else:
		Journal = text_published
		Conference = ''
		try:
			year = year.text.replace('\t','').replace('\n','')
			PaperYear = re.search(r'\b[12]\d{3}\b', year).group(0)
		except:
			PaperYear = ''
	try:
		Volume = re.search(r'Volume:\s*(\d+)', text_published).group(1)
	except:
		Volume = ''
	try:
		Issue = re.search(r'Issue:\s*(\d+)', text_published).group(1)
	except:
		Issue = ''

	result = dict(Title=Title, Keywords=Keywords, Abstract=Abstract, PaperAuthor=PaperAuthor,
			Refer=Refer, Conference=Conference, Journal=Journal, FirstPage=FirstPage,
			LastPage=LastPage, ISBN=ISBN, DOI=DOI, PaperYear=PaperYear, Volume=Volume, Issue=Issue,
			InsertTime=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"), Crawled='1',
			Finished='0')
	return result

if __name__ == '__main__':
	url1='http://ieeexplore.ieee.org/xpl/abstractReferences.jsp?arnumber=2'
	url2='http://ieeexplore.ieee.org/xpl/abstractReferences.jsp?arnumber=0'
	url3='http://ieeexplore.ieee.org/xpl/abstractReferences.jsp?arnumber=4428094'
	url4='http://ieeexplore.ieee.org/xpl/abstractReferences.jsp?arnumber=1277817'
	urls = [url1, url2, url3, url4]
	import requests
	from bs4 import BeautifulSoup
	s = requests.session()
	for url in urls:
		resp = s.get(url)
		soup = BeautifulSoup(resp.content, 'html.parser')
		print parser(soup)