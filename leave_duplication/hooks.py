app_name = "leave_duplication"
app_title = "Leave Duplication"
app_publisher = "Mohammed Nasser"
app_description = "Make Duplicated Leave on Same Day"
app_email = "nasser@nasserx.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/leave_duplication/css/leave_duplication.css"
# app_include_js = "/assets/leave_duplication/js/leave_duplication.js"

# include js, css files in header of web template
# web_include_css = "/assets/leave_duplication/css/leave_duplication.css"
# web_include_js = "/assets/leave_duplication/js/leave_duplication.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "leave_duplication/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "leave_duplication.utils.jinja_methods",
# 	"filters": "leave_duplication.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "leave_duplication.install.before_install"
# after_install = "leave_duplication.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "leave_duplication.uninstall.before_uninstall"
# after_uninstall = "leave_duplication.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "leave_duplication.utils.before_app_install"
# after_app_install = "leave_duplication.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "leave_duplication.utils.before_app_uninstall"
# after_app_uninstall = "leave_duplication.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "leave_duplication.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"leave_duplication.tasks.all"
# 	],
# 	"daily": [
# 		"leave_duplication.tasks.daily"
# 	],
# 	"hourly": [
# 		"leave_duplication.tasks.hourly"
# 	],
# 	"weekly": [
# 		"leave_duplication.tasks.weekly"
# 	],
# 	"monthly": [
# 		"leave_duplication.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "leave_duplication.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "leave_duplication.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "leave_duplication.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["leave_duplication.utils.before_request"]
# after_request = ["leave_duplication.utils.after_request"]

# Job Events
# ----------
# before_job = ["leave_duplication.utils.before_job"]
# after_job = ["leave_duplication.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"leave_duplication.auth.validate"
# ]
