#!/usr/bin/python
# module linguistics

# This module contains a class to abstract the phonetic inventory of a language. Ideally, it
# should contain a list of strings, where each string contains a representation of a phoneme
# (implemented thinking of unicode for IPA characters of X-SAMPA, but ideally, it should be
# able to work with a user generated, as long as it is not ambiguous), and a set of
# distinctive feautres, and their values for each phoneme. Among its functionalities, should
# validate the data provided for the user and, if satisfactory, create the object, it should
# verify if a string correspond to a phoneme in the inventory, if two strings corresponding
# to phonemes correspond to phonemes of the same type (for example, the inventory could
# differentiate between vowels and consonants), and, given a string of phonemes, it sould
# parse it.
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


#################
#################
##             ##
##   PHONEME   ##
##  INVENTORY  ##
##             ##
#################
#################
class PhoneticInventory:
    # This class is not only a container for the phonetic inventory of a particular
    # language, but also the logic to parse strings into the phoneme component. This is
    # because a phoneme might be represented with more than one character. The validations
    # and other controls need to be figure out as we go on.


    def __init__(self,arguments):
        # Initialize the PhoneticInventory according to the specifications on the arguments
        # dictionary.
        #
        # TODO:
        #  1. It should be able to load from a saved file.
        #  2. It should be able to be initialized not only from a spreadsheet or a saved
        #     file, but also, passing the arguments directly.

        ##############
        # SETTING UP #
        ##############
        self.initialValidation(arguments)

        if self.isDefinedBySpreedsheet(arguments):
            self.phonemeTypes = self.defineTypesFromSpreadsheet(arguments)



    def defineTypesFromSpreadsheet(self,arguments):
        # This method initializes the types from the spreadsheet specified.
        typesToReturn = {}
        phonemeTypeArguments = {}
        spreadsheetAddress = arguments[SPREADSHEET_ADDRESS_KEY]

        for phonemeTypeName in self.namesOfTypes:
            phonemeTypeDataFrame = pd.read_excel(spreadsheetAddress, \
                                                 sheet_name = phonemeTypeName)
            phonemeTypeArguments[BY_DATAFRAME_KEY] = True
            phonemeTypeArguments[DATAFRAME_KEY]    = phonemeTypeDataFrame
            phonemeTypeArguments[TYPE_NAME_KEY]    = phonemeTypeName
            typesToReturn[phonemeTypeName]         = PhonemeType(phonemeTypeArguments)

        return typesToReturn



    def initialValidation(self, arguments):
        # Performs a set of initial validations on the data provided. If no exception is
        # raised, it just finishes. It sets some of the attributes, if they are properly
        # formatted in the arguments.

        if not NUMBER_OF_TYPES_KEY in arguments.keys():
            errorString  = "The number of types shuld be specified. It is not."
            raise ValueError(errorString)

        if not TYPES_NAMES_KEY in arguments.keys():
            errorString  = "The names of the phoneme types shuld be specified. "
            errorString += "They are not."
            raise ValueError(errorString)

        self.numberOfTypes = arguments[NUMBER_OF_TYPES_KEY]
        self.namesOfTypes  = arguments[TYPES_NAMES_KEY]

        if not isinstance(self.numberOfTypes,int) or not self.numberOfTypes > 0:
            # Checks that the number of types is positive.
            errorString  = "The number of types shuld be a positive integer. It is not."
            raise ValueError(errorString)

        if not len(self.namesOfTypes) == self.numberOfTypes:
            # Checks if the number of types and the number of type names match
            errorString  = "The number of types spedified and the number of names of types "
            errorString += "specified do not match."
            raise ValueError(errorString)

        if not len(self.namesOfTypes) == len(set(self.namesOfTypes)):
            errorString  = "The names of types should not repeat. There are repetitions."
            raise ValueError(errorString)



    def isDefinedBySpreedsheet(self, arguments):
        # This is a simple method that verifies if the arguments specify if the phonetic
        # inventory to be defined by a spreadsheet input.
        if BY_SPREADSHEET_KEY not in arguments.keys():
            return False
        elif not isinstance(arguments[BY_SPREADSHEET_KEY], bool):
            errorString  = "The argument specifying if the inventory is defined by"
            errorString += " spreadsheet is not a boolean."
            raise ValueError(errorString)

        yesAndAddress = arguments[BY_SPREADSHEET_KEY] and \
                        SPREADSHEET_ADDRESS_KEY in arguments.keys()
        if yesAndAddress:
            return True
        if not arguments[BY_SPREADSHEET_KEY]:
            return False

        # If method has not returned yet, then, the arguments specify that it is defined by
        # spreadsheet, but there is no address for such.
        errorString  = "There should be an specified address for the spreadsheet. "
        errorString += "There is none."
        raise ValueError(errorString)


    def sameType(self, phoneme1, phoneme2):
        # TODO: This method is probably the only simple method in the entire file. It should
        #       just indicate if the phonemes are of the same type or not of the same type,
        #       for example, if the inventory differentiates between vowels and consonants.
        pass

    def featureArray(self, phoneme):
        # TODO: Takes a string that represents a phoneme, verifies that the phoneme is
        #       indeed part of the inventory and if it is, it returns the array of features
        #       for that phoneme.
        pass

    def parse(self,wordString):
        # TODO: This function should take a string containing a sequence of phonemes, and
        #       return a list with the phonemes, in order, divided. Pretty much it just
        #       splits. It has to implement a way to ignore spurious characters.
        pass

    def load(self, fileAddress):
        # This method would load the phonetic inventory from a file saved directly to disc.
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







