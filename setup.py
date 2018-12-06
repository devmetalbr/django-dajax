from distutils.core import setup


setup(
    name='django-dajax-py3dj2',
    version='0.10.0',
    author='Antonio Tomasic',
    author_email='atomasic@gmail.com',
    description=('Easy to use library to create asynchronous presentation '
                 'logic with django and dajaxice'),
    url='https://github.com/atomasic/django-dajax.git',
    license='BSD',
    packages=['dajax'],
    package_data={'dajax': ['static/dajax/*']},
    long_description=('dajax is a powerful tool to easily and super-quickly '
                      'develop asynchronous presentation logic in web '
                      'applications using python and almost no JS code. It '
                      'supports up to four of the most popular JS frameworks: '
                      'jQuery, Prototype, Dojo and mootols.'),
    install_requires=[
        'django-dajaxice-py3dj2>=0.8.0'
    ],
    classifiers=['Development Status :: 4 - Beta',
                'Environment :: Web Environment',
                'Framework :: Django',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: BSD License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Utilities'],
    python_requires='>=3.6.7'
)
