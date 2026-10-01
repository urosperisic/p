from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ("id",)
        db_table = "author"

    def __str__(self):
        return self.name


class BookQuerySet(models.QuerySet):
    def available(self):
        return self.filter(is_available=True)

    def by_author(self, author_name):
        return self.filter(author__name=author_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    published_year = models.IntegerField()
    is_available = models.BooleanField(default=True)

    objects = BookQuerySet.as_manager()

    class Meta:
        ordering = ("id",)
        db_table = "book"

    def __str__(self):
        return self.title
