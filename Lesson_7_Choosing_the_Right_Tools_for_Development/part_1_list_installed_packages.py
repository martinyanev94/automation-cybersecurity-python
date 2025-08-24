# Run this in PyCharm's Python console to check installed packages.
import pkg_resources
installed_packages = pkg_resources.working_set
package_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
for package in package_list:
    print(package)
