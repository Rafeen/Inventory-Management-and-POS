from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sales.models.bundle_model import Bundle


@login_required(login_url='/login/')
def bundle_list(request):
    """
    This view Renders Bundle list Page    """
    bundles= Bundle.objects.all()
    context = {
        "title": "All Bundles",
        "bundles":bundles
    }
    return render(request, 'bundle_list.html',context)

