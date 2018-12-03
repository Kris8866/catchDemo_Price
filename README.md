   目前，为了加速页面的加载速度，页面的很多部分都是用JS生成的，而对于用scrapy爬虫来说就是一个很大的问题，
<br>因为scrapy没有JS engine，所以爬取的都是静态页面，对于JS生成的动态页面都无法获得。

* 解决方案：
  * 利用第三方中间件来提供JS渲染服务： scrapy-splash 等
  * 利用webkit或者基于webkit库
  
  Demo使用Splash：
 <br> Splash是一个Javascript渲染服务。
 <br> 它是一个实现了HTTP API的轻量级浏览器。
 <br> Splash是用Python实现的，同时使用Twisted和QT。
 <br> Twisted（QT）用来让服务具有异步处理能力，以发挥webkit的并发能力。
  
* 步骤：
  * 安装DockerToolbox
  * 安装scrapy-splash，执行语句：pip install scrapy-splash
  * 修改settings.py：
  
      SPLASH_URL = 'http://192.168.99.100:8050'  

      DOWNLOADER_MIDDLEWARES = {
        'scrapy_splash.SplashCookiesMiddleware': 723,
        'scrapy_splash.SplashMiddleware': 725,
        'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
      }

      SPIDER_MIDDLEWARES = {
        'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
      }

      DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter’

      HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


  * 重写爬虫的strat_request方法

  
