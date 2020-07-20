# based on
# https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/
# https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/

from bs4 import BeautifulSoup as soup
import requests


class Proxies:
    url = 'https://free-proxy-list.net/'

    def __init__(self):
        self.header = {'User-Agent': 'Mozilla/5.0'}
        self.proxyList = []
        self.currentProxy = None
        self.getProxiesDefault()
        # self.getNextProxy()

    def getProxiesDefault(self):
        """
        Makes a request to the free proxy url and parses the resulting html to find all the proxies and their port
        :return: N/A
        """
        try:
            req = requests.get(self.url, headers=self.header)  # sending requests with headers
            url = req.content  # opening and reading the source code
        except requests.exceptions.RequestException as e:
            print('Error getting Proxies')
            raise e
        else:
            pageSoup = soup(url, "lxml")  # structuring the source code in proper format
            rows = pageSoup.findAll("tr")  # finding all rows in the table if any.
            rows = rows[1:300]  # removes column headers

            self.proxyList = []
            for row in rows:
                cols = row.findAll('td')
                cols = [element.text for element in cols]
                IP = cols[0]  # ipAddress which presents in the first element of cols list
                portNum = cols[1]  # portNum which presents in the second element of cols list
                proxy = IP + ":" + portNum  # concatenating both ip and port
                protocol = cols[6]  # portName variable result will be yes / No
                if protocol == "yes":  # checks if the proxy supports https
                    self.proxyList.append(proxy)

    def refreshProxies(self):
        """
        Refreshes the proxy list. Use this only if you need to manually refresh the list and apply some changes on top
        of the regular list refresh.
        :return: N/A
        """
        self.getProxiesDefault()
        # self.currentProxy = self.proxyList[0]
        # return self.currentProxy

    def getNextProxy(self):
        """
        Gets the next proxy on the list and refreshes the list if it is the last proxy proxy in the list.
        :return: The next proxy available
        """
        if self.currentProxy is None:
            self.currentProxy = self.proxyList[0]
            return self.currentProxy
        elif self.currentProxy != self.proxyList[-1]:
            self.currentProxy = self.proxyList[self.proxyList.index(self.currentProxy) + 1]
            return self.currentProxy
        else:
            self.getProxiesDefault()
            self.currentProxy = self.proxyList[0]
            return self.currentProxy

    def checkProxy(self):
        """
        Checks to see if the current proxy is working by testing a connection to google using the proxy
        :return: the status code or the error that arises
        """
        userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        buildProxy = {'http': self.currentProxy}
        try:
            r = requests.get('https://www.google.com', headers={'User-Agent': userAgent}, proxies=buildProxy, timeout=8)
            return r.status_code
        except (requests.exceptions.Timeout,
                requests.exceptions.ProxyError,
                requests.exceptions.SSLError,
                requests.exceptions.ConnectionError) as e:
            return e


if __name__ == '__main__':
    proxies = Proxies()
    # proxies.getProxiesDefault()
    # proxy = proxies.currentProxy
    # proxies.getNextProxy()
    # print(proxies.currentProxy)
    # proxy = proxies.proxyGen
    # print(next(proxy))
    # proxies.refresh()
    # print(next(proxies.proxyGen))
    # for item in items:
    #     print(item)
    print(proxies.getNextProxy())
    print(proxies.getNextProxy())
