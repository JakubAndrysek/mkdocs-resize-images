# MkDocs Resize Images Plugin

<p align="center">
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FJakubAndrysek%2Fmkdocs-resize-images&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=true"/></a>
<img src="https://img.shields.io/github/license/JakubAndrysek/mkdocs-resize-images?style=flat-square">
<img src="https://img.shields.io/github/v/release/JakubAndrysek/mkdocs-resize-images?style=flat-square">
<img src="https://img.shields.io/github/stars/JakubAndrysek/mkdocs-resize-images?style=flat-square">
<img src="https://img.shields.io/github/forks/JakubAndrysek/mkdocs-resize-images?style=flat-square">
<img src="https://img.shields.io/github/issues/JakubAndrysek/mkdocs-resize-images?style=flat-square">
<img src="https://static.pepy.tech/personalized-badge/mkdocs-resize-images?period=month&units=international_system&left_color=black&right_color=orange&left_text=Downloads">
</p>

This MkDocs plugin finds all folders with a certain name, by default `assets-large`, resizes all images in those folders according to the plugin configuration.
Then saves the resized images in a different folder, by default `assets`. 
The plugin also supports caching: if a file has not changed since the last time the plugin ran, it won't be processed again.

## Installation

Install the plugin using pip from [PyPI](https://pypi.org/project/mkdocs-resize-images/):

```bash
pip install mkdocs-resize-images
```

Activate the plugin in `mkdocs.yml`:

```yaml
plugins:
  - search
  - resize-images
```

Create `.gitignore` file in your project root directory and add the following line to it:

```bash
assets-large # or whatever you have set as source-dir

.resize-hash # if you have enabled caching
```


## Usage

By default, the plugin will look for images in all directories named assets-large, resize them to 800x600 pixels, and then save the resized images in assets directories in the same parent directories as the assets-large directories.

You can configure the plugin in your mkdocs.yml:

```yaml
plugins:
  - search
  - resize-images:
      source-dir: assets-large
      target-dir: assets
      enable_cache: True
      size: [800, 600]
      extensions: ['.jpg', '.jpeg', '.png', '.gif', '.svg']
```

`source-dir`: The name of the directories to search for images to resize. Default is `assets-large`.

`target-dir`: The name of the directories to save the resized images in. Default is `assets`.

`size`: The size to resize the images to, specified as [width, height]. Default is `[800, 600]`.

`extensions`: List of image file extensions to consider for resizing. The plugin will look for images with these extensions in both lower and upper case. Default is `['.jpg', '.jpeg', '.png', '.gif', '.svg']`.

`enable_cache`: Whether to enable caching. If enabled, the plugin will check if a file has changed since the last time the plugin ran, and if not, it won't process the file again. Default is `True`.