"""
Start with your work from Exercise 9-8 (page 173). Store
the classes User, Privileges, and Admin in one module. Create a separate file,
make an Admin instance, and call show_privileges() to show that everything is
working correctly.
"""

from privileges import Admin  # import class Admin

admin = Admin("Joshua", "Hutasoit", 21, "Makan")

admin.privileges.show_privileges()  # panggil method admin yang membuat instance privilege
