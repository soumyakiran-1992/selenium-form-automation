from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse

def send_email_view(request):
    subject = "Python (Selenium) Assignment - Soumya Kiran Puppala"
    body = "Hi,\n\nPlease find my Python (Selenium) assignment.\n\nfind the assignments :\n\n1.	Screenshot of the form filled via code (as mentioned in STEP 3 of the assignment).
	2.	Source code (GitHub repository).-https://github.com/soumyakiran-1992/selenium-form-automation
	3.	Brief documentation of your approach.-having some experience with automation and took help of ai.
	4.	Your resume.-please find attached
	5.	Links to past projects/work samples.-worked at ncr corp and tuteehub solution
	6.	Confirm your availability to work full time (10 am to 7 pm) for the next 3-6 months.-yes i can work \n\nBest regards,\nSoumya Kiran Puppala"
    from_email = settings.EMAIL_HOST_USER
    to_emails = 'tech@themedius.ai'          
    cc_emails = 'hr@themedius.ai'            

    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=from_email,
        to=to_emails,
        cc=cc_emails
    )


    file_path = os.path.join(settings.BASE_DIR, 'assignment.zip')  
    email.attach_file("C:\Users\rakhi\Downloads\Resume.docx")

l
    email.send(fail_silently=False)

    return HttpResponse(f"✅ Email sent successfully to {to_emails[0]} with CC to {cc_emails[0]} and attachment.")


   