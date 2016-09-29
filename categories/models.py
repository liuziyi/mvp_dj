from django.core.urlresolvers import reverse 
from django.db import models
from django.utils.text import slugify 

class Category(models.Model):
	title = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(unique=True)
	active = models.BooleanField()

	class Meta:
		verbose_name_plural = "categories"

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("category_detail", kwargs={"slug": self.slug})

def image_upload_to(instance, filename):
	title = instance.category.title 
	slug = slugify(title)
	return "categories/%s/%s" % (slug, filename)

class CategoryImage(models.Model):
	category = models.ForeignKey(Category)
	image = models.ImageField(upload_to=image_upload_to)

	def __unicode__(self):
		return self.category.title
