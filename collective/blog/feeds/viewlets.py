from plone.app.layout.viewlets import ViewletBase
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

class FeedsViewlet(ViewletBase):
    index = ViewPageTemplateFile('feedsviewlet.pt')
