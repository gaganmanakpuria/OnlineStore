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


class AddressUsages(models.Model):
    address_usages_id = models.BigIntegerField(primary_key=True)
    associated_owner = models.ForeignKey('Persons', models.DO_NOTHING)
    owner_type_code = models.CharField(max_length=30)
    address = models.ForeignKey('Addresses', models.DO_NOTHING)
    usage_type_code = models.CharField(max_length=30)
    expired_flag = models.CharField(max_length=1)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    # class Meta:
    #     managed = True
    #     db_table = 'address_usages'


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


class AvailableLanguages(models.Model):
    language = models.CharField(primary_key=True, max_length=30)
    default_flag = models.CharField(max_length=1)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'available_languages'


class CategoryTranslations(models.Model):
    category = models.OneToOneField('ProductCategoriesBase', models.DO_NOTHING, primary_key=True)
    category_name = models.CharField(max_length=50)
    category_description = models.CharField(max_length=1000, blank=True, null=True)
    language = models.CharField(max_length=30)
    source_lang = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'category_translations'
        unique_together = (('category', 'language'),)


class CountryCodes(models.Model):
    iso_country_code = models.CharField(primary_key=True, max_length=2)
    country_name = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=30)
    source_lang = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'country_codes'
        unique_together = (('iso_country_code', 'language'),)


class CouponUsages(models.Model):
    customer = models.OneToOneField('Persons', models.DO_NOTHING, primary_key=True)
    discount = models.ForeignKey('DiscountsBase', models.DO_NOTHING)
    applied_date = models.DateTimeField()
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'coupon_usages'
        unique_together = (('customer', 'discount'),)


class CustomerIdentifications(models.Model):
    customer = models.OneToOneField('Persons', models.DO_NOTHING, primary_key=True)
    id_type_code = models.CharField(max_length=30)
    id_detail = models.CharField(max_length=20)
    additional_information = models.CharField(max_length=1000, blank=True, null=True)
    verified_flag = models.CharField(max_length=1)
    verified_date = models.DateTimeField(blank=True, null=True)
    verified_by = models.ForeignKey('Persons', models.DO_NOTHING, db_column='verified_by', blank=True, null=True,related_name='PersonsVarified')
    verification_method_code = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'customer_identifications'


class CustomerInterests(models.Model):
    customer = models.ForeignKey('Persons', models.DO_NOTHING)
    customer_interests_id = models.BigIntegerField(primary_key=True)
    category = models.ForeignKey('ProductCategoriesBase', models.DO_NOTHING)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'customer_interests'
        unique_together = (('customer', 'category'), ('customer', 'category'),)


