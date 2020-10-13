#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pylint: disable=no-self-use, missing-docstring, invalid-name

import sys
from runbook import RunBook


# noinspection PyMethodMayBeStatic,PyShadowingNames
class MyRunBook:
    def create_ssh_key_pair(self):
        print("Run:")
        print("\tssh-keygen -t rsa -f ~/{}".format(context['username']))

    def git_commit(self):
        print("Copy ~/new_key.pub into the `user_keys` Git repository, then run these commands:")
        print("\tgit commit {}".format(context['username']))
        print("\tgit push")

    def wait_for_build(self):
        build_url = "http://example.com/builds/user_keys"
        print("Wait for the build job at {0} to finish".format(build_url))

    def retrieve_user_email(self):
        dir_url = "http://example.com/directory"
        print("Go to {0}".format(dir_url))
        print("Find the email address for user '{}'".format(context['username']))
        context['email'] = input("Paste the email address and press enter: ")

    def send_private_key(self):
        print("Go to 1Password")
        print("Paste the contents of ~/new_key into a new document")
        print("Share the document with {}".format(context['username']))


if __name__ == '__main__':
    context = dict(username=sys.argv[1])
    RunBook(MyRunBook)  # or RunBook.run(MyRunBook), either syntax will work
