import requests, threading, datetime, os

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t
def notify(title, text):
    os.system("""
              osascript -e 'tell application "Music" to play track 1 of playlist "Playlist"'
              """)
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def getContent(url):
    pageUrl = url
    getPage = requests.get(pageUrl)
    getPage.raise_for_status()
    content = getPage.json()
    return content

def checkContent():
    url1 = "https://richmondpublichealth.janeapp.com/api/v2/openings/for_discipline?location_id=3&discipline_id=2&treatment_id=8&date=&num_days=7"
    url2 = "https://vancouvercovid19vaccineclinic.janeapp.com/api/v2/openings/for_discipline?location_id=6&discipline_id=1&treatment_id=16&date=&num_days=7"
    a = getContent(url1)
    b = getContent(url2)
    print(str(a)+" "+str(b)+" "+str(datetime.datetime.now().strftime('%d %H:%M:%S'))+'\n')
    with open("/Users/Joshua/desktop/testing/results.txt",'a') as fh:
        fh.write(str(a)+"\n"+str(b)+"\n"+str(datetime.datetime.now().strftime('%d %H:%M:%S'))+'\n')
        fh.close()
    if a or b:
        notify("SUCCESS!","checkout out pycharm and results.txt")
        print("here is richmond\n")
        print(a)
        print("here is spinal cord place\n")
        print(b)


if __name__=='__main__':
    print("starting...")
    set_interval(checkContent,30)
