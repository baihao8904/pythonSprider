import urllib.request
import re
import multiprocessing
import threading

class textProxy(object):
    def __init__(self):
        self.sFile = '2017-02-22proxy.txt'
        self.dFile = 'alive.txt'
        self.URL = 'http://www.baidu.com'
        self.thread = 10
        self.timeout =3
        self.regex = re.compile('baidu.com')
        self.aliveList = []

        self.run()

    def run(self):
        with open(self.sFile,'r') as fp:
            lines = fp.readlines()
            line = lines.pop()
            while lines:
                for i in range(self.thread):
                    td = threading.Thread(target=self.LinkwithProxy,args=(line,))
                    td.start()
                    if lines:
                        line = lines.pop()
                    else:
                        continue
        with open(self.dFile,'a+') as fp:
            for i in range(len(self.aliveList)):
                fp.write(self.aliveList[i])

    def LinkwithProxy(self,line):
        lineList = line.split('\t')
        protocol = lineList[2].lower()
        server = protocol + '://' + lineList[0] + ":" + lineList[1]
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({protocol:server}))
        urllib.request.install_opener(opener)
        try:
            response = urllib.request.urlopen(self.URL,timeout = self.timeout)
        except:
            print('%s conect failed' %server)
            return
        else:
            try:
                astr = str(response.read())
            except:
                print("%s connect failed" %server)
                return
            if self.regex.search(astr):
                print("%s connect success ....." %server)
                self.aliveList.append(line)

if __name__ == '__main__':
    TP = textProxy()
