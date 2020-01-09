from django import template
import datetime

register = template.Library()

#{% current_time "%Y-%m-%d %H:%M:%S" %}
#<p>The time is {% current_time "%Y-%m-%d %H:%M:%S" %}</p> 2014-1-1 10:10:10

@register.tag(name='current_time')
def do_current_time(parse, token):
	try:
		tag, format = token.split_contents()
	except ValueError:
		msg = "%r" token.split_contents()[0]
		raise template.TemplateSyntaxError(msg)
	return CurrentTimeNode(format[1:-1])

class CurrentTimeNode(template.Node):
	"""docstring for ClassName"""
	def __init__(self, format):
		self.format = str(format)
	
	def render(self, context):
		now = datetimme.datetime.now()
		return now.strftime(self.format)

@register.simple_tag
def current_time(format):
	try:
		return datetime.datetime.now().strftime(str(format))
	except UnicodeError:
		raise "some error"