# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from dj_app.models import linkdetailM

class ScrapyProjectPipeline:
    def process_item(self, item, spider):
        try:
            linkdetailM.objects.create(title=item['title'],date=item['date'],risk=item['risk'],cve=item['cve'], cwe=item['cwe'])
            pass
        except Exception as e:
            print("\n")
            spider.logger.error("\nFailed to load quote, Reason For Failure:{}".format(e))
            print(item)
        return item
