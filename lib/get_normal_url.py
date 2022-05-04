from urllib.parse import urlparse

def get_standard_url(url):
    """
    若输入的没有加上http，https，自动转为标准的url格式，防止报错
    """
    if not url.startswith("http"):
        url = "http://" + url
    o = urlparse(url)  # ParseResult(scheme='http', netloc='www.baidu.com:80', path='/index.php',
                       # params='', query='id=1&uid=2', fragment='')
    return "{}://{}".format(o.scheme, o.netloc)
