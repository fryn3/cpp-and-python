from distutils.core import setup, Extension, DEBUG

sfc_module = Extension('superfastcode', sources = ['module.cpp'])

setup(name = 'superfastcode', version = '1.0',
    description = 'Python Package with superfastcode C++ Extension',
    ext_modules = [sfc_module]
    )
