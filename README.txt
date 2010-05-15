Introduction
============

collective.blog.feeds provides blog feeds for standard Plone folders and 
collections. It builds on basesyndication and fatsyndication and uses their
architecture and templates, but provides concrete implementations for
standard Plone content.

To create the feeds all you need to do is make collective.blog.feeds be a 
dependent product in your buildout, and include the ZCML one way or another.
Plone folders, large folders and collections will then gain a set of new
views: atom.xml, feed.rdf, feed11.rdf, rss.xml and itunes.xml.


What this product do not have
-----------------------------

There is no Plone Control Panel in this product, nor will there ever be one,
so you need to change the settings through the ZMI. There will also never be
any per-folder settings, as that would require extending the schema for 
folders or have a dedicated blog type, both which will defeat the main goal
of this product: simplicity and flexibility.
