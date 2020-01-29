import webbrowser

url = input("Enter your Youtube url here: ")

url = url[:12]+"ss"+url[:12]
webbrowser.open(url)
