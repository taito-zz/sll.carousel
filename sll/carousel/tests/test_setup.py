from sll.carousel.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_sll_carousel_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.carousel'))

    def test_browserlayer(self):
        from sll.carousel.browser.interfaces import ISllCarouselLayer
        from plone.browserlayer import utils
        self.failUnless(ISllCarouselLayer in utils.registered_layers())

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
