#!/usr/bin/python
# module linguistics

# This module contains a class to abstract the utilities necessary for a
# particular comparative corpus. The basic idea is that there are N different
# words that come from K different languages, but the container allows for
# missing cognates. For example, it could include the Swadesh list for all
# Romance languages, and have some missing. The class allows for quick access
# whether by the term, or by the language, or by both.
#
# Copyright (c) 2025 Universidad de Costa Rica.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   - Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#   - Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#   - Neither the name of the <organization> nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL DAVID JIMENEZ BE LIABLE FOR ANY DIRECT, DIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Researchers:
#         David Jimenez <david.jimenezlopez@ucr.ac.cr>
#         Haakon Krohn <haakonstensrud.krohn@ucr.ac.cr>

# This module contains the methods, classes and variables necessary for the
# implementation of a cognate corpus object necessary for a research project.

import pandas as pd

from math import isnan

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
    # Class that contains a corpus of a vocabulary of size N for K different
    # languages, where missing terms are allowed. It also contains some utility
    # functions for access, validation, creation, etc.

    def __init__(self,arguments):
        #
        # TODO:
        #   1.
        #
        self.initialValidation(arguments)
        if self.isDefinedBySpreedsheet(arguments):
            self.defineCorpusFromSpreadsheet(arguments)


    def initialValidation(self,arguments):
        #
        # TODO:
        #   - Other checkins could be performed.
        #
        spreadsheetDefined = (BY_SPREADSHEET_KEY in arguments.keys()) and \
                                isinstance(arguments[BY_SPREADSHEET_KEY], bool)
        if spreadsheetDefined and arguments[BY_SPREADSHEET_KEY]:
            sheetAddressNotDefined = (not SPREADSHEET_ADDRESS_KEY in\
                arguments.keys()) or (not SHEET_NAME_KEY in arguments.keys())
            if sheetAddressNotDefined:
                errorString  = "If the corpus is defined by spreadsheet, a "
                errorString += "spreadsheet address and a sheet name must be "
                errorString += "provided. At least one of them is not provided."
                raise ValueError(errorString)
        if BY_SPREADSHEET_KEY in arguments.keys():
            if not isinstance(arguments[BY_SPREADSHEET_KEY], bool):
                errorString  = "The BY_SPREADSHEET_VALUE field should be a "
                errorString += "boolean. It is not."
                raise ValueError(errorString)


    def isDefinedBySpreedsheet(self, arguments):
        #
        # TODO: Implement.
        #
        if not BY_SPREADSHEET_KEY in arguments.keys():
            return False
        else:
            return arguments[BY_SPREADSHEET_KEY]


    def defineCorpusFromSpreadsheet(self, arguments):
        #
        # TODO: Implement.
        #
        sheetAddress = arguments[SPREADSHEET_ADDRESS_KEY]
        sheetName    = arguments[SHEET_NAME_KEY]
        corpusDataFrame = pd.read_excel(sheetAddress, sheet_name = sheetName)
        corpusDict = corpusDataFrame.to_dict()
        self.languageNames = list(corpusDataFrame.axes[1])
        self.termList = list(corpusDict[self.languageNames[0]].values())
        numberOfValues = len(self.termList)
        numberOfLanguages = len(self.languageNames)
        self.languageNames.pop(0)
        self.dictionary = {}
        self.type = DICTIONARY
        for language in self.languageNames:
            tempDict = {}
            for k in range(numberOfValues):
                term = self.termList[k]
                word = corpusDict[language][k]
                isEmpty = isinstance(word,float) and isnan(word)
                if isEmpty:
                    tempDict[term] = EMPTY_WORD
                else:
                    tempDict[term] = word

            self.dictionary[language] = tempDict
        self.createCorpusList()


    def createCorpusList(self):
        self.corpus = []
        for term in self.termList:
            tempCognateList = []
            for language in self.languageNames:
                word = self.dictionary[language][term]
                if word != EMPTY_WORD:
                    tempCognateList.append(word)
            if len(tempCognateList) > 0:
                self.corpus.append(tempCognateList)


    def flattenCorpus(self):
        flattenedCorpus = []
        for termGroup in self.corpus:
            for word in termGroup:
                if word not in flattenedCorpus:
                    flattenedCorpus.append(word)
        return flattenedCorpus


    def load(self, fileAddress):
        # This method would load the phonetic inventory from a file saved
        # directly to disc.
        #
        # TODO:
        #  1. Implement
        #
        pass


    def save(self, fileAddress):
        # This method would save the phonetic inventory to a file saved directly to disc.
        #
        # TODO:
        #  1. Implement
        #
        pass



#####################
#####################
#####################
###               ###
###               ###
###   CONSTANTS   ###
###   AND KEYS    ###
###               ###
###               ###
#####################
#####################
#####################

EMPTY_WORD      = ''

#########
# TYPES #
#########
DICTIONARY = "DICTIONARY"
COGNATE_LIST = "COGNATE LIST"


BY_SPREADSHEET_KEY      = "BY SPREADSHEET"
SPREADSHEET_ADDRESS_KEY = "SPREADSHEET ADDRESS"
SHEET_NAME_KEY          = "SHEET NAME"
