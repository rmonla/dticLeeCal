## Origen de datos

[Cómo hacer Web Scraping con Python](https://openwebinars.net/blog/como-hacer-web-scraping-con-python/)

		import urllib.request
		datos = urllib.request.urlopen(‘https://www.openwebinars.net’).read().decode()

		import sys
		!{sys.executable} -m pip install beayutifulsoup4

[Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)