import re

name = 'F:\dokumenty\dont_wanna_see.htm'
handle = open(name)
txt = handle.read()

lst = txt.split("td sorttable_customkey=")

for element in lst[1:]:
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
    if link:
        print "link: ", link_str[1 : len(link_str) - 1]

    title = re.search('<br>.*?<br>', element)
    title_str = title.group()
    if title:
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

