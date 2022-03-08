import json
import urllib.request
import webbrowser
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

img = open("pod.jpg","wb")
page = open("page.html","w")

request='https://api.nasa.gov/planetary/apod?api_key=dahmUZMZOFGcLfn8t0A3cp7Prvkv8EQhAk9gSx05'
object = urllib.request.urlopen(request)
data=json.loads(object.read())


type = data["media_type"]
url = data["url"]
date= data["date"]
desc=data["explanation"]

if (type=="image"):
	pic=urllib.request.urlopen(url)

	img.write(pic.read())

	page.write("<!DOCTYPE html><html><head><title>Page Title</title></head><body><div style=\"text-align:center;\"><h1>Astronomy Picture of the Day</h1><h2>"+date+"</h2><img src=\"pod.jpg\" style=\"display: block;margin-left: auto;margin-right: auto; width: 50%;\"><p>"+desc+"</p></div></body></html>")

	webbrowser.open("page.html")
elif (type=="video"):
	page.write("<!DOCTYPE html><html><head><title>Page Title</title></head><body><div style=\"text-align:center;\"><h1>Astronomy Picture of the Day</h1><h2>"+date+"</h2><iframe width=\"560\" height=\"315\" src="+url+"; frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe><p>"+desc+"</p>></div></body></html>")
	webbrowser.open("page.html")
