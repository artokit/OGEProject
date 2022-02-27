from .models import TheoryPost


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['popular'] = TheoryPost.objects.all().order_by('-count_view')[:5]
        return context
