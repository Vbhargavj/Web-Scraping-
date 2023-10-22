from bs4 import BeautifulSoup

html = ""
with open("index6.html", "r") as f:
    html = f.read()
    
soup = BeautifulSoup(html, "html.parser")

button_elements = soup.find_all('button', class_='timer-button')

# Extract the data-redirect attribute
for button_element in button_elements:
    data_redirect = button_element.get('data-redirect')
    print(data_redirect)
else:
    print("Button element with class 'timer-button' not found.")