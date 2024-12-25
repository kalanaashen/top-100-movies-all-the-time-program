from bs4 import BeautifulSoup
import requests


response=requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

empire_website=response.text


soup=BeautifulSoup(empire_website,'html.parser')
movies=soup.find_all(name="h3",class_="listicleItem_listicle-item__title__BfenH")

movie_titles=[]

for movie_title in movies:
    movie_titles.append(movie_title.getText())


lenght = len(movie_titles)

file=open("top 100 movies all the time.txt",'w')

for i in range(lenght-1,0,-1):

    file.write(movie_titles[i])
    file.write("\n")


file.close()