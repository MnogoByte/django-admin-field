django-admin-field
==================

Django ModelAdmin field syntax simplifier.

Common django admin field customization syntax for looks like this. ::

    class FileAdmin(ModelAdmin)
        list_display = ('name', 'human_size')

        def human_size(self, obj):
            return filesizeformat(obj.size)
        human_size.short_description = 'size'
        human_size.admin_order_field = 'size'


This lib allows allows to sorten it and make it reusable. ::


    class FileAdmin(ModelAdmin)
        list_display = ('name', 'human_size')
        human_size = AdminField('size', filesizeformat)


Inheritance
------------------
You can create some reusable fields, for multipy usage. ::

    class AdminSizeField(AdminFieldBase):
        DEFAULT_FIELD = 'size'
        method = staticmethod(human_size)


    class FileAdmin(ModelAdmin)
        list_display = ('name', 'human_size')
        human_size = AdminSizeField()

Attributes
------------------
By default, 'short description' and 'admin order field' will be taken from the
field name. But you can overide it by kwargs. ::

    class FileAdmin(ModelAdmin)
        list_display = ('name', 'human_size')
        human_size = AdminField('size', filesizeformat,
            short_description='real size', allow_tags=True)

Foreign keys
------------------
By default ModelAdmin doesn't allow you to use foreign keys in list_display.
Feel free to do it with AdminField. It will atomaticaly optain description
and sort field. ::

    class UserFileAdmin(ModelAdmin)
        list_display = ('name', 'file__size')
        file__size = AdminField('file__size', filesizeformat)

Don't forget to select related model. ::

    class UserFileAdmin(ModelAdmin)
        select_related = ['file']
        list_display = ('name', 'file__size')
        file__size = AdminField('file__size', filesizeformat)

        def queryset(self, request):
            return super(AdminModelSelectRelated, self).queryset(request).select_related(*self.select_related)
