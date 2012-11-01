# Given name of calling program, a url and a string to wrap,
# output string in html body with basic metadata and open in Firefox tab.

def wrapStringInHTML(program, body):
    import datetime
    from webbrowser import open_new_tab
   
    filename = program + '.html'
    f = open(filename,'w')
    wrapper = """<html>
        <head>
        <title>%s output</title>
        </head>
        <body><p>%s</p></body>
        </html>"""
    whole = wrapper % (program, body)
    f.write(whole)
    f.close()   

    #Change the filepath variable below to match the location of your directory
    filename = 'file:///Users/jeriwieringa/Documents/Github/mining-example/' + filename

    open_new_tab(filename)