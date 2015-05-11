import os

import jinja2

import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def get(self):

		lessons=["Stage 4"]

		sub_topic=["Networks, HTML Templates, Forms, Webpage"]

		sub_topic_list=['Network - a network is a group of entities that can communicate, even though they are not all directly connected. Must have at least 3 entities.',
        'Network needs to be able to encode and interpret messages (with bits); need a way to route messages; need rules to decide who gets to use the resources.',
        'Latency - used to measure the time it takes for the message to get from the source to the destination (unit of time), e.g. milliseconds.',
        'Bandwidth - amount of information (bits) that can be transmitted per unit of time (milliseconds); bandwidth typically measured as Mbps.',
        'Bit - the smallest unit of information; can choose between two things with 1 bit (e.g. 0 and 1). Use multiple bits to increase the amount of information that can be distinguished; every new bit added doubles how much can be distinguished.',
        'Protocol - a set of rules that tell how two entities talk to each other; on the internet, the client (web browser) and server uses Hypertext Transfer Protocol (HTTP). HTTP is the name of the protocol and defines the rules for this to happen.'
        'Routers figure out the next hops, which are used as a way to direct the message.',
        'Best effort service - in general, there are no rules enforced on the internet in terms of priority on who gets to use the resources.',
        'HTNL documents - contains the following sections: doctype; opening and closing HTML tags; the head which contains title, meta-data, java script, css cscript, etc.; and the body tag which contains the content of what appears on the webpage.',
        'URL - Uniform Resource Locator - has 3 main parts: protocol (e.g. HTTP or HTTPS), then host (can be an IP address or the name of the server), then the path (e.g. / )'
        'URLs can have a Query parameter (aka Get parameter) - use the ? followed by name=value (e.g. ?p=1); you can use multiple queries by using an & between each query. These are separate from the path, but included as part of the whole URL.'
        'Cache - something that stores data so you do not have to retrieve it later. It can be used to make data requests faster.'
        'Fragment - is separated from the rest of the URL by a # sign - references a particular part of a webpage you are looking at. This is not sent to the server when you make a request - it just exists in the browser.',
        'Port - when you make a web request to a server, in order to make an internet connection you need the address of the server and the port (e.g. 80 is the default); you can specifiy a port using :port, e.g. :8000'
        'HTTP - the main protocol of the web; used for browser to talk to web servers; a simple text protocol; request line has 3 main parts: method, path, and version; method is the request you are making of the server, e.g. GET, POST); the path is the actual document being requested from the server (this includes the path part after the main server address, and the query) - this would be the relative path; you could use the full path by including the main server address; the version is always HTTP/version number, e.g. HTTP/1.1 or HTTP/1.0.',
        'Headers in an HTTP request line get sent with the request line (name: value). Host header specifies the host part of the URL - this header is required in HTTP 1.1.',
        'User-Agent headers -describes who is making the request, generally your browser, e.g. Chrome. These headers are important so the server can block or slow down a particular agent when it is bombarding a site, etc.',
        'HTTP Responses - server sends back a response to the browser, e.g. the document requested, etc. this is done with the Status Line, which contains HTTP version, status code, and reason phrase which is an english translation of the status code (e.g. HTTP/1.1 200 ok). Common status codes include 300 (ok), 302 (doc is found someplace else), 404 (not found), and 500 (server error). Codes starting with 2 means it worked; with 3 means there is more work to be done technically to find the document; 4 means there is an issue on the browser side; 5 means there is an issue with the server side.',
        'Status line is followed by headers - incl. Date (when request happened), Server (not recommended to use), Content-Type (type of doc being returned, such as html), Content-Length (how long the doc is) etc.',
        'Servers - purpose is to respond to HTTP requests; two types of server responses - static (pre-written file that the server returns, e.g. image) and dynamic (the response is built on the fly by a program (web application) that is running; a web application builds content.',
        'Forms - enables a user to enter information into a website with fields, radio buttons, check boxes, etc.',
        'xx']

		items = self.request.get_all("word")
		self.render("html-div-lists.html", items = items,lessons=lessons,sub_topic=sub_topic, sub_topic_list=sub_topic_list)


app = webapp2.WSGIApplication([('/', MainPage),], debug = True)
