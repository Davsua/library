from django.db import models
import uuid
from core.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Library(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name_address

    @property
    def name_address(self) -> str:
        return f"{self.name} | {self.address}"


class Book(models.Model):
    GENRE_CHOICES = [
        ("s", "suspense"),
        ("t", "Terror"),
        ("c", "Comedy"),
        ("l", "Love"),
        ("d", "drama")
    ]
    title = models.CharField(max_length=50, null=True)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=1, null=True)
    author = models.CharField(max_length=30, null=True)
    sumary = models.CharField(max_length=120, null=True)
    book_item = models.IntegerField(null=True)
    shelf = models.IntegerField(null=True)
    uuid = models.UUIDField(default=uuid.uuid4())  # like ref (unique)
    library = models.ForeignKey(
        Library, on_delete=models.CASCADE, default="1")
    status = models.BooleanField(default=True)  # in library for defect

    def __str__(self):
        return f"{self.title} | {self.genre} | {self.library.name}"

    @property
    def name_uuid(self) -> dict:
        return {
            "number": self.number,
            "uuid": self.uuid
        }


class Booktenant(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.id} | {self.book.title} | {self.tenant.email} "


@receiver(post_save, sender=Booktenant)
def update_status_book(sender, instance, created, **kwargs):
    if created:
        book_item = instance
        book_id = book_item.book.id
        book = Book.objects.get(pk=book_id)
        # print(instance)
        # print(rack)
        book.status = False
        book.save()

# @receiver(post_delete, sender=RackItem)
# def update_status_rack(sender, instance, **kwargs):
#    rack_item = instance
#    rack_id = rack_item.rack.id
#    rack = Rack.objects.get(pk=rack_id)
#    rack.status = True
#    rack.save()
