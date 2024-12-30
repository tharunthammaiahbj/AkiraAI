Documentation | Scrape.do[![](/images/scrape-logo.svg)](/)

* [Blog](/blog/)
* [Features](/#features)
* [Pricing](/pricing/)
* [FAQs](/#faqs)
* [Documentation](/documentation/)

[Dashboard](https://dashboard.scrape.do)[Home](/)Documentation![](/images/up-arrow.svg)

Scrape.do Documentation
=======================

You can find all the information you need to get started with Scrape.do in our documentation.

Table of Contents



+ [Quick Start](#quick-start)
  
  - [How it works?](#how-it-works)
  - [Overview](#overview)
+ [Token](#token)
+ [URL](#url)
+ [Proxy Settings](#proxy-settings)
  - [Super (Residential & Mobile)](#super-residential--mobile)
  - [Geo Targeting](#geo-targeting)
  - [Regional Geo Targeting](#regional-geo-targeting)
  - [Sticky Sessions](#sticky-sessions)
+ [Proxy Mode](#proxy-mode)
  - [What is Proxy Mode?](#what-is-proxy-mode)
  - [Proxy Information](#proxy-information)
+ [Request](#request)
  - [POST/PUT Request](#postput-request)
  - [Custom Headers](#custom-headers)
  - [Extra Headers](#extra-headers)
  - [Forward Headers](#forward-headers)
  - [Set Cookies](#set-cookies)
  - [Disable Redirection](#disable-redirection)
  - [Callback & Webhook](#callback--webhook)
  - [Timeout](#timeout)
  - [Retry Timeout](#retry-timeout)
  - [Disable Retry](#disable-retry)
  - [Device](#device)
+ [Headless Browser](#headless-browser)
  - [JS Render](#js-render)
  - [Wait Until](#wait-until)
  - [Custom Wait](#custom-wait)
  - [Wait CSS Selector](#wait-css-selector)
  - [Width](#width)
  - [Height](#height)
  - [Block Resources](#block-resources)
  - [Screenshot](#screenshot)
  - [Play with Browser](#play-with-browser)
  - [ReturnJSON](#returnjson)
+ [Response](#response)
  - [Output Format](#output-format)
  - [Downloading Pictures & Files](#downloading-pictures--files)
  - [Transparent Response](#transparent-response)
  - [Response Headers](#response-headers)
+ [Information](#information)
  - [Usage Statistics API](#usage-statistics-api)
  - [Status Codes](#status-codes)
  - [Request Costs](#request-costs)
+ [Knowledge Base](#knowledge-base)
  - [You should know](#you-should-know)
  - [Solve Blocking Issue](#solve-blocking-issue)
  - [Frequently Asked Technical Questions](#frequently-asked-technical-questions)
+ [Frequently Used Libraries](#frequently-used-libraries)
  - [Python Scrapy Example](#python-scrapy-example)
  - [Scrapy](#scrapy)
  - [Puppeteer Example](#puppeteer-example)
  - [Python Selenium Example](#python-selenium-example)
  - [Playwright With The Example of Chrome](#playwright-with-the-example-of-chrome)

Choose your favorite language

[![](/images/frameworks/curl.svg)

cURL](#)[![](/images/frameworks/python.svg)

Python](#)[![](/images/frameworks/nodejs.svg)

Node JS](#)[![](/images/frameworks/c-sharp.svg)

C#](#)[![](/images/frameworks/php.svg)

PHP](#)[![](/images/frameworks/java.svg)

Java](#)[![](/images/frameworks/go-lang.svg)

Go Lang](#)[![](/images/frameworks/ruby.svg)

Ruby](#)

Quick Start
-----------

#### 

Scrape.do is a service that allows you to access raw data before the target website understands that you are sending bot traffic, bypassing the blocking problems you experience while scraping your target website, thanks to its rotating proxy, headless browser and captcha handling mechanisms. All the requests you send are upgraded and compared to the requests of a real user. The firewalls of the target websites have a hard time distinguishing these requests, and your success rate will thus exceed 99%.

With Scrape.do, you can use a datacenter, residential or mobile proxy from the region or country you want, manage the entire process, including headless browsers, according to the needs of the target website, and save you from spending your time on crawling processes.

* Our service will return you raw data from the target web page. Therefore, if the target url returns you JSON, our service will return JSON, if it returns HTML, our service will return HTML.
* Your API credits will only be used for successful requests. For more details, please visit the **Status Codes** and **Request Costs** area.
* If you want to learn more about how Scrape.do works, you can take a look at our explanations in the [**How ​​it works?**](#how-it-works) section and understand what it does technically.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/anything'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")url="http://api.scrape.do?token={}&url={}".format(token,targetUrl)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:''}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varrespponse=client.SendAsync(request).Result;varcontent=respponse.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN",];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="+encoded_url+"").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:""})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### How it works?

Scrape.do is an advanced API service that bypasses anti-bot protection systems by performing advanced fingerprint manipulations through residential, mobile and datacenter rotating proxies and allows scraping the data you need on the target web page.

It simulates the web scraping request you send to the requests made by a real user, including the header information, starting from the TLS handshake process so that the target website is not detected by the firewall systems. You don’t have to deal with low-level bypass solutions and anti-bot systems.

Scrape.do is not just a proxy service. It works to protect you from the needs of target websites such as blocking, captcha resolution, headless browser.

It undertakes all the difficulties experienced by companies or people who need data while extracting data and allows you to do your main job. It is a system that we have designed to have a teammate who solves all the crawling stages on your behalf, like an employee from the team, for all problems in your scraping infrastructure.

---

### Overview

You can view all the parameters of Scrape.do from the list below and have an overview of all of them quickly.

| Parameter | Type | Default | Description | Details |
| --- | --- | --- | --- | --- |
| token \* | string |  | The token to use for authentication. | [More](#token) |
| url \* | string |  | Target web page url. | [More](#url) |
| super | bool | false | Use Residential & Mobile Proxy Networks | [More](#super-residential--mobile) |
| geoCode | string |  | Choose right country for your target web page | [More](#geo-targeting) |
| regionalGeoCode | string |  | Choose continent for your target web page | [More](#regional-geo-targeting) |
| sessionId | int |  | Use the same IP address continuously with using a session | [More](#sticky-sessions) |
| customHeaders | bool | false | Handle all request headers for the target web page. | [More](#custom-headers) |
| extraHeaders | bool | false | Use it if you want to change header values or if you want to add a new header over the ones we have added | [More](#extra-headers) |
| forwardHeaders | bool | false | Allows you to forward your own headers to the target website | [More](#forward-headers) |
| setCookies | string |  | Set cookies for the target web page. | [More](#set-cookies) |
| disableRedirection | bool | false | Disable request redirection for your use-case | [More](#disable-redirection) |
| callback | string |  | Get results via a webhook without waiting for your requests | [More](#callback--webhook) |
| timeout | int | 60000 | Set maximum timeout for your requests | [More](#timeout) |
| retryTimeout | int | 15000 | Set maximum timeout for our retry mechanism | [More](#retry-timeout) |
| disableRetry | bool | false | Disable retry mechanism for your use-case | [More](#disable-retry) |
| device | string | desktop | It is the parameter that allows you to specify the device type. | [More](#device) |
| render | bool | false | If you have a web page that you only need to open with a browser and you need to wait for the results to load, simply pass the parameter. | [More](#js-render) |
| waitUntil | string | domcontentloaded | With this parameter, you can change this property and make the page load correctly according to your needs. | [More](#wait-until) |
| customWait | int | 0 | Sets the browser is waiting time on the target web page after content loaded | [More](#custom-wait) |
| waitSelector | string |  | CSS selector to wait for in the target web page | [More](#wait-css-selector) |
| width | int | 1920 | Width, parameter in pixels of the browser | [More](#width) |
| height | int | 1080 | Height, parameter in pixels of the browser | [More](#height) |
| blockResources | bool | true | Block CSS and Image sources on your target web page | [More](#block-resources) |
| screenShot | bool | false | Return a screenshot from your target web page | [More](#screenshot) |
| fullScreenShot | bool | false | Return a full screenshot from your target web page | [More](#full-screen-shot) |
| particularScreenShot | string |  | Return a screenshot of a particular area from your target web page | [More](#particular-screenshot) |
| playWithBrowser | string |  | You can simulate browser actions like click, scroll, execute js etc. | [More](#play-with-browser) |
| output | string | raw | You can get the output in default format raw, or in markdown. | [More](#output-format) |
| transparentResponse | bool | false | Disable Scrape.do status code, body, error handling mechanism and return pure response from target web page for all requests | [More](#transparent-response) |
| returnJSON | bool | false | Returns network requests. It presents the content information as a property string. shownetworkrequest only returns logs of xhr and fetch requests. | [More](#returnjson) |

---

Token
-----

\* required token = string 

All your requests are authorized with the token information of your account. Therefore, you need to own a token. If you do not have an account, you can immediately become a member **here** and obtain token information.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/anything'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")url="http://api.scrape.do?token={}&url={}".format(token,targetUrl)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:''}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varrespponse=client.SendAsync(request).Result;varcontent=respponse.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN",];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="+encoded_url+"").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:""})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

URL
---

\* required &  url = encoded target url 

We are waiting for you to send the url information of the target website you want to scrape. If you are using API mode, you definitely need to encode the url parameter using the url encoder.

* No need to encode url if you use **Proxy Mode**.
* Supported protocols are `HTTP` and `HTTPS`

#### Why need the url encode?

When you write a url in the query parameter and do not use the url encode, it overflows the query param and therefore causes us to perceive it as a different parameter. In this scenario, we cannot correctly read the url of the target site. In order not to allow this, we check all parameters on your behalf and in such a case we return you 400 status code.

#### Example Code Snippet

* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
sudo apt-get install gridsite-clients urlencode "YOUR_URL"
```
![](/images/copy.svg)
```
importurllib.parseencoded_url=urllib.parse.quote("YOUR_URL")
```
![](/images/copy.svg)
```
letencoded_url=encodeURIComponent("YOUR_URL")
```
![](/images/copy.svg)
```
varencoded_url=System.Web.HttpUtility.UrlEncode("YOUR_URL")
```
![](/images/copy.svg)
```
<?php$url_encoded=urlencode("YOUR_URL");?>
```
![](/images/copy.svg)
```
Stringencoded_url=URLEncoder.encode("YOUR_URL","UTF-8");
```
![](/images/copy.svg)
```
packagemainimport("fmt""net/url")funcmain(){encoded_url:=url.QueryEscape("YOUR_URL")fmt.Println(string(encoded_url))}
```
![](/images/copy.svg)
```
require'cgi'encoded_url=CGI.escapestr
```

---

Proxy Settings
--------------

### Super (Residential & Mobile)

 &  super = true  default =false

Every proxy is actually an IP address. Each IP address has an ASN (Autonomous System Number) information. Anti bot solutions can block you based on your IP quality because they have this ASN information. It offers two different types of proxies on Scrape.do.

**Datacenter:** Inexpensive but likely to be blocked by advanced bot solutions. We have a total of over 90.000+ datacenter rotating proxy addresses.

**Residential & Mobile:** More expensive but less detectable by anti-bot services. More than **95.000.000+** proxies are hosted in our Residential & Mobile rotating proxy pool. To use it, it is sufficient to pass `super=True` parameter. By using the [Geo Targeting](#geo-targeting) feature, you can target the country the target website serves and increase your success rates even more.

* If you do not use this feature, the system will use **Datacenter Proxy** by default.
* With Residential & Mobile Proxy, each successful request consumes **10 Successful API credits**. If Headless Browsers is used, each successful request will consume **25 Successful API credits**.
* If you do not use **Geo Targeting** when you use Residential & Mobile proxy, our system will send request via United States `geoCode=us` by default.
* Our proxy pools are regularly checked, rotated and performance monitored. It can be customized specifically for the target website or for customer needs. We work hard to create the best quality and fastest proxies in the world.

> **Important**: Super proxy infrastructure requires a minimum of **Business Plan** and above!

You can check credit usage for each request type in the [**Request Costs**](#request-costs) section.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/anything&super=true'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:super=true@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")superParam="true"url="http://api.scrape.do?token={}&url={}&super={}".format(token,targetUrl,superParam)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:super=true@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varsuperParam="true";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&super=${superParam}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'super=true'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&super=true";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"super=true")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","super"=>"true"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:super=true@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="+encoded_url+"&super=true").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:super=true@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&super=true",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:super=true@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&super=true")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"super=true"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Geo Targeting

 &  geoCode = us 

It may be considered unusual for some local websites to receive worldwide traffic. Therefore, they can ban traffic from other countries. By using geotargeting, you can counter potential blocking.

Allows you to send requests through supported countries using geotargeting. In this way, you can more easily scrape the targeted website by focusing on a specific country.

All you have to do is send a request by selecting a country like `geoCode=us`

> To use this feature with DataCenter proxy, you must have a minimum **Pro Plan** subscription!

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?url=https://httpbin.co/anything&token=YOUR_TOKEN&geoCode=us'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:geoCode=us@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")geoCode="us"url="http://api.scrape.do?token={}&url={}&geoCode={}".format(token,targetUrl,geoCode)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:geoCode=us@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");vargeoCode="us";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&geoCode=${geoCode}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'geoCode=us'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&geoCode=us";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"geoCode=us")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","geoCode"=>"us"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:geoCode=us@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?url="+encoded_url+"&token=YOUR_TOKEN&geoCode=us").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:geoCode=us@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&geoCode=us",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:geoCode=us@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&geoCode=us")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"geoCode=us"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```
#### Supported Country Codes

Datacenter NetworkResidential & Mobile Network (Super)

* ![](/images/country-flags/AL.svg)`AL:`Albania
* ![](/images/country-flags/ID.svg)`ID:`Indonesia
* ![](/images/country-flags/LV.svg)`LV:`Latvia
* ![](/images/country-flags/FI.svg)`FI:`Finland
* ![](/images/country-flags/AU.svg)`AU:`Australia
* ![](/images/country-flags/CA.svg)`CA:`Canada
* ![](/images/country-flags/CL.svg)`CL:`Chile
* ![](/images/country-flags/CN.svg)`CN:`China
* ![](/images/country-flags/HR.svg)`HR:`Croatia
* ![](/images/country-flags/ES.svg)`ES:`Spain
* ![](/images/country-flags/LT.svg)`LT:`Lithuania
* ![](/images/country-flags/DK.svg)`DK:`Denmark
* ![](/images/country-flags/CZ.svg)`CZ:`Czech Republic
* ![](/images/country-flags/US.svg)`US:`United States
* ![](/images/country-flags/GB.svg)`GB:`Great Britain
* ![](/images/country-flags/DE.svg)`DE:`Germany
* ![](/images/country-flags/HU.svg)`HU:`Hungary
* ![](/images/country-flags/EE.svg)`EE:`Estonia
* ![](/images/country-flags/AR.svg)`AR:`Argentina
* ![](/images/country-flags/RO.svg)`RO:`Romania
* ![](/images/country-flags/JP.svg)`JP:`Japan
* ![](/images/country-flags/MY.svg)`MY:`Malaysia
* ![](/images/country-flags/AT.svg)`AT:`Austria
* ![](/images/country-flags/TR.svg)`TR:`Turkey
* ![](/images/country-flags/RU.svg)`RU:`Russia
* ![](/images/country-flags/FR.svg)`FR:`France
* ![](/images/country-flags/RS.svg)`RS:`Serbia
* ![](/images/country-flags/IL.svg)`IL:`Israel
* ![](/images/country-flags/PT.svg)`PT:`Portugal
* ![](/images/country-flags/IN.svg)`IN:`India
* ![](/images/country-flags/BR.svg)`BR:`Brazil
* ![](/images/country-flags/BE.svg)`BE:`Belgium
* ![](/images/country-flags/ZA.svg)`ZA:`South Africa
* ![](/images/country-flags/UA.svg)`UA:`Ukraine
* ![](/images/country-flags/PK.svg)`PK:`Pakistan
* ![](/images/country-flags/HK.svg)`HK:`HongKong
* ![](/images/country-flags/MT.svg)`MT:`Malta
* ![](/images/country-flags/SE.svg)`SE:`Sweden
* ![](/images/country-flags/PL.svg)`PL:`Poland
* ![](/images/country-flags/NL.svg)`NL:`Netherland
* ![](/images/country-flags/NO.svg)`NO:`Norway
* ![](/images/country-flags/AE.svg)`AE:`United A. E.
* ![](/images/country-flags/SA.svg)`SA:`Saudi Arabia
* ![](/images/country-flags/MX.svg)`MX:`Mexico
* ![](/images/country-flags/GR.svg)`GR:`Greece
* ![](/images/country-flags/EG.svg)`EG:`Egypt
* ![](/images/country-flags/SK.svg)`SK:`Slovakia
* ![](/images/country-flags/CH.svg)`CH:`Switzerland
* ![](/images/country-flags/IT.svg)`IT:`Italy
* ![](/images/country-flags/SG.svg)`SG:`Singapore

* ![](/images/country-flags/AF.svg)`AF:`Afghanistan
* ![](/images/country-flags/AL.svg)`AL:`Albania
* ![](/images/country-flags/AD.svg)`AD:`Andorra
* ![](/images/country-flags/AO.svg)`AO:`Angola
* ![](/images/country-flags/AR.svg)`AR:`Argentina
* ![](/images/country-flags/AM.svg)`AM:`Armenia
* ![](/images/country-flags/AW.svg)`AW:`Aruba
* ![](/images/country-flags/AU.svg)`AU:`Australia
* ![](/images/country-flags/AT.svg)`AT:`Austria
* ![](/images/country-flags/AZ.svg)`AZ:`Azerbaijan
* ![](/images/country-flags/BS.svg)`BS:`Bahamas
* ![](/images/country-flags/BD.svg)`BD:`Bangladesh
* ![](/images/country-flags/BY.svg)`BY:`Belarus
* ![](/images/country-flags/BE.svg)`BE:`Belgium
* ![](/images/country-flags/BZ.svg)`BZ:`Belize
* ![](/images/country-flags/BJ.svg)`BJ:`Benin
* ![](/images/country-flags/BT.svg)`BT:`Bhutan
* ![](/images/country-flags/BO.svg)`BO:`Bolivia
* ![](/images/country-flags/BA.svg)`BA:`Bosnia Herzegovina
* ![](/images/country-flags/BR.svg)`BR:`Brazil
* ![](/images/country-flags/VG.svg)`VG:`British Virgin I.
* ![](/images/country-flags/BG.svg)`BG:`Bulgaria
* ![](/images/country-flags/KH.svg)`KH:`Cambodia
* ![](/images/country-flags/CM.svg)`CM:`Cameroon
* ![](/images/country-flags/CA.svg)`CA:`Canada
* ![](/images/country-flags/CF.svg)`CF:`Central A. Rep.
* ![](/images/country-flags/TD.svg)`TD:`Chad
* ![](/images/country-flags/CL.svg)`CL:`Chile
* ![](/images/country-flags/CN.svg)`CN:`China
* ![](/images/country-flags/CO.svg)`CO:`Colombia
* ![](/images/country-flags/CR.svg)`CR:`Costa Rica
* ![](/images/country-flags/CI.svg)`CI:`Cote D'ivoire
* ![](/images/country-flags/HR.svg)`HR:`Croatia
* ![](/images/country-flags/CU.svg)`CU:`Cuba
* ![](/images/country-flags/CY.svg)`CY:`Cyprus
* ![](/images/country-flags/CZ.svg)`CZ:`Czech Republic
* ![](/images/country-flags/DK.svg)`DK:`Denmark
* ![](/images/country-flags/DJ.svg)`DJ:`Djibouti
* ![](/images/country-flags/DM.svg)`DM:`Dominica
* ![](/images/country-flags/EC.svg)`EC:`Ecuador
* ![](/images/country-flags/EG.svg)`EG:`Egypt
* ![](/images/country-flags/EE.svg)`EE:`Estonia
* ![](/images/country-flags/ET.svg)`ET:`Ethiopia
* ![](/images/country-flags/FJ.svg)`FJ:`Fiji
* ![](/images/country-flags/FI.svg)`FI:`Finland
* ![](/images/country-flags/FR.svg)`FR:`France
* ![](/images/country-flags/GM.svg)`GM:`Gambia
* ![](/images/country-flags/GB.svg)`GB:`Great Britain
* ![](/images/country-flags/GE.svg)`GE:`Georgia
* ![](/images/country-flags/DE.svg)`DE:`Germany
* ![](/images/country-flags/GH.svg)`GH:`Ghana
* ![](/images/country-flags/GR.svg)`GR:`Greece
* ![](/images/country-flags/HT.svg)`HT:`Haiti
* ![](/images/country-flags/HN.svg)`HN:`Honduras
* ![](/images/country-flags/HK.svg)`HK:`HongKong
* ![](/images/country-flags/HU.svg)`HU:`Hungary
* ![](/images/country-flags/IS.svg)`IS:`Iceland
* ![](/images/country-flags/IL.svg)`IL:`Israel
* ![](/images/country-flags/IN.svg)`IN:`India
* ![](/images/country-flags/ID.svg)`ID:`Indonesia
* ![](/images/country-flags/IR.svg)`IR:`Iran
* ![](/images/country-flags/IQ.svg)`IQ:`Iraq
* ![](/images/country-flags/IE.svg)`IE:`Ireland
* ![](/images/country-flags/IL.svg)`IL:`Israel
* ![](/images/country-flags/IT.svg)`IT:`Italy
* ![](/images/country-flags/JM.svg)`JM:`Jamaica
* ![](/images/country-flags/JP.svg)`JP:`Japan
* ![](/images/country-flags/JO.svg)`JO:`Jordan
* ![](/images/country-flags/KZ.svg)`KZ:`Kazakhstan
* ![](/images/country-flags/KE.svg)`KE:`Kenya
* ![](/images/country-flags/LB.svg)`LB:`Lebanon
* ![](/images/country-flags/LR.svg)`LR:`Liberia
* ![](/images/country-flags/LI.svg)`LI:`Liechtenstein
* ![](/images/country-flags/LT.svg)`LT:`Lithuania
* ![](/images/country-flags/LV.svg)`LV:`Latvia
* ![](/images/country-flags/LU.svg)`LU:`Luxembourg
* ![](/images/country-flags/MK.svg)`MK:`Macedonia
* ![](/images/country-flags/MG.svg)`MG:`Madagascar
* ![](/images/country-flags/MY.svg)`MY:`Malaysia
* ![](/images/country-flags/MV.svg)`MV:`Maldives
* ![](/images/country-flags/ML.svg)`ML:`Mali
* ![](/images/country-flags/MT.svg)`MT:`Malta
* ![](/images/country-flags/MR.svg)`MR:`Mauritania
* ![](/images/country-flags/MU.svg)`MU:`Mauritius
* ![](/images/country-flags/MX.svg)`MX:`Mexico
* ![](/images/country-flags/MD.svg)`MD:`Moldova
* ![](/images/country-flags/MC.svg)`MC:`Monaco
* ![](/images/country-flags/MN.svg)`MN:`Mongolia
* ![](/images/country-flags/ME.svg)`ME:`Montenegro
* ![](/images/country-flags/MA.svg)`MA:`Morocco
* ![](/images/country-flags/MZ.svg)`MZ:`Mozambique
* ![](/images/country-flags/MM.svg)`MM:`Myanmar
* ![](/images/country-flags/NL.svg)`NL:`Netherlands
* ![](/images/country-flags/NZ.svg)`NZ:`New Zealand
* ![](/images/country-flags/NG.svg)`NG:`Nigeria
* ![](/images/country-flags/NO.svg)`NO:`Norway
* ![](/images/country-flags/OM.svg)`OM:`Oman
* ![](/images/country-flags/PK.svg)`PK:`Pakistan
* ![](/images/country-flags/PA.svg)`PA:`Panama
* ![](/images/country-flags/PY.svg)`PY:`Paraguay
* ![](/images/country-flags/PE.svg)`PE:`Peru
* ![](/images/country-flags/PH.svg)`PH:`Philippines
* ![](/images/country-flags/PT.svg)`PT:`Portugal
* ![](/images/country-flags/PL.svg)`PL:`Poland
* ![](/images/country-flags/PR.svg)`PR:`Puerto Rico
* ![](/images/country-flags/QA.svg)`QA:`Qatar
* ![](/images/country-flags/RO.svg)`RO:`Romania
* ![](/images/country-flags/SA.svg)`SA:`Saudi Arabia
* ![](/images/country-flags/SN.svg)`SN:`Senegal
* ![](/images/country-flags/RS.svg)`RS:`Serbia
* ![](/images/country-flags/SC.svg)`SC:`Seychelles
* ![](/images/country-flags/SG.svg)`SG:`Singapore
* ![](/images/country-flags/SK.svg)`SK:`Slovakia
* ![](/images/country-flags/SI.svg)`SI:`Slovenia
* ![](/images/country-flags/ZA.svg)`ZA:`South Africa
* ![](/images/country-flags/KR.svg)`KR:`South Korea
* ![](/images/country-flags/SS.svg)`SS:`South Sudan
* ![](/images/country-flags/ES.svg)`ES:`Spain
* ![](/images/country-flags/SD.svg)`SD:`Sudan
* ![](/images/country-flags/SE.svg)`SE:`Sweden
* ![](/images/country-flags/CH.svg)`CH:`Switzerland
* ![](/images/country-flags/TW.svg)`TW:`Taiwan
* ![](/images/country-flags/TH.svg)`TH:`Thailand
* ![](/images/country-flags/TN.svg)`TN:`Tunisia
* ![](/images/country-flags/TG.svg)`TG:`Togo
* ![](/images/country-flags/TR.svg)`TR:`Turkey
* ![](/images/country-flags/TM.svg)`TM:`Turkmenistan
* ![](/images/country-flags/AE.svg)`AE:`United A. E.
* ![](/images/country-flags/UG.svg)`UG:`Uganda
* ![](/images/country-flags/UA.svg)`UA:`Ukraine
* ![](/images/country-flags/UY.svg)`UY:`Uruguay
* ![](/images/country-flags/US.svg)`US:`United States
* ![](/images/country-flags/UZ.svg)`UZ:`Uzbekistan
* ![](/images/country-flags/VE.svg)`VE:`Venezuela
* ![](/images/country-flags/VN.svg)`VN:`Vietnam
* ![](/images/country-flags/YE.svg)`YE:`Yemen
* ![](/images/country-flags/ZM.svg)`ZM:`Zambia
* ![](/images/country-flags/ZW.svg)`ZW:`Zimbabwe
> If you are looking for a country code that is not listed above, you can contact us via [support@scrape.do](mailto:support@scrape.do). We can add the country you need to our system.

---

### Regional Geo Targeting

 &  regionalGeoCode = europe 

It may be more efficient for you to scrape some websites by region. For example, scraping an e-commerce site serving in the European Union using any one of more than one European country can always help to keep your success rate higher.

> This feature can only be used with **Super Proxy**!

You can access regionally with the `regionalGeoCode=europe` parameter.

| **Available Regions** | Region Code |
| --- | --- |
| Europe | europe |
| Asia | asia |
| Africa | africa |
| Oceania | oceania |
| North America | northamerica |
| South America | southamerica |

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?url=https://httpbin.co/anything&token=YOUR_TOKEN&super=true&regionalGeoCode=europe'\
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:super=true&regionalGeoCode=europe@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")superParam="true"regionalGeoCode="europe"url="http://api.scrape.do?token={}&url={}&super={}&regionalGeoCode={}".format(token,targetUrl,superParam,regionalGeoCode)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:super=true&regionalGeoCode=europe@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varregionalGeoCode="europe";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&super=true&regionalGeoCode=${regionalGeoCode}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'super=true&regionalGeoCode=europe'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&super=true&regionalGeoCode=europe";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"super=true&regionalGeoCode=europe")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","super"=>"true","regionalGeoCode"=>"europe"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:super=true&regionalGeoCode=europe@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?url="+encoded_url+"&token=YOUR_TOKEN&super=true&regionalGeoCode=europe").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:super=true&regionalGeoCode=europe@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_CODE"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&super=true&regionalGeoCode=europe",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:super=true&regionalGeoCode=europe@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&super=true&regionalGeoCode=europe")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"super=true&regionalGeoCode=europe"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Sticky Sessions

 &  sessionId = 1234 

When you want to use the same proxy address for a certain period of time, you can pass the `sessionId=1234` parameter. It can be any integer value. Each unique integer value will be the ID of a session.

* SessionId value must be between 0 and 1000000.
* If no request is sent within 5 minutes, the session you created will be closed automatically.
* If the request sent with SessionId fails, a new proxy address will be provided and the session will be changed.
* If you need to use new proxy constantly, you don’t need to use session!
* If used with **Geo Targeting** or **Regional Geo Targeting**, the session will be created only for the relevant country or region.
* Sessions are created only for successful requests!

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/anything&sessionId=1234'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:sessionId=1234@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")sessionId="1234"url="http://api.scrape.do?token={}&url={}&sessionId={}".format(token,targetUrl,sessionId)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:sessionId=1234@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varsessionId="1234"varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&sessionId=${sessionId}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'sessionId=1234'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&sessionId=1234";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"sessionId=1234")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","sessionId"=>"1234"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:sessionId=1234@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="+encoded_url+"&sessionId=1234").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:sessionId=1234@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&sessionId=1234",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:sessionId=1234@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&sessionId=1234")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"sessionId=1234"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

Proxy Mode
----------

### What is Proxy Mode?

It may take time for companies or people currently working with a proxy provider to use the API system in our system. Therefore, you can easily switch from other proxy providers via Proxy Mode.

There is no difference between proxy mode and API mode other than the access method.

> Your operating system or running software **must trust** the [Scrape.do CA Certificate](/scrapedo_ca.crt) in its keychain, or SSL verification **must be disabled** with Proxy Mode. This is because we upgrade and forward your requests without sending them to the target site. This approach prevents certificate issues when SSL verification is performed on the `HTTPS` protocol.

### Proxy Information

![](/images/copy.svg)
```
protocol: http or https host: proxy.scrape.do port: 8080 username: YOUR_TOKEN password: PARAMETER Example format: http://token:parameters@proxy.scrape.do:8080
```
> Replace `PARAMETER` with the parameters you want to use. If you don’t know what parameters are, you can being by using `render=false` parameter. You can pass all parameters([**here**](/documentation/#overview)) in documents as parameters.

#### Example format for using multiple parameters:

![](/images/copy.svg)
```
http://token:render=false&super=true&geoCode=us@proxy.scrape.do:8080
```
#### Important Notes

* Proxy Mode uses `customHeaders=True` by default. That’s why we recommend you to read the **Custom Headers** documents. If you want to disable it, just pass CustomHeaders=false.
* You can use it by entering the same proxy information in places that accept HTTPS proxy.
* If you are using your own browser automation via Proxy Mode, we do not recommend using **Headless Browser** features! (it would be more accurate to `render=false`)
* Proxy Mode and API Mode use the same subscription package, there is no extra charge.

#### Example cURL

![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:@proxy.scrape.do:8080" 'https://httpbin.co/anything' -v
```

---

Request
-------

Scrape.do upgrades the requests you send so that they are not blocked by anti-bot solutions. In the meantime, there may be header, body or other information that you need to transmit to the target site. Or, if you know how the target website works, you can increase your success rates with the features here.

### POST/PUT Request

You can change the method type for all the requests to send with Scrape.do. We support `GET`, `POST`, `PUT`, `PATCH`, `HEAD` and `DELETE` methods.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request POST 'https://api.scrape.do?token=YOUR_URL&url=https://httpbin.co/anything'\ --header 'Content-Type: application/json'\ --data-raw '{"test-key":"test-value"}'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:@proxy.scrape.do:8080"'https://httpbin.co/anything' -v \ --header 'Content-Type: application/json'\ --data-raw '{"test-key":"test-value"}'
```
![](/images/copy.svg)
```
importrequestsimportjsonimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")url="http://api.scrape.do?token={}&url={}".format(token,targetUrl)payload=json.dumps({"test-key":"test-value"})headers={'Content-Type':'application/json'}response=requests.request("POST",url,headers=headers,data=payload)print(response.text)
```
![](/images/copy.svg)
```
importjsonimportrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}payload=json.dumps({"test-key":"test-value"})headers={'Content-Type':'application/json'}response=requests.request("POST",url,proxies=proxies,verify=False,headers=headers,data=payload)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varconfig={'method':'POST','url':`https://api.scrape.do?token=${token}&url=${targetUrl}`,'headers':{'Content-Type':'application/json'},body:JSON.stringify({"test-key":"test-value"})};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"POST",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:''}},headers:{'Content-Type':'application/json'},body:JSON.stringify({"test-key":"test-value"})}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}";varrequest=newHttpRequestMessage(HttpMethod.Post,requestURL);varbody=@"{""test-key"":""test-value""}";request.AddParameter("application/json",body,ParameterType.RequestBody);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"")};varrequest=newHttpRequestMessage(HttpMethod.Post,url);varbody=@"{""test-key"":""test-value""}";request.AddParameter("application/json",body,ParameterType.RequestBody);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();$headers[]='Content-Type: application/json';$body=['test-key'=>'test-value',];$body=http_build_query($body);curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_POSTFIELDS,$body);curl_setopt($curl,CURLOPT_HTTPHEADER,$headers);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN",];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'POST');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();$headers[]='Content-Type: application/json';curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);curl_setopt($curl,CURLOPT_POSTFIELDS,'{"test-key":"test-value"}');curl_setopt($curl,CURLOPT_HTTPHEADER,$headers);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'POST');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("application/json");RequestBodybody=RequestBody.create(mediaType,"{\"test-key\":\"test-value\"}");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_URL&url="+encoded_url+"").method("POST",body).addHeader("Content-Type","application/json").build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{MediaTypemediaType=MediaType.parse("application/json");RequestBodybody=RequestBody.create(mediaType,"{\"test-key\":\"test-value\"}");Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:render=true@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.POST(url,body).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url""strings")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s",token,encoded_url)method:="POST"payload:=strings.NewReader(`{"test-key":"test-value"}`)client:=&http.Client{}req,err:=http.NewRequest(method,url,payload)iferr!=nil{fmt.Println(err)return}req.Header.Add("Content-Type","application/json")res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url""strings")funcmain(){proxyStr:="http://YOUR_TOKEN:@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}payload:=strings.NewReader(`{  "test-key" : "test-value"  }`)req,err:=http.NewRequest("POST","https://httpbin.co/anything",payload)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}req.Header.Add("Content-Type","application/json")resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'require'json'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Post.new(url)request.body=JSON.dump({"test-key":"test-value"})response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:""})res["Content-Type"]="application/json",res.body=JSON.dump({"test-key":"test-value"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Custom Headers

 &  customHeaders = true  default =false

You can interfere with all headers sent to the target website via our service. Scrape.do sends User-Agent, Accept, Cookies, etc. from you. It takes all header parameters and forwards them. You must set `customHeaders=True` to use the feature.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/headers&customHeaders=True'--header 'Test-Header-Key: TestValue'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:customHeaders=True@proxy.scrape.do:8080"'https://httpbin.co/headers' -v --header 'Test-Header-Key: TestValue'
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/headers")customHeaders="true"payload={}url="http://api.scrape.do?token={}&url={}&customHeaders={}".format(token,targetUrl,customHeaders)headers={'Test-Header-Key':'TestValue'}response=requests.request("GET",url,headers=headers,data=payload)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/headers"token="YOUR_TOKEN"proxyModeUrl="http://{}:customHeaders=true@proxy.scrape.do:8080".format(token)headers={'Test-Header-Key':'TestValue'}proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False,headers=headers)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/headers");varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&customHeaders=true`,'headers':{'Test-Header-Key':'TestValue',}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'customHeaders=true'}},}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/headers");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&customHeaders=true";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);request.Headers.Add("Test-Header-Key","TestValue");varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/headers";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"customHeaders=true")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);request.Headers.Add("Test-Header-Key","TestValue");varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/headers","token"=>"YOUR_TOKEN","customHeaders"=>"true"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",'Test-Header-Key: TestValue'));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/headers";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:customHeaders=true@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",'Test-Header-Key: TestValue'));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/headers","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="encoded_url"&customHeaders=True").method("GET",body).addHeader("Test-Header-Key","TestValue").build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:customHeaders=True@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).addHeader("Test-Header-Key","TestValue").viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/headers")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&customHeaders=true",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}req.Header.Add("Test-Header-Key","TestValue")res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:customHeaders=true@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/headers",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}req.Header.Add("Test-Header-Key","TestValue")resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/headers"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&customHeaders=true")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)request['Test-Header-Key']='TestValue'response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/headers',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"customHeaders=true"})res["Test-Header-Key"]="TestValue"puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```
> If you leave the User-Agent information blank in the header field of the requests sent via programming languages, it can be filled with a default value like ‘python/httpclient’. Therefore, we strongly recommend that you use a real User-Agent with this feature.

#### Result

![](/images/copy.svg)
```
{"headers":{"Accept":"*/*","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Authority":"httpbin.co","Cache-Control":"no-cache,no-cache","Host":"httpbin.co","Referer":"https://httpbin.co","Sec-Ch-Ua":"\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"","Sec-Ch-Ua-Mobile":"?0","Sec-Ch-Ua-Platform":"\"macOS\"","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"none","Sec-Fetch-User":"?1","Test-Header-Key":"TestValue","Upgrade-Insecure-Requests":"1","User-Agent":"PostmanRuntime/7.29.2","X-Amzn-Trace-Id":"Root=1-63748965-50104cf629bc898d03188f57"}}
```

---

### Extra Headers

 &  extraHeaders = true  default =false

It is a feature that you can use only when there is one or more header parameters that you want to use for the needs of the target website, without breaking the requests we have created for the target website.

After setting the query parameter as `extraHeaders=true`, the header values ​​you will send with the `Sd-**` prefix will be sent to the target website.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/headers&extraHeaders=true'\ --header 'sd-Test: TestValue'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:extraHeaders=true@proxy.scrape.do:8080"'https://httpbin.co/headers' -v --header 'sd-Test: TestValue'
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/headers")extraHeaders="true"payload={}url="http://api.scrape.do?token={}&url={}&extraHeaders={}".format(token,targetUrl,extraHeaders)headers={'sd-Test':'TestValue'}response=requests.request("GET",url,headers=headers,data=payload)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/headers"token="YOUR_TOKEN"proxyModeUrl="http://{}:extraHeaders=true@proxy.scrape.do:8080".format(token)headers={'sd-Test':'TestValue'}proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/headers");varextraHeaders="true"varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&extraHeaders=${extraHeaders}`,'headers':{'sd-Test':'TestValue',}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'extraHeaders=true'}},headers:{'sd-Test':'TestValue',}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/headers");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&extraHeaders=true";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);request.Headers.Add("sd-Test","TestValue");varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/headers";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"extraHeaders=true")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);request.Headers.Add("sd-Test","TestValue");varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/headers","token"=>"YOUR_TOKEN","extraHeaders"=>"true"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",'sd-Test: TestValue'));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/headers";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:extraHeaders=true@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",'sd-Test: TestValue'));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/headers","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="+encoded_url+"&extraHeaders=true").method("GET",body).addHeader("sd-Test","TestValue").build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:extraHeaders=true@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/headers")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&extraHeaders=true",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}req.Header.Add("sd-Test","TestValue")res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:extraHeaders=true@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/headers",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}req.Header.Add("sd-Test","TestValue")resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/headers"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&extraHeaders=true")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)request["sd-Test"]="TestValue"response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/headers',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"extraHeaders=true"})res["sd-Test"]="TestValue"puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```
#### Example Result

![](/images/copy.svg)
```
{"headers":{"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Authority":"httpbin.co","Cache-Control":"no-cache","Host":"httpbin.co","Referer":"https://httpbin.co","Sec-Ch-Ua":"\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"","Sec-Ch-Ua-Mobile":"?0","Sec-Ch-Ua-Platform":"\"macOS\"","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"none","Sec-Fetch-User":"?1","Test":"TestValue","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","X-Amzn-Trace-Id":"Root=1-63748c46-2e20cdb45d2d89455b4e4fd0"}}
```
### Forward Headers

 &  forwardHeaders = boolean  default =false

You may need to forward your own headers to the target web page you want to scrape without auto generated headers. In this case you can use `forwardHeaders=True` query parameter.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/headers&forwardHeaders=True'--header 'Test-Header-Key: TestValue'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:forwardHeaders=True@proxy.scrape.do:8080"'https://httpbin.co/headers' -v --header 'Test-Header-Key: TestValue'
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")render="true"url="http://api.scrape.do?token={}&url={}&render={}".format(token,targetUrl,render)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/headers"token="YOUR_TOKEN"proxyModeUrl="http://{}:forwardHeaders=true@proxy.scrape.do:8080".format(token)headers={'Test-Header-Key':'TestValue'}proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False,headers=headers)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/headers");varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&forwardHeaders=true`,'headers':{'Test-Header-Key':'TestValue',}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'forwardHeaders=true'}},headers:{'Test-Header-Key':'TestValue',}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/headers");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&forwardHeaders=true";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);request.Headers.Add("Test-Header-Key","TestValue");varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="ada2f36f657e4bcf8470227cd8d4c639d549aa97127";stringurl="https://httpbin.co/headers";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"forwardHeaders=true")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);request.Headers.Add("Test-Header-Key","TestValue");varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/headers","token"=>"YOUR_TOKEN","forwardHeaders"=>"true"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",'Test-Header-Key: TestValue'));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/headers";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:forwardHeaders=true@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",'Test-Header-Key: TestValue'));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/headers","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="encoded_url"&forwardHeaders=True").method("GET",body).addHeader("Test-Header-Key","TestValue").build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:forwardHeaders=True@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).addHeader("Test-Header-Key","TestValue").viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/headers")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&forwardHeaders=true",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}req.Header.Add("Test-Header-Key","TestValue")res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:forwardHeaders=true@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/headers",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}req.Header.Add("Test-Header-Key","TestValue")resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/headers',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"forwardHeaders=true"})res["Test-Header-Key"]="TestValue"puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/headers',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"forwardHeaders=true"})res["Test-Header-Key"]="TestValue"puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```
#### Example Result

![](/images/copy.svg)
```
{"headers":{"Accept":"*/*","Accept-Encoding":"gzip, deflate, br","Host":"httpbin.co","Test-Header-Key":"TestValue","User-Agent":"curl/7.85.0","X-Amzn-Trace-Id":"Root=1-63f5d502-4fa0a57019562b1b55fed4f6"}}
```

---

### Set Cookies

 &  setCookies = url encoded cookies  default =false

You can pass cookies to the target website by encoding `setCookies=cookie1=value1;cookie2=value2;` and our system will send the cookies you have forwarded to the target website.

You don’t need to use **extraHeaders** or **customHeaders** parameters to send cookies to the target website. You can use the **setCookies** parameter to send cookies to the target website.

> You should use url encode for your cookie values. For example; setCookies=cookie1%3Dvalue1%3B. You can see more details [here](#url).

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?url=https://httpbin.co/anything&token=YOUR_TOKEN&setCookies=cookie1%3Dvalue1%3Bcookie2%3Dvalue2%3Bcookie3%3Dvalue3%3B'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:setCookies=cookie1%3Dvalue1%3Bcookie2%3Dvalue2%3Bcookie3%3Dvalue3%3B;@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"encodedCookies=urllib.parse.quote("cookie1=value1;cookie=value2;cookie3=value3;")targetUrl=urllib.parse.quote("https://httpbin.co/headers")url="http://api.scrape.do?token={}&url={}&setCookies={}".format(token,targetUrl,encodedCookies)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3importurllib.parseurllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"encodedCookies=urllib.parse.quote("cookie1=value1;cookie=value2;cookie3=value3;")proxyModeUrl="http://{}:setCookies={}@proxy.scrape.do:8080".format(token,encodedCookies)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varcookies="cookie1=value1;cookie=value2;cookie3=value3;";varencodedCookies=encodeURIComponent(cookies);varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&setCookies=${encodedCookies}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";varcookies="cookie1=value1;cookie=value2;cookie3=value3;";varencodedCookies=encodeURIComponent(cookies);axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'setCookies='+encodedCookies}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");stringcookies="cookie1=value1;cookie=value2;cookie3=value3;";varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&setCookies={WebUtility.UrlEncode(cookies)}";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";stringencodedCookies=WebUtility.UrlEncode("cookie1=value1;cookie=value2;cookie3=value3;");varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,$"setCookies={encodedCookies}")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();$token="YOUR_TOKEN";$encodedUrl=urlencode("https://httpbin.co/anything");$encodedCookies=urlencode('cookie1=value1;cookie=value2;cookie3=value3;');$url="https://api.scrape.do?token={$token}&url={$encodedUrl}&setCookies={$encodedCookies}";curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,$url);$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$encodedCookies="setCookies=cookie1%3Dvalue1%3Bcookie%3Dvalue2%3Bcookie3%3Dvalue3%3B";$proxy=sprintf("http://%s:%s@proxy.scrape.do:8080",$token,$encodedCookies);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Stringcookies=URLEncoder.encode("cookie1=value1;cookie=value2;cookie3=value3;","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?url="+encoded_url+"&token=YOUR_TOKEN&setCookies="+cookies+"").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:setCookies=cookie1=value1;cookie=value2;cookie3=value3;@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")cookies:=url.QueryEscape("cookie1=value1;cookie=value2;cookie3=value3;")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&setCookies=%s",token,encoded_url,cookies)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"cookies:=url.QueryEscape("cookie1=value1;cookie=value2;cookie3=value3;")proxyStr:=fmt.Sprintf("http://%s:setCookies=%s@proxy.scrape.do:8080",token,cookies)proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"cookies=CGI.escape"cookie1=value1;cookie=value2;cookie3=value3;"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&setCookies="+cookies+"")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'require'cgi'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestcookies=CGI.escape"cookie1=value1;cookie=value2;cookie3=value3;"res=HTTParty.get('https://httpbin.co/anything',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"setCookies="+cookies+""})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```
#### Example Result

![](/images/copy.svg)
```
{"cookies":{"cookie1":"value1","cookie2":"value2","cookie3":"value3"}}
```

---

### Disable Redirection

 &  disableRedirection = boolean  default =false

Scrape.do by default follow redirected target web pages and returns results from where it redirected. It has a maximum of 10 redirections. If you reach the limit, the system will stop redirection and return a response with the last status.

In some cases, you may not want to use the redirection mechanism. By passing the `disableRedirection=true` parameter, you can prevent default redirection.

> When you use this feature, you can find the url information that the target website wants to redirect you to in the `Scrape.do-Target-Redirected-Location` header.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_URL&url=https://httpbin.co/anything&disableRedirection=true'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:disableRedirection=true@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")disabledRedirection="true"url="http://api.scrape.do?token={}&url={}&disableRedirection={}".format(token,targetUrl,disabledRedirection)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:disableRedirection=true@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");vardisableRedirection="true";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&disableRedirection=${disableRedirection}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'disableRedirection=true'}},}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&disableRedirection=true";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"disableRedirection=true")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","disableRedirection"=>"true"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:disableRedirection=true@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_URL&url="+encoded_url+"&disableRedirection=true").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:disableRedirection=true@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&disableRedirection=true",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:disableRedirection=true@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&disableRedirection=true")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"disableRedirection=true"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Callback & Webhook

 &  callback = url encoded webhook address 

With this feature, you don’t have to wait for the request results. You can send us a webhook address by encoding `callback=http://yourdomain.com/webhook` and our system will wait for the result of the request for you. When the result is received, it returns your request via the webhook you have forwarded.

#### Important Notes

* You must return 200 or 201 status code to us via webhook.
* If we can’t send you the result by webhook correctly, we will send you a request again, up to a maximum of 5 times every 2 minutes.
* Our system will send you the result as **POST**.
* The url you transmit with callback should be encoded. For more details, you can go to the url field and see how to encode it.
* You can make callback requests up to your maximum concurrency limit at the same time. For example, if you have a limit of 40 simultaneous requests, you cannot expect 41 callback calls. Our system will return you a maximum of 40 results at the same time.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?url=https://httpbin.co/anything&token=YOUR_TOKEN&callback=https://webhook.site/bc3ba9a9-7df9-421e-b991-6fd38065bb5c'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:callback=https://mywebsite.com/webhook@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")callbackUrl=urllib.parse.quote("https://mywebsite.com/webhook")url="http://api.scrape.do?token={}&url={}&callback={}".format(token,targetUrl,callbackUrl)response=requests.request("POST",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:callback=https://mywebsite.com/webhook@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("POST",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varcallbackUrl=encodeURIComponent("https://mywebsite.com/webhook");varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&callback=${callbackUrl}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";varcallback='https://mywebsite.com/webhook';varencodedcallback=encodeURIComponent(callback);axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'callback='+encodedcallback}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");stringcallbackWebhookURL=WebUtility.UrlEncode("https://mywebsite.com/webhook");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&callback={callbackWebhookURL}";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"callback=https://mywebsite.com/webhook")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","callback"=>"https://mywebsite.com/webhook"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:callback=https://mywebsite.com/webhook@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Stringencoded_callbackUrl=URLEncoder.encode("https://mywebsite.com/webhook","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?url="+encoded_url+"&callback="+encoded_callbackUrl+"").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:callback=https://mywebsite.com/webhook@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")encoded_callbackUrl:=url.QueryEscape("https://mywebsite.com/webhook")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&callback=%s",token,encoded_url,encoded_callbackUrl)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:callback=https://mywebsite.com/webhook@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"strWebhook=CGI.escape"https://mywebsite.com/webhook"url=URI("https://api.scrape.do?token=YOUR_TOKEN&url="+str+"&callback="+strWebhook+"")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"callback=https://mywebsite.com/webhook"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Timeout

 &  timeout = integer  default =60000

You can set the timeout value for the request you will send to the target website.

The value it can take must be between 5000 ms and 120000 ms. If the time is exceeded, system will return you that the request failed.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/anything&timeout=5000'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:timeout=5000@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")timeout="5000"url="http://api.scrape.do?token={}&url={}&timeout={}".format(token,targetUrl,timeout)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:timeout=5000@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");vartimeout="5000";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&timeout=${timeout}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'timeout=5000'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&timeout=5000";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varrespponse=client.SendAsync(request).Result;varcontent=respponse.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"timeout=5000")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","timeout"=>"5000"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:timeout=5000@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="encoded_url"&timeout=5000").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:timeout=5000@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&timeout=5000",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:timeout=5000@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&timeout=5000")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"timeout=5000"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Retry Timeout

 &  retryTimeout = integer  default =15000

Our system determines the maximum waiting time with this parameter while waiting for results from the target website. When the time is exceeded, it sends a new request and checks it cyclically.

You can change this parameter, which is 15000 ms by default. The values it can take can be between 5000ms and 55000ms.

**Important:** Using this parameter can affect your success rates.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/anything&retryTimeout=5000'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:retryTimeout=5000@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")timeout="5000"url="http://api.scrape.do?token={}&url={}&retryTimeout={}".format(token,targetUrl,timeout)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:retryTimeout=5000@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");vartimeout="5000";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&retryTimeout=${timeout}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'retryTimeout=5000'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&retryTimeout=5000";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"retryTimeout=5000")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","retryTimeout"=>"5000"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:retryTimeout=5000@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="+encoded_url+"&retryTimeout=5000").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:retryTimeout=5000@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encodedUrl:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&retryTimeout=5000",token,encodedUrl)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:retryTimeout=5000@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&retryTimeout=5000")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"retryTimeout=5000"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Disable Retry

 &  disableRetry = boolean  default =false

When you use this parameter, our system will not retry the request if it fails.

Regardless of the initial response status, it will return you the result as successful or unsuccessful.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/anything&disableRetry=true'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:disableRetry=true@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")disableRetry="true"url="http://api.scrape.do?token={}&url={}&disableRetry={}".format(token,targetUrl,disableRetry)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:disableRetry=true@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");vardisableRetry="true";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&disableRetry=${disableRetry}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'disableRetry=true'}},}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&disableRetry=true";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"disableRetry=true")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","disableRetry"=>"true"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:disableRetry=true@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="+encoded_url+"&disableRetry=true").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:disableRetry=true@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&disableRetry=true",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:disableRetry=true@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&disableRetry=true")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"disableRetry=true"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Device

 &  Device = string  default =desktop

The device parameter is used to determine the type of device used for data scraping through our API service. We offer two options: “Desktop” and “Mobile”. These options allow us to identify which devices users are accessing and optimize data scraping for the desired device. A website can be presented in different designs on desktop computers and mobile devices. Therefore, the correct identification of the device used in data scraping increases the accuracy and relevance of the obtained data.

**Important:** You can improve the user experience. For example, mobile-optimized data scraping provides faster response times and better performance.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.org/anything&device=desktop'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:device=desktop@proxy.scrape.do:8080"'https://httpbin.org/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.org/anything")device="desktop"url="http://api.scrape.do?token={}&url={}&device={}".format(token,targetUrl,device)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.org/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:device=desktop@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.org/anything");vardevice="desktop";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&device=${device}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'device=desktop'}},}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.org/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&device=desktop";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.org/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"device=desktop")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.org/anything","token"=>"YOUR_TOKEN","device"=>"desktop"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.org/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:device=desktop@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.org/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="+encoded_url+"&device=desktop").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="http://httpbin.org/anything";URIproxyURI=newURI("http://YOUR_TOKEN:device=desktop@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.org/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&device=desktop",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:device=desktop@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.org/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.org/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&device=desktop")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.org/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"device=desktop"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

Headless Browser
----------------

By using real browser instances, you can scrape the data presented by the target web page through the browser.

In web pages created using frameworks such as React, Angular, Vue or JQuery, data can be loaded after a while, and in this case, you may need to use a headless browser when scraping.

We can produce solutions for some difficult to scrap websites via headless browser. So this parameter is sure to be an easier solution for hard to scrape websites.

Thanks to our infrastructure, you can easily cope with these difficulties without dealing with physical resources and headless browser configurations.

---

### JS Render

 &  render = boolean  default =false
> Each render request uses 5 concurrency.

If you have a web page that you only need to open with a browser and you need to wait for the results to load, simply pass the `render=true` parameter. Our infrastructure will connect to the target website for you using the headless browser network and try to bring the results.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/anything&render=true'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:render=true@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")render="true"url="http://api.scrape.do?token={}&url={}&render={}".format(token,targetUrl,render)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:render=true@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varrender="true";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&render=${render}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'render=true'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&device=desktop";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"render=true")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","render"=>"true"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:render=true@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="+encoded_url+"&render=true").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:render=true@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&render=true",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:render=true@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&render=True")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"render=true"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Wait Until

 &  waitUntil = string  default =domcontentloaded

Our headless browser system uses `waitUntil=domcontentloaded` during navigation by default. However, in some cases, you may need to change it. With this parameter, you can change this feature and ensure that the page is loaded correctly according to your needs.

The values ​​that the **waitUntil** parameter can take should be ‘domcontentloaded’, ’networkidle0’ and ’networkidle2’. ‘domcontentloaded’ waits for the DOMContentLoaded event to fire. ’networkidle0’ waits until there are no more than 0 network connections for at least 500 ms. ’networkidle2’ waits until there are no more than 2 network connections for at least 500 ms.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/anything&waitUntil=domcontentloaded&render=true'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:waitUntil=domcontentloaded&render=true@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl="https://httpbin.co/anything"opts="domcontentloaded"encoded_url=urllib.parse.quote(targetUrl)url="http://api.scrape.do?token={}&url={}&waitUntil={}&render=true".format(token,encoded_url,opts)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:waitUntil=domcontentloaded&render=true@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl="https://httpbin.co/anything"varencodedUrl=encodeURIComponent(targetUrl);varopts="domcontentloaded";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${encodedUrl}&waitUntil=${opts}&render=true`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'waitUntil=domcontentloaded&render=true'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={WebUtility.UrlEncode(url)}&waitUntil=domcontentloaded&render=true";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varrespponse=client.SendAsync(request).Result;varcontent=respponse.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"waitUntil=domcontentloaded&render=true")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varrespponse=client.SendAsync(request).Result;varcontent=respponse.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","waitUntil"=>"domcontentloaded","render"=>"true"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:waitUntil=domcontentloaded&render=true@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="encoded_url"&waitUntil=domcontentloaded&render=true").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:waitUntil=domcontentloaded&render=true@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&waitUntil=domcontentloaded&render=true",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:waitUntil=domcontentloaded&render=true@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str="https://httpbin.co/anything"encoded_url=CGI.escapestrurl=URI("https://api.scrape.do?url="+encoded_url+"&token=YOUR_TOKEN&waitUntil=domcontentloaded&render=true")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"waitUntil=domcontentloaded&render=true"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Custom Wait

 &  customWait = integer  default =0

With the JS Render infrastructure, you may want to wait for a certain period of time to ensure that all results are loaded correctly on the web page you go to. If you need to wait less or more, it is very easy to change this parameter.

* It can take values: It can be between 0 and 35000 ms.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/anything&customWait=1000&render=true'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:render=true&customWait=1000@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")customWait="1000"render="true"url="http://api.scrape.do?token={}&url={}&customWait={}&render={}".format(token,targetUrl,customWait,render)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:render=true&customWait=1000@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varcustomWait="1000";varrender=true;varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&customWait=${customWait}&render=${render}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'render=true&customWait=1000'}},}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&render=true&customWait=1000";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"render=true&customWait=1000")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","customWait"=>"1000","render"=>"true"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:render=true&customWait=1000@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="+encoded_url+"&customWait=1000&render=true").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:customWait=1000&render=true@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&customWait=1000&render=true",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:render=true&customWait=1000@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&customWait=1000&render=true")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"render=true&customWait=1000"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Wait CSS Selector

 &  waitSelector = .sample-selector 

With the JS Render infrastructure, the data you expect on the web page you go to can be returned via special elements. We can wait for the results in these fields with the WaitSelector and return the result to you when the relevant element is loaded.

For example, you can wait for the element specified in the example below using `waitSelector=.element` or `waitSelector=#element-id`. The system waits for the parameter you transmit to occur in the content for up to 10 seconds. If the result does not occur, the answer will be returned to you in its raw form.

> **Important** You need to url encode the **WaitSelector** value!

#### Target Data in Browser

![](/images/copy.svg)
```
<divclass="element"id="element-id">... content </div>
```
#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?url=https://httpbin.co/anything&render=True&token=YOUR_TOKEN&waitSelector=.class_name'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:waitSelector=.class_name@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")render="true"waitSelector=".class_name"url="http://api.scrape.do?token={}&url={}&render={}&waitSelector={}".format(token,targetUrl,render,waitSelector)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:waitSelector=.class_name&render=true@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varrender="true";varwaitSelector=".class_name";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&render=${render}&waitSelector=${waitSelector}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'waitSelector=.class_name&render=true'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");stringwaitSelector=".class_name"varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&render=true&waitSelector={waitSelector}";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varrespponse=client.SendAsync(request).Result;varcontent=respponse.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"waitSelector=.class_name")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varrespponse=client.SendAsync(request).Result;varcontent=respponse.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","render"=>"true","waitSelector"=>".class_name"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:waitSelector=.class_name&render=true@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?url="+encoded_url+"&render=true&token=YOUR_TOKEN&waitSelector=.class_name").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:render=true&waitSelector=.class_name@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&render=true&waitSelector=.class_name",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:waitSelector=.class_name@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&render=True&waitSelector=.class_name")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"waitSelector=.class_name"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Width

 &  width = integer  default =1920

You can change the dimensions of the browser by passing the `width=1920` parameter.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?url=https://httpbin.co/anything&render=true&token=YOUR_TOKEN&width=1920&height=1024'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:render=true&height=1024&width=1920@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")render="true"width="1920"height="1024"url="http://api.scrape.do?token={}&url={}&render={}&width={}&height={}".format(token,targetUrl,render,width,height)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:render=true&height=1024&width=1920@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varrender="true";varwidth="1920";varheight="1024"varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&render=${render}&width=${width}&height=${height}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'render=true&height=1024&width=1920'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&render=true&width=1920&height=1024";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"render=true&height=1024&width=1920")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","render"=>"true","width"=>"1920","height"=>"1024"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:render=true&height=1024&width=1920@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?url="+encoded_url+"&render=true&token=YOUR_TOKEN&width=1920&height=1024").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:render=True&height=1024&width=1920@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&render=true&width=1920&height=1024",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:render=true&height=1024&width=1920@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&render=true&width=1920&height=1024")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"render=true&height=1024&width=1920"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Height

 &  height = integer  default =1080

You can change the dimensions of the browser by passing the `height=1080` parameter.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?url=https://httpbin.co/anything&token=YOUR_TOKEN&render=true&height=1024&width=1920'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:render=true&height=1024&width=1920@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")render="true"height="1024"width="1920"url="http://api.scrape.do?token={}&url={}&render={}&height={}&width={}".format(token,targetUrl,render,height,width)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:render=true&height=1024&width=1920@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varrender="true";varheight="1024";varwidth="1920";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&render=${render}&height=${height}&width=${width}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'render=true&height=1024&width=1920'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&render=true&height=1024&width=1920";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"render=true&height=1024&width=1920")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","render"=>"true","height"=>"1024","width"=>"1920"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:render=true&height=1024&width=1920@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?url="+encoded_url+"&token=YOUR_TOKEN&render=True&height=1024&width=1920").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:render=True&height=1024&width=1920@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&render=True&height=1024&width=1920",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:render=true&height=1024&width=1920@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&render=True&height=1024&width=1920")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"render=true&height=1024&width=1920"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Block Resources

 &  blockResources = boolean  default =true

By default, it is a true feature so that the results are loaded faster and returned to you faster on the website you go through the Headless browser. If you want to turn this feature off, simply pass the `blockResources=false` parameter.

> This feature may affect success rates for some target websites. Therefore, marking **false** on problematic web pages may increase your success rate.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?url=https://httpbin.co/anything&render=True&token=YOUR_TOKEN&blockResources=false'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:render=true&blockResources=false@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")render="true"blockResources="false"url="http://api.scrape.do?token={}&url={}&render={}&blockResources={}".format(token,targetUrl,render,blockResources)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:render=true&blockResources=false@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything")varrender="true";varblockResources="false";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&render=${render}&blockResources=${blockResources}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'render=true&blockResources=false'}},}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&render=True&blockResources=false";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"render=True&blockResources=false")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","render"=>"true","blockResources"=>"false"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:render=true&blockResources=false@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?url="+encoded_url+"&render=true&token=YOUR_TOKEN&blockResources=false").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:render=true&blockResources=false@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encodedUrl:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&blockResources=false&render=true",token,encodedUrl)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:render=true&blockResources=false@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&render=True&token=YOUR_TOKEN&blockResources=false")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"render=true&blockResources=false"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Screenshot

 &  screenShot = boolean  default =false

If you need what the target web page looks like, it’s easy to do with Scrape.do. You can take a screenshot and download it simply by sending the `screenShot=true` parameter.

> When you use the ScreenShot feature, our infrastructure will continue to operate with `blockResources=false` and `render=true` so that the contents are loaded completely correctly.

#### Important Notes

* Screenshot feature cannot be used without `returnJSON=true` parameter!
* You can use only one of the three screenshot features at the same time.
* The **screenShot** parameter and the **playwithBrowser** parameter cannot be used together. If you need to take more than one screenshot, you can add it as an action with [Play with Browser](#play-with-browser).

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do/?token=YOUR_TOKEN&screenShot=true&render=true&returnJSON=true&url=http://example.com/'\
```
![](/images/copy.svg)
```
curl -k -x "https://YOUR_TOKEN:screenShot=true&render=true&returnJSON=true@proxy.scrape.do:8080"'http://example.com/' -v
```
![](/images/copy.svg)
```
importbase64importjsonimportrequestsimporturllib.parsetoken="YOUR_TOKEN"raw_url="http://example.com/"url=urllib.parse.quote(raw_url)req_url=f"https://api.scrape.do?token={token}&url={url}&screenShot=true&render=true&returnJSON=true"resp=requests.get(req_url)ifresp.status_code!=requests.codes.ok:resp.raise_for_status()json_map=json.loads(resp.text)image_b64=json_map["screenShots"][0]["image"]image_bytes=base64.b64decode(image_b64)file_path="Example.png"withopen(file_path,"wb")asfile:file.write(image_bytes)
```
![](/images/copy.svg)
```
importurllib3importrequestsimportbase64importjsonimporturllib.parseurllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="http://example.com/"token="YOUR_TOKEN"proxyModeUrl="http://{}:render=true&screenShot=true&returnJSON=true@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)ifresponse.status_code==200:json_map=json.loads(response.text)image_b64=json_map["screenShots"][0]["image"]image_bytes=base64.b64decode(image_b64)file_path="Example.png"withopen(file_path,"wb")asfile:file.write(image_bytes)else:print(response)
```
![](/images/copy.svg)
```
constaxios=require('axios');constfs=require('fs');consttoken='YOUR_TOKEN';consturl=encodeURIComponent('http://example.com/');constrequestURL=`https://api.scrape.do?token=${token}&url=${url}&screenShot=true&render=true&returnJSON=true`;axios.get(requestURL).then(response=>{if(response.status===200){constcontent=response.data;constimageB64=content.screenShots[0].image;constfilePath='Example.png';fs.writeFile(filePath,Buffer.from(imageB64,'base64'),err=>{if(err){console.error(err);}});}else{console.log(response.status);}}).catch(error=>{console.error(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');constfs=require('fs');consttoken="YOUR_TOKEN";consttargetUrl="http://example.com/";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'screenShot=true&render=true&returnJSON=true'}},responseType:'arraybuffer'}).then(response=>{constimageBuffer=response.data;constfilePath='Example.png';// Dosyayı kaydet fs.writeFile(filePath,imageBuffer,err=>{if(err){console.error(err);}else{console.log('SUCCESS ! '+filePath);}});}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("http://example.com/");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&screenShot=true&render=true&returnJSON=true";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;if(response.StatusCode==HttpStatusCode.OK){varcontent=response.Content.ReadAsStringAsync().Result;JTokencParse=JToken.Parse(content);stringimageB64=cParse.SelectToken("screenShots[0].image").ToString();stringfilePath="Example.png";File.WriteAllBytes(filePath,Convert.FromBase64String(imageB64));}else{Console.WriteLine(response);}
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="http://example.com/";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"screenShot=true&render=true&returnJSON=true")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=respponse.Content.ReadAsStringAsync().Result;if(response.StatusCode==HttpStatusCode.OK){varcontent=response.Content.ReadAsStringAsync().Result;JTokencParse=JToken.Parse(content);stringimageB64=cParse.SelectToken("screenShots[0].image").ToString();stringfilePath="Example.png";File.WriteAllBytes(filePath,Convert.FromBase64String(imageB64));}else{Console.WriteLine(response);}
```
![](/images/copy.svg)
```
<?php$token="YOUR_TOKEN";$rawURL="http://example.com/";$url=urlencode($rawURL);$reqURL=sprintf("https://api.scrape.do?token=%s&url=%s&screenShot=true&render=true&returnJSON=true",$token,$url);$response=file_get_contents($reqURL);if(!$response){die("Failed to fetch response.");}$jsonMap=json_decode($response,true);if(!$jsonMap){die("Failed to parse response.");}$imageB64=$jsonMap["screenShots"][0]["image"];$imageBytes=base64_decode($imageB64);$filePath="Example.png";$file=fopen($filePath,"wb");if(!$file){die("Failed to open file for writing.");}fwrite($file,$imageBytes);fclose($file);
```
![](/images/copy.svg)
```
<?php$token="YOUR_TOKEN";$targetUrl="http://example.com/";$proxyUrl="http://{$token}:screenShot=true&render=true&returnJSON=true@proxy.scrape.do:8080";$ch=curl_init();curl_setopt($ch,CURLOPT_URL,$targetUrl);curl_setopt($ch,CURLOPT_PROXY,$proxyUrl);curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);curl_setopt($ch,CURLOPT_FOLLOWLOCATION,true);curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,false);$response=curl_exec($ch);if(curl_errno($ch)){echo'Error: '.curl_error($ch);exit;}curl_close($ch);$jsonMap=json_decode($response,true);$imageB64=$jsonMap["screenShots"][0]["image"];$imageBytes=base64_decode($imageB64);$filePath="Example.png";$file=fopen($filePath,'wb');if(!$file){echo"Error opening file";exit;}fwrite($file,$imageBytes);fclose($file);?>
```
![](/images/copy.svg)
```
Stringtoken="YOUR_TOKEN";StringrawUrl="http://example.com/";Stringurl=URLEncoder.encode(rawUrl,"UTF-8");StringreqUrl=String.format("https://api.scrape.do?token=%s&url=%s&screenShot=true&render=true&returnJSON=true",token,url);CloseableHttpClienthttpClient=HttpClients.createDefault();HttpGethttpGet=newHttpGet(reqUrl);CloseableHttpResponseresponse=httpClient.execute(httpGet);try{HttpEntityentity=response.getEntity();StringresponseBody=entity!=null?EntityUtils.toString(entity):null;JSONObjectjsonObject=newJSONObject(responseBody);StringimageB64=jsonObject.getJSONArray("screenShots").getJSONObject(0).getString("image");byte[]imageBytes=Base64.getDecoder().decode(imageB64);StringfilePath="Example.png";FileOutputStreamfos=newFileOutputStream(filePath);fos.write(imageBytes);fos.close();}finally{response.close();}
```
![](/images/copy.svg)
```
Stringurl="http://example.com/";URIproxyURI=newURI("http://YOUR_TOKEN:screenShot=true&render=true&returnJSON=true@proxy.scrape.do:8080");StringbasicAuth=Base64.getEncoder().encodeToString(proxyURI.getUserInfo().getBytes());Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();JSONObjectjsonObject=newJSONObject(response);StringimageB64=jsonObject.getJSONArray("screenShots").getJSONObject(0).getString("image");byte[]imageBytes=Base64.getDecoder().decode(imageB64);StringfilePath="Example.png";FileOutputStreamfos=newFileOutputStream(filePath);fos.write(imageBytes);fos.close();
```
![](/images/copy.svg)
```
packagemainimport("encoding/base64""encoding/json""fmt""io/ioutil""net/http""net/url""os")funcmain(){token:="YOUR_TOKEN"rawURL:="http://example.com/"url:=url.QueryEscape(rawURL)reqURL:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&screenShot=true&render=true&returnJSON=true",token,url)resp,err:=http.Get(reqURL)iferr!=nil{panic(err)}deferresp.Body.Close()ifresp.StatusCode!=http.StatusOK{panic(resp.Status)}bytes,err:=ioutil.ReadAll(resp.Body)iferr!=nil{panic(err)}jsonMap:=make(map[string]interface{})err=json.Unmarshal(bytes,&jsonMap)iferr!=nil{panic(err)}imageB64:=jsonMap["screenShots"].([]interface{})[0].(map[string]interface{})["image"].(string)imageBytes,err:=base64.StdEncoding.DecodeString(imageB64)iferr!=nil{panic(err)}filePath:="Example.png"file,err:=os.Create(filePath)iferr!=nil{panic(err)}deferfile.Close()_,err=file.Write(imageBytes)iferr!=nil{panic(err)}}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""encoding/base64""encoding/json""fmt""io/ioutil""net/http""net/url""os")funcmain(){proxyStr:="http://YOUR_TOKEN:screenShot=true&render=true&returnJSON=true@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","http://example.com/",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}bytes,err:=ioutil.ReadAll(resp.Body)iferr!=nil{panic(err)}jsonMap:=make(map[string]interface{})err=json.Unmarshal(bytes,&jsonMap)iferr!=nil{panic(err)}imageB64:=jsonMap["screenShots"].([]interface{})[0].(map[string]interface{})["image"].(string)imageBytes,err:=base64.StdEncoding.DecodeString(imageB64)iferr!=nil{panic(err)}filePath:="Example.png"file,err:=os.Create(filePath)iferr!=nil{panic(err)}deferfile.Close()_,err=file.Write(imageBytes)iferr!=nil{panic(err)}}
```
![](/images/copy.svg)
```
require'base64'require'json'require'net/http'require'uri'token="YOUR_TOKEN"raw_url="http://example.com/"url=URI.encode_www_form_component(raw_url)req_url="https://api.scrape.do?token=#{token}&url=#{url}&screenShot=true&render=true&returnJSON=true"uri=URI.parse(req_url)resp=Net::HTTP.get_response(uri)ifresp.code!='200'raise"Error: #{resp.code} - #{resp.message}"endjson_map=JSON.parse(resp.body)image_b64=json_map["screenShots"][0]["image"]image_bytes=Base64.decode64(image_b64)file_path="Example.png"File.open(file_path,"wb")do|file|file.write(image_bytes)end
```
![](/images/copy.svg)
```
require'httparty'require'base64'require'json'require'uri'HTTParty::Basement.default_options.update(verify:false)defsend_requestproxy_addr='proxy.scrape.do'proxy_port=8080proxy_user='YOUR_TOKEN'proxy_pass='screenShot=true&render=true&returnJSON=true'url='http://example.com/'uri=URI(url)proxy_uri=URI("http://#{proxy_user}:#{proxy_pass}@#{proxy_addr}:#{proxy_port}")res=HTTParty.get(uri.to_s,http_proxyaddr:proxy_addr,http_proxyport:proxy_port,http_proxyuser:proxy_user,http_proxypass:proxy_pass,http_proxy:proxy_uri)puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Headers: #{res.headers}"json_map=JSON.parse(res.body)image_b64=json_map["screenShots"][0]["image"]image_bytes=Base64.decode64(image_b64)file_path="Example.png"File.open(file_path,"wb")do|file|file.write(image_bytes)endrescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

#### Full Screenshot

 &  fullScreenShot = boolean  default =false

By default, Screen Shot takes a screenshot only for the part of the web page that is visible on the screen. If you need a screenshot of the entire web page, just pass `fullScreenShot=true`. The system will take a screenshot of the entire page for you.

#### Important Notes

* Full Screenshot feature cannot be used without `returnJSON=true` parameter!
* You can use only one of the three screenshot features at the same time.
* The **fullScreenShot** parameter and the **playwithBrowser** parameter cannot be used together. If you need to take more than one screenshot, you can add it as an action with [Play with Browser](#play-with-browser).

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do/?token=YOUR_TOKEN&render=true&fullScreenShot=true&returnJSON=true&url=http://example.com/'\
```
![](/images/copy.svg)
```
curl -k -x "https://YOUR_TOKEN:render=true&screenShot=true&returnJSON=true@proxy.scrape.do:8080"'http://example.com/' -v
```
![](/images/copy.svg)
```
importbase64importjsonimportrequestsimporturllib.parsetoken="YOUR_TOKEN"raw_url="http://example.com/"url=urllib.parse.quote(raw_url)req_url=f"https://api.scrape.do?token={token}&url={url}&fullScreenShot=true&render=true&returnJSON=true"resp=requests.get(req_url)ifresp.status_code!=requests.codes.ok:resp.raise_for_status()json_map=json.loads(resp.text)image_b64=json_map["screenShots"][0]["image"]image_bytes=base64.b64decode(image_b64)file_path="Example.png"withopen(file_path,"wb")asfile:file.write(image_bytes)
```
![](/images/copy.svg)
```
importurllib3importrequestsimportbase64importjsonimporturllib.parseurllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="http://example.com/"token="YOUR_TOKEN"proxyModeUrl="http://{}:render=true&fullScreenShot=true&returnJSON=true@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)ifresponse.status_code==200:json_map=json.loads(response.text)image_b64=json_map["screenShots"][0]["image"]image_bytes=base64.b64decode(image_b64)file_path="Example.png"withopen(file_path,"wb")asfile:file.write(image_bytes)else:print(response)
```
![](/images/copy.svg)
```
constaxios=require('axios');constfs=require('fs');consttoken='YOUR_TOKEN';consturl=encodeURIComponent('http://example.com/');constrequestURL=`https://api.scrape.do?token=${token}&url=${url}&fullScreenShot=true&render=true&returnJSON=true`;axios.get(requestURL).then(response=>{if(response.status===200){constcontent=response.data;constimageB64=content.screenShots[0].image;constfilePath='Example.png';fs.writeFile(filePath,Buffer.from(imageB64,'base64'),err=>{if(err){console.error(err);}});}else{console.log(response.status);}}).catch(error=>{console.error(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');constfs=require('fs');consttoken="YOUR_TOKEN";consttargetUrl="http://example.com/";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'fullScreenShot=true&render=true&returnJSON=true'}},responseType:'arraybuffer'}).then(response=>{constimageBuffer=response.data;constfilePath='Example.png';// Dosyayı kaydet fs.writeFile(filePath,imageBuffer,err=>{if(err){console.error(err);}else{console.log('SUCCESS ! '+filePath);}});}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("http://example.com/");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&fullScreenShot=true&render=true&returnJSON=true";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;if(response.StatusCode==HttpStatusCode.OK){varcontent=response.Content.ReadAsStringAsync().Result;JTokencParse=JToken.Parse(content);stringimageB64=cParse.SelectToken("screenShots[0].image").ToString();stringfilePath="Example.png";File.WriteAllBytes(filePath,Convert.FromBase64String(imageB64));}else{Console.WriteLine(response);}
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="http://example.com/";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"fullScreenShot=true&render=true&returnJSON=true")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;if(response.StatusCode==HttpStatusCode.OK){varcontent=response.Content.ReadAsStringAsync().Result;JTokencParse=JToken.Parse(content);stringimageB64=cParse.SelectToken("screenShots[0].image").ToString();stringfilePath="Example.png";File.WriteAllBytes(filePath,Convert.FromBase64String(imageB64));}else{Console.WriteLine(response);}
```
![](/images/copy.svg)
```
<?php$token="YOUR_TOKEN";$rawURL="http://example.com/";$url=urlencode($rawURL);$reqURL=sprintf("https://api.scrape.do?token=%s&url=%s&fullScreenShot=true&render=true&returnJSON=true",$token,$url);$response=file_get_contents($reqURL);if(!$response){die("Failed to fetch response.");}$jsonMap=json_decode($response,true);if(!$jsonMap){die("Failed to parse response.");}$imageB64=$jsonMap["screenShots"][0]["image"];$imageBytes=base64_decode($imageB64);$filePath="Example.png";$file=fopen($filePath,"wb");if(!$file){die("Failed to open file for writing.");}fwrite($file,$imageBytes);fclose($file);
```
![](/images/copy.svg)
```
<?php$token="YOUR_TOKEN";$targetUrl="http://example.com/";$proxyUrl="http://{$token}:fullScreenShot=true&render=true&returnJSON=true@proxy.scrape.do:8080";$ch=curl_init();curl_setopt($ch,CURLOPT_URL,$targetUrl);curl_setopt($ch,CURLOPT_PROXY,$proxyUrl);curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);curl_setopt($ch,CURLOPT_FOLLOWLOCATION,true);curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,false);$response=curl_exec($ch);if(curl_errno($ch)){echo'Error: '.curl_error($ch);exit;}curl_close($ch);$jsonMap=json_decode($response,true);$imageB64=$jsonMap["screenShots"][0]["image"];$imageBytes=base64_decode($imageB64);$filePath="Example.png";$file=fopen($filePath,'wb');if(!$file){echo"Error opening file";exit;}fwrite($file,$imageBytes);fclose($file);?>
```
![](/images/copy.svg)
```
Stringtoken="YOUR_TOKEN";StringrawUrl="http://example.com/";Stringurl=URLEncoder.encode(rawUrl,"UTF-8");StringreqUrl=String.format("https://api.scrape.do?token=%s&url=%s&fullScreenShot=true&render=true&returnJSON=true",token,url);CloseableHttpClienthttpClient=HttpClients.createDefault();HttpGethttpGet=newHttpGet(reqUrl);CloseableHttpResponseresponse=httpClient.execute(httpGet);try{HttpEntityentity=response.getEntity();StringresponseBody=entity!=null?EntityUtils.toString(entity):null;JSONObjectjsonObject=newJSONObject(responseBody);StringimageB64=jsonObject.getJSONArray("screenShots").getJSONObject(0).getString("image");byte[]imageBytes=Base64.getDecoder().decode(imageB64);StringfilePath="Example.png";FileOutputStreamfos=newFileOutputStream(filePath);fos.write(imageBytes);fos.close();}finally{response.close();}
```
![](/images/copy.svg)
```
Stringurl="http://example.com/";URIproxyURI=newURI("http://YOUR_TOKEN:fullScreenShot=true&render=true&returnJSON=true@proxy.scrape.do:8080");StringbasicAuth=Base64.getEncoder().encodeToString(proxyURI.getUserInfo().getBytes());Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();JSONObjectjsonObject=newJSONObject(response);StringimageB64=jsonObject.getJSONArray("screenShots").getJSONObject(0).getString("image");byte[]imageBytes=Base64.getDecoder().decode(imageB64);StringfilePath="Example.png";FileOutputStreamfos=newFileOutputStream(filePath);fos.write(imageBytes);fos.close();
```
![](/images/copy.svg)
```
packagemainimport("encoding/base64""encoding/json""fmt""io/ioutil""net/http""net/url""os")funcmain(){token:="YOUR_TOKEN"rawURL:="http://example.com/"url:=url.QueryEscape(rawURL)reqURL:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&fullScreenShot=true&render=true&returnJSON=true",token,url)resp,err:=http.Get(reqURL)iferr!=nil{panic(err)}deferresp.Body.Close()ifresp.StatusCode!=http.StatusOK{panic(resp.Status)}bytes,err:=ioutil.ReadAll(resp.Body)iferr!=nil{panic(err)}jsonMap:=make(map[string]interface{})err=json.Unmarshal(bytes,&jsonMap)iferr!=nil{panic(err)}imageB64:=jsonMap["screenShots"].([]interface{})[0].(map[string]interface{})["image"].(string)imageBytes,err:=base64.StdEncoding.DecodeString(imageB64)iferr!=nil{panic(err)}filePath:="Example.png"file,err:=os.Create(filePath)iferr!=nil{panic(err)}deferfile.Close()_,err=file.Write(imageBytes)iferr!=nil{panic(err)}}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""encoding/base64""encoding/json""fmt""io/ioutil""net/http""net/url""os")funcmain(){proxyStr:="http://YOUR_TOKEN:fullScreenShot=true&render=true&returnJSON=true@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","http://example.com/",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}bytes,err:=ioutil.ReadAll(resp.Body)iferr!=nil{panic(err)}jsonMap:=make(map[string]interface{})err=json.Unmarshal(bytes,&jsonMap)iferr!=nil{panic(err)}imageB64:=jsonMap["screenShots"].([]interface{})[0].(map[string]interface{})["image"].(string)imageBytes,err:=base64.StdEncoding.DecodeString(imageB64)iferr!=nil{panic(err)}filePath:="Example.png"file,err:=os.Create(filePath)iferr!=nil{panic(err)}deferfile.Close()_,err=file.Write(imageBytes)iferr!=nil{panic(err)}}
```
![](/images/copy.svg)
```
require'base64'require'json'require'net/http'require'uri'token="YOUR_TOKEN"raw_url="http://example.com/"url=URI.encode_www_form_component(raw_url)req_url="https://api.scrape.do?token=#{token}&url=#{url}&fullScreenShot=true&render=true&returnJSON=true"uri=URI.parse(req_url)resp=Net::HTTP.get_response(uri)ifresp.code!='200'raise"Error: #{resp.code} - #{resp.message}"endjson_map=JSON.parse(resp.body)image_b64=json_map["screenShots"][0]["image"]image_bytes=Base64.decode64(image_b64)file_path="Example.png"File.open(file_path,"wb")do|file|file.write(image_bytes)end
```
![](/images/copy.svg)
```
require'httparty'require'base64'require'json'require'uri'HTTParty::Basement.default_options.update(verify:false)defsend_requestproxy_addr='proxy.scrape.do'proxy_port=8080proxy_user='YOUR_TOKEN'proxy_pass='fullScreenShot=true&render=true&returnJSON=true'url='http://example.com/'uri=URI(url)proxy_uri=URI("http://#{proxy_user}:#{proxy_pass}@#{proxy_addr}:#{proxy_port}")res=HTTParty.get(uri.to_s,http_proxyaddr:proxy_addr,http_proxyport:proxy_port,http_proxyuser:proxy_user,http_proxypass:proxy_pass,http_proxy:proxy_uri)puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Headers: #{res.headers}"json_map=JSON.parse(res.body)image_b64=json_map["screenShots"][0]["image"]image_bytes=Base64.decode64(image_b64)file_path="Example.png"File.open(file_path,"wb")do|file|file.write(image_bytes)endrescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

#### Particular Screenshot

 &  particularScreenShot = #elementSelector 

Sometimes you may want to take a screenshot of only a certain element loaded on the screen. In this scenario, our system will take a screenshot for the selector you have forwarded. By passing the `particularScreenShot=#elementSelector` parameter, you can take a screenshot of the relevant element.

> ParticularScreenShot property expects **url encoded** value.

#### Important Notes

* Particular Screenshot feature cannot be used without `returnJSON=true` parameter!
* You can use only one of the three screenshot features at the same time.
* The **particularScreenShot** parameter and the **playwithBrowser** parameter cannot be used together. If you need to take more than one screenshot, you can add it as an action with [Play with Browser](#play-with-browser).

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do/?token=YOUR_TOKEN&render=true&particularScreenShot=h1&returnJSON=true&url=http://example.com/'\
```
![](/images/copy.svg)
```
curl -k -x "https://YOUR_TOKEN:render=true&particularScreenShot=h1&returnJSON=true@proxy.scrape.do:8080"'http://example.com/' -v
```
![](/images/copy.svg)
```
importbase64importjsonimportrequestsimporturllib.parsetoken="YOUR_TOKEN"raw_url="http://example.com/"url=urllib.parse.quote(raw_url)selector=urllib.parse.quote("h1")req_url=f"https://api.scrape.do?token={token}&url={url}&particularScreenShot={selector}&render=true&returnJSON=true"resp=requests.get(req_url)ifresp.status_code!=requests.codes.ok:resp.raise_for_status()json_map=json.loads(resp.text)image_b64=json_map["screenShots"][0]["image"]image_bytes=base64.b64decode(image_b64)file_path="Example.png"withopen(file_path,"wb")asfile:file.write(image_bytes)
```
![](/images/copy.svg)
```
importurllib3importrequestsimportbase64importjsonimporturllib.parseurllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="http://example.com/"token="YOUR_TOKEN"proxyModeUrl="http://{}:render=true&particularScreenShot=h1&returnJSON=true@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)ifresponse.status_code==200:json_map=json.loads(response.text)image_b64=json_map["screenShots"][0]["image"]image_bytes=base64.b64decode(image_b64)file_path="Example.png"withopen(file_path,"wb")asfile:file.write(image_bytes)else:print(response)
```
![](/images/copy.svg)
```
constaxios=require('axios');constfs=require('fs');consttoken='YOUR_TOKEN';consturl=encodeURIComponent('http://example.com/');varselector=encodeURIComponent("h1");constrequestURL=`https://api.scrape.do?token=${token}&url=${url}&particularScreenShot=${selector}&returnJSON=true`;axios.get(requestURL).then(response=>{if(response.status===200){constcontent=response.data;constimageB64=content.screenShots[0].image;constfilePath='Example.png';fs.writeFile(filePath,Buffer.from(imageB64,'base64'),err=>{if(err){console.error(err);}});}else{console.log(response.status);}}).catch(error=>{console.error(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');constfs=require('fs');consttoken="YOUR_TOKEN";consttargetUrl="http://example.com/";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'particularScreenShot=h1&render=true&returnJSON=true'}},responseType:'arraybuffer'}).then(response=>{constimageBuffer=response.data;constfilePath='Example.png';// Dosyayı kaydet fs.writeFile(filePath,imageBuffer,err=>{if(err){console.error(err);}else{console.log('SUCCESS ! '+filePath);}});}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("http://example.com/");stringselector=WebUtility.UrlEncode("h1");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&particularScreenShot={selector}&render=true&returnJSON=true";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;if(response.StatusCode==HttpStatusCode.OK){varcontent=response.Content.ReadAsStringAsync().Result;JTokencParse=JToken.Parse(content);stringimageB64=cParse.SelectToken("screenShots[0].image").ToString();stringfilePath="Example.png";File.WriteAllBytes(filePath,Convert.FromBase64String(imageB64));}else{Console.WriteLine(response);}
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="http://example.com/";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"particularScreenShot=h1&render=true&returnJSON=true")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=respponse.Content.ReadAsStringAsync().Result;if(response.StatusCode==HttpStatusCode.OK){varcontent=response.Content.ReadAsStringAsync().Result;JTokencParse=JToken.Parse(content);stringimageB64=cParse.SelectToken("screenShots[0].image").ToString();stringfilePath="Example.png";File.WriteAllBytes(filePath,Convert.FromBase64String(imageB64));}else{Console.WriteLine(response);}
```
![](/images/copy.svg)
```
<?php$token="YOUR_TOKEN";$rawURL="http://example.com/";$url=urlencode($rawURL);$reqURL=sprintf("https://api.scrape.do?token=%s&url=%s&particularScreenShot=h1&render=true&returnJSON=true",$token,$url);$response=file_get_contents($reqURL);if(!$response){die("Failed to fetch response.");}$jsonMap=json_decode($response,true);if(!$jsonMap){die("Failed to parse response.");}$imageB64=$jsonMap["screenShots"][0]["image"];$imageBytes=base64_decode($imageB64);$filePath="Example.png";$file=fopen($filePath,"wb");if(!$file){die("Failed to open file for writing.");}fwrite($file,$imageBytes);fclose($file);
```
![](/images/copy.svg)
```
<?php$token="YOUR_TOKEN";$targetUrl="http://example.com/";$proxyUrl="http://{$token}:particularScreenShot=h1&render=true&returnJSON=true@proxy.scrape.do:8080";$ch=curl_init();curl_setopt($ch,CURLOPT_URL,$targetUrl);curl_setopt($ch,CURLOPT_PROXY,$proxyUrl);curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);curl_setopt($ch,CURLOPT_FOLLOWLOCATION,true);curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,false);$response=curl_exec($ch);if(curl_errno($ch)){echo'Error: '.curl_error($ch);exit;}curl_close($ch);$jsonMap=json_decode($response,true);$imageB64=$jsonMap["screenShots"][0]["image"];$imageBytes=base64_decode($imageB64);$filePath="Example.png";$file=fopen($filePath,'wb');if(!$file){echo"Error opening file";exit;}fwrite($file,$imageBytes);fclose($file);?>
```
![](/images/copy.svg)
```
Stringtoken="YOUR_TOKEN";StringrawUrl="http://example.com/";Stringurl=URLEncoder.encode(rawUrl,"UTF-8");Stringencoded_selector=URLEncoder.encode("h1","UTF-8");StringreqUrl=String.format("https://api.scrape.do?token=%s&url=%s&&particularScreenShot=%s&render=true&returnJSON=true",token,url,encoded_selector);CloseableHttpClienthttpClient=HttpClients.createDefault();HttpGethttpGet=newHttpGet(reqUrl);CloseableHttpResponseresponse=httpClient.execute(httpGet);try{HttpEntityentity=response.getEntity();StringresponseBody=entity!=null?EntityUtils.toString(entity):null;JSONObjectjsonObject=newJSONObject(responseBody);StringimageB64=jsonObject.getJSONArray("screenShots").getJSONObject(0).getString("image");byte[]imageBytes=Base64.getDecoder().decode(imageB64);StringfilePath="Example.png";FileOutputStreamfos=newFileOutputStream(filePath);fos.write(imageBytes);fos.close();}finally{response.close();}
```
![](/images/copy.svg)
```
Stringurl="http://example.com/";URIproxyURI=newURI("http://YOUR_TOKEN:particularScreenShot=h1&render=true&returnJSON=true@proxy.scrape.do:8080");StringbasicAuth=Base64.getEncoder().encodeToString(proxyURI.getUserInfo().getBytes());Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();JSONObjectjsonObject=newJSONObject(response);StringimageB64=jsonObject.getJSONArray("screenShots").getJSONObject(0).getString("image");byte[]imageBytes=Base64.getDecoder().decode(imageB64);StringfilePath="Example.png";FileOutputStreamfos=newFileOutputStream(filePath);fos.write(imageBytes);fos.close();
```
![](/images/copy.svg)
```
packagemainimport("encoding/base64""encoding/json""fmt""io/ioutil""net/http""net/url""os")funcmain(){token:="YOUR_TOKEN"rawURL:="http://example.com/"encodedUrl:=url.QueryEscape(rawURL)encodedSelector:=url.QueryEscape("h1")reqURL:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&particularScreenShot=%s&render=true&returnJSON=true",token,encodedUrl,encodedSelector)resp,err:=http.Get(reqURL)iferr!=nil{panic(err)}deferresp.Body.Close()ifresp.StatusCode!=http.StatusOK{panic(resp.Status)}bytes,err:=ioutil.ReadAll(resp.Body)iferr!=nil{panic(err)}jsonMap:=make(map[string]interface{})err=json.Unmarshal(bytes,&jsonMap)iferr!=nil{panic(err)}imageB64:=jsonMap["screenShots"].([]interface{})[0].(map[string]interface{})["image"].(string)imageBytes,err:=base64.StdEncoding.DecodeString(imageB64)iferr!=nil{panic(err)}filePath:="Example.png"file,err:=os.Create(filePath)iferr!=nil{panic(err)}deferfile.Close()_,err=file.Write(imageBytes)iferr!=nil{panic(err)}}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""encoding/base64""encoding/json""fmt""io/ioutil""net/http""net/url""os")funcmain(){proxyStr:="http://YOUR_TOKEN:particularScreenShot=h1&render=true&returnJSON=true@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","http://example.com/",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}bytes,err:=ioutil.ReadAll(resp.Body)iferr!=nil{panic(err)}jsonMap:=make(map[string]interface{})err=json.Unmarshal(bytes,&jsonMap)iferr!=nil{panic(err)}imageB64:=jsonMap["screenShots"].([]interface{})[0].(map[string]interface{})["image"].(string)imageBytes,err:=base64.StdEncoding.DecodeString(imageB64)iferr!=nil{panic(err)}filePath:="Example.png"file,err:=os.Create(filePath)iferr!=nil{panic(err)}deferfile.Close()_,err=file.Write(imageBytes)iferr!=nil{panic(err)}}
```
![](/images/copy.svg)
```
require'base64'require'json'require'net/http'require'uri'require'cgi'token="YOUR_TOKEN"raw_url="http://example.com/"url=URI.encode_www_form_component(raw_url)selector=CGI.escape"h1"req_url="https://api.scrape.do?token=#{token}&url=#{url}&particularScreenShot=#{selector}&render=true&returnJSON=true"uri=URI.parse(req_url)resp=Net::HTTP.get_response(uri)ifresp.code!='200'raise"Error: #{resp.code} - #{resp.message}"endjson_map=JSON.parse(resp.body)image_b64=json_map["screenShots"][0]["image"]image_bytes=Base64.decode64(image_b64)file_path="Example.png"File.open(file_path,"wb")do|file|file.write(image_bytes)end
```
![](/images/copy.svg)
```
require'httparty'require'base64'require'json'require'uri'HTTParty::Basement.default_options.update(verify:false)defsend_requestproxy_addr='proxy.scrape.do'proxy_port=8080proxy_user='YOUR_TOKEN'proxy_pass='particularScreenShot=h1&render=true&returnJSON=true'url='http://example.com/'uri=URI(url)proxy_uri=URI("http://#{proxy_user}:#{proxy_pass}@#{proxy_addr}:#{proxy_port}")res=HTTParty.get(uri.to_s,http_proxyaddr:proxy_addr,http_proxyport:proxy_port,http_proxyuser:proxy_user,http_proxypass:proxy_pass,http_proxy:proxy_uri)puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Headers: #{res.headers}"json_map=JSON.parse(res.body)image_b64=json_map["screenShots"][0]["image"]image_bytes=Base64.decode64(image_b64)file_path="Example.png"File.open(file_path,"wb")do|file|file.write(image_bytes)endrescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Play with Browser

Scrape.do supports basic JavaScript instructions to interact with the web page you want to scrape. You can create a list of instructions and send it to the system. The system will execute the instructions in the order you send them and return the result to you.

> You should url encode `playWithBrowser` query parameter value. You can see more details about url encoding [**here**](#url).

Example of a script with multiple instructions:

![](/images/copy.svg)
```
[{"Action":"Click","Selector":"#button_id"},{"Action":"Wait","Timeout":5000}]
```
#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'http://api.scrape.do?render=true&playWithBrowser=%5B%7B%22Action%22%3A%22Click%22%2C%22Selector%22%3A%22%23html-page%22%7D%5D&token=YOUR_TOKEN&url=https://httpbin.co/'\
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:render=true&playWithBrowser=%5B%7B%22Action%22%3A%22Click%22%2C%22Selector%22%3A%22%23html-page%22%7D%5D@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsejsonData='[{"Action": "Click","Selector":"#html-page"}]'encodedJsonData=urllib.parse.quote_plus(jsonData)token="YOUR_TOKEN"targetUrl=urllib.parse.quote_plus("https://httpbin.co/")render="true"url=f"http://api.scrape.do?token={token}&url={targetUrl}&render={render}&playWithBrowser={encodedJsonData}"response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsejsonData='[{"Action": "Click","Selector":"#html-page"}]'encodedJsonData=urllib.parse.quote_plus(jsonData)url="http://httpbin.co/"token="YOUR_TOKEN"proxyModeUrl=f"http://{token}:playWithBrowser={encodedJsonData}&render=true@proxy.scrape.do:8080"proxies={"http":proxyModeUrl,"https":proxyModeUrl,}try:response=requests.request("GET",url,proxies=proxies)print(response.text)exceptrequests.exceptions.ProxyErrorase:print(f"Proxy Error: {e}")exceptrequests.exceptions.RequestExceptionase:print(f"Request Error: {e}")
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/");varjsonData='[{"Action":"Click","Selector":"#html-page"}]';varencodedJsonData=encodeURIComponent(jsonData);varrender="true";varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&render=${render}&playWithBrowser=${encodedJsonData}`};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="http://httpbin.co/";varjsonData='[{"Action":"Click","Selector":"#html-page"}]';varencodedJsonData=encodeURIComponent(jsonData);axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'render=true&playWithBrowser='+encodedJsonData}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/");varmyData=newList<Object>(){new{Action="Click",Selector="#html-page"}};stringjsonData=JsonConvert.SerializeObject(myData);stringencodedResult=WebUtility.UrlEncode(jsonData);varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&playWithBrowser={encodedResult}&render=true";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
usingSystem.Net;usingNewtonsoft.Json;stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/";varmyData=newList<Object>(){new{Action="Click",Selector="#html-page"}};stringjsonData=JsonConvert.SerializeObject(myData);stringencodedResult=WebUtility.UrlEncode(jsonData);varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"render=true&playWithBrowser="+encodedResult+"")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$array=[['Action'=>'Click','Selector'=>'#html-page']];$encodedJsonData=urlencode(json_encode($array));$data=["url"=>"https://httpbin.co/","token"=>"YOUR_TOKEN","render"=>"true","PlayWithBrowser"=>urldecode($encodedJsonData)];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$array=[['Action'=>'Click','Selector'=>'#html-page']];$values_json=urlencode(json_encode($array));$url="https://httpbin.co/";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:render=true&playWithBrowser=%s@proxy.scrape.do:8080",$token,$values_json);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
StringjsonData="[{\"Action\": \"Click\",\"Selector\":\"#html-page\"}]";StringencodedJsonData=URLEncoder.encode(jsonData,StandardCharsets.UTF_8);Stringtoken="YOUR_TOKEN";StringtargetUrl=URLEncoder.encode("https://httpbin.co/",StandardCharsets.UTF_8);Stringrender="true";Stringurl=String.format("http://api.scrape.do?token=%s&url=%s&render=%s&playWithBrowser=%s",token,targetUrl,render,encodedJsonData);HttpClientclient=HttpClient.newHttpClient();HttpRequestrequest=HttpRequest.newBuilder().GET().uri(URI.create(url)).build();HttpResponse<String>response=client.send(request,HttpResponse.BodyHandlers.ofString());System.out.println(response.body());
```
![](/images/copy.svg)
```
StringjsonData="[{\"Action\":\"Click\",\"Selector\":\"#html-page\"}]";StringencodedJsonData=URLEncoder.encode(jsonData,"UTF-8");StringproxyStr=String.format("http://YOUR_TOKEN:render=true&playWithBrowser=%s@proxy.scrape.do:8080",encodedJsonData);URLproxyURL=newURL(proxyStr);HttpURLConnectionproxyConnection=(HttpURLConnection)proxyURL.openConnection();proxyConnection.connect();URLurl=newURL("https://httpbin.co/");HttpURLConnectionhttpRequest=(HttpURLConnection)url.openConnection();httpRequest.setRequestProperty("Proxy-Authorization",proxyConnection.getHeaderField("Proxy-Authorization"));httpRequest.connect();BufferedReaderin=newBufferedReader(newInputStreamReader(httpRequest.getInputStream()));StringinputLine;StringBuilderresponse=newStringBuilder();while((inputLine=in.readLine())!=null){response.append(inputLine);}in.close();System.out.println("Response Code : "+httpRequest.getResponseCode());System.out.println("Response Message : "+httpRequest.getResponseMessage());System.out.println("Response Body : "+response.toString());proxyConnection.disconnect();
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/")jsonData:=`[{"Action":"Click","Selector":"#html-page"}]`encodedJsonData:=url.QueryEscape(jsonData)url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&render=true&playWithBrowser=%s",token,encoded_url,encodedJsonData)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){jsonData:=`[{"Action":"Click","Selector":"#html-page"}]`encodedJsonData:=url.QueryEscape(jsonData)proxyStr:=fmt.Sprintf("http://YOUR_TOKEN:render=true&playWithBrowser=%s@proxy.scrape.do:8080",encodedJsonData)proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'require"base64"require'json'jsonData=[{"Action":"Click","Selector":"#html-page"}]encodedJsonData=CGI.escape(JSON.dump(jsonData))str=CGI.escape"https://httpbin.co/"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&render=true&playWithBrowser="+encodedJsonData+"")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'require'cgi'HTTParty::Basement.default_options.update(verify:false)defsend_request# Classic (GET )jsonData=[{"Action":"Click","Selector":"#html-page"}]encodedJsonData=CGI.escape(JSON.dump(jsonData))res=HTTParty.get('https://httpbin.co/',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"render=true&playWithBrowser="+encodedJsonData+""})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

You can add multiple instructions to the script. Below are examples of all the different instructions you can use.

#### Click

To click a button, you will need to use this feature. Use it with the CSS selector of the button you want to click. The scraper will click on the #buttonId button and then return the HTML of the target page.

![](/images/copy.svg)
```
[{"Action":"Click","Selector":"#button_id"}]
```
#### Wait

Use the wait command with the time in ms you want to **“wait”** for when you need to wait for a fixed amount of time.

![](/images/copy.svg)
```
[{"Action":"Wait","Timeout":1000}]
```
#### Wait Selector

If there is no expected content as a result of a successful return, you can wait for the element by specifying the desired time in ms with the **“wait-selector”** property.

![](/images/copy.svg)
```
[{"Action":"WaitSelector","WaitSelector":"#btn","Timeout":1000}]
```
#### Scroll Horizontally

Use the **“scrool-x”** attribute with the number of pixels you want to scroll to scroll the target website page horizontally.

![](/images/copy.svg)
```
[{"Action":"ScrollX","Value":100}]
```
#### Scroll Vertically

To scroll the target website page vertically, use the **“scrool-y”** attribute with the number of pixels you want to scroll.

![](/images/copy.svg)
```
[{"Action":"ScrollY","Value":100}]
```
#### Scroll To

With the **“scroll-to”** property, you can scroll for x - y on a per-pixel basis.

![](/images/copy.svg)
```
[{"Action":"ScrollTo","Selector":"#btn"}]
```
#### Fill

Use the **“fill”** attribute to fill an entry on the target website page. Use it with the CSS selector of the input you want to fill and the value you want to fill it with.

![](/images/copy.svg)
```
[{"Action":"Fill","Selector":"#input","Value":"test"}]
```
#### Execute

JavaScript code is executed. If you need to run custom JavaScript, you should use the **“execute”** property.

![](/images/copy.svg)
```
[{"Action":"Execute","Execute":"window.document.cookie"}]
```
#### Screenshot

The `returnJSON=true` parameter needs to be used.

![](/images/copy.svg)
```
[{"Action":"ScreenShot"}][{"Action":"ScreenShot","fullScreenShot":"true"}][{"Action":"ScreenShot","particularScreenShot":"#elementSelector"}]
```

---

### ReturnJSON

Returns network requests. It presents the content information as a property string. shownetworkrequest only returns logs of xhr and fetch requests. Response does not return network requests with images as content. If you are using the screenShot parameter, it will output it as a b64-encoded string.

> `ReturnJSON` cannot be used without `render=True` parameter!

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/anything&render=true&returnJSON=true'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:render=true&returnJSON=true@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")render="true"returnJson="true"url="http://api.scrape.do?token={}&url={}&render={}&returnJSON={}".format(token,targetUrl,render,returnJson)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:render=true&returnJSON=true@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");varrender="true";varreturnJson="true"varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&render=${render}&returnJSON=${returnJson}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'render=true&returnJSON=true'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&render=true&returnJSON=true";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"render=true&returnJSON=true")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","render"=>"true","returnJSON"=>"true"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:render=true&returnJSON=true@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="+encoded_url+"&render=true&returnJSON=true").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:render=true&returnJSON=true@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&render=true&returnJSON=true",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:render=true&returnJSON=true@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&render=True&returnJSON=True")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"render=true",http_proxypass:"returnJSON=true"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

Response
--------

Here we present the parameters where the responses returned by our system can be customized.

### Output Format

 &  output = string  default =raw

Scrape.do does support markdown output for LLM data training or other necessary purposes. You can use the `output=markdown` parameter to obtain the output in markdown format when the response content-type is `text/html`.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/&output=markdown'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:output=markdown@proxy.scrape.do:8080"'https://httpbin.co/' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/")url="http://api.scrape.do?token={}&url={}&output=markdown".format(token,targetUrl)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/"token="YOUR_TOKEN"proxyModeUrl="http://{}:output=markdown@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/");varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&output=markdown`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'output=markdown'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&output=markdown";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"output=markdown")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varrespponse=client.SendAsync(request).Result;varcontent=respponse.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/","token"=>"YOUR_TOKEN","output"=>"markdown",];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:output=markdown@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="+encoded_url+"&output=markdown").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/";URIproxyURI=newURI("http://YOUR_TOKEN:output=markdown@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&output=markdown",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:output=markdown@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&output=markdown")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"output=markdown"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```
### Downloading Pictures & Files

You don’t need any extra configuration to download pictures or files. Just send request with target url and get result.

> There is a 4MB response body limit per request in our system, with super this limit is 2 MB.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'http://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/image'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:@proxy.scrape.do:8080"'https://httpbin.co/image' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/image")url="http://api.scrape.do?token={}&url={}".format(token,targetUrl)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/image"token="YOUR_TOKEN"proxyModeUrl="http://{}:@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/image");varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/image";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:''}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/image");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/image";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token)};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/image","token"=>"YOUR_TOKEN"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/image";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/image","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_URL&url="+encoded_url+"").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/image";URIproxyURI=newURI("http://YOUR_TOKEN:@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/image")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/image",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/image"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/image',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Transparent Response

 &  transparentResponse = boolean  default =false

In the responses received via Scrape.do, the error codes specified by our system are returned by default in the response status code. However, in some cases, users may want to use the information that the target web page uses when returning a reply, instead of using them.

In such cases, it is sufficient to pass the `transparentResponse=true` parameter.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.scrape.do?token=YOUR_TOKEN&url=https://httpbin.co/anything&transparentResponse=true'
```
![](/images/copy.svg)
```
curl -k -x "http://YOUR_TOKEN:transparentResponse=true@proxy.scrape.do:8080"'https://httpbin.co/anything' -v
```
![](/images/copy.svg)
```
importrequestsimporturllib.parsetoken="YOUR_TOKEN"targetUrl=urllib.parse.quote("https://httpbin.co/anything")transparentResponse="true"url="http://api.scrape.do?token={}&url={}&transparentResponse={}".format(token,targetUrl,transparentResponse)response=requests.request("GET",url)print(response.text)
```
![](/images/copy.svg)
```
importrequestsimporturllib3urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)url="https://httpbin.co/anything"token="YOUR_TOKEN"proxyModeUrl="http://{}:transparentResponse=true@proxy.scrape.do:8080".format(token)proxies={"http":proxyModeUrl,"https":proxyModeUrl,}response=requests.request("GET",url,proxies=proxies,verify=False)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');vartoken="YOUR_TOKEN";vartargetUrl=encodeURIComponent("https://httpbin.co/anything");vartransparentResponse="true"varconfig={'method':'GET','url':`https://api.scrape.do?token=${token}&url=${targetUrl}&transparentResponse=${transparentResponse}`,'headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
constaxios=require('axios');consttoken="YOUR_TOKEN";consttargetUrl="https://httpbin.co/anything";axios({method:"GET",url:targetUrl,proxy:{protocol:'http',host:'proxy.scrape.do',port:8080,auth:{username:token,password:'transparentResponse=true'}}}).then(response=>{console.log(response.data);}).catch(error=>{console.error(error.message);});
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl=WebUtility.UrlEncode("https://httpbin.co/anything");varclient=newHttpClient();varrequestURL=$"https://api.scrape.do?token={token}&url={url}&transparentResponse=true";varrequest=newHttpRequestMessage(HttpMethod.Get,requestURL);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
stringtoken="YOUR_TOKEN";stringurl="https://httpbin.co/anything";varproxy=newWebProxy{Address=newUri("http://proxy.scrape.do:8080"),Credentials=newNetworkCredential(token,"transparentResponse=true")};varrequest=newHttpRequestMessage(HttpMethod.Get,url);varhandler=newHttpClientHandler{Proxy=proxy,UseProxy=true};handler.ServerCertificateCustomValidationCallback=(sender,cert,chain,sslPolicyErrors)=>{returntrue;};varclient=newHttpClient(handler);varresponse=client.SendAsync(request).Result;varcontent=response.Content.ReadAsStringAsync().Result;Console.WriteLine(content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);$data=["url"=>"https://httpbin.co/anything","token"=>"YOUR_TOKEN","transparentResponse"=>"true"];curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_URL,"https://api.scrape.do?".http_build_query($data));curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);curl_setopt($curl,CURLOPT_HEADER,false);curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);$url="https://httpbin.co/anything";$token="YOUR_TOKEN";$proxy=sprintf("http://%s:transparentResponse=true@proxy.scrape.do:8080",$token);curl_setopt($curl,CURLOPT_URL,$url);curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'GET');curl_setopt($curl,CURLOPT_PROXY,$proxy);curl_setopt($curl,CURLOPT_HTTPHEADER,array("Accept: */*",));$response=curl_exec($curl);curl_close($curl);echo$response;?>
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Stringencoded_url=URLEncoder.encode("https://httpbin.co/anything","UTF-8");Requestrequest=newRequest.Builder().url("https://api.scrape.do?token=YOUR_TOKEN&url="encoded_url"&transparentResponse=true").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
importjava.net.URI;importjava.util.Base64;importorg.apache.hc.client5.http.fluent.Request;importorg.apache.hc.core5.http.HttpHost;publicclassTestRequest{publicstaticvoidmain(finalString...args)throwsException{Stringurl="https://httpbin.co/anything";URIproxyURI=newURI("http://YOUR_TOKEN:transparentResponse=true@proxy.scrape.do:8080");StringbasicAuth=newString(Base64.getEncoder().encode(proxyURI.getUserInfo().getBytes()));Stringresponse=Request.get(url).addHeader("Proxy-Authorization","Basic "+basicAuth).viaProxy(HttpHost.create(proxyURI)).execute().returnContent().asString();System.out.println(response);}}
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http""net/url")funcmain(){token:="YOUR_TOKEN"encoded_url:=url.QueryEscape("https://httpbin.co/anything")url:=fmt.Sprintf("https://api.scrape.do?token=%s&url=%s&transparentResponse=true",token,encoded_url)method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
packagemainimport("crypto/tls""fmt""io/ioutil""net/http""net/url")funcmain(){proxyStr:="http://YOUR_TOKEN:transparentResponse=true@proxy.scrape.do:8080"proxyURL,err:=url.Parse(proxyStr)iferr!=nil{fmt.Println(err)}transport:=&http.Transport{Proxy:http.ProxyURL(proxyURL),TLSClientConfig:&tls.Config{InsecureSkipVerify:true},}client:=&http.Client{Transport:transport,}req,err:=http.NewRequest("GET","https://httpbin.co/anything",nil)parseFormErr:=req.ParseForm()ifparseFormErr!=nil{fmt.Println(parseFormErr)}resp,err:=client.Do(req)iferr!=nil{fmt.Println("Failure : ",err)}respBody,_:=ioutil.ReadAll(resp.Body)fmt.Println("response Status : ",resp.Status)fmt.Println("response Headers : ",resp.Header)fmt.Println("response Body : ",string(respBody))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"require'cgi'str=CGI.escape"https://httpbin.co/anything"url=URI("https://api.scrape.do?url="+str+"&token=YOUR_TOKEN&transparentResponse=true")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
![](/images/copy.svg)
```
require'httparty'HTTParty::Basement.default_options.update(verify:false)# Classic (GET )defsend_requestres=HTTParty.get('https://httpbin.co/anything?json',{http_proxyaddr:"proxy.scrape.do",http_proxyport:"8080",http_proxyuser:"YOUR_TOKEN",http_proxypass:"transparentResponse=true"})puts"Response HTTP Status Code: #{res.code}"puts"Response HTTP Response Body: #{res.body}"puts"Response HTTP Response Body: #{res.header}"rescueStandardError=>eputs"HTTP Request failed (#{e.message})"endsend_request()
```

---

### Response Headers

By default, Scrape.do will return all the header information it receives from the target website. Our system also aims to make your work easier by adding the following header parameters to the response.

| Header | Description |
| --- | --- |
| Scrape.do-Cookies | All cookie information returned from the target web page `';'` joins with and returns you in one go. |
| Scrape.do-Remaining-Credits | Total credits remaining from your subscription |
| Scrape.do-Request-Cost | Tells how many credits a request costs |
| Scrape.do-Resolved-Url | Transmits the url that the response returns. Useful for results that are redirected |
| Scrape.do-Target-Url | The url of the target web page you sent the request to |
| Scrape.do-Initial-Status-Code | Represents the first successful response received by the target website. In responses with redirect, the first response status code will be like 30X. |
| Scrape.do-Target-Redirected-Location | When you do not want the target website to be redirected, it presents the `Location` header information in the response that the target website returns. |

---

Information
-----------

### Usage Statistics API

If you want to know usage statistics for your Scrape.do subscription, you can use the following API endpoint:

![](/images/copy.svg)
```
https://api.scrape.do/info?token=API_TOKEN
```
> As part of security measures, you can send a maximum of 10 requests per minute to this end-point. When you exceed this limit, you will receive 429 status code.

#### Example Code Snippet

* API Mode
* Proxy Mode
* Curl 
  + [Curl](javascript:void(0);)
  + [Python](javascript:void(0);)
  + [Node JS](javascript:void(0);)
  + [C#](javascript:void(0);)
  + [PHP](javascript:void(0);)
  + [Java](javascript:void(0);)
  + [Go](javascript:void(0);)
  + [Ruby](javascript:void(0);)

![](/images/copy.svg)
```
curl --location --request GET 'https://api.Scrape.do/info?token=YOUR_TOKEN'
```
![](/images/copy.svg)
```
importrequestsurl="https://api.Scrape.do/info?token=YOUR_TOKEN"payload={}headers={}response=requests.request("GET",url,headers=headers,data=payload)print(response.text)
```
![](/images/copy.svg)
```
varaxios=require('axios');varconfig={'method':'GET','url':'https://api.Scrape.do/info?token=YOUR_TOKEN','headers':{}};axios(config).then(function(response){console.log(response.data);}).catch(function(error){console.log(error);});
```
![](/images/copy.svg)
```
varclient=newRestClient("https://api.Scrape.do/info?token=YOUR_TOKEN");client.Timeout=-1;varrequest=newRestRequest(Method.GET);IRestResponseresponse=client.Execute(request);Console.WriteLine(response.Content);
```
![](/images/copy.svg)
```
<?php$curl=curl_init();curl_setopt_array($curl,array(CURLOPT_URL=>'https://api.Scrape.do/info?token=YOUR_TOKEN',CURLOPT_RETURNTRANSFER=>true,CURLOPT_ENCODING=>'',CURLOPT_MAXREDIRS=>10,CURLOPT_TIMEOUT=>0,CURLOPT_FOLLOWLOCATION=>true,CURLOPT_HTTP_VERSION=>CURL_HTTP_VERSION_1_1,CURLOPT_CUSTOMREQUEST=>'GET',));$response=curl_exec($curl);curl_close($curl);echo$response;
```
![](/images/copy.svg)
```
OkHttpClientclient=newOkHttpClient().newBuilder().build();MediaTypemediaType=MediaType.parse("text/plain");RequestBodybody=RequestBody.create(mediaType,"");Requestrequest=newRequest.Builder().url("https://api.Scrape.do/info?token=YOUR_TOKEN").method("GET",body).build();Responseresponse=client.newCall(request).execute();
```
![](/images/copy.svg)
```
packagemainimport("fmt""io/ioutil""net/http")funcmain(){url:="https://api.Scrape.do/info?token=YOUR_TOKEN"method:="GET"client:=&http.Client{}req,err:=http.NewRequest(method,url,nil)iferr!=nil{fmt.Println(err)return}res,err:=client.Do(req)iferr!=nil{fmt.Println(err)return}deferres.Body.Close()body,err:=ioutil.ReadAll(res.Body)iferr!=nil{fmt.Println(err)return}fmt.Println(string(body))}
```
![](/images/copy.svg)
```
require"uri"require"net/http"url=URI("https://api.Scrape.do/info?token=YOUR_TOKEN")https=Net::HTTP.new(url.host,url.port)https.use_ssl=truerequest=Net::HTTP::Get.new(url)response=https.request(request)putsresponse.read_body
```
#### Result

![](/images/copy.svg)
```
{"IsActive":true,// Subscription status "ConcurrentRequest":40,// Number of concurrent requests "MaxMonthlyRequest":3500000,// Maximum number of requests per month "RemainingConcurrentRequest":15,// Remaining number of concurrent requests "RemainingMonthlyRequest":2565023,// Remaining number of requests per month }
```

---

### Status Codes

You can see the list of default response status codes and credit usage status used by Scrape.do in the return type below.

| Status Code | Description | Consumes Credit |
| --- | --- | --- |
| 2xx | Success API Call | YES |
| 404 | Target not found | YES |
| 429 | You are sending too fast requests. (Concurrency limit exceeded) | NO |
| 401 | You have not credit or your subscription has been suspended! | NO |
| 400 | Bad request for Scrape.do | NO |
| 400 | Bad request for the target website. | YES |
| 502 | Request has been failed. Please try again. | NO |
| 510 | The request was canceled by the HTTP client. You can see the status code in the dashboard logs. | NO |

> Please note that when you use `transparentResponse=true` you will get status codes returned by the target website. If there is a problem caused by the proxy, our system may return 502 status code in addition to the target web page.

---

### Request Costs

Our system only charges you for successful results.

> Status codes that we count as successful requests: `2XX`, `400`, `404`, `410`

#### Credit by request type

| Features | Credits Usage |
| --- | --- |
| Normal Request (Datacenter) | 1 |
| Datacenter + Headless Browser | 5 |
| Residential & Mobile Request (Super) | 10 |
| Residential & Mobile Request + Headless Browser | 25 |

If there are requests where you see your target website returning the above status codes but failing, please note that we can get this into our custom rules by contacting us at [support@scrape.do](mailto:support@scrape.do)!

#### Domains where we apply some special pricing

| Target Webpage | Credits Cost | Description |
| --- | --- | --- |
| google.\* | 10 | We use residential (super) proxy by default and each successful request consumes 10 credits. |
| LinkedIn | 30 | LinkedIn is a special target webpage. |
| realestate.com.au | 25 | We need to use residential (super) proxy and browser by default. |
| shopee.\* | 25 | We have a custom solution for the target website. You should use super=true. Web requests use 25 credits, and API requests use 75 credits. |
| chewy.com | 50 | We have a custom solution for the target website. You should use super=true. |
| aircanada.com | 75 | The credit cost is related to super=true & render=true. |
| carsales.com.au | dynamic (25-200) | You have to contact us for access. |
| g2.com | 25 | We have a custom solution for the target website. |
| leboncoin.fr | 10 | The system uses default super=true for the target website. |
| capterra.com | 10 | The system uses default super=true for the target website. |
| akakce.com | 10 | The system uses default super=true for the target website. |
| naver.com | 15 | The system uses custom scraping infrastructure with super=true for the target website. |
| therealreal.com | 25 | The system uses default super=true & render=true for the target website. |
| sahibinden | contact us | You have to contact us. |
| mscdirect.com | 25 | We have a custom solution for the target website. You should use super=true. |

---

Knowledge Base
--------------

### You should know

1. In your communication with our system, you can reduce network traffic and increase your performance by using **accept-encoding: gzip, deflate, br** header value in your requests. Scrape.do supports gzip, deflate and brotli compression types.
2. When you get 502 status codes, you should try again. If there is no problem specific to the target web page, our system expects you to achieve a success rate of over 85%+. If you fall below this success rate, please contact support and we will check your requests.
3. It will always be better and easier for your business to have a queuing system in your web scraping project and manage failed requests in this queuing system.
4. Spreading your requests over a certain period of time can greatly reduce your error rates, and getting the maximum response you can get as soon as possible by using your simultaneous request limits at full capacity can also increase your success rates. For this, you can determine which one will be better for you by doing tests.

---

### Solve Blocking Issue

You’ve sent a few requests to your target site, and we’ve explained below what you can do when you get blocked and no successful response. If you have not achieved a result even though you have done what is described here, please contact support and let us know. Rest assured that we will get back to you about the problem as soon as possible.

1. **Use Super Proxy and Geo Targeting**
   
   * You can use our high quality residential and mobile proxy pools with the `super=true` parameter, and you can make a request through the country served by the target web page by choosing the country via `geoCode=us`. For other countries, you can check the [**Geo Targeting**](#geo-targeting) section.
2. **Use Headless Browser**
   
   * By using our headless browser network with the `render=true` parameter, you can enter the target website with a real browser and try to get the results.
   * If you are blocked despite using Headless Browser, you can try again by adding `blockResources=false` parameters.
   * If there is still no successful result, we can make the browser wait on the relevant page for 2 seconds with `customWait=2000`. By increasing this time, you can customize it in different combinations according to the needs of the target website.
   * If there is no expected content in the successful return result, you can wait for the element with the [**Wait Selector**](#wait-css-selector) feature.
3. **Contact Support**
   
   * If you have done all the steps above and still have no success, please contact [**support**](mailto:support@scrape.do) and let us know. We will check your requests and get back to you as soon as possible.

---

### Frequently Asked Technical Questions

**I need to forward headers to the target website. How can I forward?**

* [**CustomHeaders**](#custom-headers) and [**ExtraHeaders**](#extra-headers) in the [**Request**](#request) category in our documents should read the fields.

**How ​​often does a proxy change?**

* Our system changes and rotates the proxy for every request made to the target website. If you have a need to intervene, take a look at the [**Sticky Session**](#sticky-sessions) field.

**Is 2MB response limit enough?**

* We respond to millions requests per day, and we can say with confidence that there has been no HTML content that has exceeded the 2M limit so far. Since the content from the target site is returned as compressed, it is practically impossible with HTML to have a compressed content that exceeds the 2MB limit for web pages.

**Can I Scrape LinkedIn?**

* We support the scraping of public pages for LinkedIn.

---

Frequently Used Libraries
-------------------------

### Python Scrapy Example

#### Scrapydo

You may prefer to use our Scrapy wrapper library in order to configure it faster and more easily.

Get the library with the following command:

```
pip3 install scrapy-scrapedo 
```

Then you can use the library as follows:

![](/images/copy.svg)
```
fromscrapydoimportscrapy,scrapedoclassScrapedoSampleCrawler(scrapy.Spider):name="Scrape-do Sample Crawler"def__init__(self):super().__init__(scrapedo.RequestParameters(token="TOKEN",# Get your Scrape.do token from: dashboard.scrape.doparams={"geoCode":"us","super":False,"render":True,"playWithBrowser":[{"Action":"Click","Selector":"#manpage > div.mp > ul > li:nth-child(3) > a"},{"Action":"Wait","Timeout":2000},{"Action":"Execute","Execute":"document.URL"}],}))defstart_requests(self):urls=['https://httpbin.co/',]forurlinurls:yieldself.Request(url=url,callback=self.parse)defparse(self,response):print(response.body)print("target:",self.target_url(response))
```

Since `scrapydo/scrapy` only a wrapper library, you can use all the features of Scrapy with it.

### Scrapy

Scrape.do also supports raw Scrapy usage. You can use the following example to utilize Scrapy with Scrape.do.

![](/images/copy.svg)
```
importscrapy,urllib.parseclassTestSpider(scrapy.Spider):name="test"defupdate_url(self,url):return"https://api.scrape.do/?token=YOUR_TOKEN&url="+urllib.parse.quote(url)defstart_requests(self):urls=['https://example.com',]forurlinurls:yieldscrapy.Request(url=self.update_url(url),callback=self.parse)defparse(self,response):print(response.body)
```
> Note that when you use raw Scrapy library, you have to add `/` after `https://api.scrape.do` and before `?`. Otherwise, you may get `400 Bad Request` errors. The final request url should look like `"https://api.scrape.do/?token=TOKEN&url=..."`

You can use most of used libraries through the [**Proxy Mode**](#proxy-mode).

![](/images/copy.svg)
```
importscrapyclassTestSpider(scrapy.Spider):name="test"defstart_requests(self):urls=['https://example.com',]meta={"proxy":"http://YOUR_TOKEN:render=false@proxy.scrape.do:8080"}forurlinurls:yieldscrapy.Request(url=url,callback=self.parse,meta=meta)
```

---

### Puppeteer Example

![](/images/copy.svg)
```
constpuppeteer=require('puppeteer');(async()=>{constblockedResourceTypes=['beacon','csp_report','font','image','imageset','media','object','texttrack','stylesheet',];constusername="YOUR_TOKEN"constpassword="render=false"constaddress="proxy.scrape.do:8080"constbrowser=awaitpuppeteer.launch({args:[`--proxy-server=http://${address}`],acceptInsecureCerts:true,headless:false});constpage=awaitbrowser.newPage();// We suggest you block resources for low concurrency and credit usage awaitpage.setRequestInterception(true);page.on('request',request=>{if(blockedResourceTypes.indexOf(request.resourceType())!==-1){console.log(`Blocked type:${request.resourceType()} url:${request.url()}`)request.abort();}else{request.continue();}});awaitpage.authenticate({username,password});awaitpage.goto('https://www.example.com');awaitnewPromise(resolve=>setTimeout(resolve,3000));awaitbrowser.close();})();
```

---

### Python Selenium Example

![](/images/copy.svg)
```
# pip install selenium-wirefromseleniumwireimportwebdriverusername="YOUR_TOKEN"password="render=false"formatted_proxy=f"http://{username}:{password}@proxy.scrape.do:8080"options={"proxy":{"http":formatted_proxy,"https":formatted_proxy,"verify_ssl":False,},}URL="https://httpbin.co/anything?json"chrome_options=webdriver.ChromeOptions()## block images and javascriptchrome_prefs={"profile.default_content_setting_values":{"images":2,"javascript":2,}}chrome_options.experimental_options["prefs"]=chrome_prefsdriver=webdriver.Chrome(executable_path="CHROME_EXECUTABLE_PATH",chrome_options=chrome_options,seleniumwire_options=options,)driver.get(URL)
```

---

### Playwright With The Example of Chrome

![](/images/copy.svg)
```
const{chromium}=require('playwright');(async()=>{constproxy={server:'http://proxy.scrape.do:8080',username:'YOUR_TOKEN',password:'',};constbrowser=awaitchromium.launch({headless:false,proxy:{server:proxy.server,username:proxy.username,password:proxy.password,},args:['--ignore-certificate-errors']});constpage=awaitbrowser.newPage();awaitpage.goto('https://www.example.com/');awaitpage.waitForTimeout(3000);awaitbrowser.close();})();
```

---

Start scraping today with 1000 free credits.

Instant setup, immediate results.

No Credit Card Required

[Start Scraping For FREE](https://dashboard.scrape.do/signup)![](/images/scrape-white.svg)

* [Support](mailto:support@scrape.do?subject=Support%20Request)
* [Sales](mailto:sales@scrape.do?subject=Sales%20Request)
* [Blog](/blog/)
* [Pricing](/pricing/)
* [Dashboard](https://dashboard.scrape.do)

* [![](/images/linkedin-logo.svg)](https://www.linkedin.com/company/scrape-do)

* [Contact](mailto:hello@scrape.do)
* [Features](/#features)
* [FAQ](/#faqs)

* [Term of Use](/terms-of-use/)
* [Privacy Policy](/privacy-policy/)
* [Affiliate Program](/affiliate/)

* [Web Scraping is Legal?](/blog/is-it-legal-to-scrape-public-data/)
* [Web Scraping Proxies](/blog/the-10-best-rotating-proxy-service-for-web-scraping/)
* [Rotating Proxy](/blog/rotating-proxies-everything-you-need-to-know/)
* [Search Engine Scraping](/blog/is-scraping-google-search-result-beneficial-for-your-business/)
### Learn Web Scraping

* [Web Scraping in Python](/blog/web-scraping-with-python-advanced-guide/)
* [Web Scraping in NodeJS](/blog//web-scraping-in-nodejs-advanced-techniques-and-best-practices/)
* [Web Scraping in Java](/blog/advanced-web-scraping-in-java-a-comprehensive-guide/)
* [Web Scraping in PHP](/blog/advanced-web-scraping-techniques-in-php-a-comprehensive-guide/)
* [Web Scraping in R](/blog/web-scraping-with-r/)
* [Web Scraping in Ruby](/blog/web-scraping-in-ruby-advanced-techniques-and-best-practices/)
* [Web Scraping in Golang](/blog/web-scraping-in-golang/)
* [Web Scraping in C#](/blog/c-sharp-web-scraping/)
* [Web Scraping in Rust](/blog/web-scraping-in-rust/)
* [Web Scraping in C++](/blog/web-scraping-with-c++/)
* [Web Scraping in C](/blog/web-scraping-with-c/)
* [Web Scraping In Perl](/blog/web-scraping-in-perl/)
* [Scrapy Python Web Scraping](/blog/advanced-web-scraping-with-scrapy-a-python-tutorial-for-efficient-data-extraction/)
* [Selenium Web Scraping](/blog/web-scraping-with-selenium/)
* [Playwright Web Scraping](/blog/web-scraping-with-playwright/)
* [Puppeteer Web Scraping](/blog/advanced-puppeteer-web-scraping-techniques-for-automated-data-extraction/)

Copyright © 2020 - 2024 Scrape.do | PACKEND, LLC

![](/images/footer/mc.svg)![](/images/footer/visa.svg)![](/images/footer/amex.svg)![](/images/footer/bitcoin.svg)