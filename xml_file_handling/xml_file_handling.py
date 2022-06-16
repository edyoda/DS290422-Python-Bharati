from bs4 import BeautifulSoup

file = open("D:\\DS290422\\DS290422-Python-Bharati\\xml_file_handling\\xml_test.xml","r")
soup = BeautifulSoup(file,'html.parser')
# print(soup)

# find_all is used to convert soup object into list object
data = soup.find_all('student')
# print(data)

# find() is used to fetch the first instance on the bases of tag
name = soup.find('naam',{"name":"third"})
print(name.text)

for i in data:
    print(i.find('naam').text)