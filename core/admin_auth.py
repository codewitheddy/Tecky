from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class AdminLoginView(LoginView):
    template_name = 'admin/login.html'
    success_url = reverse_lazy('dashboard:dashboard')
    
    def get_success_url(self):
        return reverse_lazy('dashboard:dashboard')