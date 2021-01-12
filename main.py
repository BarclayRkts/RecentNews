from selenium import webdriver
import feedparser
import time

#Get a news website and get the most recent news articles from that website and open up one of those websites

def parse(number):
    links = []
    urls = ["https://news.ycombinator.com/rss","https://threatpost.com/feed/", "https://nakedsecurity.sophos.com/feed/", "https://www.sciencedaily.com/rss/", "https://cacm.acm.org/"]

    website = feedparser.parse(urls[int(number) - 1]) 

    for i in range(5):
        post = website.entries[i]
        links.append(post.link)
        print(f"[{i+1}]: {post.title}")
    
    article_num = input("Choose the link you want to open (1-5): ")

    openLink(links[int(article_num) - 1])

def openLink(link):
    driver = webdriver.Chrome()

    driver.get(link)
    time.sleep(100)
    


def main():
    print("--News Website List--")
    print("[1]: HackerNews")
    print("[2]: ThreatPost")
    print("[3]: NakedSecurity")
    print("[4]: ScienceDaily")
    print("[5]: ACM")
    website_num = input("Enter Website by number (1-5): ")
    parse(website_num)

main()













