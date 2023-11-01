# How to release a new version

* `<full_name>` is e.g., `sphinx_documatt_theme`
* `<short_name>` is e.g., `documatt`

## Part 1: Git release

On the `main` branch:

1. Increment the version in the `<full_name>/setup.py`.
2. Describe what's new in in the `docs/themes/<short_name>.rst`, in Changelog section.
3. Create a commit with the message `chore(<short_name>): release <version>`.
4. Tag the commit with `git tag -a <short_name>:<version>`.
4. `git push origin HEAD`.

## Part 2: PyPI release

1. If no errors so far, build with `tox -e build_<short_name>` that creates sdist and wheel in `<full_name>/dist/`.
2. Upload to TestPyPI with `tox -e publish_<short_name>` and go to `https://test.pypi.org/project/<full_name>/<version>/`.
3. If you are happy with it, upload to PyPI with `tox -e publish_<short_name> -- --repository pypi`.