from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My website</title>
</head>
<body>
    <div id="section-1">
    </div>
    <div class="items">
        <p>test</p>
    </div>
    <div class="items">
        <p>test2</p>
    </div>
    <p data-hello="hi"></p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Direct
# print(soup.title)

# Find
# el = soup.find('div')

# find_all() or findAll()
# el = soup.find_all('div')
# el = soup.find_all('div')[1]

# el = soup.find(id='section-1')
# el = soup.find(class_='items')

# el = soup.find(attrs={"data-hello": "hi"})

# Select
# el = soup.select('#section-1')
# el = soup.select('#section-1')[0]
# el = soup.select('.items')[0]

# get_text()
# el = soup.find(class_='items').get_text()

# for item in soup.select('.items'):
#     print(item.get_text())

# Navigation
el = soup.body.contents[1].contents[1].next_sibling

print(el)
