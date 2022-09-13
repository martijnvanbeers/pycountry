
try:
    import pkg_resources

    resource_filename = pkg_resources.resource_filename
except ImportError:

    def resource_filename(package_or_requirement, resource_name):
        return os.path.join(os.path.dirname(__file__), resource_name)

else:
    try:
        __version__ = pkg_resources.get_distribution("pycountry").version
    except pkg_resources.DistributionNotFound:
        __version__ = "n/a"


