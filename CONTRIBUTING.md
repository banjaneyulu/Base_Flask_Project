# How to contribute

I like to encourage you to contribute to the repository.

This should be as easy as possible for you but there are a few things
to consider when contributing.  The following guidelines for
contribution should be followed if you want to submit a pull request.

## How to prepare

* You need a [GitHub account](https://github.com/signup/free)
* Submit an [issue ticket](https://github.com/banjaneyulu/Base_Flask_Project/issues)
  for your issue if there is no issue raised yet.
	* Describe the issue and include steps to reproduce if it's a bug.
	* Ensure to mention the earliest version that you know is affected.
* If you can and want to fix this, fork the repository on GitHub

## Make Changes

* In your forked repository, create a topic branch for your upcoming
  patch. (e.g. `feature/new-backend` or `bug/issue_01`)
	* Usually this is based on the `master` branch.
	* Create a branch based on master `git branch bug/issue_01`
      then checkout the new branch with `git checkout bug/issue_01`.
      Please avoid working directly on the `master` branch.
* Make commits of logical units and describe them properly.
* Make sure you stick to [PEP8](https://www.python.org/dev/peps/pep-0008/)
  coding style that is used already.
* If possible, submit tests to your patch / new feature so it can be tested easily.
* Assure nothing is broken by running all the tests.
* Add a meaningful entry to the `CHANGELOG.md` document.

## Submit Changes

* Push your changes to a topic branch in your fork of the repository.
* Open a pull request to the original repository and choose the right
  original branch you want to patch.
* If not done in commit messages (which you really should do) please
  reference and update your issue with the code changes. But _please
  do not close the issue yourself_.

# Additional Resources

* [General GitHub documentation](http://help.github.com/)
* [GitHub pull request documentation](http://help.github.com/send-pull-requests/)
* [Read the Issue Guidelines by @necolas](https://github.com/necolas/issue-guidelines/blob/master/CONTRIBUTING.md)
  for more details

