from django.db import models

# Create your models here.

#Django model Field:
'''
- html widget
- Validation
- db size
'''
# Create the choice of the job part time or full time
JOB_TYPE = (
  ('Full Time','Full Time'),
  ('Part Time','Part Time'),
)
class Job(models.Model): #table
  title = models.name = models.CharField(max_length=100)  #column
  job_type = models.name = models.CharField(max_length=15,choices = JOB_TYPE
  )
  description = models.TextField(max_length=1000)
  published_at = models.DateTimeField(auto_now=True)
  vacancy = models.IntegerField(default=1)
  salary = models.IntegerField(default=0)
  experience = models.IntegerField(default=1)

  #Return the title of the job 
  def __str__(self):
      return self.title
