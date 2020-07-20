# ProxyGetter
Python script that pulls proxies from https://free-proxy-list.net/

_Note_: Creating the Proxy class will imediately run the proxy getting method so that the proxies are scraped. This functionality can easily be disabled by deleting the method run in the initialization (init) method.

## Methods ##

### getProxiesDefault ###
Pulls and parses the proxies from the url above.

### getNextProxy ###
Cycles to the next proxy in the list. If the current proxy is the last proxy in the list this method will refresh the proxies and set the current proxy to the first proxy in the refreshed list.

### refreshProxies ###
Manually refresh the proxies and apply some logic. Only use this if you need to add a specific functionality before/after refreshing the proxy list.

### checkProxy ###
Can be used to check if the current proxy is working/valid by testing a connection to google.
