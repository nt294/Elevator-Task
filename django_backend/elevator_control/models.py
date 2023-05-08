from django.db import models


class Floor(models.Model):
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f'Floor {self.number}'


class Elevator(models.Model):
    DIRECTION_CHOICES = [
        ('UP', 'Up'),
        ('DOWN', 'Down'),
        ('IDLE', 'Idle'),
    ]

    number = models.IntegerField(unique=True)

    current_floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='current_elevators')
    target_floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='target_elevators', null=True,
                                     blank=True)
    direction = models.CharField(max_length=4, choices=DIRECTION_CHOICES, default='IDLE')
    serviced_floors = models.ManyToManyField(Floor, related_name='serviced_elevators')

    def __str__(self):
        return f'Elevator {self.number} serving floors {self.serviced_floors.all()}'


class ControlPanel(models.Model):
    location_floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='control_panels')

    def __str__(self):
        return f'Control panel on floor {self.location_floor.number}'
