#!/usr/bin/python
"""
scrape cognitiveclass.ai to get courses and
learning paths
"""

# MODULES
from bs4 import BeautifulSoup
from pprint import pprint
import json
import logging
import requests
# import sys

# SET UP LOGGING
logging.basicConfig(
    filename='cognitive_class_scrape.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s',
)
logger = logging.getLogger(__name__)


# HELPER FUNCTIONS
def write_to_file(file_name, contents):
    '''
    writes to specified file the list of contents passed
    '''
    logger.info("Writing to file '{}'...".format(file_name))
    fo = open(file_name, 'w')

    for content in contents:
        output = "{}\n".format(json.dumps(content, indent=4))
        fo.write(output)

    fo.close()

    logger.info("Completed writing to file '{}'...".format(file_name))


# COGNITIVE CLASS AI COURSES
def scrape_web_page(web_page):
    '''
    scrapes provided web page and returns list of courses
    '''
    logger.info("Scraping '{}'...".format(web_page))
    session = requests.Session()
    resp = session.get(web_page)

    soup = BeautifulSoup(resp.text, 'lxml')
    course_list = soup.find_all('h4', attrs={'class': 'card-title'})

    #print('Course Code|Course Name|Course Link')
    courses = []
    for course in course_list:
        #print(course)
        link = course.find('a')
        course_code = course.find('span', attrs={'class': 'course-code'})

        #print("{0}|{1}|{2}".format(course_code.text.strip(), link.text.strip(), link['href']))
        course = {
            'course_name': link.text.strip(),
            'course_code': course_code.text.strip(),
            'course_link': link['href'],
        }
        courses.append(course)

    logger.info('Found {} courses'.format(len(courses)))
    logger.info("Completed scraping '{}'".format(web_page))
    return courses


def scrape_cognitive_class_courses(num_pages):
    '''
    scrapes cognitive class courses
    '''
    logger.info("Scraping {} pages...".format(num_pages))

    page = 'https://cognitiveclass.ai/courses/'

    all_courses = []
    for i in range(1, num_pages + 1):
        web_page = page + 'page/' + str(i)
        logger.info("Attempting to scrape {}...".format(web_page))
        all_courses.extend(scrape_web_page(web_page))

    logger.info("{} courses found on {}".format(len(all_courses), page))
    logger.info("Done scraping {} pages...".format(num_pages))
    return all_courses


def get_cognitive_class_courses():
    '''
    get courses from cognitiveclass.ai
    '''
    logger.info("Getting cognitive class courses...")
    num_pages = 3
    cognitive_courses = scrape_cognitive_class_courses(num_pages)
    logger.info("{} cognitive class courses found".format(len(cognitive_courses)))

    file_name = 'cognitive_class_course_list.txt'

    write_to_file(file_name, cognitive_courses)

    '''
    for course in cognitive_courses:
        pprint(course)
        logger.info("{}".format(json.dumps(course, indent=4)))
    '''
    logger.info("Completed getting cognitive class courses")


# COGNITIVE CLASS AI LEARNING PATHS
def scrape_lp_web_page(web_page):
    '''
    scrapes provided web page and returns list of learning paths
    '''
    logger.info("Scraping '{}'...".format(web_page))
    session = requests.Session()
    resp = session.get(web_page)

    soup = BeautifulSoup(resp.text, 'lxml')
    learning_path_list = soup.find_all('div', attrs={'class': 'row list-item'})
    #print(learning_path_list)

    # parse web page to get list of learning paths
    learning_paths = []
    for lp in learning_path_list:
        learning_path = {}
        #print(lp)

        # get learning path info
        h3 = lp.find('h3', attrs={'class': 'path-title media-heading'})
        link = h3.find('a')
        learning_path['lp_name'] = link.text.strip()
        learning_path['lp_url'] = link['href']

        lp_infos = lp.find('p', attrs={'class': 'path-stats'})
        for word in lp_infos.text.strip().split('\n'):
            lp_attributes = word.split()
            attribute = 'lp_' + lp_attributes[0][:-1].lower()
            learning_path[attribute] = lp_attributes[1]

        learning_paths.append(learning_path)

    logger.info('Found {} learning paths'.format(len(learning_paths)))
    logger.info("Completed scraping '{}'".format(web_page))
    return learning_paths

def scrape_cognitive_class_learning_paths(num_pages):
    '''
    scrapes cognitive class learning paths
    '''
    logger.info("Scraping {} pages...".format(num_pages))

    page = 'https://cognitiveclass.ai/learn/all/'

    all_learning_paths = []
    for i in range(1, num_pages + 1):
        web_page = page + 'page/' + str(i)
        logger.info("Attempting to scrape {}...".format(web_page))
        all_learning_paths.extend(scrape_lp_web_page(web_page))

    logger.info("{} learning paths found".format(len(all_learning_paths)))
    logger.info("Done scraping {} pages...".format(num_pages))
    return all_learning_paths

def get_cognitive_class_learning_paths():
    '''
    get courses from cognitiveclass.ai
    '''
    logger.info("Getting cognitive class learning paths...")
    num_pages = 2
    learning_paths = scrape_cognitive_class_learning_paths(num_pages)
    logger.info("{} cognitive class learning paths found".format(len(learning_paths)))

    file_name = 'cognitive_class_learning_paths.txt'
    write_to_file(file_name, learning_paths)

    '''
    for learning_path in learning_paths:
        pprint(learning_path)
        logger.info("{}".format(json.dumps(learning_path, indent=4)))
    '''
    logger.info("Completed getting cognitive class learning paths")

def main():
    '''main program'''
    get_cognitive_class_courses()
    get_cognitive_class_learning_paths()


if __name__ == '__main__':
    main()
