# my_django_app/templatetags/vueassets.py
import json
import os
from django import template
from django.conf import settings
from django.templatetags.static import static
from django.contrib.staticfiles import finders

register = template.Library()


def get_manifest():
    """
    Locate and load ‘example_vue_app/asset-manifest.json’ (or manifest.json)
    from any STATICFILES_DIRS or app/static folder.
    """
    # 1) Try the named asset-manifest.json
    manifest_name = 'example_vue_app/asset-manifest.json'
    path = finders.find(manifest_name)
    if path and os.path.isfile(path):
        with open(path, 'r') as f:
            return json.load(f)

    # 2) Fallback to manifest.json (if you renamed it)
    alt = 'example_vue_app/manifest.json'
    path = finders.find(alt)
    if path and os.path.isfile(path):
        with open(path, 'r') as f:
            return json.load(f)

    # 3) Nothing found
    return {}


# Cache the manifest to avoid reading file multiple times per request
_manifest_cache = None


@register.simple_tag
def vue_asset(asset_name):
    global _manifest_cache
    if _manifest_cache is None:
        _manifest_cache = get_manifest()

    manifest = _manifest_cache
    key = asset_name if asset_name in manifest else os.path.basename(asset_name)
    hashed = manifest.get(key)

    if not hashed:
        # No hashed entry → serve the plain file
        return static(f'example_vue_app/{asset_name}')

    # Strip STATIC_URL + subpath if present
    prefix = settings.STATIC_URL.rstrip('/') + '/example_vue_app/'
    if hashed.startswith(prefix):
        hashed = hashed[len(prefix):]

    return static(f'example_vue_app/{hashed}')


@register.simple_tag
def clear_vue_manifest_cache():
    """Clear the manifest cache (useful for development)"""
    global _manifest_cache
    _manifest_cache = None
    print("Manifest cache cleared")
    return ""