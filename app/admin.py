from django.contrib import admin
from app.models import Post,MRAPP,file_log,Document

admin.site.register(Post)

'''class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')
    search_fields = ('name',)


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')
    list_filter = ('is_spicy',)
    ordering = ('-price',)
    fields = ('price', 'restaurant')'''


admin.site.register(MRAPP)

admin.site.register(Document)

class file_logAdmin(admin.ModelAdmin):
    list_display = ('fname', 'user','MRAPP','inp_time', 'out_time','com_time','status')

admin.site.register(file_log , file_logAdmin)
