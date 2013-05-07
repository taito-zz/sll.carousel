import mock
import unittest


class TestCase(unittest.TestCase):
    """TestCase for upgrade step"""

    @mock.patch('sll.carousel.upgrades.reimport_profile')
    def test_reimport_viewlets(self, reimport_profile):
        from sll.carousel.upgrades import reimport_viewlets
        context = mock.Mock()
        reimport_viewlets(context)
        reimport_profile.assert_called_with(context, 'profile-sll.carousel:default', 'viewlets')
