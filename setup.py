# -*- coding: utf-8 -*-
"""Installer for the codesyntax.distributions package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="codesyntax.distributions",
    version="1.0a1",
    description="An add-on for Plone",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Distribution",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Mikel Larreategi",
    author_email="mlarreategi@codesyntax.com",
    url="https://github.com/collective/codesyntax.distributions",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/codesyntax.distributions",
        "Source": "https://github.com/collective/codesyntax.distributions",
        "Tracker": "https://github.com/collective/codesyntax.distributions/issues",
        # 'Documentation': 'https://codesyntax.distributions.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["codesyntax"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "Plone",
        "setuptools",
        "plone.api",
        "plone.distribution",
        "codesyntax.login",
        "collective.easyform",
        "plone.formwidget.recaptcha",
        "plone.formwidget.hcaptcha",
        "collective.z3cform.norobots",
        "collective.folderishtypes",
        "collective.behavior.seo",
        "cs.htmlmailer",

    ],
    extras_require={
        "test": [
            "plone.app.testing",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = codesyntax.distributions.locales.update:update_locale
    """,
)
