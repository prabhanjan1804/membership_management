from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from members.models import Member
from datetime import timedelta

class Command(BaseCommand):
    help = 'Send reminder emails to members whose membership expires in 15 days'

    def handle(self, *args, **kwargs):
        target_date = timezone.now().date() + timedelta(days=15)
        members = Member.objects.filter(membership_expiry=target_date)

        for member in members:
            send_mail(
                subject='Deine Mitgliedschaft läuft bald ab!',
                message=(
                    f'Hallo {member.name},\n\n'
                    f'Deine Mitgliedschaft bei der Studentischen Selbstverwaltung endet am {member.membership_expiry}.\n'
                    f'Wenn du weiterhin Mitglied bleiben möchtest, fülle bitte das Formular zur passiven Verlängerung aus:\n\n'
                    f'http://127.0.0.1:8000/renew/\n\n'
                    f'Beste Grüße,\n'
                    f'Ihr Vorstand'
                ),
                from_email='noreply@stusta.de',
                recipient_list=[member.email],
                fail_silently=False,
            )

        self.stdout.write(f"Reminder emails sent to {members.count()} members.")