#!/usr/bin/python
# module linguistics

# This module contains a class to abstract an aligner of sequences, may they be phonemic,
# proteomic or genetic. It uses the logic, whether from the Needleman-Wunsch (global
# alignment) or Smith-Waterman (local alignment).
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


class Aligner:

    def __init__(self,substitutionMatrix):
        # TODO: This creator is actually pretty basic, as it only receives a substitution
        #       matrix and sets it as its own.
        self.PROFILES = "PROFILES"
        self.GENETIC = "GENETIC_ALGORITHM"
        pass

    def singleAlignment(self, sequence1, sequence2, global=True):
        # TODO: It needs to implement the alignment for global or local alignment for the
        #       sequences given. It needs to make the verification that the sequences given
        #       are valid.
        pass

    def multipleAlignment(self, sequences, mode=self.PROFILES):
        # TODO: It needs to implement the multiple alignment of sequences, and it can be
        #       made according to profile alignment, or genetic algorithms.
        pass
