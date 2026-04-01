# Scrapy settings for zp project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


BOT_NAME = "zp"
LOG_LEVEL="WARNING"
SPIDER_MODULES = ["zp.spiders"]
NEWSPIDER_MODULE = "zp.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "zp (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Concurrency and throttling settings
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
    "cookie":"x-zp-client-id=90763235-3520-4d2d-88d9-c0bd9761c325; _uab_collina=177505327027165259772096; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219d496b6f3d58a-0133e6ff3a392b8-4c657b58-1693734-19d496b6f3ed53%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTlkNDk2YjZmM2Q1OGEtMDEzM2U2ZmYzYTM5MmI4LTRjNjU3YjU4LTE2OTM3MzQtMTlkNDk2YjZmM2VkNTMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219d496b6f3d58a-0133e6ff3a392b8-4c657b58-1693734-19d496b6f3ed53%22%7D; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; Hm_lvt_7fa4effa4233f03d11c7e2c710749600=1775053272; HMACCOUNT=6526A49CA0B0B2E7; smidV2=202604012221120513830da7565c5043dd09b15180d60600d573d8d8a23d000; x-zp-device-sn=44d968c0dffa46f7b9773d7cb82d44b4; LastCity=%E9%95%BF%E6%B2%99; LastCity%5Fid=749; .thumbcache_6ae5bae2234b6b08bc266e51013b081d=XLm4sYdx2MpApljkpcNJBi9jVMGV0XqYoa5gP0TV8TreMPfKB8eRk5deGPmPeZD+NgbbashBZ8laQFRbFYZIJQ%3D%3D; FSSBBIl1UgzbN7NS=5qjbtwj1v2CFwZRt37F3KvA4RrG2yb0bb_G28A50CKEeszOQrGB3uuvaL2qI4z.rEp_1PR_.8OXz0mN1Xzg68vG; locationInfo_search={%22code%22:%22%22}; Hm_lpvt_7fa4effa4233f03d11c7e2c710749600=1775053314; FSSBBIl1UgzbN7NT=5FQ0jqDvJtGqqqqDw13OpNGiev8AlH910Q1qbdMq4a4MkCOyiTJAL7XFO8FZVki1qHn246Qj10rMqCtNKDJg248VuwsR_NYQu3.awGNSpEg5hoBpKW5ZBm825lLid19RfqCmW2G.gMLtZjheiMyMGX1onYz2utV3UhuXhk7DOLOc9PPEWYovlPFq4qJbbJvQ7J6dVjwBwFzv_7jMxvr_HOCPEp.QjULGBHLVk9_AXz41_w1jjJ9mDewlLhpNqv2MhXDABXC8cfN5YAJkr_FaCNW3FH5R_Zt.SRuiE.1LlalFXAFrxi4t5f8Vl_jFs9izuDLBYj_hPQXwxRcEhOObsVF",
    "referer":"https://www.zhaopin.com/"
}


# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "zp.middlewares.ZpSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "zp.middlewares.ZpDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "zp.pipelines.ZpPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"
