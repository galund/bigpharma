"""
bigpharma models.
"""
from django.db.models import fields

from opal import models

class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Antimicrobial(models.Antimicrobial): pass
class Investigation(models.Investigation): pass