class DemoOptions(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    value = models.CharField(max_length=120, blank=True, null=True)
    java_data_type = models.CharField(max_length=120)
    description = models.CharField(max_length=4000)

    class Meta:
        managed = True
        db_table = 'demo_options'


class DiscountTranslations(models.Model):
    discount_translations_id = models.BigIntegerField(primary_key=True)
    discount = models.ForeignKey('DiscountsBase', models.DO_NOTHING)
    description = models.CharField(max_length=4000)
    language = models.CharField(max_length=30)
    source_language = models.CharField(max_length=15)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'discount_translations'


class DiscountsBase(models.Model):
    discount_id = models.BigIntegerField(primary_key=True)
    discount_type_code = models.CharField(max_length=30)
    discount_amount = models.BigIntegerField()
    apply_as_percentage_flag = models.CharField(max_length=1)
    easy_code = models.CharField(max_length=20, blank=True, null=True)
    add_free_shipping_flag = models.CharField(max_length=1)
    onetime_discount_flag = models.CharField(max_length=1)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'discounts_base'


class EligibleDiscounts(models.Model):
    membership = models.ForeignKey('MembershipsBase', models.DO_NOTHING)
    discount = models.OneToOneField(DiscountsBase, models.DO_NOTHING, primary_key=True)
    valid_from_date = models.DateTimeField(blank=True, null=True)
    valid_to_date = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'eligible_discounts'
        unique_together = (('discount', 'membership'),)


class HelpTranslations(models.Model):
    help_translations_id = models.BigIntegerField(primary_key=True)
    help_id = models.BigIntegerField()
    help_usage = models.CharField(max_length=200)
    help_text = models.CharField(max_length=2000)
    language = models.CharField(max_length=30)
    source_language = models.CharField(max_length=15)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'help_translations'


class LookupCodes(models.Model):
    lookup_type = models.CharField(primary_key=True, max_length=30)
    lookup_code = models.CharField(max_length=30)
    meaning = models.CharField(max_length=80)
    description = models.CharField(max_length=240, blank=True, null=True)
    language = models.CharField(max_length=30)
    source_lang = models.CharField(max_length=30)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'lookup_codes'
        unique_together = (('lookup_type', 'lookup_code', 'language'),)


class MembershipTranslations(models.Model):
    membership_translations_id = models.BigIntegerField(primary_key=True)
    membership = models.ForeignKey('MembershipsBase', models.DO_NOTHING)
    membership_name = models.CharField(max_length=120)
    description = models.CharField(max_length=2000, blank=True, null=True)
    language = models.CharField(max_length=30)
    source_language = models.CharField(max_length=15)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'membership_translations'


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


class OrderItems(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING, primary_key=True)
    line_item_id = models.BigIntegerField()
    product = models.ForeignKey('ProductsBase', models.DO_NOTHING)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'order_items'
        unique_together = (('order', 'line_item_id'),)


class Orders(models.Model):
    order_id = models.BigIntegerField(primary_key=True)
    order_date = models.DateTimeField()
    order_shipped_date = models.DateTimeField(blank=True, null=True)
    order_status_code = models.CharField(max_length=30)
    order_total = models.FloatField()
    customer = models.ForeignKey('Persons', models.DO_NOTHING)
    ship_to_name = models.CharField(max_length=120, blank=True, null=True)
    ship_to_address = models.ForeignKey(Addresses, models.DO_NOTHING)
    ship_to_phone_number = models.CharField(max_length=20, blank=True, null=True)
    shipping_option = models.ForeignKey('ShippingOptionsBase', models.DO_NOTHING)
    payment_option = models.ForeignKey('PaymentOptions', models.DO_NOTHING, blank=True, null=True)
    discount = models.ForeignKey(DiscountsBase, models.DO_NOTHING, blank=True, null=True,related_name='Discount')
    coupon = models.ForeignKey(DiscountsBase, models.DO_NOTHING, blank=True, null=True, related_name='Coupon')
    free_shipping_flag = models.CharField(max_length=1)
    customer_collect_flag = models.CharField(max_length=1)
    collection_warehouse = models.ForeignKey('Warehouses', models.DO_NOTHING, blank=True, null=True)
    giftwrap_flag = models.CharField(max_length=1)
    giftwrap_message = models.CharField(max_length=2000, blank=True, null=True)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'orders'


class PaymentOptions(models.Model):
    payment_option_id = models.BigIntegerField(primary_key=True)
    customer = models.ForeignKey('Persons', models.DO_NOTHING)
    payment_type_code = models.CharField(max_length=30)
    billing_address_id = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
    account_number = models.BigIntegerField()
    card_type_code = models.CharField(max_length=30, blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    check_digits = models.SmallIntegerField(blank=True, null=True)
    routing_identifier = models.CharField(max_length=15, blank=True, null=True)
    institution_name = models.CharField(max_length=120, blank=True, null=True)
    valid_from_date = models.DateTimeField(blank=True, null=True)
    valid_to_date = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'payment_options'


# class Persons(models.Model):
#     person_id = models.BigIntegerField(primary_key=True)
#     principal_name = models.CharField(max_length=60)
#     title = models.CharField(max_length=12, blank=True, null=True)
#     first_name = models.CharField(max_length=30, blank=True, null=True)
#     last_name = models.CharField(max_length=30, blank=True, null=True)
#     person_type_code = models.CharField(max_length=30)
#     supplier = models.ForeignKey('Suppliers', models.DO_NOTHING, blank=True, null=True)
#     provisioned_flag = models.CharField(max_length=1, blank=True, null=True)
#     primary_address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)
#     registered_date = models.DateTimeField(blank=True, null=True)
#     membership = models.ForeignKey(MembershipsBase, models.DO_NOTHING, blank=True, null=True)
#     email = models.CharField(max_length=25)
#     confirmed_email = models.CharField(max_length=25, blank=True, null=True)
#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#     mobile_phone_number = models.CharField(max_length=20, blank=True, null=True)
#     credit_limit = models.FloatField(blank=True, null=True)
#     date_of_birth = models.DateTimeField(blank=True, null=True)
#     marital_status_code = models.CharField(max_length=30)
#     gender = models.CharField(max_length=1)
#     children_under_18 = models.SmallIntegerField(blank=True, null=True)
#     approximate_income = models.BigIntegerField(blank=True, null=True)
#     contact_method_code = models.CharField(max_length=30, blank=True, null=True)
#     contactable_flag = models.CharField(max_length=1)
#     contact_by_affilliates_flag = models.CharField(max_length=1)
#     created_by = models.CharField(max_length=60)
#     creation_date = models.DateTimeField()
#     last_updated_by = models.CharField(max_length=60)
#     last_update_date = models.DateTimeField()
#     object_version_id = models.BigIntegerField()

#     class Meta:
#         managed = True
#         db_table = 'persons'
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
		user.is_staff = True
		user.is_superuser = False
		user.is_active = True
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
    # person_id = models.BigIntegerField(primary_key=True,auto_created=True, serialize=False,null=False,blank=False)
    principal_name = models.CharField(max_length=60 ,blank=True, null=True)
    title = models.CharField(max_length=12, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    person_type_code = models.CharField(max_length=30,blank=True, null=True)
    # supplier = models.ForeignKey('Suppliers', models.DO_NOTHING, blank=True, null=True)
    provisioned_flag = models.CharField(max_length=1, blank=True, null=True)
    primary_address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)
    registered_date = models.DateTimeField(blank=True, null=True)
    membership = models.ForeignKey(MembershipsBase, models.DO_NOTHING, blank=True, null=True)
    email = models.EmailField(max_length=250,unique=True,db_index=True)
    confirmed_email = models.EmailField(unique=True,max_length=25, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    mobile_phone_number = models.CharField(max_length=20, blank=True, null=True,unique=True)
    credit_limit = models.FloatField(blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    marital_status_code = models.CharField(max_length=30,blank=True, null=True)
    gender = models.CharField(max_length=1,blank=True, null=True)
    children_under_18 = models.SmallIntegerField(blank=True, null=True)
    approximate_income = models.BigIntegerField(blank=True, null=True)
    contact_method_code = models.CharField(max_length=30, blank=True, null=True)
    contactable_flag = models.CharField(max_length=1,blank=True, null=True)
    contact_by_affilliates_flag = models.CharField(max_length=1,blank=True, null=True)
    created_by = models.CharField(max_length=60,blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    # last_updated_by = models.CharField(max_length=60)
    username = models.CharField(max_length=250,unique=True)
    last_update_date = models.DateTimeField( verbose_name="last login " ,auto_now=True,blank=True, null=True)
    object_version_id = models.BigIntegerField(blank=True, null=True)
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
		

    


class ProductCategoriesBase(models.Model):
    category_id = models.BigIntegerField(primary_key=True)
    parent_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    category_locked_flag = models.CharField(max_length=1)
    representative_product = models.ForeignKey('ProductsBase', models.DO_NOTHING, blank=True, null=True)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'product_categories_base'


class ProductImages(models.Model):
    product_image_id = models.BigIntegerField(primary_key=True)
    product = models.ForeignKey('ProductsBase', models.DO_NOTHING)
    default_view_flag = models.CharField(max_length=1)
    detail_image = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    image = models.BinaryField()
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'product_images'


class ProductTranslations(models.Model):
    product = models.OneToOneField('ProductsBase', models.DO_NOTHING, primary_key=True)
    language = models.CharField(max_length=30)
    source_lang = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=4000)
    additional_info = models.CharField(max_length=4000, blank=True, null=True)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'product_translations'
        unique_together = (('product', 'language'),)


class ProductsBase(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)
    parent_category_id = models.BigIntegerField(blank=True, null=True)
    category = models.ForeignKey(ProductCategoriesBase, models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=50)
    product_status = models.CharField(max_length=30)
    cost_price = models.FloatField(blank=True, null=True)
    list_price = models.FloatField()
    min_price = models.FloatField()
    warranty_period_months = models.SmallIntegerField(blank=True, null=True)
    shipping_class_code = models.CharField(max_length=30)
    external_url = models.CharField(max_length=200, blank=True, null=True)
    attribute_category = models.CharField(max_length=30, blank=True, null=True)
    attribute1 = models.CharField(max_length=150, blank=True, null=True)
    attribute2 = models.CharField(max_length=150, blank=True, null=True)
    attribute3 = models.CharField(max_length=150, blank=True, null=True)
    attribute4 = models.CharField(max_length=150, blank=True, null=True)
    attribute5 = models.CharField(max_length=150, blank=True, null=True)
    attribute6 = models.CharField(max_length=150, blank=True, null=True)
    attribute7 = models.CharField(max_length=150, blank=True, null=True)
    attribute8 = models.CharField(max_length=150, blank=True, null=True)
    attribute9 = models.CharField(max_length=150, blank=True, null=True)
    attribute10 = models.CharField(max_length=150, blank=True, null=True)
    attribute11 = models.CharField(max_length=150, blank=True, null=True)
    attribute12 = models.CharField(max_length=150, blank=True, null=True)
    attribute13 = models.CharField(max_length=150, blank=True, null=True)
    attribute14 = models.CharField(max_length=150, blank=True, null=True)
    attribute15 = models.CharField(max_length=150, blank=True, null=True)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'products_base'


class ShippingOptionTranslations(models.Model):
    shipping_translations_id = models.BigIntegerField(primary_key=True)
    shipping_option = models.ForeignKey('ShippingOptionsBase', models.DO_NOTHING)
    shipping_method = models.CharField(max_length=100)
    language = models.CharField(max_length=30)
    source_lang = models.CharField(max_length=4000)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'shipping_option_translations'


class ShippingOptionsBase(models.Model):
    shipping_option_id = models.BigIntegerField(primary_key=True)
    country_code = models.CharField(max_length=2, blank=True, null=True)
    cost_per_class1_item = models.FloatField()
    cost_per_class2_item = models.FloatField()
    cost_per_class3_item = models.FloatField()
    free_shipping_allowed_flag = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'shipping_options_base'


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


class WarehouseStockLevels(models.Model):
    product = models.OneToOneField(ProductsBase, models.DO_NOTHING, primary_key=True)
    warehouse = models.ForeignKey('Warehouses', models.DO_NOTHING)
    quantity_on_hand = models.IntegerField()
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'warehouse_stock_levels'
        unique_together = (('product', 'warehouse'),)


class Warehouses(models.Model):
    warehouse_id = models.BigIntegerField(primary_key=True)
    address = models.ForeignKey(Addresses, models.DO_NOTHING)
    warehouse_name = models.CharField(max_length=35)
    created_by = models.CharField(max_length=60)
    creation_date = models.DateTimeField()
    last_updated_by = models.CharField(max_length=60)
    last_update_date = models.DateTimeField()
    object_version_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'warehouses'

