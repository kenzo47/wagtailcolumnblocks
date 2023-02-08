from setuptools import setup

setup(
    name='wagtailcolumnblocks',
    description='Wagtail Column Blocks',
    use_scm_version=True,
    author='Tim van der Linden',
    author_email='tim@shisaa.be',
    url='https://github.com/timusan/wagtailcolumnblocks',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    license='BSD',
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Framework :: Django :: 3.0',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],

    packages=['wagtailcolumnblocks'],
    include_package_data=True,

    install_requires=[
        'wagtail >= 4.0',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
)
