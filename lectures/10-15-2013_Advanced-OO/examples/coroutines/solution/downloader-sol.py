import urllib2

def downloader(url):
    reader = urllib2.urlopen(url)
    for line in reader:
        try:
            x = yield line
        except GeneratorExit:
            break

streams = [
   downloader('http://google.com'),
   downloader('http://bing.com'),
]

# poor man's scheduler
while len(streams) > 0:
    for s in streams:
        try:
            line = s.next()
            if line.find('DOCTYPE') > -1:
                print "STOPPING"
                s.throw(GeneratorExit)
        except StopIteration:
            line = None

        if line:
            print "downloader %d : %s" % (streams.index(s), line)
        else:
            s.close()
            streams.remove(s)
