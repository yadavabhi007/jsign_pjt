from django.db import models
from jsignature.fields import JSignatureField


class Signature(models.Model):
    signature = JSignatureField()
