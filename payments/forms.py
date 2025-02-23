# payments/forms.py
from django import forms
from .models import Payment, Student
from django.core.validators import MinValueValidator
from django.utils.safestring import mark_safe

class PaymentForm(forms.ModelForm):
    amount = forms.DecimalField(
        label="Amount (₹)",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(1)],
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.01',
            'min': '1',
            'placeholder': 'Enter amount to pay'
        })
    )

    class Meta:
        model = Payment
        fields = ['amount']  # Other fields handled programmatically

    def __init__(self, *args, **kwargs):
        self.student = kwargs.pop('student', None)
        super().__init__(*args, **kwargs)
        
        if self.student:
            self.fields['amount'].widget.attrs['max'] = float(self.student.due_fee)
            self.fields['amount'].help_text = mark_safe(
                f"<small class='text-muted'>Maximum payable amount: ₹{self.student.due_fee}</small>"
            )

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if self.student:
            if amount > self.student.due_fee:
                raise forms.ValidationError(
                    f"Amount cannot exceed due fee of ₹{self.student.due_fee}"
                )
            if amount <= 0:
                raise forms.ValidationError(
                    "Payment amount must be greater than zero"
                )
        return amount

class StudentSearchForm(forms.Form):
    roll_number = forms.CharField(
        label="Search Student",
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Roll Number'
        })
    )