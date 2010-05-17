import os
import unittest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.Five import testbrowser
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite(products=['collective.blog.feeds'])

import collective.blog.feeds

class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml',
                             collective.blog.feeds)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass
        
class FunctionalTestCase(ptc.FunctionalTestCase, TestCase):
    
    def test_feeds(self):
        # Use a browser to log into the portal:
        admin = testbrowser.Browser()
        admin.handleErrors = False
        portal_url = self.portal.absolute_url()
        admin.open(portal_url)
        admin.getControl(name='__ac_name').value = ptc.portal_owner
        admin.getControl(name='__ac_password').value = ptc.default_password
        admin.getControl('Log in').click()

        # Create a folder to act as the blog:
        admin.getLink(id='folder').click()
        admin.getControl(name='title').value = 'A Blog'
        admin.getControl(name='form.button.save').click()
        # Publish it:
        admin.getLink(id='workflow-transition-publish').click()
        # Save this url for easy access later:
        blog_url = admin.url
        
        # In the folder, create four content types, a Document, a News Item,
        # a File and an Event:
        admin.getLink(id='document').click()
        admin.getControl(name='title').value = 'A Document Blog Entry'
        admin.getControl(name='text').value = 'The main body of the Document'
        admin.getControl(name='form.button.save').click()
        admin.getLink(id='workflow-transition-publish').click()
        
        admin.open(blog_url)
        admin.getLink(id='news-item').click()
        admin.getControl(name='title').value = 'A News Item Blog Entry'
        admin.getControl(name='text').value = 'The main body of the News Item'
        testfile = os.path.join(os.path.dirname(__file__), 'testlogo.jpg')
        thefile = admin.getControl(name='image_file')
        thefile.filename = 'testlogo.jpg'
        thefile.value = open(testfile, 'rb')
        admin.getControl(name='form.button.save').click()
        admin.getLink(id='workflow-transition-publish').click()

        admin.open(blog_url)
        admin.getLink(id='file').click()
        admin.getControl(name='title').value = 'A File Blog Entry'
        testfile = os.path.join(os.path.dirname(__file__), 'testaudio.mp3')
        thefile = admin.getControl(name='file_file')
        thefile.filename = 'testaudio.mp3'
        thefile.value = open(testfile, 'rb')
        admin.getControl(name='form.button.save').click()

        admin.open(blog_url)
        admin.getLink(id='event').click()
        admin.getControl(name='title').value = 'An Event Blog Entry'
        admin.getControl(name='text').value = 'The main body of the Event'
        admin.getControl(name='form.button.save').click()
        admin.getLink(id='workflow-transition-publish').click()
        
        #############################
        ## Now, make sure things work
        #############################
        
        # First, check that the feeds are listed in the header:
        anon = testbrowser.Browser()
        anon.handleErrors = False
        anon.open(blog_url)
        self.assert_('atom.xml' in anon.contents)
        self.assert_('feed.rdf' in anon.contents)
        self.assert_('feed11.rdf' in anon.contents)
        self.assert_('rss.xml' in anon.contents)
        self.assert_('itunes.xml' in anon.contents)
        
        # Now check that the correct info is in the feeds. We'll assume that
        # basesyndication/fatsyndication is not broken, and check only rss.xml.
        anon.open(blog_url+'/rss.xml')
        # The document:
        self.assert_('The main body of the Document' in anon.contents)
        # The news item with image:
        self.assert_('The main body of the News Item' in anon.contents)
        self.assert_('/image' in anon.contents)
        # The file:
        self.assert_('<enclosure' in anon.contents)
        self.assert_('testaudio.mp3' in anon.contents)
        # But *not* the event, as it has no feed adapter.
        self.assert_('The main body of the Event' not in anon.contents)

def test_suite():
    return unittest.TestSuite([
        unittest.makeSuite(FunctionalTestCase),
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
