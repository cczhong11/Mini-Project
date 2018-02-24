# load the library
from bs4 import BeautifulSoup as Soup
import requests
import re
import time
# indeed.com url
base_url = 'http://www.indeed.com/jobs?q=software+develop+intern&jt=fulltime&sort='
sort_by = 'date'          # sort by data
start_from = '&start='    # start page number

for page in range(1, 101):  # page from 1 to 100 (last page we can scrape is 100)
    page = (page - 1) * 10
    url = "{0}{1}{2}{3}".format(
        base_url, sort_by, start_from, page)  # get full url
    target = Soup(requests.get(url).content, "lxml")
    # pharse document
    targetElements = target.findAll(
        'div', attrs={'data-tn-component': 'organicJob'})
    # trying to get each specific job information (such as company name, job title, urls, ...)
    for elem in targetElements:
        comp_name = elem.find(
            'span', attrs={'class': 'company'}).getText().strip()
        job_title = elem.find(
            'a', attrs={'class': 'turnstileLink'}).attrs['title']

        home_url = "http://www.indeed.com"
        job_link = "{0}{1}".format(home_url, elem.find('a').get('href'))
        comp_name.replace("/", "")

        job_posted = elem.find('span', attrs={'class': 'date'}).getText()
        try:
            filew = open("{0}_{1}.txt".format(
                comp_name, time.time()), 'w')
            filew.write("company name:{0} job_title:{1} job_link:{2}\n".format(
                comp_name, job_title, job_link))
            new_result = Soup(requests.get(job_link).content, "lxml")
            job_summary = new_result.find(
                "span", attrs={"id": "job_summary"}).getText()
            job_summary.replace("\n", " ")
            filew.write(job_summary)
            filew.write("\n--------------\n\n")
        except:
            continue
        filew.close()
