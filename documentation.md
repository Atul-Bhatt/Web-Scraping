# Scrapy Documentation

- Run Scrawler using its name (variable in Spider class)

```console
scrapy crawl <crawler_name>
```

- If you don't want to implement the start_requests() method of Spider then use the start_urls attribute
  of spider method and initialize it with a list of urls. It will use the default start_requests() method.

- Even if we don't call parse method it is called because Scrapy's default callback method is parse.
- Scrapy Shell

```console
scrapy shell "http://quotes.toscrape.com/page/1/"
```

- -O overwrites, -o appends(to a json)

- appending to a json file makes it invalid, if you want to append then use json line format, eg: quotes.jl

```console
scrapy crawl quotes -O quotes.json
```

---

Commands article in documentation

- the directory where scrapy.cfg file resides is the root directory.
- The config file contains name of the module that defines project settings.
- Multiple projects can share a config file:

```python
[settings]
default = myproject1.settings
project2 = myproject2.settings
```

- By default scrapy will use "default", but you can define a different project using SCRAPY_PROJECT environment variable
- Check the current bot

```console
scrapy settings --get BOT_NAME
```

(in windows powershell)

```console
$env:SCRAPY_PROJECT = "project2"
```

Now the botname will change to myproject2

- scrapy -h (will give you a list of all the commands)
  - bench : Run quick benchmark test
  - check : Check spider contracts
  - commands
  - crawl : Run a spider
  - edit : Edit spider
  - fetch : Fetch a URL using the Scrapy downloader (options) --no-redirect, --headers, --spider=SPIDER
  - genspider : Generate new spider using pre-defined templates
  - list : List available spiders
  - parse : Parse URL (using its spider) and print the results
  - runspider : Run a self-contained spider (without creating a project)
  - settings : Get settings values
  - shell : Interactive scraping console
  - startproject : Create new project
  - version : Print Scrapy version
  - view : Open URL in browser, as seen by Scrapy

---

https://docs.scrapy.org/en/latest/topics/spiders.html

- As an example, you can implement start_requests when you want to send a post request for example login
  class MySpider(scrapy.Spider):
  name = 'myspider'

        def start_requests(self):
            return [scrapy.FormRequest("http://www.example.com/login",
                                   formdata={'user': 'john', 'pass': 'secret'},
                                   callback=self.logged_in)]

        def logged_in(self, response):
            # here you would extract links to follow and return Requests for
            # each of them, with another callback
            pass

- CrawlSpider
- XMLFeedSpider
- CSVFeedSpider
- SitemapSpider

---

https://docs.scrapy.org/en/latest/topics/selectors.html

- to select text node use ::text
- to select attribute values use ::attr(name), where name is the name of the attribute you want the value of
- \*::text gives text values of all the decendants

```python
response.css('#image *::text').getall()
```

- Selector also has a .re() method for extracting data using regular expressions (it returns a string not a Selector)

- If you want to use xpath on SelectorList or Selector use "." before it:

```python
sel.css('.shout').xpath('./time/@datetime').getall()
```

- more examples:

```python
    div = response.xpath('//div')
    p_elements = response.xpath('//p') # this is wrong
    p_elements = response.xpath('.//p') # this is right
```

- //node[1] vs (//node)[1]

  - //node[1] will select all the first elements of that node
  - (//node)[1] will select only first element of the first node

- use $ to pass variables to xpath:

```python
response.xpath('//div[@id=$val]/a/text()', val='images').get()
```

- If there is a namespace in the xml file then you can remove namespace to select the elements:

```python
response.selector.remove_namespaces()
```

- Use test() funciton of re when contains() or starts-with() are insufficient

```python
sel.xpath('//li[re:test(@class, "item-\d$")]//@href').getall()
```

---

https://docs.scrapy.org/en/latest/topics/items.html

- Scrapy supports the following type of items, via the itemadapter library:
  - dictionaries
  - Item objects : scrapy.item.Item( [arg] )
  - dataclass objects
  - attrs objects

### Item:

- Item objects provide the following addional API members
  - copy()
  - deepcopy()
  - fields

---

https://docs.scrapy.org/en/latest/topics/loaders.html ---will read in future

---

# Now We Make Projects

Creating a bot that will scrape information about all the laptops with prices.
