from django.db import models

# Create a Blog modules. V
# title V
# publication date V
# body V
# image V


class Blog(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# add the blog app to the setting. V

# create migration V

# migrate V

# add to the admin
