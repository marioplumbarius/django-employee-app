from django.db import models

class AbstractBaseModel(models.Model):
    """
        AbstractBaseModel contains common fields between models.

        All models should extend this class.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Department(AbstractBaseModel):
    """
        Department represents the sector a set of employees belongs to.
    """

    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class Employee(AbstractBaseModel):
    """
        Employee represents the people from a given department.
    """

    name = models.CharField(max_length=250, db_index=True)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
