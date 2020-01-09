
from django.utils.safestring import mark_safe

class PageInfo(object):
	def __init__(self, current_page, all_count, per_item = 5):
		self.CurrentPage = current_page
		self.AllCount = all_count
		self.PerItem = per_item

	@property
	def start(self):
		return (self.CurrentPage - 1) * self.PerItem

	@property
	def end(self):
		return self.CurrentPage * self.PerItem

	@property
	def all_page_count(self):
		temp = divmod(self.AllCount, self.PerItem)
		if temp[1] == 0:
			all_count = temp[0]
		else:
			all_count = temp[0] + 1
		return all_count


# 分页查询
def Pager(page, all_pages_count):
	all_pages_html = []

	first_page = "<a href='/pindex/1'>首页</a>"
	all_pages_html.append(first_page)

	if page == 1:
		prev_page = "<a href='#'>上一页</a>"
	else:
		prev_page = "<a href='/pindex/%s'>上一页</a>" % str(page - 1)
	all_pages_html.append(prev_page)

	stepback = 6
	stepforward = 5
	pageshownumber = stepback + stepforward
	
	if all_pages_count < pageshownumber:
		# show 1 ~ to all page self.AllCount
		begin = 1
		end = all_pages_count
	else: #all_pages_count > pageshownumber
		if page < stepback:
		  # 1 ~ all_pages_count
			begin = 1
			end = pageshownumber
		elif page >= stepback:
			if (page + stepforward) < all_pages_count:
				begin = all_pages_count - pageshownumber
				end = all_pages_count
			begin = page - stepback
			if page + stepforward > all_pages_count:
				end = all_pages_count + 1
			else:
				end = page + stepforward


	# 显示当前页范围 附近的页
	for i in range(begin, end):
	# for i in range(all_pages_count):
		print(i, begin, end , page)
		if (i) == page:
			html = "<a class='selected' href='/pindex/%d'>%d</a>" % (i , i)
		else:
			html  = "<a href='/pindex/%d'>%d</a>" % (i, i)
		# if (i+1) == page:
		# 	html = "<a class='selected' href='/pindex/%d'>%d</a>" % (i + 1, i + 1)
		# else:
		# 	html  = "<a href='/pindex/%d'>%d</a>" % (i + 1, i + 1)

		all_pages_html.append(html)

	if page == all_pages_count:
		next_page = "<a href='#'>下一页</a>"
	else:
 		next_page = "<a href='/pindex/%s'>下一页</a>" % str(page+1)

	all_pages_html.append(next_page)

	end_page = "<a href='/pindex/%d'>尾页</a>" % (all_pages_count)
	all_pages_html.append(end_page)


	# marksafe
	pages = mark_safe((" ").join(all_pages_html))
	return pages

