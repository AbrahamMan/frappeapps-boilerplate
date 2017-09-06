# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappeapps_boilerplate"
app_title = "FrappeApps Boilerplate"
app_publisher = "Frappe Technologies Pvt. Ltd."
app_description = "This is a boilerplate for Frappe Apps. Let's dive into development, and do contribute with some awesome apps."
app_icon = "octicon octicon-file-directoryocticon octicon-file-directory"
app_color = "grey"
app_email = "hello@aaimaa.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappeapps_boilerplate/css/frappeapps_boilerplate.css"
# app_include_js = "/assets/frappeapps_boilerplate/js/frappeapps_boilerplate.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappeapps_boilerplate/css/frappeapps_boilerplate.css"
# web_include_js = "/assets/frappeapps_boilerplate/js/frappeapps_boilerplate.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "frappeapps_boilerplate.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappeapps_boilerplate.install.before_install"
# after_install = "frappeapps_boilerplate.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappeapps_boilerplate.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappeapps_boilerplate.tasks.all"
# 	],
# 	"daily": [
# 		"frappeapps_boilerplate.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappeapps_boilerplate.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappeapps_boilerplate.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappeapps_boilerplate.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappeapps_boilerplate.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappeapps_boilerplate.event.get_events"
# }

