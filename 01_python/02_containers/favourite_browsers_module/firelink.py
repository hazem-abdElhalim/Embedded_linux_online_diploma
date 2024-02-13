import webbrowser

facebook_link = "http://www.facebook.com/"
twitter_link = "http://https://twitter.com/"
google_link = "http://www.google.com"
instagram_link = "http://instagram.com"
ASU_link = "https://eng.asu.edu.eg/"
def brave_link(url):
    webbrowser.get("C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s").open(url)
