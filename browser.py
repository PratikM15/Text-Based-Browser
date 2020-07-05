import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore
import sys

args = sys.argv
if len(args) == 2:
    directory = args[1]

else:
    directory = 'tb_tabs'


if not os.path.exists(directory):
    os.mkdir(directory)

my_stack = deque()
while True:
    url = input("Enter URL: ")
    copy = url
    try:
        copy = copy.replace(".com","")
        copy = copy.replace("https://", "")
        filename = directory + "/" + copy
    except:
        pass
    if os.path.exists(filename):
        file1 = open(filename, 'r')
        content = file1.read()
        print(content)
        my_stack.append(content)
        file1.close()
    elif url == 'exit':
        break
    elif url == 'back':
        print(my_stack[-2])
    elif '.' in url:
        if not url.startswith('https://'):
            url = "https://" + url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        result = ""
        for element in list(soup.find_all(text=True)):
            if element.parent.name == "a":
                result += Fore.BLUE + element.strip() + Fore.RESET
            else:
                result += element
        result = result.replace("<", "").replace(">", "")
        if not result:
            print("error: probably 404 - not found")
            continue
        entry = directory + "/" + copy
        file1 = open(entry, 'w')
        file1.write(result)
        print(result)
    else:
        print("Error: Incorrect URL")


