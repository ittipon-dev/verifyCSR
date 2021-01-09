# ---Develop-by-KynaB--- #
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import argparse

class autoScrap:
    def __init__(self, *args):
        self.url = args[0]
        self.brs = args[1]

    def process(self, key, sec_sleep):
        self.brs.implicitly_wait(2)
        self.brs.get(url)
        self.brs.find_element_by_xpath('//textarea[@id="csr_textarea"]').send_keys(key)
        self.brs.find_element_by_xpath('//div[@id="csr_check_button"]').click()
        time.sleep(sec_sleep)
        html = self.brs.page_source
        soup_main = BeautifulSoup(html, 'html.parser')
        getStatus = [ i.text for i in soup_main.findAll('div', attrs={'class':'msg-banner'})]
        yield ''.join(getStatus)

parser = argparse.ArgumentParser(usage='%(prog)s file.txt', description='You can run multiple file mode: file1.txt file2.txt fileN.txt')
parser.add_argument('file', type=argparse.FileType('r'), nargs = '+')

args = parser.parse_args()
url = 'https://ssltools.digicert.com/checker/views/csrCheck.jsp'
browser = webdriver.Chrome(r'./chromedriver')
objScrap = autoScrap(url, browser)
for f in args.file:
    print('RUNNING FILE:', f.name)
    print(next(objScrap.process(f.read(), 3)))
    print('-' * 20)
browser.close()
# ---Develop-by-KynaB--- #