import frappe

@frappe.whitelist(allow_guest=True)
def get_user_feed(previous=False):
    if frappe.session.user:
        zineify_user = frappe.get_doc("Zineify User", frappe.session.user)
        return zineify_user.get_feed(previous)
    else:
        # TODO: use the local cached user, create anonymouse user, with chached and pass it to cached user id
        pass