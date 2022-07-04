from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


CLIENT_TYPE_CHOICE = (
    ('Client', 'Client'),
    ('Farmer', 'Farmer'),
    ('Input Partner', 'Input Partner'),
    ('AFEXBroker', 'AFEXBroker'),
    ('Broker', 'Broker'),
    ('Dealer', 'Broker'),
    ('Affiliate', 'Affiliate'),
    ('Broker-Dealer', 'Broker-Dealer'),
    ('Promoter', 'Promoter'),
    ('Investor', 'Investor'),
)


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Client(BaseModel):
    cid = models.CharField(max_length=60, unique=True, db_index=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(
        max_length=300, null=True, blank=True, default="")
    client_type = models.CharField(
        choices=CLIENT_TYPE_CHOICE, max_length=300, null=True, blank=True, default="")
    country_code = models.CharField(
        max_length=30, blank=True, null=True, default="")
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=50, null=True, blank=True, default="")
    created_by = models.ForeignKey(
        to=User, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['cid']

    def __str__(self):
        return self.cid

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class ClientWallet(BaseModel):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    total_balance = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    available_balance = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    lien_balance = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.cid} - {self.available_balance}"

    @property
    def cid(self):
        return self.client.cid
