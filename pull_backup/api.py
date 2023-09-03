import frappe


@frappe.whitelist()
def download_backup(filename):
	from frappe.utils.response import download_backup
	return download_backup("/backups/"+filename)
