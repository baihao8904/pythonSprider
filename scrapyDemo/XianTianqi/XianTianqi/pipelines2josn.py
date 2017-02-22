import time
import json
import codecs

class  XiantianqiPipeline(object):
    def process_item(self,item,spider):
        today = time.strftime("%Y-%m-%d",time.localtime())
        filename = today+'.json'
        with open(filename,'a') as fp:
            fp.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
        return item