#!/usr/bin/env python
# encoding: utf-8
# Thomas Nagy 2009-2010 (ita)

"""
Detect the Clang++ C++ compiler
"""

import os, sys
from waflib.Tools import ccroot, ar, gxx
from waflib.Configure import conf

@conf
def find_clangxx(conf):
	"""
	Find the program clang++, and execute it to ensure it really is clang++
	"""
	cxx = conf.find_program('clang++', var='CXX')
	conf.get_cc_version(cxx, clang=True)
	conf.env.CXX_NAME = 'clang'

def configure(conf):
	conf.find_clangxx()
	conf.find_ar()
	conf.gxx_common_flags()
	conf.gxx_modifier_platform()
	conf.cxx_load_tools()
	conf.cxx_add_flags()
	conf.link_add_flags()
