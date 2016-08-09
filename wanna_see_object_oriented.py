from film import *
import re

name = 'F:\dokumenty\wanna_see.htm'
handle = open(name)
txt = handle.read()

lst = txt.split("td sorttable_customkey=")

print 'length of the initial list:', len(lst), '(there are 2450 movies on the list)'

films_str = list()

for element in lst:
    if re.search('^".*?"><a href="', element) and not re.search('^"[0-9]+" class=', element):
        films_str.append(element)

print 'length of the films list:', len(films_str), '\n'

films = list()

for element in films_str:
    film = Film()

    polish_title = re.search('".*?"', element)
    if polish_title:
        polish_title_str = polish_title.group()
        polish_title_str = polish_title_str[1 : len(polish_title_str) - 1]

        film.polish_title = polish_title_str


    year = re.search('</a> .[0-9]+. <br>', element)
    if year:
        year_str = year.group()
        year_str = year_str[6 : len(year_str) - 6]

        film.year = year_str


    link = re.search('<a href=".*?"', element)
    if link:
        link = re.search('".*?"', link.group())
        link_str = link.group()
        if link_str.find('www.filmweb.pl') == -1:
            link_str = ' http://www.filmweb.pl' + link_str[1 : ]
        link_str = link_str[1 : len(link_str) - 1]

        film.link = link_str


    title = re.search('<br>.*?<br>', element)
    if title:
        title_str = title.group()
        if title_str.find('kraj') != -1:
            title_str =  polish_title_str[1 : len(polish_title_str) - 1]
        else:
            title_str =  title_str[4 : len(title_str) - 4]

        film.title = title_str


    country = re.search('kraj:.*?</a> <br>', element)
    if country:
        country_lst = country.group().split(' , ')   # possibly more than one country. anyway list returned
        for i in range(0, len(country_lst)):
            country_lst[i] = re.search('">.*?</a>', country_lst[i]).group()
            country_lst[i] = country_lst[i][2 : len(country_lst[i]) - 4]

        film.country = country_lst


    genre = re.search('<br>gatunek:.*?</div>', element)
    if genre:
        genre_lst = genre.group().split(' , ')
        for i in range(0, len(genre_lst)):
            genre_lst[i] = re.search('">.*?</a>', genre_lst[i]).group()
            genre_lst[i] = genre_lst[i][2 : len(genre_lst[i]) - 4]

        film.genre = genre_lst

    films.append(film)

print films[0]