from bs4 import BeautifulSoup
import urllib.request
#from urllib2 import urlopen
from random import randint
import webbrowser

rec_arr = []

def searchVideo(search):
	print('Searching videos...')
	videos_found = []
	main_page = "https://www.youtube.com"
	#print(type(search))
	search_term = main_page + "/results?search_query=" + search
	#print('Search term', search_term)
	resp = urllib.request.urlopen(search_term)
	soup = BeautifulSoup(resp, "html.parser")
	
	divs = soup.find_all("div", {"class": "yt-lockup-content"})
	for i in divs:
		href = i.find('a', href=True)
		input = main_page + href['href']
		videos_found.append(input)

	#print('Results:', rec_arr)
	print('Completed searching videos!')
	return videos_found


def selectVideo(videos):
	print('Selecting videos...')
	rand_int = randint(0, len(videos) - 1)
	#print('Rand int:', rand_int)
	#print(videos[rand_int], type(videos[rand_int]))
	video_link = videos[rand_int] #.strip('[]')
	#print(video_link)
	video_title = getVideoTitle(video_link)
	print('Done selecting videos!')
	return video_link, video_title


def getVideoTitle(video_link):
	print('Getting video title...')
	resp = urllib.request.urlopen(video_link)

	soup = BeautifulSoup(resp, "html.parser")
	video_title = soup.find('h1', {"class": "watch-title-container"}).find('span').text.strip()
	print('Completed getting video title!')
	return video_title


search_String = 'instant pot recipe'
videos = searchVideo(search_String.replace(" ", "%20"))
video_link, video_title = selectVideo(videos)
print("'{}' Video: {}".format(video_title, video_link))
