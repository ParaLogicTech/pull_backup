# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

__version__ = '0.0.1'


@frappe.whitelist()
def download_backup(filename):
	from frappe.utils.response import download_backup
	return download_backup("/backups/"+filename)

