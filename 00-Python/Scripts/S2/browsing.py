# favourite sites

import webbrowser

facebook = "https://www.facebook.com/"
twitter = "https://twitter.com/"
linkedin = "https://www.linkedin.com/"
instagram = "https://www.instagram.com/"
github = "https://github.com/"
youtube ="https://www.youtube.com/"

print("Which website you want?\n1- Facebook   2- Twitter   3- Linkedin   4- Instgram   5- Github   6- Youtube   ")
num = int(input('Enter a valid number: '))

if num == 1:
    webbrowser.open(facebook)
elif num  == 2:
    webbrowser.open(twitter)
elif num  == 3:
    webbrowser.open(linkedin)
elif num  == 4:
    webbrowser.open(instagram)
elif num  == 5:
    webbrowser.open(github)
elif num  == 6:
    webbrowser.open(youtube)  
else:
    print("invalid number , try again!") 







