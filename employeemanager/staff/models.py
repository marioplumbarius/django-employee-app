from django.db import models

class BaseModel(models.Model):
    """
        BaseModel contains common fields between models.

        All models should extend this class.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Department(BaseModel):
    """
        Department represents the sector a set of employees belongs to.
    """

    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class Employee(BaseModel):
    """
        Employee represents the people from a given department.
    """

    name = models.CharField(max_length=250, db_index=True)
    email = models.EmailField(db_index=True, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name