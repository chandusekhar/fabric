# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-09 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabric', '0004_auto_20190320_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabricipaddress',
            name='description',
            field=models.CharField(blank=True, help_text=b'A short description of the IP address', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='portinterface',
            name='name',
            field=models.CharField(help_text=b'The unique name of the fabric switch port', max_length=256),
        ),
        migrations.AlterField(
            model_name='switch',
            name='driver',
            field=models.CharField(default=b'ofdpa3', help_text=b'The driver used by the SDN controller', max_length=256),
        ),
        migrations.AlterField(
            model_name='switch',
            name='name',
            field=models.CharField(help_text=b'The unique name of the fabric switch', max_length=256),
        ),
        migrations.AlterField(
            model_name='switchport',
            name='admin_state',
            field=models.CharField(blank=True, choices=[(b'enabled', b'enabled'), (b'disabled', b'disabled')], default=b'enabled', help_text=b'desired administrative state of port', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='switchport',
            name='oper_status',
            field=models.CharField(blank=True, choices=[(b'enabled', b'enabled'), (b'disabled', b'disabled')], help_text=b'operational status of port', max_length=32, null=True),
        ),
    ]