
from mailjet_rest import Client
import os
from django.conf import settings




def mail_to_helpdesk(employee):
    mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_API_SECRET), version='v3.1')
    data = {
      'Messages': [
    		{
    			"From": {
    				"Email": "hofmanneil@yahoo.com",
    				"Name": "hofmanneil"
    			},
    			"To": [
    				{
    					"Email": "hofmanneil04+helpdesk@gmail.com",
    					"Name": "passenger 1"
    				}
    			],
    			"TemplateID": 1056232,
    			"TemplateLanguage": True,
    			"Subject": "New Employee ",
    			"Variables": {
        "employee_name": employee.firstname + ' ' + employee.lastname
      }
    		}
    	]
    }
    result = mailjet.send.create(data=data)
    print (result.status_code)
    print (result.json())

def mail_to_hr(employee):
    mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_API_SECRET), version='v3.1')
    data = {
      'Messages': [
    		{
    			"From": {
    				"Email": "hofmanneil@yahoo.com",
    				"Name": "Helpdesk"
    			},
    			"To": [
    				{
    					"Email": "hofmanneil04+human_resources@gmail.com",
    					"Name": "Human Resources"
    				}
    			],
    			"TemplateID": 1059088,
    			"TemplateLanguage": True,
    			"Subject": "Assigned Hardware",
    			"Variables": {
        "employee_name": employee.firstname + ' ' + employee.lastname
      }
    		}
    	]
    }
    result = mailjet.send.create(data=data)
    print (result.status_code)
    print (result.json())

def mail_to_employee(employee):
    mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_API_SECRET), version='v3.1')
    data = {
      'Messages': [
    		{
    			"From": {
    				"Email": "hofmanneil@yahoo.com",
    				"Name": "Helpdesk"
    			},
    			"To": [
    				{
    					"Email": "hofmanneil04+employee@gmail.com",
    					"Name": "Helpdesk"
    				}
    			],
    			"TemplateID": 1059138,
    			"TemplateLanguage": True,
    			"Subject": "Assigned Hardware",
    			"Variables": {
        "employee_name": "",
        "employee_username": ""
      }
    		}
    	]
    }
    result = mailjet.send.create(data=data)
    print (result.status_code)
    print (result.json())
