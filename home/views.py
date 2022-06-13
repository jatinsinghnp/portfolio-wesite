from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ContactUsForm

from .models import (
    PersonalInfo,
    PersonalDetailInfo,
    Skill,
    Education,
    MyPortFolio,
    Blog,
)

# Create your views here.


class HomePageView(ListView):
    template_name = "index.html"
    model = PersonalInfo
    context_object_name = "persons"


class AboutPageView(ListView):
    template_name = "about.html"
    model = PersonalDetailInfo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["persons"] = PersonalDetailInfo.objects.all()
        context["skills"] = Skill.objects.all().order_by("-uuid")
        context["educations"] = Education.objects.all()
        return context


class PortfolioPageView(ListView):
    template_name = "portfolio.html"
    model = MyPortFolio
    context_object_name = "ports"


class ContactUsView(CreateView):
    template_name = "contact.html"
    form_class = ContactUsForm
    success_url = reverse_lazy("contact-page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["persons"] = PersonalDetailInfo.objects.all()
        return context

    def form_valid(self, form):

        messages.success(self.request, "messages has been sent")
        form.save()
        return super(ContactUsView, self).form_valid(form)


class BlogPageView(ListView):
    model = Blog
    template_name = "blog.html"
    context_object_name = "blogs"


class BlogPostView(DetailView):
    model = Blog
    template_name = "blog-post.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog"] = Blog.objects.get(slug=self.kwargs.get('slug',None))
        return context
    