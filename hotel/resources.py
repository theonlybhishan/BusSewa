from import_export import resources
from .models import Hotels


class HotelsAdmin(resources.ModelResource):
    class meta:
        model = Hotels