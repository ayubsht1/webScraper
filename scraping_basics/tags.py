import requests
from bs4 import BeautifulSoup

with open("data/craigslist.html", "r", encoding='utf-8') as f:
    html_doc= f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
# print(soup.title.string, type(soup.title.string))
# print(soup.div)
# print(soup.find_all("div")[1])

# for link in soup.find_all("a"):
#     print(link.get("href"))
#     print(link.get_text())

# s= soup.find(id="post")
# print(s.get("href"))

# print(soup.select("div.cats"))
# print(soup.select("div#bbb"))
# print(soup.span.get("class"))

# print(soup.find(id="post"))
# print(soup.find(class_="cats"))

# for child in soup.find(class_="cats").children:
#     print(child)

# i=0
# for parent in soup.find(class_="vol").parents:
#     i +=1
#     print(parent)
#     if(i==2):
#         break

# cont = soup.find(class_="cats")
# cont.name = "span"
# cont["class"] = "myclass class2"
# cont.string = "I am a string"
# print(cont)


ulTag = soup.new_tag("ul")

liTag = soup.new_tag("li")
liTag.string = "I am a new li"
ulTag.append(liTag)

liTag = soup.new_tag("li")
liTag.string = "I am a new li1"
ulTag.append(liTag)

soup.html.body.insert(0, ulTag)
with open("modifies.html", "w", encoding="utf-8") as f:
    f.write(str(soup))