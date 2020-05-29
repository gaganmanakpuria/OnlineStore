# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# for custom user
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.base_user import BaseUserManager





class Addresses(models.Model):
    address_id = models.BigIntegerField(primary_key=True)
    address1 = models.CharField(max_length=40)
    address2 = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=12, blank=True, null=True)
    state_province = models.CharField(max_length=40)
    country_id = models.CharField(max_length=2)
    longitude = models.BigIntegerField(blank=True, null=True)
    latitude = models.BigIntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'addresses'




class MembershipsBase(models.Model):
    membership_id = models.BigIntegerField(primary_key=True)
    membership_type_code = models.CharField(max_length=30)
    contact_id = models.BigIntegerField()
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'memberships_base'



class PersonsManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


	def create_staffuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_staff = False
		user.is_superuser = False
		user.is_active = False
		user.save(using=self._db)
		return user
	def create_activeuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_active = True
		user.is_staff = False
		user.is_superuser = False
		user.save(using=self._db)
		return user
class Persons(AbstractBaseUser):
    # person_id = models.AutoField(primary_key=True,null=False,editable=False)
    # principal_name = models.CharField(max_length=60 ,blank=True, null=True)
    # title = models.CharField(max_length=12, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    # person_type_code = models.CharField(max_length=30,blank=True, null=True)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING, blank=True, null=True)
    # provisioned_flag = models.CharField(max_length=1, blank=True, null=True)
    primary_address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)
    registered_date = models.DateTimeField(blank=True, null=True)
    membership = models.ForeignKey(MembershipsBase, models.DO_NOTHING, blank=True, null=True)
    email = models.EmailField(max_length=250,unique=True,db_index=True)
    # confirmed_email = models.EmailField(unique=True,max_length=25, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    mobile_phone_number = models.CharField(max_length=20, blank=True, null=True,unique=True)
    credit_limit = models.FloatField(blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    marital_status_code = models.CharField(max_length=30,blank=True, null=True)
    gender = models.CharField(max_length=1,blank=True, null=True)
    # children_under_18 = models.SmallIntegerField(blank=True, null=True)
    approximate_income = models.BigIntegerField(blank=True, null=True)
    # contact_method_code = models.CharField(max_length=30, blank=True, null=True)
    # contactable_flag = models.CharField(max_length=1,blank=True, null=True)
    # contact_by_affilliates_flag = models.CharField(max_length=1,blank=True, null=True)
    # created_by = models.CharField(max_length=60,blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True)
    # last_updated_by = models.CharField(max_length=60)
    username = models.CharField(max_length=250,unique=True)
    last_update_date = models.DateTimeField( verbose_name="last login " ,auto_now=True,blank=True, null=True)
    # object_version_id = models.BigIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    objects = PersonsManager()
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True
		

    




class Suppliers(models.Model):
    supplier_id = models.BigIntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=120)
    supplier_status = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    ui_skin = models.CharField(max_length=60, blank=True, null=True)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'suppliers'


class statussupliers(models.Model):
    status=models.CharField(max_length=250)
