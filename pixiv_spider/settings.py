# Scrapy settings for pixiv_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = 'pixiv_spider'
LOG_LEVEL = 'WARNING'
SPIDER_MODULES = ['pixiv_spider.spiders']
NEWSPIDER_MODULE = 'pixiv_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
USER_AGENT = random.choice(USER_AGENT_LIST)
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'authority': 'www.pixiv.net',
    'accept': 'application/json',
    'accept-Language': 'en',
    'referer': 'https://www.pixiv.net/users/3718340',
    'cookie': 'first_visit_datetime_pc=2021-04-13+21%3A36%3A35; p_ab_id=8; p_ab_id_2=0; p_ab_d_id=413719587; yuid_b=EUWZSYQ; _ga=GA1.2.2015959074.1618317397; a_type=0; b_type=1; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=32813706=1^9=p_ab_id=8=1^10=p_ab_id_2=0=1^11=lang=zh=1; privacy_policy_notification=0; privacy_policy_agreement=3; c_type=23; howto_recent_view_history=72627586; ki_s=214908%3A0.0.0.0.2%3B214994%3A0.0.0.0.2%3B215190%3A0.0.0.0.2%3B215821%3A0.0.0.0.2%3B220959%3A0.0.0.0.2; tag_view_ranking=m3EJRa33xU~zIv0cf5VVk~18TSf2zYVV~HLTvFcV98c~G-1lNBdD_I~0xsDLqCEW6~BEa426Zwwo~4CEfWpm7-W~VMrBpQAvH4~WdKNu4p5bE~Ce-EdaHA-3~RIyarR2CI5~SHHnteIIjz~_hSAdpN9rx~n5zFB79WVQ~X9TSlql6xU~qcYo_5oqVP~azESOjmQSV~EC_zlSgtNf~NAZkCbgfgD~6fOoWmKgJo~0Sds1vVNKR~ilrMB93OMp~nVghDke_m3~tgP8r-gOe_~bsw9MCIN-u~yTl3lZyJa_~PNvsDKwKjA~qIDsnltE2o~6Gmbz4FGpt~WzlUQugVff~-IrOV3901X~BU9SQkS-zU~Q959js6mBM~05XvkINl3k~O0WKFZuVbs~O8n4dPo2XK~ea8DYxYsty~pZqm_nW-BV~pE_tPPwrBT~D528yvjAo-~lsA8L6UX4U~tTvZK72fmv~3z4qRu63nb~NsbQEogeyL~ML8s4PH95U~zZZn32I7eS~rqvM6GS14_~-NrgV4e3XX~XUQrb0GUuy~tlMe_sMs3I~pT_f2fSQOG~LH9ZWWU5Vx~EpYbhjcmwq~9ODMAZ0ebV~Wxk4MkYNNf~sAwDH104z0~eU_5lTnadR~_2YTVu3joV~eO1DDlgyGh~u3It6EcNU9~KVTNu2QtIE~b8b4-hqot7~a5xd3Ca-Sm~i83OPEGrYw~81BOcT1ZAV~zyKU3Q5L4C~bte2rs8f0a~5RvyKm3yea~YuIxJMq4Ls~m_zSvOjici~nubrRZtYEJ~hfCvniImMk~cLKuAZBgE6~cqG-yQnJkm~RolC8IrBVO~q3eUobDMJW~cYou8NDJiN~engSCj5XFq~uC2yUZfXDc~iDXN8FWRIH~OoPRFFFRVB~dqSObM91AS~qc3_0F0xbS~gVfGX_rH_Y~hDBVvbKDlc~qs1FGS26bJ~O6NIA3TLTJ~0CaTbfGZYk~u_aBqUn1Z8~zutfFrwwcY~JOfwHvqq38~-0JKThjl-M~c1SYLhLs6X~OnkltWFYNJ~9wN-K8_crj~sRQy4rKivk~aIc065hOjg~_JSqwu0FLF~ZKaEaSznut; __utmc=235335808; _gcl_au=1.1.1050831800.1636170895; _gid=GA1.2.291242485.1636170897; device_token=8f8d65aa9743a82111aed50f50afe005; PHPSESSID=32813706_mTnBuOAj7Yd8skSLsM7i72PXP6Dkeen5; __utma=235335808.2015959074.1618317397.1636183021.1636186605.28; __utmz=235335808.1636186605.28.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __cf_bm=lmL0haU9yREN8fmG2HgFIK0Hk8JuazXAQyMNqQ2Toxs-1636186606-0-ATzhF8rcD3CpfaYFoNeWNPNrNGPYJILZ2lQM3qpuYxFuiJQjakdShrUb5N9pbaSzKSX0Zo40QyxHMHfOmiOxv1UWUyIKCSm+NvVjC2Mej6LcVVttEZdnBpxIX6V6ntsZaeN88d+tePTqf+ej1l9BM+jL6SKCRDB1p4Vp+WmxmWh8GFsTCqeQZW0drr3vueXd2g==; __utmt=1; ki_r=; ki_t=1619537558427%3B1636164028882%3B1636186953792%3B16%3B60; __utmb=235335808.3.10.1636186605',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'pixiv_spider.middlewares.PixivSpiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'pixiv_spider.middlewares.Proxy': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'pixiv_spider.pipelines.PixivSpiderPipeline': 300,
    'pixiv_spider.pipelines.DownloadImagesPipeline': 10,
}
# 设置图片下载路径
IMAGES_STORE = r'E:\Code\pixiv_spider\爬取pixiv图片'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
