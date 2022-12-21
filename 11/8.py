url = input()
print(url[url.find("?q=") + 3:url.find("&")])
