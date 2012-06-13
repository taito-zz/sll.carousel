from sll.carousel.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_sll_carousel_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.carousel'))

    def test_is_Carousel_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('Carousel'))

    def test_browserlayer(self):
        from sll.carousel.browser.interfaces import ISllCarouselLayer
        from plone.browserlayer import utils
        self.failUnless(ISllCarouselLayer in utils.registered_layers())

    def test_cssregistry_configured__applyPrefix(self):
        css = getToolByName(self.portal, 'portal_css')
        item = css.getResource('++resource++sll.carousel.stylesheets/carousel.css')
        self.assertTrue(item.getApplyPrefix())

    def test_cssregistry_configured__authenticated(self):
        css = getToolByName(self.portal, 'portal_css')
        item = css.getResource('++resource++sll.carousel.stylesheets/carousel.css')
        self.assertFalse(item.getAuthenticated())

    def test_cssregistry_configured__cacheable(self):
        css = getToolByName(self.portal, 'portal_css')
        item = css.getResource('++resource++sll.carousel.stylesheets/carousel.css')
        self.assertTrue(item.getCacheable())

    def test_cssregistry_configured__compression(self):
        css = getToolByName(self.portal, 'portal_css')
        item = css.getResource('++resource++sll.carousel.stylesheets/carousel.css')
        self.assertEqual(item.getCompression(), 'safe')

    def test_cssregistry_configured__conditionalcomment(self):
        css = getToolByName(self.portal, 'portal_css')
        item = css.getResource('++resource++sll.carousel.stylesheets/carousel.css')
        self.assertFalse(item.getConditionalcomment())

    def test_cssregistry_configured__cookable(self):
        css = getToolByName(self.portal, 'portal_css')
        item = css.getResource('++resource++sll.carousel.stylesheets/carousel.css')
        self.assertTrue(item.getCookable())

    def test_cssregistry_configured__enabled(self):
        css = getToolByName(self.portal, 'portal_css')
        item = css.getResource('++resource++sll.carousel.stylesheets/carousel.css')
        self.assertTrue(item.getEnabled())

    def test_cssregistry_configured__expression(self):
        css = getToolByName(self.portal, 'portal_css')
        item = css.getResource('++resource++sll.carousel.stylesheets/carousel.css')
        self.assertFalse(item.getExpression())

    def test_cssregistry_configured__media(self):
        css = getToolByName(self.portal, 'portal_css')
        item = css.getResource('++resource++sll.carousel.stylesheets/carousel.css')
        self.assertFalse(item.getMedia())

    def test_cssregistry_configured__rel(self):
        css = getToolByName(self.portal, 'portal_css')
        item = css.getResource('++resource++sll.carousel.stylesheets/carousel.css')
        self.assertEqual(item.getRel(), 'stylesheet')

    def test_cssregistry_configured__rendering(self):
        css = getToolByName(self.portal, 'portal_css')
        item = css.getResource('++resource++sll.carousel.stylesheets/carousel.css')
        self.assertEqual(item.getRendering(), 'link')

    def test_cssregistry_configured__title(self):
        css = getToolByName(self.portal, 'portal_css')
        item = css.getResource('++resource++sll.carousel.stylesheets/carousel.css')
        self.assertFalse(item.getTitle())

    def test_viewlets__Products_Carousel_viewlet__order(self):
        from zope.component import getUtility
        from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
        storage = getUtility(IViewletSettingsStorage)
        self.assertEqual(
            storage.getOrder('plone.portaltop', '*'),
            (
                u'plone.header',
                u'Products.Carousel.viewlet',
            )
        )

    def test_viewlets__Products_Carousel_viewlet__hidden(self):
        from zope.component import getUtility
        from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
        storage = getUtility(IViewletSettingsStorage)
        self.assertEqual(
            storage.getHidden('plone.abovecontent', '*'),
            (u'Products.Carousel.viewlet',)
        )

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.carousel'])
        self.failIf(installer.isProductInstalled('sll.carousel'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.carousel'])
        from sll.carousel.browser.interfaces import ISllCarouselLayer
        from plone.browserlayer import utils
        self.failIf(ISllCarouselLayer in utils.registered_layers())

    def test_uninstall__cssregistry(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.carousel'])
        css = getToolByName(self.portal, 'portal_css')
        self.failIf(
            '++resource++sll.carousel.stylesheets/carousel.css' in css.getResourceIds()
            )
