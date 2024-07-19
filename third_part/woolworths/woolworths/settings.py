# Scrapy settings for woolworths project
#
# For simplicity, this file contains only basic settings. You may add or
# modify settings as needed for your project.

BOT_NAME = 'woolworths'

SPIDER_MODULES = ['woolworths.spiders']
NEWSPIDER_MODULE = 'woolworths.spiders'

# User-Agent header to avoid being blocked by websites
USER_AGENT = 'woolworths (+http://www.yourdomain.com)'

# The maximum number of concurrent requests to be performed by the Scrapy engine
CONCURRENT_REQUESTS = 16

# The delay between consecutive requests to the same website (in seconds)
DOWNLOAD_DELAY = 2

# Disable cookies to avoid tracking issues
COOKIES_ENABLED = False

# Configure item pipelines
ITEM_PIPELINES = {
    'woolworths.pipelines.WoolworthsPipeline': 1,
}

# Configure the feed to output data in CSV format
FEEDS = {
    'output.csv': {
        'format': 'csv',
        'overwrite': True,
        'encoding': 'utf-8',  # Use utf-8 encoding to handle special characters
    },
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
}

# The default values for various settings (optional)
ROBOTSTXT_OBEY = True  # Whether to obey robots.txt rules

# Logging settings (optional)
LOG_LEVEL = 'INFO'  # Set to 'DEBUG' for more detailed logs

# Set the download timeout
DOWNLOAD_TIMEOUT = 180  # Timeout in seconds

# Configure auto-throttling settings (optional)
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

# Configure HTTP caching (optional)
HTTPCACHE_ENABLED = False
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
