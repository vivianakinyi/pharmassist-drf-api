from django.db import models

class RxTerm(models.Model):
	rxcui = models.CharField (max_length=8, null=False)
	generic_rxcui = models.CharField (max_length=8, blank=True)
	tty = models.CharField (max_length=20, blank=False)
	full_name = models.CharField (max_length=3000, blank=False)
	rxn_dose_form = models.CharField (max_length=100, blank=False)
	full_generic_name = models.CharField (max_length=3000, blank=False)
	brand_name = models.CharField (max_length=500, blank=True)
	display_name = models.CharField (max_length=3000, blank=False)
	route = models.CharField (max_length=100, blank=False)
	new_dose_form = models.CharField (max_length=100, blank=False)
	strength = models.CharField (max_length=500, blank=False)
	suppress_for = models.CharField (max_length=30, blank=True)
	display_name_synonym = models.CharField (max_length=500, blank=True)
	is_retired = models.CharField (max_length=8, blank=True)
	sxdg_rxcui = models.CharField (max_length=8, blank=True)
	sxdg_tty = models.CharField (max_length=20, blank=True)
	sxdg_name = models.CharField (max_length=3000, blank=True)
	psn = models.CharField (max_length=3000, blank=True)

	def __str__(self):
		return "{0} : {1}".format(self.tty, self.display_name)










	# RXCUI             	varchar(8) NOT NULL,
 #   GENERIC_RXCUI     	varchar(8),
 #   TTY               	varchar (20) NOT NULL,
 #   FULL_NAME         	varchar (3000) NOT NULL,
 #   RXN_DOSE_FORM     	varchar (100) NOT NULL,
 #   FULL_GENERIC_NAME 	varchar (3000) NOT NULL,
 #   BRAND_NAME        	varchar (500),
 #   DISPLAY_NAME      	varchar (3000) NOT NULL,
 #   ROUTE	     	varchar (100) NOT NULL,
 #   NEW_DOSE_FORM     	varchar (100) NOT NULL,
 #   STRENGTH	     	varchar (500) NOT NULL,
 #   SUPPRESS_FOR	     	varchar (30),
 #   DISPLAY_NAME_SYNONYM varchar (500),
 #   IS_RETIRED		varchar (8), 
 #   SXDG_RXCUI           varchar (8),
 #   SXDG_TTY             varchar (20),
 #   SXDG_NAME		varchar	(3000),   
 #   PSN			varchar (3000)

