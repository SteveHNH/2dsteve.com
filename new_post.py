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
"---\n"]

with open("content/posts/" + filename, "w") as f:
    f.writelines(front_matter)

print("post " + filename + " created")

