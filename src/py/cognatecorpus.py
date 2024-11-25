#!/usr/bin/python
# module linguistics

# This module contains a class to abstract the utilities necessary for a particular
# comparative corpus. The basic idea is that there are N different words that come from K
# different languages, but the container allows for missing cognates. For example, it could
# include the Swadesh list for all Romance languages, and have some missing. The class
# allows for quick access whether by the term, or by the language, or by both.
#
# Copyright (c) 2025 Universidad de Costa Rica.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#   - Redistributions of source code must retain the above copyright notice, this list of
#     conditions and the following disclaimer.
#   - Redistributions in binary form must reproduce the above copyright notice, this list
#     of conditions and the following disclaimer in the documentation and/or other materials
#     provided with the distribution.
#   - Neither the name of the <organization> nor the names of its contributors may be used
#     to endorse or promote products derived from this software without specific prior
#     written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# DAVID JIMENEZ BE LIABLE FOR ANY DIRECT, DIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Researchers:
#         David Jimenez <david.jimenezlopez@ucr.ac.cr>
#         Haakon Krohn <haakonstensrud.krohn@ucr.ac.cr>

# This module contains the methods, classes and variables necessary for the
# implementation of a phonetic system necessary for a research project.

import pandas as pd

###################
###################
###################
###             ###
###             ###
###   CLASSES   ###
###             ###
###             ###
###################
###################
###################


###############
###############
##           ##
##  COGNATE  ##
##  CORPUS   ##
##           ##
###############
###############
class CognateCorpus:
    # Class that contains a corpus of a vocabulary of size N for K different languages,
    # where missing terms are allowed. It also contains some utility functions for access,
    # validation, creation, etc.

    def __init__(self,arguments):
        self.initialValidation(arguments)
        if self.isDefinedBySpreedsheet(arguments):
            self.defineCorpusFromSpreadsheet(arguments)


    def defineCorpusFromSpreadsheet(self, arguments):
        # It makes the respective initialization of the corpus object.
        #
        # TODO: Implement.
        #
        pass

    def isDefinedBySpreedsheet(self, arguments):
        # This returns true if the arguments specify that the corpus is defined by a
        # spreadsheet.
        #
        # TODO: Implement.
        #
        booleanToReturn = True
        return booleanToReturn

    def initialValidation(self,arguments):
        # It performs an initial validation of the arguments provided. The arguments
        # correspond to a dictionary that specify certain options.
        #
        # TODO: Implement.
        #
        pass
