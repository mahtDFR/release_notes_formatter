import os
from xml.etree import ElementTree

file_name = '47jira.xml'
full_file = os.path.abspath(os.path.join(file_name))

print("input file = " + full_file)

dom = ElementTree.parse(full_file)

tickets = dom.findall('channel/item')

print(str(len(tickets)) + " items in list" + "\n")

f = open(file_name[:-4] + ".md", "w")

for t in tickets:

    title = t.find('title')
    ticket_number = t.find('key')
    description = t.find('summary')
    status = t.find('resolution')
    link = t.find('link')

    f.write("<!-- Status: " + status.text + " -->" + "\n")
    f.write(link.text + "\n<BR>")
    f.write("**" + title.text[12:].capitalize() + ".** ")
    f.write("\n\n")

f.close()

    #TODO:resolution version
    #TODO:arrange new features and bugfixes together as separate lists
    #TODO:if statement for line ending in .
    #TODO: capitalize first letter only if uncapitalized, leave the rest alone
    #TODO:add path finding
    #TODO: make script detect xml files in folder
    #TODO:fix double full stops
    #TODO:convert md to plain text for in-app changelog
    # TODO: find source issues and pull requests
