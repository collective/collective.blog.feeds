from Products.fatsyndication.adapters.feedsource import BaseFeedSource
from Products.CMFCore.utils import getToolByName
from Products.basesyndication.interfaces import IFeedEntry


class FeedSource(BaseFeedSource):
        
    def getFeedEntries(self, max_only=True):
        portal_properties = getToolByName(self.context, 'portal_properties', None)
        site_properties = getattr(portal_properties, 'site_properties', None)
        portal_types = site_properties.getProperty('blog_types', None)
        if portal_types == None:
            portal_types = ('Document', 'News Item',)

        brains = self._getBrains(portal_types)
        if max_only:
            brains = brains[:self.getMaxEntries()]
        return [IFeedEntry(x.getObject()) for x in brains]

    
class FolderFeedSource(FeedSource):

    def _getBrains(self, portal_types):
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        return catalog.searchResults(path={'query': path, 'depth':1},
                                     portal_type=portal_types,
                                     sort_on='effective')

    
class TopicFeedSource(FeedSource):
    
    def _getBrains(self, portal_types):
        return self.context.queryCatalog()

    
from Products.fatsyndication.adapters.feedentry import DocumentFeedEntry

class NewsItemFeedEntry(DocumentFeedEntry):
    
    def getBody(self):
        return self.context.getImage().tag() + self.context.CookedBody()
