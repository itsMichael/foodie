from django.views.generic import TemplateView

    
class Homepage(TemplateView):
    template_name = "index.html"    


class HomeView(TemplateView):
    template_name = "partials/homeView.html"    


class ProductView(TemplateView):
    template_name = "partials/productView.html"    


class VitaminView(TemplateView):
    template_name = "partials/vitaminView.html"   


class PreservativeView(TemplateView):
    template_name = "partials/preservativeView.html"     