from django.db import models


class Contact(models.Model):
	Username = models.CharField(max_length=30)
	Password = models.CharField(max_length=30)
	

        

	role=(('Guest',"Guest"),
		('Admin',"Admin"))
	UserType=models.CharField(max_length=10,choices=role,default="user")
        
    
    
      

	

	
	
	

	
		


	
