from django.views.generic import FormView, TemplateView

from .forms import SearchForm
from .utils import get_page_analysis

# Create your views here.


class ShowTableSummaryView(FormView):
    template_name = 'analyser/index.html'
    form_class = SearchForm

    def form_valid(self, form):
        url = form.cleaned_data.get('url')
        result = get_page_analysis(url)
        return self.render_to_response(self.get_context_data(form=form, result=result))


class ShowTableSummaryViaAPIView(TemplateView):
    template_name = 'analyser/index2.html'

    def get_context_data(self, **kwargs):
        context = super(ShowTableSummaryViaAPIView, self).get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context


