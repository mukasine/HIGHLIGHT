class News:
    '''
    News class to define News Objects
    '''
def __init__(self,id,title,name,author,description,urlToImage,url):
        self.id =id
        self.name= name
        self.author = author
        self.description=description
        self.title= title
        self.urlToImage=urlToImage
        self.url=url
        {% extends 'base.html'%}
class articles:
    '''
    articles class to define articles Objects
    '''
def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description