from setuptools import setup, find_packages

setup(
    name='django-attributes',
    version=__import__('attributes').__version__,
    license="BSD",

    install_requires = [],

    description='A reusable applicaton to add arbitrary attributes to a model. Idea yoinked from Satchmo',
    long_description=open('README').read(),

    author='Colin Powell',
    author_email='colin@onecardinal.com',

    url='http://github.com/powellc/django-attributes',
    download_url='http://github.com/powellc/django-attributes/downloads',

    include_package_data=True,

    packages=['attributes'],

    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
