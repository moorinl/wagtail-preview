from django.conf import settings
from django.templatetags.static import static
from django.utils.html import format_html_join
from wagtail.core import hooks


@hooks.register("insert_editor_js")
def insert_preview_js():
    js_files = ["wagtailadmin/wagtail_preview.js"]
    js_includes = format_html_join(
        "\n",
        '<script src="{0}"></script>',
        ((static(filename),) for filename in js_files),
    )
    return js_includes
