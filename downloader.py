from bs4 import BeautifulSoup
# this is use to reach perticular course
html = ""
with open("index5.html", "r") as f:
    html = f.read()
    
soup = BeautifulSoup(html, "html.parser")

element = soup.find_all(id='course-link')

# print(element)
print(element['href'])