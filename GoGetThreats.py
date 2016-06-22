import urllib, re, datetime

i = datetime.datetime.now()

def header(x):
    x.write ('Breaking news headlines\n')
    x.write ('http://www.breakingnews.com\n')
    todaysDate = i.strftime("%A %d, %B %Y")
    x.write (todaysDate)
    x.write ('\n\n\n')
    
# Text File 
fileOutput = raw_input ('Enter a name for the news file: ')
rawInput = str(fileOutput)
textfile = open(rawInput+'.txt',"w")
header (textfile)

# Scrapper
htmlfile = urllib.urlopen("http://www.breakingnews.com")
htmltext = htmlfile.read()
regex = '<div class="headline">(.+?)</div>'
pattern = re.compile(regex)
news = re.findall(pattern, htmltext)

keywords = ['murder',
            'killed',
            'dead',
            'lockdown',
            'crash',
            'fire',
            'suspicious',
            'bomb']

i = 0
counter = 1
while i < len(news):
    entry = counter, news[i]
    textfile.write(str(entry))
    textfile.write('\n\n')
    i+=1
    counter +=1
    for keys in keywords:
        if keys in news[i-1]:
            textfile.write('^^^^^^^^^^^^^^^^^\nThreat possible\n\n')
        else:
            pass
textfile.close()
print "Done"
    
