import csv
import time

#这样写会写入很多header
# class  XiantianqiPipeline(object):
#     def process_item(self,item,spider):
#         today = time.strftime("%Y-%m-%d",time.localtime())
#         filename = today+'.csv'
#         filenames = ['cityDate','week','img','temperature','weather','wind']
#         with open(filename,'a') as fp:
#             csvwriter = csv.DictWriter(fp,fieldnames=filenames,restval='NULL')
#             csvwriter.writeheader()
#             csvwriter.writerow(item)
#         return item

def write_to_csv(item):
    thetime = time.strftime("%Y-%m-%d",time.localtime())
    filenames = ['cityDate', 'week', 'img', 'temperature', 'weather', 'wind']
    writer = csv.writer(open(thetime+'.csv', 'a'),lineterminator='\n')
    writer.writerow(filenames)
    writer.writerow([item[key] for key in item.keys()])


class XiantianqiPipeline(object):
    def process_item(self, item, spider):
        write_to_csv(item)
        return item