# from django.contrib import admin
# from accounts.models import User
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# class UserModelAdmin(BaseUserAdmin):
#   # The fields to be used in displaying the User model.
#   # These override the definitions on the base UserModelAdmin
#   # that reference specific fields on auth.User.
#   list_display = ('id', 'email', 'name', 'tc', 'is_admin')
#   list_filter = ('is_admin',)
#   fieldsets = (
#       ('User Credentials', {'fields': ('email', 'password')}),
#       ('Personal info', {'fields': ('name', 'tc')}),
#       ('Permissions', {'fields': ('is_admin',)}),
#   )
#   # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
#   # overrides get_fieldsets to use this attribute when creating a user.
#   add_fieldsets = (
#       (None, {
#           'classes': ('wide',),
#           'fields': ('email', 'name', 'tc', 'password1', 'password2'),
#       }),
#   )
#   search_fields = ('email',)
#   ordering = ('email', 'id')
#   filter_horizontal = ()


# # Now register the new UserModelAdmin...
# admin.site.register(User, UserModelAdmin)


from django.contrib import admin
from accounts.models import User, Customer, Vendor, UserType, MenuGroupCategory,Category,Company
from accounts.models import MenuGroup, MenuMaster, TaskMaster, UserTaskAccess, FieldMaster, TaskFieldMaster

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','usertype','company','username','email','name',
                     'tc', 'note', 'is_published', 'gprname', 'seque', 'is_admin', 'is_staff', 'menugroup1', 'menugroup2', 'menugroup3', 'menugroup4')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('username', 'password')}),
        ('Personal info', {
         'fields': ('name', 'company', 'note', 'is_published', 'tc', 'gprname', 'seque')}),
        ('Permissions', {'fields': ('is_admin', 'is_customer', 'is_vendor')}),
    )
    list_editable = ('is_published', 'menugroup1',
                     'menugroup2', 'menugroup3', 'menugroup4',)
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('usertype','company','name','username','email', 'password1', 'password2','tc', 'note', 'is_published', 'gprname', 'seque', 'menugroup1', 'menugroup2', 'menugroup3', 'menugroup4'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
admin.site.register(MenuGroup)
admin.site.register(MenuMaster)
admin.site.register(TaskMaster)
admin.site.register(UserTaskAccess)
admin.site.register(FieldMaster)
admin.site.register(TaskFieldMaster)
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(MenuGroupCategory)
admin.site.register(UserType)
# admin.site.register(Field_Master)
admin.site.register(Category)
admin.site.register(Company)
