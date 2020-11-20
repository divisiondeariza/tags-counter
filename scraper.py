from urllib import request
from html.parser import HTMLParser

class TagCounter(HTMLParser):
    def __init__(self, url):
        super().__init__()
        r = request.urlopen(url)
        self.body = str(r.read())
        self.tags = {}
        self.feed(self.body)

    def get_top_used_tags(self):
        tags = [(k,v) for (k,v) in self.tags.items()]
        tags.sort(key=lambda e: e[0])
        tags.sort(key=lambda e: e[1], reverse=True)
        return tuple(tags[0:5])

    def count_total_tags(self):
        return sum([v for (k,v) in self.tags.items()])

    def handle_starttag(self, tag, attrs):
        if tag in self.tags:
            self.tags[tag] = self.tags[tag] + 1
        else:
            self.tags[tag] = 1

class Tabulator:
    def generate(self, tags_tuple):
        size_col_tags = max(len(k) for (k,v) in tags_tuple) + 3
        header = "TAG" + " "*(size_col_tags-3) + "| COUNT"
        separator = "="*size_col_tags + "|" + "="*6
        rows = [k + " "*(size_col_tags-len(k)) + "| " + str(v) for (k,v) in tags_tuple]
        table = [header, separator] + rows
        return "\n".join(table)