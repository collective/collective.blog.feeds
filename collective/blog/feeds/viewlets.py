from plone.app.layout.viewlets import ViewletBase
try:
    from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
except:
    from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
    
class FeedsViewlet(ViewletBase):
    index = ViewPageTemplateFile('feedsviewlet.pt')
