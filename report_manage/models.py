from django.db import models

# Create your models here.
from django.utils import timezone

STATISTIC_STATUS_CHOICE = (
    (0, '未知'),
    (1, '未统计'),
    (2, '已统计'),
)


class AbsErrorReportModel(models.Model):
    """
    错误基类
    """
    fatal_exception = models.IntegerField('FATAL EXCEPTION', null=False, blank=False, default=0)
    tombstone = models.IntegerField('Tombstone', null=False, blank=False, default=0)
    vm_exitin = models.IntegerField('Tombstone', null=False, blank=False, default=0)
    shutting_down_vm = models.IntegerField('Shutting down VM', null=False, blank=False, default=0)
    activity_pause_timeout = models.IntegerField(
        'Activity pause timeout', null=False, blank=False, default=0, help_text='Activity pause timeout')
    app_not_response = models.IntegerField(
        'Application is not responding', null=False, blank=False, default=0, help_text='Application is not responding')
    null_pointer_exception = models.IntegerField(
        'NullPointerException', null=False, blank=False, default=0, help_text='NullPointerException'
    )
    illegal_state_exception = models.IntegerField(
        'IllegalStateException', null=False, blank=False, default=0, help_text='IllegalStateException'
    )
    format_exception = models.IntegerField(
        'FormatException', null=False, blank=False, default=0, help_text='FormatException'
    )
    not_found_exception = models.IntegerField(
        'NotFoundException', null=False, blank=False, default=0, help_text='NotFoundException'
    )
    init_before_start_services = models.IntegerField(
        'InitBeforeStartServices', null=False, blank=False, default=0, help_text='InitBeforeStartServices'
    )
    out_of_memory = models.IntegerField(
        'outOfMemory', null=False, blank=False, default=0, help_text='outOfMemory'
    )
    anr_in = models.IntegerField(
        'ANR in', null=False, blank=False, default=0, help_text='ANR in'
    )
    exit_zygote = models.IntegerField(
        'Exit zygote', null=False, blank=False, default=0, help_text='Exit zygote'
    )
    sv_gpio_probe_start = models.IntegerField(
        'sv_gpio_probe start', null=False, blank=False, default=0, help_text='sv_gpio_probe start'
    )
    kernel_panic = models.IntegerField(
        'Kernel panic', null=False, blank=False, default=0, help_text='Kernel panic'
    )
    kernel_bug = models.IntegerField(
        'kernel BUG at', null=False, blank=False, default=0, help_text='kernel BUG at'
    )
    causing_watchdog_bite = models.IntegerField(
        'Causing a watchdog bite', null=False, blank=False, default=0, help_text='Causing a watchdog bite'
    )
    waring = models.IntegerField(
        'WARNING', null=False, blank=False, default=0, help_text='WARNING'
    )

    class Meta:
        abstract = True


class AbsReportModel(models.Model):
    user_id = models.IntegerField('用户ID', null=False, blank=False, default=0)
    test_type_code = models.CharField('测试类型编码', max_length=64, null=False, default='')
    device_code = models.CharField('设备编码', max_length=64, default='')
    test_version_code = models.CharField('测试版本编码', max_length=64, null=False, default='')
    create_time = models.DateTimeField('记录创建时间', default=timezone.now)

    class Meta:
        abstract = True


class TestTypeModel(models.Model):
    """
    测试类型
    """
    name = models.CharField('测试类型名称', max_length=64, null=False, default='')
    code = models.CharField('测试类型编码', max_length=64, null=False, default='')

    class Meta:
        db_table = 'test_type'
        ordering = ['-id']
        permissions = ()


class TestVersionModel(models.Model):
    """
    测试版本
    """
    name = models.CharField('测试版本名称', max_length=64, null=False, default='')
    code = models.CharField('测试版本code', max_length=64, null=False, default='')

    class Meta:
        db_table = 'test_version'
        permissions = ()


class TestDeviceCodeModel(models.Model):
    """
    测试设备编码
    """
    name = models.CharField('测试设备名称', max_length=64, null=False, default='')
    code = models.CharField('测试设备code', max_length=64, null=False, default='')

    class Meta:
        db_table = 'test_device'
        permissions = ()


class OriginReportErrorModel(AbsErrorReportModel):
    class Meta:
        db_table = 'origin_error_report'
        permissions = ()
        ordering = ['-id']


class OriginReportModel(AbsReportModel):
    """
    原始表
    """
    statistics_status = models.IntegerField('统计状态', choices=STATISTIC_STATUS_CHOICE, default=0)
    test_start_time = models.DateTimeField('测试执行开始时间', default=timezone.now)
    test_end_time = models.DateTimeField('测试执行完成时间', default=timezone.now)
    origin_report_id = models.IntegerField('原始表记录ID', null=False, default=0)

    class Meta:
        db_table = 'origin_report'
        permissions = ()
        ordering = ['-id']


