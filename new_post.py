#!/usr/bin/python

import argparse
from datetime import date
from time import strftime

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--title', required=True, help="Title of the post")
args = parser.parse_args()

def main():
    TITLE = "NEW-POST"
    if args.title:
        TITLE = args.title
    today = date.today()
    filename = today.strftime("%Y-%m-%d") + f"-{TITLE}.md"
    url = today.strftime("%Y/%m/%d")
    post_time = strftime("%Y-%m-%d %H:%M:%S+00:00")
    
    front_matter = ["---\n",
    "author: Stephen Adams\n",
    "date: " + post_time + "\n",
    "draft: false\n",
    f"title: {TITLE}\n",
    "type: post\n",
    "url: /" + url + f"/{TITLE}/\n",
    "#image: /img/some_featured_image.jpg\n",
    "#tags:\n",
    "#LIST: books,code,comics,everything,fatherhood,gadgets,games,internet,life,movies,music,nerd,podcasting,politics,random,science,tech,tv,video,work,writing\n",
    "---\n"]
    
    with open("content/posts/" + filename, "w") as f:
        f.writelines(front_matter)
    
    print("post " + filename + " created")

if __name__ == "__main__":
    main()
