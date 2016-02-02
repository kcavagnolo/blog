f = open('dsci_links')
o = open('dsci_items', 'w')
o.write("<ul>")
i = 1
for l in f:
    l = l.strip()
    l = l.split()
    s = l[0]
    l = l[1]
    o.write('<li><a href="'+str(l)+'">'+str(i)+" "+str(s)+'</a></li>\n')
    i += 1
a = "</body>\n</html>\n"
o.write("</ul>")
f.close()
o.close()