#
#
# class AbsReportModel(models.Model):
#     user_id = models.IntegerField(
#         '用户id', null=False, blank=False, default=0, help_text='默认0， admin代表未知')
#     code = models.CharField('保留字段', max_length=32, null=False, default='', help_text='保留字段')
#     type_id = models.IntegerField('测试类型', default=0)
#     # type = models.IntegerField('报告类型', choices=REPORT_TYPE_CHOICE, default=0)
#     create_time = models.DateTimeField('创建时间', default=timezone.now, help_text='落库时间，不是统计时间')
#     start_time = models.DateTimeField(
#         '开始时间', default=timezone.now, help_text='测试脚本开始执行时间，该时间作为统计时间')
#
#     fatal_exception = models.IntegerField('FATAL EXCEPTION', null=False, blank=False, default=0)
#     tombstone = models.IntegerField('Tombstone', null=False, blank=False, default=0)
#     vm_exitin = models.IntegerField('Tombstone', null=False, blank=False, default=0)
#     shutting_down_vm = models.IntegerField('Shutting down VM', null=False, blank=False, default=0)
#     activity_pause_timeout = models.IntegerField(
#         'Activity pause timeout', null=False, blank=False, default=0, help_text='Activity pause timeout')
#     app_not_response = models.IntegerField(
#         'Application is not responding', null=False, blank=False, default=0, help_text='Application is not responding')
#     null_pointer_exception = models.IntegerField(
#         'NullPointerException', null=False, blank=False, default=0, help_text='NullPointerException'
#     )
#     illegal_state_exception = models.IntegerField(
#         'IllegalStateException', null=False, blank=False, default=0, help_text='IllegalStateException'
#     )
#     format_exception = models.IntegerField(
#         'FormatException', null=False, blank=False, default=0, help_text='FormatException'
#     )
#     not_found_exception = models.IntegerField(
#         'NotFoundException', null=False, blank=False, default=0, help_text='NotFoundException'
#     )
#     init_before_start_services = models.IntegerField(
#         'InitBeforeStartServices', null=False, blank=False, default=0, help_text='InitBeforeStartServices'
#     )
#     out_of_memory = models.IntegerField(
#         'outOfMemory', null=False, blank=False, default=0, help_text='outOfMemory'
#     )
#     anr_in = models.IntegerField(
#         'ANR in', null=False, blank=False, default=0, help_text='ANR in'
#     )
#     exit_zygote = models.IntegerField(
#         'Exit zygote', null=False, blank=False, default=0, help_text='Exit zygote'
#     )
#     sv_gpio_probe_start = models.IntegerField(
#         'sv_gpio_probe start', null=False, blank=False, default=0, help_text='sv_gpio_probe start'
#     )
#     kernel_panic = models.IntegerField(
#         'Kernel panic', null=False, blank=False, default=0, help_text='Kernel panic'
#     )
#     kernel_bug = models.IntegerField(
#         'kernel BUG at', null=False, blank=False, default=0, help_text='kernel BUG at'
#     )
#     causing_watchdog_bite = models.IntegerField(
#         'Causing a watchdog bite', null=False, blank=False, default=0, help_text='Causing a watchdog bite'
#     )
#     waring = models.IntegerField(
#         'WARNING', null=False, blank=False, default=0, help_text='WARNING'
#     )
#
#     class Meta:
#         abstract = True
#
#
# class ReportOriginModel(AbsReportModel):
#     is_active = models.BooleanField('是否有效', default=True, help_text='是否有效')
#     status = models.IntegerField(
#         '状态', choices=REPORT_STATUS_CHOICE, default=0, help_text='统计状态')
#     time_type = models.IntegerField('时间类型', choices=TIME_TYPE_CHOICE, default=1)
#
#     class Meta:
#         db_table = 'origin_report'
#         permissions = ()
#         ordering = ['-start_time']
#         verbose_name = '原始报告'
#         verbose_name_plural = verbose_name
#
#
# class LatestReportModel(AbsReportModel):
#     is_active = models.BooleanField('是否有效', default=True, help_text='是否有效')
#     status = models.IntegerField(
#         '状态', choices=REPORT_STATUS_CHOICE, default=0, help_text='统计状态')
#     time_type = models.IntegerField('时间类型', choices=TIME_TYPE_CHOICE, default=1)
#
#     class Meta:
#         db_table = 'latest_report'
#         permissions = ()
#         ordering = ['-create_time']
#         verbose_name = '最新的报告'
#         verbose_name_plural = verbose_name
#
#
# class DayReportModel(AbsReportModel):
#     is_active = models.BooleanField('是否有效', default=True, help_text='是否有效')
#     status = models.IntegerField(
#         '状态', choices=REPORT_STATUS_CHOICE, default=0, help_text='统计状态')
#
#     class Meta:
#         db_table = 'day_report'
#         permissions = ()
#         ordering = ['-create_time']
#         verbose_name = '日报告'
#         verbose_name_plural = verbose_name
#
#
# class MonthReportModel(AbsReportModel):
#
#     class Meta:
#         db_table = 'month_report'
#         permissions = ()
#         ordering = ['-create_time']
#         verbose_name = '月报告'
#         verbose_name_plural = verbose_name
#
#
# class YearReportModel(AbsReportModel):
#
#     class Meta:
#         db_table = 'year_report'
#         permissions = ()
#         ordering = ['-create_time']
#         verbose_name = '年报告'
#         verbose_name_plural = verbose_name