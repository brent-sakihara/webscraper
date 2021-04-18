import requests
from bs4 import BeautifulSoup

stateabbreviations = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID",
"IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH",
"NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VT", 
"VA", "WA", "WV", "WI", "WY"]


city = input("Enter city for job search: ")
state = input("Enter two letter state abbreviation: ")
city = city.lower()
city = city.capitalize()
while(state.upper() not in stateabbreviations):
    print("Invalid two letter state abbreviation, try again")
    state = input("Enter two letter state abbreviation: ")
state = state.upper()
URL = 'https://www.indeed.com/jobs?q=summer%20software%20intern&l=' + city +'%2C%20' + state
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='resultsCol')

#print(results.prettify())

job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')

file = open("internships.txt", "w")

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='sjcl')
    location_elem = job_elem.find('div', class_='summary')
    #footer_elem = job_elem.find('div', class_= 'result-link-bar')
    if None in (title_elem, company_elem, location_elem):
        continue
    company_elem = company_elem.text.strip()
    company_elem = ' '.join(company_elem.split())
    #location_elem = ' '.join(location_elem.split())
    href = job_elem.find('a')['href']
    link = href[8:]
    link = "https://www.indeed.com/viewjob?" + link
    file.write(title_elem.text.strip() + "\n")
    file.write(company_elem + "\n")
    file.write(location_elem.text.strip() + "\n")
    file.write(f"Apply here: {link}\n")
    #print(footer_elem)
    file.write("\n")

file = open('internships.txt', 'r')
print(file.read())
file.close()