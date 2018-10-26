#!/usr/bin/env python

import markdown
import subprocess

#subprocess.check_call(["/bin/sh", "-c", "/usr/local/bin/git pull --ff-only"])
md = open("index.md").read()
md = md.replace("{{date}}", subprocess.check_output(["/bin/sh", "-c", "git log --pretty=%cd --date=format:'%e %B %Y' index.md | head -1"]))
html = markdown.markdown(md)
page = open("_layouts/default.html").read()
page = page.replace("{{title}}", "Now")
page = page.replace("{{content}}", html)
print("Content-Type: text/html")
print("")
print(page)
