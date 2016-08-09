import re

# to do: check automatically if nr of lines is equal to number of movies to be seen

name = 'F:\dokumenty\wanna_see.htm'
handle = open(name)
txt = handle.read()

lst = txt.split("td sorttable_customkey=")

print 'length of the initial list:', len(lst), '(there are 2450 movies on the list)'

films = list()

for element in lst:
    if re.search('^".*?"><a href="', element) and not re.search('^"[0-9]+" class=', element):
        films.append(element)

print 'length of the films list:', len(films), '\n'

for element in films[1 : 10]:
    print element

    polish_title = re.search('".*?"', element)
    polish_title_str = polish_title.group()
    if polish_title:
        print "polish title: ", polish_title_str[1 : len(polish_title_str) - 1]

    year = re.search('</a> .[0-9]+. <br>', element)
    year_str = year.group()
    if year:
        print "year: ", year_str[6 : len(year_str) - 6]

    link = re.search('<a href=".*?"', element)
    link = re.search('".*?"', link.group())
    link_str = link.group()
    if link_str.find('www.filmweb.pl') == -1:
        link_str = ' http://www.filmweb.pl' + link_str[1 : ]
    if link:
        print "link: ", link_str[1 : len(link_str) - 1]

    title = re.search('<br>.*?<br>', element)
    title_str = title.group()
    if title:
        if title_str.find('kraj') != -1:
            print "title: ", polish_title_str[1 : len(polish_title_str) - 1]
        else:
            print "title: ", title_str[4 : len(title_str) - 4]

    country = re.search('kraj:.*?</a> <br>', element)
    country_lst = country.group().split(' , ')   # possibly more than one country. anyway list returned
    for i in range(0, len(country_lst)):
        country_lst[i] = re.search('">.*?</a>', country_lst[i]).group()
        country_lst[i] = country_lst[i][2 : len(country_lst[i]) - 4]

    print 'country: ', country_lst


    genre = re.search('<br>gatunek:.*?</div>', element)
    genre_lst = genre.group().split(' , ')
    for i in range(0, len(genre_lst)):
        genre_lst[i] = re.search('">.*?</a>', genre_lst[i]).group()
        genre_lst[i] = genre_lst[i][2 : len(genre_lst[i]) - 4]

    print 'genre: ', genre_lst

    print ''



