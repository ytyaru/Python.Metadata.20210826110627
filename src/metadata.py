#!/usr/bin/env python3
# coding: utf8
import os, sys, csv, json, datetime, locale
from string import Template
from collections import namedtuple
class Metadata:
    @classmethod
    def call(cls):
        locale.setlocale(locale.LC_ALL, '')
        cmds = []
        cmds.append(['metadata'])
        cmds.append(['url','author','since','copyright','license','description','features','notes'])

