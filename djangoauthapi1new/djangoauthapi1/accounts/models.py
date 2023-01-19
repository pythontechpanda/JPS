# from django.db import models
# from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

# #  Custom User Manager
# class UserManager(BaseUserManager):
#   def create_user(self, email, name, tc, password=None, password2=None):
#       """
#       Creates and saves a User with the given email, name, tc and password.
#       """
#       if not email:
#           raise ValueError('User must have an email address')

#       user = self.model(
#           email=self.normalize_email(email),
#           name=name,
#           tc=tc,
#       )

#       user.set_password(password)
#       user.save(using=self._db)
#       return user

#   def create_superuser(self, email, name, tc, password=None):
#       """
#       Creates and saves a superuser with the given email, name, tc and password.
#       """
#       user = self.create_user(
#           email,
#           password=password,
#           name=name,
#           tc=tc,
#       )
#       user.is_admin = True
#       user.save(using=self._db)
#       return user

# #  Custom User Model
# class User(AbstractBaseUser):
#   email = models.EmailField(
#       verbose_name='Email',
#       max_length=255,
#       unique=True,
#   )
#   name = models.CharField(max_length=200)
#   tc = models.BooleanField()
#   is_active = models.BooleanField(default=True)
#   is_admin = models.BooleanField(default=False)
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)

#   objects = UserManager()

#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['name', 'tc']

#   def __str__(self):
#       return self.email

#   def has_perm(self, perm, obj=None):
#       "Does the user have a specific permission?"
#       # Simplest possible answer: Yes, always
#       return self.is_admin

#   def has_module_perms(self, app_label):
#       "Does the user have permissions to view the app `app_label`?"
#       # Simplest possible answer: Yes, always
#       return True

#   @property
#   def is_staff(self):
#       "Is the user a member of staff?"
#       # Simplest possible answer: All admins are staff
#       return self.is_admin


# New...............


from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User
#  Custom User Manager


