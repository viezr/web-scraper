#!/usr/bin/env python3
'''
HTML generator for data lists
'''

def generate_html(data_list, keywords = []):
    '''
    Function for generation html file with data, filtered by keywords
    '''

    html_head_part1 = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>My news</title>
  <style>
'''
    with open("utils/html_generator.css") as css:
        html_style = css.read()
        html_style = html_style.replace("\n\n", "\n")
        html_style = html_style.replace("{\n", "{")
        html_style = html_style.replace("\n}", "}")
        html_style = html_style.replace(";\n", ";")
        html_style = html_style.replace("    ", " ")

    html_head_part2 = '''
  </style>
</head>
<body>
  <div class="page">
    <div class="header">
      <div class="container">
        <h1 class="title">My news</h1>
      </div>
    </div>
    <div class="container">
'''
    html_tail = '''
    </div><!-- end of container-->
  </div><!-- end of page-->
</body>
</html>
'''
    line = '''<div class="line"><div class="line-1"></div><div class="line-space"></div><div class="line-2"></div><div class="line-space"></div><div class="line-3"></div><div class="line-space"></div><div class="line-4"></div><div class="line-space"></div><div class="line-5"></div></div>'''

    html_file = "data.html"

    def li_gen(item):
        '''
        Generate list item
        '''
        li = "        <li>\n"
        li += f"          <a href=\"{item['link']}\">\n"
        li += f"            <span class=\"date\">{item['date']}</span>{item['title']}\n"
        li += "          </a>\n"
        li += "        </li>\n"
        return li

    f = open( html_file, mode="w" )

    keywords = ', '.join(keywords)
    content = html_head_part1 + html_style + html_head_part2
    content += f"    <p class=\"keywords\">Keywords: {keywords}</p>\n"

    for site in data_list:
        site_name = site["site"]
        content += f"      <h2 class=\"subtitle\">{site_name}</h2>\n"
        content += f"      {line}\n"
        content += "      <ul>\n"
        for item in site["data"]:
            content += li_gen(item)
        content += "    </ul>\n"
    content += html_tail

    f.write(content)
    f.close()
