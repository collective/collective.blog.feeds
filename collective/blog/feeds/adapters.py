from Products.CMFPlone.interfaces import syndication
from Products.CMFPlone.browser.syndication import adapters
from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.ATContentTypes.interfaces import IATNewsItem

class NewsItemItem(adapters.BaseItem):
    
    @property
    def body(self):
        return self.context.getImage() and self.context.getImage().tag() + \
               self.context.CookedBody() or self.context.CookedBody()

