from django.db import models

# ========================
# МОДЕЛЬ ВРАЧА
# ========================
class Doctor(models.Model):
    name = models.CharField("Имя", max_length=100)
    specialty = models.CharField("Специализация", max_length=100)
    email = models.EmailField("Электронная почта", default='example@example.com')
    photo = models.ImageField("Фото", upload_to='doctors/')

    def __str__(self):
        return f"{self.name} ({self.specialty})"


# ========================
# МОДЕЛЬ УСЛУГ
# ========================
class Service(models.Model):
    title = models.CharField("Название услуги", max_length=100)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title


# ========================
# МОДЕЛЬ ОТЗЫВОВ
# ========================
class Review(models.Model):
    patient = models.CharField("Пациент", max_length=100)
    doctor = models.ForeignKey(Doctor, verbose_name="Врач", on_delete=models.CASCADE)
    text = models.TextField("Текст отзыва")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return f"{self.patient} — {self.doctor.name}"


# ========================
# МОДЕЛЬ ЗАПИСИ НА ПРИЁМ
# ========================
class Appointment(models.Model):
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Электронная почта")
    service = models.ForeignKey(Service, verbose_name="Услуга", on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, verbose_name="Врач", on_delete=models.SET_NULL, null=True)
    date = models.DateField("Дата")
    time = models.TimeField("Время")

    def __str__(self):
        return f"{self.name} — {self.service}"
