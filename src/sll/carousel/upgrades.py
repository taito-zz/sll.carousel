from abita.utils.utils import reimport_profile


PROFILE_ID = 'profile-sll.carousel:default'


def reimport_viewlets(context, logger=None):
    """Reimport viewlets"""
    reimport_profile(context, PROFILE_ID, 'viewlets')
