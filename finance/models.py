from django.conf import settings
from django.db import models

class Account(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	owner = models.ManyToManyField(
		'Person'
		)

	SAVINGS = 'SV'
	CHEQUE = 'CQ'
	CREDIT = 'CR'
	LOAN = 'LN'

	type_choices = [
		(SAVINGS, 'Savings'),
		(CHEQUE, 'Cheque'),
		(CREDIT, 'Credit'),
		(LOAN, 'Loan'),
		]

	type = models.CharField(
		max_length=2,
		choices = type_choices,
		default = CHEQUE
		)

	def __str__(self):
		return '%s %s' % (self.id,self.name)

class Transaction(models.Model):
	account = models.ForeignKey(Account, on_delete=models.PROTECT)

	CREDIT = 'CR'
	DEBIT = 'DR'

	type_choices = [
		(CREDIT, 'Credit'),
		(DEBIT, 'Debit')
		]

	type = models.CharField(
		max_length=2,
		choices=type_choices,
		)

	timeOccur = models.DateTimeField()

	def __str__(self):
		return self.id


class Person(models.Model):
	firstName = models.CharField(max_length=50)
	otherName1 = models.CharField(max_length=50,blank=True) 
	otherName2 = models.CharField(max_length=50,blank=True)
	otherName3 = models.CharField(max_length=50,blank=True)
	surname = models.CharField(max_length=50)

	def __str__(self):
		return "%s %s" % (self.firstName, self.surname)

