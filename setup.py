from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()


# https://pypi.org/project/mkdocs-resize-images/
setup(
    name='mkdocs-resize-images',
    version='1.0.0',
    description='MkDocs plugin to resize images according to the configuration.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords='mkdocs plugin, resize images, mkdocs, plugin, images, resize',
    url='https://github.com/JakubAndrysek/mkdocs-resize-images',
    author='Jakub Andrýsek',
    author_email='email@kubaandrysek.cz',
    license='MIT',
    python_requires='>=3.7',
    install_requires=['mkdocs', 'Pillow'],
	extras_require={
		'dev': [
			'mkdocs-material',
			'mkdocs-open-in-new-tab',
			'mkdocs-glightbox',
			'mkdocs-git-revision-date-localized-plugin',
		]
	},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.plugins': [
			'resize-images = resize_images.plugin:ResizeImagesPlugin'
        ]
    },
)
