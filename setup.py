from setuptools import setup


setup(
    name='cldfbench_teop',
    py_modules=['cldfbench_teop'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'teop=cldfbench_teop:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
        'pyglottolog',
        'pydictionaria>=2.1',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
