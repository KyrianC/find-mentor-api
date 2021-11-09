from django.db import models
from django.utils.text import slugify


def category_thumbnail_path(instance, filename):
    ext = filename.split(".")[-1]
    if isinstance(instance, SubCategory):
        filename = instance.slug + "." + ext
        return f"categories/thumbnail/{instance.parent_category.title}/{filename}"
    filename = "index." + ext
    return f"categories/thumbnail/{instance.title}/{filename}"


class AbstractCategory(models.Model):
    title = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255)
    thumbnail = models.ImageField(null=True, upload_to=category_thumbnail_path)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(AbstractCategory, self).save(*args, **kwargs)


class Category(AbstractCategory):
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return f"Category('{self.title}')"


class SubCategory(AbstractCategory):
    parent_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="sub_categories",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "sub category"
        verbose_name_plural = "sub categories"

    def __str__(self):
        return f"SubCategory('{self.title}' in '{self.parent_category.title}')"
