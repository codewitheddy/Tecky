from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_redirect(request):
    """Redirect from /admin/ to our custom dashboard"""
    return redirect('dashboard:dashboard')