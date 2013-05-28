from Products.CMFPlone.browser.syndication import adapters

class NewsItemItem(adapters.BaseItem):
    
    @property
    def body(self):
        if self.context.getImage():
            return '<a href="%s">%s</a>%s' % (self.context.getImage().absolute_url(), 
                                              self.context.restrictedTraverse('image_mini').tag(),
                                              self.context.CookedBody())
        else:
            return self.context.CookedBody()
