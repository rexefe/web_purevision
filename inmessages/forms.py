from django.forms import ModelForm
from .models import InHouseProposal

# Create the form class.
class InHouseProposalForm(ModelForm):
    class Meta:
        model = InHouseProposal
        fields = '__all__'