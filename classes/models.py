from django.db import models
from django.db.models import Avg
from django.utils.text import slugify
from categories.models import SubCategory
from users.models import CustomUser


def media_upload_path(instance, filename):
    if isinstance(instance, classImages):
        instance = instance.of_class
    return f"{instance.teacher.username}/classes/{instance.title}/{filename}"


class Class(models.Model):
    category = models.ForeignKey(
        SubCategory, related_name="classes", on_delete=models.RESTRICT
    )
    teacher = models.ForeignKey(
        CustomUser,
        related_name="classes",
        on_delete=models.CASCADE,
        limit_choices_to={"is_teacher": True},
    )
    title = models.CharField(max_length=25)
    description = models.TextField()
    slug = models.SlugField(max_length=25)
    basic_price = models.PositiveSmallIntegerField()
    video = models.FileField(upload_to=media_upload_path, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["teacher", "title"]
        verbose_name = "class"
        verbose_name_plural = "classes"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Class, self).save(*args, **kwargs)

    def average_rating(self):
        avg = self.ratings.aggregate(Avg("value")).get("value__avg")
        if avg is not None:
            return round(avg)
        return avg


class ClassRating(models.Model):
    class Values(models.IntegerChoices):
        AWFUL = 0
        BAD = 25
        AVERAGE = 50
        GOOD = 75
        AMAZING = 100

    rated_class = models.ForeignKey(
        Class, related_name="ratings", on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        CustomUser,
        related_name="ratings",
        limit_choices_to={"is_teacher": False},
        on_delete=models.SET_NULL,
        null=True,
    )
    value = models.PositiveSmallIntegerField(choices=Values.choices)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rated_class.title}: {self.value}, by {self.author.username}"


class classImages(models.Model):
    of_class = models.ForeignKey(Class, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(null=True, max_length=25, upload_to=media_upload_path)


class ClassSession(models.Model):
    from_class = models.ForeignKey(
        Class, related_name="sessions", on_delete=models.PROTECT
    )
    student = models.ForeignKey(
        CustomUser,
        related_name="sessions",
        on_delete=models.PROTECT,
        limit_choices_to={"is_teacher": False},
    )
    class_duration = models.PositiveSmallIntegerField()
    appointed_time = models.DateTimeField()
    paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True)
    price_paid = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.from_class}: {self.appointed_time}"
