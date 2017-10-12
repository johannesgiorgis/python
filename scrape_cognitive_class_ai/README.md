# Description
Scrape cognitiveclass.ai to capture their courses and learning paths. A list of dictionaries is created for courses and learning paths respectively and they are output to their own files (cognitive_class_course_list.txt, cognitive_class_learning_paths.txt). Logs are placed in 'cognitive_class_scrape.log'.

# Motivation
I wanted to gather all the courses and learning paths available on cognitiveclass.ai without having to search the website.

I settled on using a python script to scrape the website, allowing me to quickly capture any updates to the website's courses or learning paths by simply re-running the script. It was an opportunity to learn more about web scraping via the BeautifulSoup library, use python's logging module instead of print statements.