class UserManager(BaseUserManager):
    def create_user(self, company, email, username, name, tc, note, gprname, seque, menugroup1, menugroup2, menugroup3, menugroup4, is_published, password=None, password2=None):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not username:
            raise ValueError('User must have an Username')

        user = self.model(
            username=self.normalize_email(username),
            name=name,
            # usertype=usertype,
            company=company,
            tc=tc,
            email=email,
            note=note,
            gprname=gprname,
            seque=seque,
            is_published=is_published,
            menugroup1=menugroup1,
            menugroup2=menugroup2,
            menugroup3=menugroup3,
            menugroup4=menugroup4,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, company, tc, note, gprname, seque, menugroup1, menugroup2, menugroup3, menugroup4, is_published, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            password=password,
            username=username,
            name=name,
            # usertype=usertype,
            company=company,
            tc=tc,
            email=email,
            note=note,
            gprname=gprname,
            seque=seque,
            is_published=is_published,
            menugroup1=menugroup1,
            menugroup2=menugroup2,
            menugroup3=menugroup3,
            menugroup4=menugroup4,
            **extra_fields,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#  Custom User Model


class UserType(models.Model):
    ADMINISSTRATOR = 1
    NORMAL_USER = 2
    CUSTOMER = 3
    VENDOR = 4
    TYPE_CHOICES = (

        (ADMINISSTRATOR, 'Administrator'),
        (NORMAL_USER, 'normal_user'),
        (CUSTOMER, 'Customer'),
        (VENDOR, 'Vendor')
    )

    id = models.PositiveBigIntegerField(choices=TYPE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    menugroup1 = models.CharField(max_length=100)
    menugroup2 = models.CharField(max_length=100)
    menugroup3 = models.CharField(max_length=100)
    menugroup4 = models.CharField(max_length=100)
    tc = models.BooleanField()
    note = models.CharField(max_length=100)
    gprname = models.CharField(max_length=100)
    seque = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_customer = models.BooleanField(default=True)
    is_vendor = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    usertype = models.ForeignKey(UserType,on_delete=models.CASCADE,default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'company', 'tc', 'note', 'gprname', 'seque',
                       'is_published', 'menugroup1', 'menugroup2', 'menugroup3', 'menugroup4']

    def __str__(self):
        # return self.get_username
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=34)


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gst = models.CharField(max_length=34)


class MenuGroupCategory(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=255)
    grpname = models.CharField(max_length=80)
    sequence = models.CharField(max_length=40)
    inactive = models.BooleanField()
    note = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class MenuGroup(models.Model):
    # menugroupcategory = models.ForeignKey(MenuGroupCategory, on_delete=models.CASCADE)
    grpname = models.CharField(max_length=120)
    sequence = models.CharField(max_length=100)
    inactive = models.BooleanField()
    note = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.grpname


class MenuMaster(models.Model):
    groupname = models.ForeignKey(MenuGroup, on_delete=models.CASCADE)
    menuname = models.CharField(max_length=20)
    taskname = models.CharField(max_length=20)

    def __str__(self):
        return self.menuname


class TaskMaster(models.Model):
    task = models.ForeignKey(MenuMaster, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    pyname = models.CharField(max_length=30)
    inactivetask = models.BooleanField()
    notetask = models.CharField(max_length=50)
    lastupdateuser = models.ForeignKey(User, on_delete=models.CASCADE)
    lastupdatedate = models.DateField(auto_now=True)
    lastupdatetime = models.TimeField(auto_now=True)
    lastupdatetask = models.CharField(max_length=50)
    lastupdateip = models.CharField(max_length=20)

    def __str__(self):
        return self.description

    # @property
    # def ipadd(self):
    #     lastip=socket.gethostbyname(socket.gethostname())
    #     self.lastupdateip=lastip
    #     return lastip

# class UserTaskAccess(models.Model):
#     usercompany=models.ForeignKey(User,on_delete=models.CASCADE)
#     useracc=models.ForeignKey(User,on_delete=models.CASCADE)
#     taskacc=models.ForeignKey(MenuMaster,on_delete=models.CASCADE)
#     inactivetaskacc=models.BooleanField()
#     notetaskacc=models.CharField(max_length=50)
#     viewaccess=models.BooleanField()
#     addaccess=models.BooleanField()
#     editaccess=models.BooleanField()
#     deleteaccess=models.BooleanField()
#     inactiveaccess=models.BooleanField()
#     lastupdateuseracc=models.CharField(max_length=50)
#     lastupdatedateacc=models.DateField(auto_now=True)
#     lastupdatetimeacc=models.TimeField(auto_now=True)
#     lastupdatetaskacc=models.CharField(max_length=50)
#     lastupdateipacc=models.CharField(max_length=20)

class Company(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserTaskAccess(models.Model):
    companyss=models.ForeignKey(Company,on_delete=models.CASCADE,blank = True, null = True)
    # useracc = models.ForeignKey(User, on_delete=models.CASCADE)
    taskacc = models.ForeignKey(MenuMaster, on_delete=models.CASCADE)
    inactivetaskacc = models.BooleanField()
    notetaskacc = models.CharField(max_length=50)
    viewaccess = models.BooleanField()
    addaccess = models.BooleanField()
    editaccess = models.BooleanField()
    deleteaccess = models.BooleanField()
    inactiveaccess = models.BooleanField()
    lastupdateuseracc = models.CharField(max_length=50)
    lastupdatedateacc = models.DateField(auto_now=True)
    lastupdatetimeacc = models.TimeField(auto_now=True)
    lastupdatetaskacc = models.CharField(max_length=50)
    lastupdateipacc = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.notetaskacc


class FieldMaster(models.Model):
    fieldmas = models.CharField(max_length=50)
    placeholdermsg = models.CharField(max_length=100)
    errormsg = models.CharField(max_length=100)
    inactivefield = models.BooleanField()
    notefield = models.CharField(max_length=50)
    lastupdateuserfield = models.CharField(max_length=50)
    lastupdatedatefield = models.DateField(auto_now=True)
    lastupdatetimefield = models.TimeField(auto_now=True)
    lastupdatetaskfield = models.CharField(max_length=50)
    lastupdateipfield = models.CharField(max_length=120)
    
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    
    def __str__(self):
        return self.fieldmas

# class TaskFieldMaster(models.Model):
#     companytaskfield=models.ForeignKey(User,on_delete=models.CASCADE)
#     usertaskfield=models.ForeignKey(User,on_delete=models.CASCADE)
#     tasktaskfield=models.ForeignKey(MenuMaster,on_delete=models.CASCADE)
#     fieldtaskfield=models.ForeignKey(FieldMaster,on_delete=models.CASCADE)
#     restricted=models.BooleanField()
#     inactivetaskfield=models.BooleanField()
#     notetaskfield=models.CharField(max_length=50)
#     lastupdateuseracc=models.CharField(max_length=50)
#     lastupdatedateacc=models.DateField(auto_now=True)
#     lastupdatetimeacc=models.TimeField(auto_now=True)
#     lastupdatetaskacc=models.CharField(max_length=50)
#     lastupdateipacc=models.CharField(max_length=20)


class TaskFieldMaster(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,default=False)
    usertaskfield = models.ForeignKey(User, on_delete=models.CASCADE)
    tasktaskfield = models.ForeignKey(MenuMaster, on_delete=models.CASCADE)
    fieldtaskfield = models.ForeignKey(FieldMaster, on_delete=models.CASCADE)
    restricted = models.BooleanField()
    inactivetaskfield = models.BooleanField()
    notetaskfield = models.CharField(max_length=50)
    lastupdateusertaskfield = models.CharField(max_length=50)
    lastupdatedatetaskfield = models.DateField(auto_now=True)
    lastupdatetimetaskfield = models.TimeField(auto_now=True)
    lastupdatetasktaskfield = models.CharField(max_length=50)
    lastupdateiptaskfield = models.CharField(max_length=20)



    def __str__(self):
        return self.notetaskfield


# Here new mosdel here  .....

class Category(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Field_Master(models.Model):
#     STATUS = (
#         ('active', 'active'),
#         ('inactive', 'inactive'),
#     )
#     f_name = models.CharField(max_length=100)
#     f_msg1 = models.TextField()
#     f_msg2 = models.TextField()
#     f_note = models.TextField()
#     status = models.CharField(max_length=100, choices=STATUS)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, blank=True, null=True)

#     def __str__(self):
#         return self.f_name


class Todo(models.Model):
    
    STATUS_CHOICES = (
        ('draft', 'Save Draft'), 
        ('published', 'Published')
        )
    f_name = models.CharField(max_length=100)
    f_msg1 = models.TextField()
    f_msg2 = models.TextField()
    f_note = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    task = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.f_name







