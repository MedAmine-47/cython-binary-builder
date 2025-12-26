import os
from setuptools import setup, Extension
from Cython.Build import cythonize

target_arch = os.environ.get("CPU_ARCH") or "x86-64"

extensions = [
    Extension(
        "myScript",
        sources=["myScript.py"],
        extra_compile_args=["-O3", f"-march={target_arch}", "-fvisibility=hidden"],
        extra_link_args=["-s"],
    )
]

setup(
    ext_modules=cythonize(
        extensions,
        compiler_directives={
            'language_level': "3",
            'boundscheck': True,
            'wraparound': True,
            'nonecheck': True,
            'embedsignature': False,
            'emit_code_comments': False,
        }
    )
)
