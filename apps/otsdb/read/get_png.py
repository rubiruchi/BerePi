# -*- coding: utf-8 -*-
# Author : https://github.com/jeonghoonkang

import urllib
#http://URL:PORT/api/query?start=2018/06/25-00:00:00&end=2018/06/26-00:00:00&m=none:keti.tinyos.packet.test?png

# main function
if __name__ == "__main__":
    print "...starting..."

    ip_port =  'aaa.bbb.com:4242'
    url = 'http://' + ip_port + '/q?start=2018/06/25-13:55:00&end=2018/06/25-14:16:34&m=none:keti.tinyos.packet.test&o=&wxh=800x600&style=linespoint&png'
    print url

    urllib.urlretrieve(url, unicode('download.png' ))

    print "\n ...ending..."
