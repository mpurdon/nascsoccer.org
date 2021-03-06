from django.views.generic.base import TemplateView

from apps.news.models import Item

class HomeView(TemplateView):
    template_name = "common/home.haml"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        try:
            context["featured_news"] = Item.objects.filter(is_active=True, is_featured=True).latest("updated_at")
        except:
            # No featured news.    Not a big deal, really.
            pass

        context["news"] = Item.objects.filter(is_active=True)[:5]

        return context
