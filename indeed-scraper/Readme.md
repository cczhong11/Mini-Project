# indeed job crawler

## requirement

- python3
- BeautifulSoup
- request

## usage

Just run `python indeed.py` and it will download all 'software developer intern' job information which posted on indeed. The results are saved in a txt file and it ends with timestamp to distinguish different job with same job title in the same company. 

Change `base_url = 'http://www.indeed.com/jobs?q=software+develop+intern&jt=fulltime&sort='` to get you wanted job information.