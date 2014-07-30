
import datetime

class Issue:
    posts = []
    jobs = []

    def __init__(self, number, title, url):
        self.number = number
        self.title = title
        self.url = url

    def set_date(date):
        self.date = date

    def add_post(post):
        self.posts.append(post)

    def add_job(job):
        self.jobs.append(job)


class Post:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

    def __init__(self, title, desc, src):
        self.title = title
        self.desc = desc
        self.src = src

class DailyPost:
    def __init__(self, title, src):
        self.title = title
        self.src = src

class Job:
    def __init__(self, company, position):
        self.company = company
        self.position = position