from zope import interface
from Products.fatsyndication.adapters.feedsource import BaseFeedSource
from Products.fatsyndication.adapters.feedentry import DocumentFeedEntry
from Products.CMFCore.utils import getToolByName
from Products.basesyndication.interfaces import IFeedEntry, IEnclosure


# Feedsource for Folder, Large Folder and Collection:

class FeedSource(BaseFeedSource):
        
    def getFeedEntries(self, max_only=True):
        portal_properties = getToolByName(self.context, 'portal_properties', None)
        site_properties = getattr(portal_properties, 'site_properties', None)
        portal_types = site_properties.getProperty('blog_types', None)
        if portal_types == None:
            portal_types = ('Document', 'News Item', 'File')

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

# FeedEntry adapters for News Item and File (podcasts, oh yeah!)

class NewsItemFeedEntry(DocumentFeedEntry):
    
    def getBody(self):
        return self.context.getImage().tag() + self.context.CookedBody()

class FileFeedEntry(DocumentFeedEntry):
    
    def getBody(self):
        return ''
    
    def getEnclosure(self):
        return IEnclosure(self.context)
 
    
# Enclosure adapter for ATFile:

class ATFileEnclosure:
    
    interface.implements(IEnclosure)
    
    def __init__(self, context):
        self.context = context
        self.file = context.getFile()
    
    def getURL(self):
        """URL of the enclosed file.
        """
        return self.context.absolute_url()

    def getLength(self):
        """Return the size/length of the enclosed file.
        """
        return int(self.file.get_size())

    def __len__(self):
        """Synonym for getLength
        """
        return self.getLength()

    def getMajorType(self):
        """Return the major content-type of the enclosed file.

            e.g. content-type = 'text/plain' would return 'text'.
        """
        return self.getType().split('/')[0]


    def getMinorType(self):
        """Return the minor content-type of the enclosed file.

            e.g. content-type = 'text/plain' would return 'plain'.
        """
        return self.getType().split('/')[1]

    def getType(self):
        """Return the content-type of the enclosed file.
        """
        return self.file.getContentType()
