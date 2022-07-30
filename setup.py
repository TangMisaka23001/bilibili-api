import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf8") as f:
    requires = f.read()

setuptools.setup(
    name='bilibili-api-python',
    version='11.8.1',
    license='GPLv3+',
    author='MoyuScript, Nemo2011',
    description='原 bilibili-api。哔哩哔哩的各种 API 调用便捷整合（视频、动态、直播等），另外附加一些常用的功能。',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["tests"]),
    keywords=[
        "bilibili",
        "api",
        "spider"
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: Chinese (Simplified)",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9", 
        "Programming Language :: Python :: 3.10"
    ],
    package_data={
        "": [
            "data/**/*.*",
            "requirements.txt",
            "data/*.*", 
            "html/*.*"
        ]
    },
    install_requires=requires.splitlines(),
    url="https://github.com/nemo2011/bilibili-api",
    python_requires=">=3.8"
)
