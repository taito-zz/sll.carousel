from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
from zope.component import getUtility

import logging


def hide_viewlet(context, viewlets, manager, logger=None):
    """Hide viewlets form viewlet manager.

    :param context: context object
    :type context: object

    :param viewlets: Tuple of viewlet names with unicode
    :type viewlets: tuple

    :param manager: Name of viewlet manager
    :type manager: unicode
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    storage = getUtility(IViewletSettingsStorage)
    message = 'Hiding viewlets: {0} from {1}.'.format(
        ', '.join(viewlets),
        manager
    )
    logger.info(message)
    storage.setHidden(manager, '*', viewlets)
    message = 'Hid viewlets: {0} from {1}.'.format(
        ', '.join(viewlets),
        manager
    )
    logger.info(message)


def setupVarious(context):

    if context.readDataFile('sll.carousel_various.txt') is None:
        return

    hide_viewlet(
        context,
        (u'Products.Carousel.viewlet', ),
        u'plone.abovecontent'
    )
