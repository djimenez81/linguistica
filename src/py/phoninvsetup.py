#!/usr/bin/python
# module linguistics

# This is a script that contains the logic for the user to load a phonetic inventory object.
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

import phoneticinventory as phinv


phinvArguments = {}



# These values have to be defined either way, and they correspond to the number of types
# of phonemes that are defined. There could be a single type of phonemes, but often, vowels
# and consonants are treated different, but the user can define as many different types of
# types as they need.
NUMBER_OF_TYPES_KEY   = "NUMBER OF TYPES"
NUMBER_OF_TYPES_VALUE = 2
TYPES_NAMES_KEY       = "TYPES NAMES"
TYPES_NAMES_VALUE     = ["Vocales", "Consonantes"]
STRICT_PARSING_KEY    = "STRICT PARSING"
STRICT_PARSING_VALUE  = False

phinvArguments[NUMBER_OF_TYPES_KEY] = NUMBER_OF_TYPES_VALUE
phinvArguments[TYPES_NAMES_KEY]     = TYPES_NAMES_VALUE
phinvArguments[STRICT_PARSING_KEY]  = STRICT_PARSING_VALUE



# If the phonetic inventory is going to be defined by a spreadsheet, this whole section
# should be uncommented. The variables with the suffix _KEY should not be modified. If
# values are going to be passed directly, this section could be completely commented, or at
# least the variable BY_SPREDSHEET_VALUE should be False. BY_SPREDSHEET_VALUE must be a
# boolean
BY_SPREADSHEET_KEY        = "BY SPREADSHEET"
BY_SPREADSHEET_VALUE      = True
SPREADSHEET_ADDRESS_KEY   = "SPREADSHEET ADDRESS"
SPREADSHEET_ADDRESS_VALUE = "../../res/rasgos_distintivos_chibchas.xlsx"


phinvArguments[BY_SPREADSHEET_KEY]      = BY_SPREADSHEET_VALUE
phinvArguments[SPREADSHEET_ADDRESS_KEY] = SPREADSHEET_ADDRESS_VALUE



# If the phonetic inventory is not defined by spreadsheet, at least for now it is assumed to
# be defined by passing  the attributes directly.

# TODO: How to pass the arguments directly.




import phoneticinventory as phinv
phinvArguments = {}
NUMBER_OF_TYPES_KEY   = "NUMBER OF TYPES"
NUMBER_OF_TYPES_VALUE = 2
TYPES_NAMES_KEY       = "TYPES NAMES"
TYPES_NAMES_VALUE     = ["Vocales", "Consonantes"]
STRICT_PARSING_KEY    = "STRICT PARSING"
STRICT_PARSING_VALUE  = False
phinvArguments[NUMBER_OF_TYPES_KEY] = NUMBER_OF_TYPES_VALUE
phinvArguments[TYPES_NAMES_KEY]     = TYPES_NAMES_VALUE
phinvArguments[STRICT_PARSING_KEY]  = STRICT_PARSING_VALUE
BY_SPREADSHEET_KEY        = "BY SPREADSHEET"
BY_SPREADSHEET_VALUE      = True
SPREADSHEET_ADDRESS_KEY   = "SPREADSHEET ADDRESS"
SPREADSHEET_ADDRESS_VALUE = "../../res/rasgos_distintivos_chibchas.xlsx"
phinvArguments[BY_SPREADSHEET_KEY]      = BY_SPREADSHEET_VALUE
phinvArguments[SPREADSHEET_ADDRESS_KEY] = SPREADSHEET_ADDRESS_VALUE


chibInv = phinv.PhoneticInventory(phinvArguments)

chibInv.parse("ʃãnõ")
chibInv.parse("tʰɛŋ")
chibInv.parse("ɲã ɽ~ĩ")
