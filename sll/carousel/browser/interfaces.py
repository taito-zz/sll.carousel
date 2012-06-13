from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager


class ISllCarouselLayer(Interface):
    """Marker interface for browserlayer."""


class ICarouselViewletManager(IViewletManager):
    """Carousel viewlet manager."""
