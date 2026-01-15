from django.contrib import admin
from .models import Doctor, Service, Review, Appointment

# ===== DOCTOR =====
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'email', 'photo')  # все нужные поля
    search_fields = ('name', 'specialty')  # поиск по имени и специализации

# ===== SERVICE =====
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)

# ===== REVIEW =====
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'created_at')
    search_fields = ('patient', 'doctor__name')

# ===== APPOINTMENT =====
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'service', 'doctor', 'date', 'time')
    search_fields = ('name', 'doctor__name', 'service__title')
    list_filter = ('date', 'doctor')
