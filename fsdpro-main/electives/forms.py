from django import forms

class TestForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for q in questions:
            self.fields[f"q_{q.id}"] = forms.ChoiceField(
                label=q.text,
                choices=[
                    (q.option1, q.option1),
                    (q.option2, q.option2),
                    (q.option3, q.option3),
                    (q.option4, q.option4),
                ],
                widget=forms.RadioSelect
            )