###############
###############
##           ##
##  PHONEME  ##
##   TYPE    ##
##           ##
###############
###############
class PhonemeType:
    # This is a container class, where the phoneme types are stored.

    def __init__(self,arguments):
        # Initialize the Phoneme Type according to the specification on the arguments
        # dictionary.
        #
        # TODO:
        #   1. Initialize if arguments are passed directly.
        #
        self.name = arguments[TYPE_NAME_KEY]
        if self.isDefinedByDataframe(arguments):
            typeDataFrame  = arguments[DATAFRAME_KEY]
            typeFeatureDic = typeDataFrame.to_dict()
            self.phonemes  = list(typeDataFrame.axes[1])
            features_key   = self.phonemes.pop(0)
            self.features  = list(typeFeatureDic[features_key].values())
            self.featuresList     = {}
            self.numberOfPhonemes = len(self.phonemes)
            self.numberOfFeatures = len(self.features)
            for phoneme in self.phonemes:
                self.featuresList[phoneme] = list(typeFeatureDic[phoneme].values())




    def isDefinedByDataframe(self, arguments):
        # Checks if the thingy is defined by data frames, and if so, checks that the data
        # in the arguments is coherent.
        if BY_DATAFRAME_KEY not in arguments.keys():
            return False

        if not isinstance(arguments[BY_DATAFRAME_KEY], bool):
            errorString  = "The argument specifying if the type is defined by"
            errorString += " dataframe is not a boolean."
            raise ValueError(errorString)

        if not arguments[BY_DATAFRAME_KEY]:
            return False

        if DATAFRAME_KEY not in arguments.keys():
            errorString  = "The arguments specify definition by dataframe, but no dataframe"
            errorString += "is provided."
            raise ValueError(errorString)

        # If it has not returned by this point, then, all the checks are satisfied.
        return True



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



#################
#################
##             ##
##   PHONEME   ##
##  INVENTORY  ##
##             ##
#################
#################
NUMBER_OF_TYPES_KEY     = "NUMBER OF TYPES"
TYPES_NAMES_KEY         = "TYPES NAMES"
BY_SPREADSHEET_KEY      = "BY SPREADSHEET"
SPREADSHEET_ADDRESS_KEY = "SPREADSHEET ADDRESS"




###############
###############
##           ##
##  PHONEME  ##
##   TYPE    ##
##           ##
###############
###############
BY_DATAFRAME_KEY = "BY_DATAFRAME"
DATAFRAME_KEY    = "DATAFRAME"
TYPE_NAME_KEY    = "TYPE_NAME"
