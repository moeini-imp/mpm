from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random

class UserAvatar(models.Model):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    DoB = models.DateField()
    avatar = models.CharField(max_length=100, default=None)
    avatar_image = models.ForeignKey(UserAvatar, on_delete=models.PROTECT, blank=True, null=True)
    money = models.IntegerField(default=1000)
    happines=models.IntegerField(default=0)
    exp=models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def buy_item(self, item_price,happines):
        if self.money >= item_price:
            self.money -= item_price
            self.happines+=happines
            self.save()
            return True
        return False

    def update_money_based_on_event(self, event):
        if event.event_type == 'in':
            self.money += event.price
        elif event.event_type == 'out':
            self.money -= event.price

    def add_loan(self,loan):
        self.money+=loan.value
    

    def store_bought_item_data(self, item_title, item_price):
        BoughtItem.objects.create(user=self, title=item_title, price=item_price)


class Events(models.Model):
    CHOICES = (
        ("in", "Income"),
        ("out", "Outcome")
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    event_type = models.CharField(choices=CHOICES, max_length=30)

    def __str__(self):
        return self.title

class CashFlow(models.Model):
    CHOICES = (
        ("in", "Income"),
        ("out", "Outcome")
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    flow_type = models.CharField(choices=CHOICES, max_length=10)
    title = models.CharField(max_length=100)
    value=models.IntegerField()
    flow_trails = models.ForeignKey(Events, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class ShopEntity(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="shopEntity/")
    description = models.TextField()
    price = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    time_available = models.DateTimeField()
    quantity=models.IntegerField(default=1)
    happiness=models.IntegerField()

    def __str__(self):
        return self.title


class BoughtItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title



class JobChallanges(models.Model):
    title=models.CharField(max_length=100)
    descriptions=models.TextField()
    hardness=models.IntegerField()
    image=models.ImageField(upload_to="JobImage/")
    income=models.IntegerField()
    estimated_time=models.IntegerField()
    challange=models.TextField()
    answers=models.TextField()


    def __str__(self):
        return self.title
    

class Loan(models.Model):
    CHOICES=(
        ('bill','bill'),
        ('wallet','wallet')
        )
    value=models.IntegerField()
    repay_time=models.IntegerField()
    interests=models.IntegerField()
    insurance=models.CharField(choices=CHOICES, max_length=50)



@receiver(pre_save, sender=Loan)
def set_loan_conditions(sender, instance, **kwargs):
    instance.value = random.randint(10,1000)
    instance.repay_time = random.randint(1, 3)
    instance.interests=random.randint(1,20) 


