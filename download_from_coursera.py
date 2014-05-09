import webbrowser
import time

def get_page(page):
    try:
        import urllib
        return urllib.urlopen(page).read()
    except:
        return ""

def next_link(page):
    start = page.find('<a target="_new" href=')
    #print (start)
    if start == -1:
        return None,0
    else:
        pos = page.find('href=',start +1 )
        
        start_quote = page.find('"',pos)
        end_quote = page.find('"',start_quote+1)
        link = page[start_quote+1:end_quote]
       # print link
        return link,end_quote

def get_all_link(page):
    l=[]
    while True:
        url,end_pos = next_link(page)
        if url == None:
            break
        else:
            l.append(url)
            page = page[end_pos+1:]
    return l

def get_mp4(list_of_all_links):
    l=[]
    for e in list_of_all_links:
        if e.find('mp4') != -1:
            l.append(e)
    return l

def open_in_browser(link):
    i=0
    while i < len(link):
        webbrowser.openurl(url)
        i = i+1

        
# paste your link below
download_vid_from = 'https://class.coursera.org/optimization-002/lecture'

open_in_browser(get_mp4(get_all_link(get_page(download_vid_from))))



