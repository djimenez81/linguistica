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




class PhoneticInventory:
    # This class is not only a container for the phonetic inventory of a particular
    # language, but also the logic to parse strings into the phoneme component. This is
    # because a phoneme might be represented with more than one character. The validations
    # and other controls need to be figure out as we go on.


    def __init__(self,arguments):
        # TODO: This initiator actually has a lot of logic inside. It should somehow
        #       receive the sourceFileName, open the file, read it, validate if it is
        #       consistent (if it would allow parsing to be done), and then set up the
        #       information inside the object. For the most part, we will follow the logic
        #       from the chibcha.py project. The settingsDic is a dictionary object
        #       containing quite a few settings for the creation of this object.


        ###############
        #  ATTRIBUTE  #
        # DEFINITIONS #
        ###############
        self.LOG = [] # Here we will store messages that could help to find problems

        # These arguments are just placeholders
        self.NUMBER_OF_TYPES_KEY     = "NUMBER OF TYPES"
        self.TYPES_NAMES_KEY         = "TYPES NAMES"
        self.BY_SPREADSHEET_KEY      = "BY SPREADSHEET"
        self.SPREADSHEET_ADDRESS_KEY = "SPREADSHEET ADDRESS"

        ##############
        # SETTING UP #
        ##############
        self.initialValidation(arguments)

        if self.isDefinedBySpreedsheet(arguments):
            self.phonemeTypes = self.defineTypesFromSpreadsheet(arguments)



    def defineTypesFromSpreadsheet(self,arguments):
        # This method initializes the types from the spreadsheet specified.

        # TODO:
        #   1. Validate that the argument dictionary contents are consistent.
        #   2. That the file can be opened.  Catch the exception if needed.
        #   3. Open the sheets and send them to the PhonemeType class.


        return True



    def initialValidation(self, arguments):
        # Performs a set of initial validations on the data provided. If no exception is
        # raised, it returns True. It sets some of the attributes, if they are properly
        # formatted in the arguments.

        if not self.NUMBER_OF_TYPES_KEY in arguments.keys():
            errorString  = "The number of types shuld be specified. It is not."
            self.LOG.append(errorString)
            raise ValueError(errorString)

        if not self.TYPES_NAMES_KEY in arguments.keys():
            errorString  = "The names of the phoneme types shuld be specified. "
            errorString += "They are not."
            self.LOG.append(errorString)
            raise ValueError(errorString)

        self.numberOfTypes = arguments[self.NUMBER_OF_TYPES_KEY]
        self.namesOfTypes  = arguments[self.TYPES_NAMES_KEY]

        if not isinstance(self.numberOfTypes,int) or not self.numberOfTypes > 0:
            # Checks that the number of types is positive.
            errorString  = "The number of types shuld be a positive integer. It is not."
            self.LOG.append(errorString)
            raise ValueError(errorString)

        if not len(self.namesOfTypes) == self.numberOfTypes:
            # Checks if the number of types and the number of type names match
            errorString  = "The number of types spedified and the number of names of types "
            errorString += "specified do not match."
            self.LOG.append(errorString)
            raise ValueError(errorString)

        if not len(self.namesOfTypes) == len(set(self.namesOfTypes)):
            errorString  = "The names of types should not repeat. There are repetitions."
            self.LOG.append(errorString)
            raise ValueError(errorString)

        return True


    def isDefinedBySpreedsheet(self, arguments):
        # This is a simple method that verifies if the arguments specify if the phonetic
        # inventory to be defined by a spreadsheet input.
        if self.BY_SPREADSHEET_KEY not in arguments.keys():
            return False
        elif isinstance(arguments[self.BY_SPREADSHEET_KEY], bool):
            return arguments[self.BY_SPREADSHEET_KEY]
        else:
            errorString  = "The argument specifying if the inventory is defined by"
            errorString += " spreadsheet is not a boolean"
            self.LOG.append(errorString)
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



class PhonemeType:
    # This is a container class, where the phoneme types are stored.
    pass
