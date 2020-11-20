from unittest import TestCase, mock
from scraper import TagCounter, Tabulator

class TestTagCounter(TestCase):

    def setUp(self):
        self.html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were

<ul>
<li><a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,</li>
<li><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and</li>
<li><a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;</li>
<li><a><b>and they lived at the bottom of a well.</b></a></li>
<li><b>...</b></li>
</ul>

</p>

</body>
</html>
"""
        self.mock_response = mock.MagicMock()
        self.mock_response.read.return_value = self.html_doc
    
    @mock.patch('scraper.request')
    def test_calls_request_library(self, mock_request):
        tag_counter = TagCounter("https://example.com")
        mock_request.urlopen.assert_called_with("https://example.com")

    @mock.patch('scraper.request')
    def test_stores_body(self, mock_request):
        mock_request.urlopen.return_value = self.mock_response
        tag_counter = TagCounter("https://example.com")
        self.assertEqual(tag_counter.body, self.html_doc)

    @mock.patch('scraper.request')
    def test_get_top_used_tags(self, mock_request):
        mock_request.urlopen.return_value = self.mock_response
        tag_counter = TagCounter("https://example.com")
        self.assertEqual(tag_counter.get_top_used_tags(), (('li', 5), ('a', 4), ('b', 3), ('p', 2), ('body', 1)))

    @mock.patch('scraper.request')
    def test_get_total_tags(self, mock_request):
        mock_request.urlopen.return_value = self.mock_response
        tag_counter = TagCounter("https://example.com")
        self.assertEqual(tag_counter.count_total_tags(), 19)

class TestTablePesentation(TestCase):
    def test_shows_table_well_indented(self):
        top_tags = (('html', 500),('a', 400),('b', 300), ('averylongtag', 200), ('p', 100))
        expected_table = """\
TAG            | COUNT
===============|======
html           | 500
a              | 400
b              | 300
averylongtag   | 200
p              | 100"""
        tabulator = Tabulator()
        self.assertEqual(tabulator.generate(top_tags), expected_table)
