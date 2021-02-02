BOT_NAME = 'landsbankinn'

SPIDER_MODULES = ['landsbankinn.spiders']
NEWSPIDER_MODULE = 'landsbankinn.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'landsbankinn.pipelines.LandsbankinnPipeline': 100,

}