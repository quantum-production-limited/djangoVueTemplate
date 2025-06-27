import json
import os
from django import template
from django.conf import settings
from django.templatetags.static import static
from django.contrib.staticfiles import finders
import logging

logger = logging.getLogger(__name__)
register = template.Library()
# Cache the manifest to avoid reading file multiple times per request
_manifest_cache = None


def get_manifest():
    """
    Load example_vue_app/asset-manifest.json (or manifest.json)
    via Django staticfiles finders.
    """
    for name in (
        "example_vue_app/asset-manifest.json",
        "example_vue_app/manifest.json",
    ):
        path = finders.find(name)
        if path and os.path.isfile(path):
            try:
                with open(path, "r") as f:
                    return json.load(f)
            except Exception as e:
                logger.error("Vue manifest load error (%s): %s", name, e)
                return {}
    return {}


@register.simple_tag
def vue_asset(asset_name):
    """
    Return the STATIC_URL for a Vue-built asset, using the manifest.
    Falls back to un-hashed file if missing.
    """
    global _manifest_cache
    if settings.DEBUG:
        # Always reload manifest in dev
        _manifest_cache = None

    if _manifest_cache is None:
        _manifest_cache = get_manifest()

    manifest = _manifest_cache
    key = asset_name if asset_name in manifest else os.path.basename(asset_name)
    hashed = manifest.get(key)
    if not hashed:
        return static(f"example_vue_app/{asset_name}")

    prefix = settings.STATIC_URL.rstrip("/") + "/example_vue_app/"
    if hashed.startswith(prefix):
        hashed = hashed[len(prefix) :]
    return static(f"example_vue_app/{hashed}")


@register.simple_tag
def clear_vue_manifest_cache():
    """Clear the manifest cache (useful for development)"""
    global _manifest_cache
    _manifest_cache = None
    print("Manifest cache cleared")
    return ""
