#!/usr/bin/python

from datetime import date
from time import strftime

today = date.today()
filename = today.strftime("%Y-%m-%d") + "-NEW-POST.md"
url = today.strftime("%Y/%m/%d")
post_time = strftime("%Y-%m-%d %H:%M:%S+00:00")

front_matter = ["---\n",
"author: Stephen Adams\n",
"date: " + post_time + "\n",
"draft: false\n",
"title: NEW-POST\n",
"type: post\n",
"url: /" + url + "/NEW-POST/\n",
"#image: /img/some_featured_image.jpg\n",
"#tags:\n",
"#LIST: books,code,comics,everything,fatherhood,gadgets,games,internet,life,movies,music,nerd,podcasting,politics,random,science,tech,tv,video,work,writing\n",
"---\n"]

with open("content/posts/" + filename, "w") as f:
    f.writelines(front_matter)

print("post " + filename + " created")

