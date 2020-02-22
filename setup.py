import setuptools
from os import path

pkg_name = "raphael_schema_test"

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(path.join(path.abspath(path.dirname(__file__)), pkg_name, 'meta.py')) as f:
    exec(f.read())

setuptools.setup(
    name=pkg_name,
    version=__version__,
    author="Raphael Guzman",
    author_email="raphael.h.guzman@gmail.com",
    description="Official DataJoint Test Schema plugin.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guzman-raphael/djpyplugin_schema_test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=['setuptools_certificate'],
    install_requires=['datajoint'],
    privkey_path='~/keys/datajoint-dev.pem',
    entry_points={
        'datajoint_plugins.schema': [
            'hub = {}.hub_schema:target'.format(pkg_name),
        ],
    },
)
