from django.http import HttpResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View


@method_decorator(csrf_exempt, name='dispatch')
class PreviewView(View):
    fallback_template_name = "wagtailpreview/fallback.html"

    def post(self, request, *args, **kwargs):
        context = {
            'meta': {
                'body': request.body
            }
        }
        template = loader.get_template(self.fallback_template_name)
        html = template.render(context, request)
        return HttpResponse(html)
