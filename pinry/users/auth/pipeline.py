from django.contrib.auth.models import Permission


def grant_permissions(backend, details, user, *args, **kwargs):
    permissions = Permission.objects.filter(codename__in=['add_pin', 'add_image'])
    user.user_permissions = permissions
    user.save()
    return locals()
