# Copyright (c) 2022, Kamal Johnson and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ZineifyUser(Document):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.i = 0

	def get_feed(self, previous=False):
		if not self.i:
			self.i = 0

		self.i+=1
		zine = frappe.get_all("Zine", pluck="name")[self.i%2]
		self.current_zine = zine
		return self.current_zine
