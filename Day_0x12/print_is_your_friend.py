#Print is Your Friend
#pages = 0
#word_per_page = 0
#pages = int(input("Number of pages: "))
#word_per_page == int(input("Number of words per page: "))
#total_words = pages * word_per_page
#print(total_words)

#The double equal to in the statement word_per_page is the issue. The == is serving as a comparison statement will will give us a False boolean 

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
