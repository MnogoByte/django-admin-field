# -*- coding: utf-8 -*-
from distutils.core import setup


setup(name='django-admin-field',
      version='0.0.2',
      description='Django ModelAdmin field syntax simplifier.',
      author='Alexander Klimenko',
      author_email='alex@erix.ru',
      long_description = open('README.rst').read(),
      url='https://github.com/meteozond/django-admin-field',
      packages=['django_admin_field'],
      classifiers=[
            "Framework :: Django",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "Operating System :: OS Independent",
            "Topic :: Software Development"
      ],
      license="BSD",
      )
