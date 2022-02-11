from django import forms 
from .models import transactionsTable

class transactions(forms.ModelForm):

	class Meta:

		model = transactionsTable
		fields=  {'name_one','name_two','amount'}
