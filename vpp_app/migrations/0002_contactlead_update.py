# Generated manually to support ContactLead model updates
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vpp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactlead',
            name='organization',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Công ty / Trường học'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactlead',
            name='customer_type',
            field=models.CharField(choices=[('retail', 'Khách mua lẻ'), ('business', 'Mua cho Doanh nghiệp / Trường học'), ('agency', 'Đăng ký làm đại lý')], default='business', max_length=50, verbose_name='Anh/chị đang là'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactlead',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Ngày gửi'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactlead',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contactlead',
            name='request_type',
            field=models.CharField(choices=[('agency_signup', 'Đăng ký đại lý'), ('wholesale_quote', 'Nhận báo giá mua sỉ'), ('quality_feedback', 'Góp ý chất lượng')], max_length=50, verbose_name='Loại yêu cầu'),
        ),
    ]
