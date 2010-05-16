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

Yes, *all* folders get this view. No, you don't have to enable syndication
on the folder, which also means you don't have to find that enable syndication
tab action that for some reason is invisible by default so that you can't turn
on the standard RSS feed without knowing Plone inside and out for some
incomprehensible reason.

It also adds the feeds to the plone header with the standard 
'<link rel="alternate" ...>' type of header links. There probably should be
a way to turn that off or on, but currently there isn't.


Settings
--------

By default this product will only use Documents, News Items and Files as 
entries in the blog feed. If you want to use some custom content types you
will need to do two things:

1. Provide an IFeedEntry adapter. Look at the "adapters.py" file for an
   examples made for News Item. As you see it's not particularily complicated.
   You also need to register the adapter, look in configure.zcml to see how
   that is done.
   
2. Create a property in portal.properties/site_properties called "blog_types"
   of the "lines" type. Then in that property add each content type that
   your site should see as being blog entries.
   
Podcasts
--------

collective.blog.feeds provides an adapter for the ATFile content type with
podcast enclosure support. You can therefore make podcasts simply by making
a folder and sticking files in it.


What this product do not have
-----------------------------

There is no Plone Control Panel in this product, nor will there ever be one,
so you need to change the settings through the ZMI. There will also never be
any per-folder settings, as that would require extending the schema for 
folders or have a dedicated blog type, both which will defeat the main goal
of this product: simplicity and flexibility.
