import thread

def button1():
    self.button = Button(text="search",padx=4, pady=4, command=self.get_lyric)
    self.button.pack()

def get_lyric(self):
    #LYRICS.COM
    self.feedback.config(text="loading...")

    site= str(self.get_googlesearch_link(self.input_text.get()))
    #print site
    page = urllib2.urlopen(site)
    soup = BeautifulSoup(page)
    main = soup.find(id="lyric_space")

thread.start_new_thread(button1, ())
thread.start_new_thread(get_lyrics, ())
