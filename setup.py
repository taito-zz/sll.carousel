from setuptools import find_packages
from setuptools import setup


setup(
    name='sll.carousel',
    version='0.1.1',
    description="Customizes Products.Carousel package for SLL Site.",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='http://www.sll.fi/',
    license='Non-free',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['sll'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.Carousel',
        'hexagonit.testing',
        'plone.browserlayer',
        'setuptools'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
