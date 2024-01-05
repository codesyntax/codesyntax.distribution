# -*- coding: utf-8 -*-
from plone import api
from plone.app.multilingual.browser.setup import SetupMultilingualSite
from plone.distribution.core import Distribution
from plone.registry.interfaces import IRegistry
from zope.component import queryMultiAdapter
from zope.component import queryUtility
from zope.globalrequest import getRequest

from plone.app.dexterity.interfaces import ITypeSchemaContext


def pre_handler(answers):
    return answers


def handler(distribution: Distribution, site, answers: dict) -> Distribution:
    return site


def post_handler(distribution: Distribution, site, answers: dict):
    # Setup the multilingual site configuration
    reg = queryUtility(IRegistry, context=site)
    reg["plone.available_languages"] = answers["available_languages"]

    setup_tool = SetupMultilingualSite()
    setup_tool.setupSite(site)

    # Setup SEO behavior on selected content types
    behavior_name = "collective.behavior.seo.seo_fields"
    content_types = ["News Item", "Event", "Document", "Collection"]
    for content_type in content_types:
        request = getRequest()
        context = queryMultiAdapter((site, request), name="dexterity-types")
        context = context.publishTraverse(request, content_type)

        behaviors = queryMultiAdapter((context, getRequest()), name="behaviors")
        behaviors.form_instance.applyChanges({behavior_name: True})

    return site
