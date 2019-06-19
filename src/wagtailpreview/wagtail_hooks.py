from django.conf import settings
from django.conf.urls import url
from django.templatetags.static import static
from django.utils.html import format_html_join
from wagtail.core import hooks

from wagtailpreview.views import PreviewView


@hooks.register('register_admin_urls')
def register_preview_url():
    return [
        url(r'^preview-streamfield/$', PreviewView.as_view(), name='preview-streamfield'),
    ]


@hooks.register("insert_editor_js")
def insert_preview_js():
    js_files = ["wagtailadmin/wagtail_preview.js"]
    js_includes = format_html_join(
        "\n",
        '<script src="{0}"></script>',
        ((static(filename),) for filename in js_files),
    )
    return js_includes
