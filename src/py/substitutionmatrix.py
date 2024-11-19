#!/usr/bin/python
# module linguistics

# This module contains a class to abstract the object of a matrix substitution for alignment
# in genetics, proteomics or, in our case, phonological information.
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

# This module contains the methods, classes and variables necessary for the implementation
# of substitution matrix for the alignment of sequences, mostly, of phonetic data.


class SubstitutionMatrix:
    # Need to do something here.


    def __init__(self,args):
        # TODO: Set up the different types of input It might be a spreadsheet with the given
        #       matrix, it might be simply an array and a double array so that the entry
        #       ij in the double array correspond to the substitution value for entry i to
        #       the entry j of the one dimentional array.
        pass

    def setSubstitutionValue(self, phoneme1, phoneme2, value):
        # TODO: Set up the values for the change from phoneme1 to phoneme2. It is written as
        #       if we were expecting this to be used in phonology (that is why we are
        #       writing it), but there is no change in the logic.
        pass

    def getSubstitutionValue(self, phoneme1, phoneme2):
        # TODO: This is just as simple. We need to figuire out how to return the value that
        #       is expected when these two phonemes.
        pass
 
