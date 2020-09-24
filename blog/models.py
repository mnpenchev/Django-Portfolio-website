from django.db import models

# Create a Blog modules. V
# title V
# publication date V
# body V
# image V
# add the blog app to the setting. V
# create migration V
# migrate V
# add to the admin


class Blog(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:305]

    def pub_date_pretty(self):
        return self.publication_date.strftime('%e %b %Y')

    def __str__(self):
        return self.title
