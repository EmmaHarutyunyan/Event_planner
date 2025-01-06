from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Event, Package, Booking


class PackageAdmin(admin.ModelAdmin):
    list_display = ('custom_style', 'category', 'price', 'description')
    search_fields = ('name', 'category__name', 'price')
    list_filter = ('category',)

  

    def custom_style(self, obj):
        category_class = ""
        if obj.category.name.lower() == 'wedding':
            category_class = 'invitation-category-wedding'
        elif obj.category.name.lower() == 'birthday':
            category_class = 'invitation-category-birthday'
        elif obj.category.name.lower() == 'corporate':
            category_class = 'invitation-category-corporate'

        price_class = "low" if obj.price < 100 else "medium" if obj.price <= 500 else "high"

        return mark_safe(f'''
            <div class="invitation-card {category_class}">
                <img src="{obj.image.url if obj.image else '/static/myapp/images/placeholder.png'}" class="invitation-image" alt="Image">
                <div class="invitation-header">{obj.name}</div> 
                <div class="invitation-price {price_class}">${obj.price}</div>
                <p class="invitation-description">{obj.description}</p>
                <button class="invitation-button">View Details</button>
            </div>
        ''')

    custom_style.allow_tags = True
    custom_style.short_description = 'Invitation Preview'

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Package, PackageAdmin)
admin.site.register(Booking)