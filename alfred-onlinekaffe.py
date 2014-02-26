# -*- coding: utf-8 -*-
import alfred
import datetime
import urllib2


def main(stats=False):
    
    line = urllib2.urlopen('http://draug.online.ntnu.no/coffee.txt').readlines()[1]
    now = datetime.datetime.today()
    coffee_time = datetime.datetime.strptime(line, "%d. %B %Y %H:%M:%S") #26. February 2014 11:05:38

    diff = now - coffee_time
    print str(diff)
    
    
    item = alfred.Item(
        uid='onlinekaffe',
        arg="",
        title=u'Kaffen er er %s gammel ' % diff,
        subtitle=u'Sist lagd %s' % str(coffee_time),
        valid=False,
        icon='icon.png'
    )
    return alfred.render([item])

if __name__ == "__main__":
    print main()
