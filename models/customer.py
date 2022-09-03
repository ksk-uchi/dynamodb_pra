from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class CustomerModel(Model):
    class Meta:
        table_name = "customer"
        host = "http://localhost:8000"
    company_name = UnicodeAttribute(hash_key=True)
    email = UnicodeAttribute(range_key=True)
    name = UnicodeAttribute(null=True)
    age = UnicodeAttribute(null=True)
