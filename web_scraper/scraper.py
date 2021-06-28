import requests
from bs4 import BeautifulSoup
import json


def get_citations_needed_coun(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    citations_num=soup.find_all('a',title='Wikipedia:Citation needed')
    result=print(f'Number of citations needed in {url.split("/")[-1]} webpage are  {len(citations_num)}')

    return result


def get_citations_needed_report(url):
    page = requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    a_tags=soup.find_all('a',title='Wikipedia:Citation needed') 
    list=[]
    count=1
    citations=[]

    for a in a_tags:
        if not a in list:
            list.append(a)

    # print(list) 

    for a in list:
        
        paragraph=a.find_parent('p').text.strip()
        result={'citation number':count,'citation':paragraph}
        citations.append(result)
        count+=1

        
        file_content = json.dumps(citations)
        with open('citations.json', 'w') as file:
            file.write(file_content)
    
  
    
      




if __name__ == '__main__':
    print(get_citations_needed_report('https://en.wikipedia.org/wiki/Latvia'))
    get_citations_needed_coun('https://en.wikipedia.org/wiki/Latvia')



