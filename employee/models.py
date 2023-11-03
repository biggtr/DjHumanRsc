from django.db import models

# Create your models here.


class Employee(models.Model):
    MALE = "M"
    FEMALE = "F"
    GenderChoices = [(MALE, "male"), (FEMALE, "female")]
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.TextField(null=True, blank=True)
    gender = models.CharField(
        choices=GenderChoices, max_length=1, default=None, null=True, blank=True
    )
    phone_number = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    birth_data = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Vacation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    comments = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.employee}'s vacation is {'approved' if self.is_approved else 'not approved'}"
