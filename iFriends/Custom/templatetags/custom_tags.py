from django import template
register = template.Library()

@register.tag(name="getLargestBlog")
def getLargestBlog(parser, token):
    try:
        tag_name, bList = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError
    return getLargestBlogNode(bList)

class getLargestBlogNode(template.Node):
    def __init__(self, bList):
        self.bList = template.Variable(bList)
    def render(self, context):
        lBlog = None
        longest = 0
        for blog in self.bList.resolve(context):
            if len(blog.text) >= longest:
                longest = len(blog.text)
                lBlog = blog
        context['largestBlog'] = lBlog
        return ''

def navLink(context):
    links = []
    link = {'name': 'Home', 'value': '/'}
    links.append(link)
    if context.has_key('pageLinks'):
        links.append(context['pageLinks'])
    return {'navLinks': links}
register.inclusion_tag('navlink.html', takes_context=True)(navLink)

@register.tag(name="teaUpper")
def teaUpper(parser, token):
    nodelist = parser.parse(('endTeaUpper',))
    parser.delete_first_token()
    return doTeaUpper(nodelist)

class doTeaUpper(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        outText = self.nodelist.render(context)
        outText = str(outText)
        outText = outText.upper()
        return outText

