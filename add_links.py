"""Add links to the transcriptions in the xml folder to the index.html file"""

import os
import re



fp = "index.html"
with open(fp, mode="r", encoding="utf-8") as inf:
    html = inf.read()
li = "\n"
templ = """  <li><a href="xml/{}" target="_blank">{}</a></li>\n"""
for fn in os.listdir("xml"):
    if fn.endswith(".xml"):
        li += templ.format(fn, fn)
print(li)
s = re.sub("<ul>.*</ul>", "<ul>{}</ul>".format(li), html, flags=re.DOTALL)
print(s)
with open(fp, mode="w", encoding="utf-8") as outf:
    outf.write(s)
