=====
Usage
=====


To develop on commonutilslib:

.. code-block:: bash

    # The following commands require pipenv as a dependency

    # To lint the project
    _CI/scripts/lint.py

    # To execute the testing
    _CI/scripts/test.py

    # To create a graph of the package and dependency tree
    _CI/scripts/graph.py

    # To build a package of the project under the directory "dist/"
    _CI/scripts/build.py

    # To see the package version
    _CI/scipts/tag.py

    # To bump semantic versioning [--major|--minor|--patch]
    _CI/scipts/tag.py --major|--minor|--patch

    # To upload the project to a pypi repo if user and password are properly provided
    _CI/scripts/upload.py

    # To build the documentation of the project
    _CI/scripts/document.py


To use commonutilslib in a project:

Working with Pushd:

.. code-block:: python

    from commonutilslib import Pushd

    import os
    with Pushd(some_path) as pushd:
        print(f'Doing things in {os.getcwd()} coming from {pushd.original_dir} and then returning back')

Working with tempdir:

.. code-block:: python

    from commonutilslib import tempdir

    import os
    with tempdir():
        print(f'Doing things in temporary directory {os.getcwd()} and deleting after done')

Working with Hasher:

.. code-block:: python

    from commonutilslib import Hasher

    hasher = Hasher()
    print(hasher.hash_file(some_file_name))
    print(hasher.hash_directory(some_directory_name))
