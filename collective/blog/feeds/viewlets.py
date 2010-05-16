from plone.app.layout.viewlets import ViewletBase
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

class FeedsViewlet(ViewletBase):
    render = ViewPageTemplateFile('feedsviewlet.pt')
