from random import choice 
import webbrowser

# open/read file 
def open_and_read_file(filename):
    patent_numbers = []
    with open(filename) as data:
        for line in data:
            patent_numbers.append(line)
    return patent_numbers

# pass in the file with list of patent numbers
patent_numbers = open_and_read_file('patent_num.txt')

# randomly choose a patent number from the list 
patent_number = choice(patent_numbers)

# generate link to that patent 
link = "http://appft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.html&r=1&p=1&f=G&l=50&d=PG01&S1=" + patent_number + "&OS=" + patent_number + "&RS=" + patent_number

# open the link in browser
webbrowser.open(link) 