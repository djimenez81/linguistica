#!/usr/bin/python
# module chibcha

# This module contains a
#
# Copyright (c) 2020 Universidad de Costa Rica.
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
# DISCLAIMED. IN NO EVENT SHALL DAVID JIMENEZ BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Researchers:
#         David Jimenez <david.jimenezlopez@ucr.ac.cr>
#         Haakon Krohn <haakonstensrud.krohn@ucr.ac.cr>
#         Ernesto García <luis.garciaestrada@ucr.ac.cr>
#         Viviana Solís <viviana.solissolis@ucr.ac.cr>

# This module contains the methods, classes and variables necessary for the
# implementation of a phonetic system necessary for a research project.


import pandas as pd
import numpy as np
import math


VOCALS = ['i', '1', 'u', 'I', 'U', 'e', '7', 'o', 'a',
          'O','i~','1~','u~','I~','e~','7~','o~','a~','0~']

CONSONANTS = ['p', 'b', 't', 'd', 'k', 'g', '?', 'F', 'B', 's',
              'z', 'K', 'S', 'Z', 'x', 'G', 'h', 'T', 'C', 'J',
              'm', 'n', 'ñ', 'N', 'r', 'R', 'l', 'L']


def prepareLists():
    # This function reads the Swadesh List file and converts it to a big
    # dictionary object.
    listsSw = pd.read_excel("../../res/listasswadesh2.xlsx", sheet_name="Hoja1")
    axes = list(listsSw.axes[1])
    listasSwadesh = listsSw.to_dict()
    spanish = listasSwadesh[axes[1]]
    K = len(axes)
    k = 2
    chibchan_lists = {}
    while k < K:
        language_name = axes[k]
        chibchan_language = listasSwadesh[language_name]
        chibchan_dict = {}
        for n in range(len(chibchan_language)):
            spanish_word = spanish[n]
            chibchan_word = chibchan_language[n]
            if type(chibchan_word) == str:
                chibchan_dict[spanish_word] = chibchan_word
        chibchan_lists[language_name] = chibchan_dict
        k += 1
    return chibchan_lists



def prepareFeatures():
    # This function reads the Feature List and converts it into two dictionary
    # objects, one for vowels and one for consonants.
    df_vow = pd.read_excel("../../res/rasgos.xlsx", sheet_name="vocales")
    df_con = pd.read_excel("../../res/rasgos.xlsx", sheet_name="consonantes")
    vowel_list = df_vow.to_dict()
    vowel_axes = list(df_vow.axes[1])
    consonant_list = df_con.to_dict()
    consonant_axes = list(df_con.axes[1])
    # features = vowel_list[vowel_axes[1]]
    vowels = {}
    consonants = {}
    k = 1
    K = len(vowel_axes)
    while k < K:
        phoneme_name = vowel_axes[k]
        phoneme_features = vowel_list[phoneme_name]
        output_features = []
        for n in range(len(phoneme_features)):
            output_features.append(phoneme_features[n])
             #logic to perform checks on nasalized vowels. Not sure what the excecuted block should be.
             #logic should work tho.
             #if len(phoneme_features) > 1 and phoneme_features[1] == '~':
                #excecute_block()
                #
                #end excecute_block()
        if type(phoneme_name) == int:
            phoneme_name = str(phoneme_name)
        vowels[phoneme_name] = output_features
        k += 1
    features = consonant_list[consonant_axes[1]]
    k = 1
    K = len(consonant_axes)
    while k < K:
        phoneme_name = consonant_axes[k]
        phoneme_features = consonant_list[phoneme_name]
        output_features = []
        for n in range(len(phoneme_features)):
            output_features.append(phoneme_features[n])
        consonants[phoneme_name] = output_features
        k += 1
    return vowels, consonants


# New global variables.
# For some reason, if I add them at the beginning, it gives an error.
chibchan_swadesh_lists = prepareLists()
vowels, consonants = prepareFeatures()


def phonemeDistance(phoneme1,phoneme2):
    # This function returns the distance between two phonemes. It assumes that
    # the phonemes are in the lists, so, careful what you feed into it. The
    # distance is simple: if one phoneme is blank (" "), then it returns 1. If
    # one of the phonemes is a vowel and the other is a consonant, then it
    # returns 1. If both are vowels or both are consonants, it returns the
    # number of differing features divided by the total number of features.
    if phoneme1 == phoneme2:
        d = 0
    elif phoneme1 == " " or phoneme2 == " ":
        d = 1
    elif phoneme1 in VOCALS and phoneme2 in CONSONANTS:
        d = 1
    elif phoneme1 in CONSONANTS and phoneme2 in VOCALS:
        d = 1
    elif phoneme1 in VOCALS and phoneme2 in VOCALS:
        feat1 = vowels[phoneme1]
        feat2 = vowels[phoneme2]
        K = len(feat1)
        dist = 0
        for k in range(K):
            if feat1[k] != feat2[k]:
                dist += 1
        d = dist/K
    elif phoneme1 in CONSONANTS and phoneme2 in CONSONANTS:
        feat1 = consonants[phoneme1]
        feat2 = consonants[phoneme2]
        K = len(feat1)
        dist = 0
        for k in range(K):
            if feat1[k] != feat2[k]:
                dist += 1
        d = dist/K
    return d

def alignWords(word1, word2):
    # This function takes two strings and alings them using the basic idea of
    # the Needleman Wunst algorithm. The direction matrix has the following
    # standard to denote the direction of procedence:
    #   0: It comes from nowhere. Only the origin should have this.
    #   1: From above
    #   2: From left
    #   3: From diagonal
    #
    # NOTE: This method should be improved by providing all the possible optimal
    #       alignments when there is more than one, to meassure later the
    #       distances of all the alignments and choose the minimal.
    #
    word1 = splitWord(word1)
    word2 = splitWord(word2)
    K = len(word1)
    N = len(word2)
    alignmentMatrix = np.empty((K+1,N+1))
    directionMatrix = np.empty((K+1,N+1))
    alignmentMatrix[:] = np.NaN
    alignmentMatrix[:,0] = 0
    alignmentMatrix[0,:] = 0
    directionMatrix[:] = np.NaN
    directionMatrix[:,0] = 1
    directionMatrix[0,:] = 2
    directionMatrix[0,0] = 0
    # This part of the code constructs the value and direction matrices.
    for k in range(K):
        phoneme1 = word1[k]
        for n in range(N):
            phoneme2 = word2[n]
            d = phonemeDistance(phoneme1,phoneme2)
            upwards   = alignmentMatrix[k,n+1]
            leftwards = alignmentMatrix[k+1,n]
            diagwards = alignmentMatrix[k,n] + 1 - d
            D = max(upwards,leftwards,diagwards)
            alignmentMatrix[k+1,n+1] = D
            if D == diagwards:
                directionMatrix[k+1, n+1] = 3
            elif D == leftwards:
                directionMatrix[k+1, n+1] = 2
            else:
                directionMatrix[k+1, n+1] = 1
    k = K
    n = N
    alignedWord1 = []
    alignedWord2 = []
    # This part of the code reconstructs the alignment from the directionMatrix.
    while k + n > 0:
        dir = directionMatrix[k,n]
        if dir == 3:
            alignedWord1.append(word1[k-1])
            alignedWord2.append(word2[n-1])
            k -= 1
            n -= 1
        elif dir == 1:
            alignedWord1.append(word1[k-1])
            alignedWord2.append(' ')
            k -= 1
        elif dir == 2:
            alignedWord2.append(word2[n-1])
            alignedWord1.append(' ')
            n -= 1
    alignedWord1.reverse()
    alignedWord2.reverse()
    return alignedWord1, alignedWord2


def wordDistance(word1,word2):
    # This function assumes that the arguments are words already aligned and
    # thus, they have the same length. It computes the average distance of the
    # characters.
    L = [phonemeDistance(word1[k],word2[k]) for k in range(len(word1))]
    return sum(L)/len(L)


def languageDistance(language1,language2):
    common_lexicon = [word for word in list(language1.keys())
                            if word in list(language2.keys())]
    distances = []
    for word in common_lexicon:
        word1 = splitWord(language1[word])
        word2 = splitWord(language2[word])
        word1, word2 = alignWords(word1,word2)
        d = wordDistance(word1,word2)
        distances.append(d)
    return sum(distances)/len(distances)

def languageMatrix():
    # This function takes the list of languages and computes the matrix of one
    # to one distances. As we are looking for the lowest
    language_list = list(chibchan_swadesh_lists.keys())
    K = len(language_list)
    language_matrix = np.zeros([K,K])
    np.fill_diagonal(language_matrix,1)
    for k in range(K):
        for n in range(k):
            d = languageDistance(chibchan_swadesh_lists[language_list[k]],
                                 chibchan_swadesh_lists[language_list[n]],)
            language_matrix[n,k] = d
            language_matrix[k,n] = d
    return language_matrix


def branchingStep(matrix,nodes):
    # This function makes a single step on the branching of the phylogenetic
    # tree. It assumes that nodes is an array 1xN, and that matrix is an numpy
    # array NxN, with N > 1. It also assume that matrix is a matrix of distances
    # symmetric and with values 1 in the diagonal, and values less than 1 in all
    # other entries.
    N = len(nodes)
    new_matrix = np.zeros((N-1,N-1))
    min_distance = np.min(matrix)
    W = np.where(matrix == min_distance)
    x = W[0][0]
    y = W[1][0]
    temp_matrix = np.delete(matrix,[x,y],0)
    temp_matrix = np.delete(temp_matrix,[x,y],1)
    new_matrix[0:N-2,0:N-2] = temp_matrix
    new_matrix[N-2,N-2] = 1
    check_array = np.delete(matrix[[x,y],:].min(axis = 0),[x,y],0)
    new_matrix[N-2,0:N-2] = check_array
    new_matrix[0:N-2,N-2] = check_array
    new_pair = [nodes[x],nodes[y]]
    new_nodes = [x for x in nodes if x not in new_pair]
    new_nodes.append(new_pair)
    return new_matrix, new_nodes

def fullBranching():
    # This is the cental method of the file. It computes the binary tree
    matrix = languageMatrix()
    nodes = list(chibchan_swadesh_lists.keys())
    while len(nodes) > 1:
        matrix,nodes = branchingStep(matrix,nodes)
    return nodes


def splitWord(word):
    # This function receives a word, that is, a string containing the X-SAMPA
    # representation of a word, and splits this word on its components. This has
    # been programmed thinking of the chibchan language family phonological
    # inventory.
    phonemes = []
    n = len(word)
    k = 0
    while k < n:
        char = word[k]
        if char == '_':
            k += 1
        elif char in VOCALS or char in CONSONANTS:
            phonemes.append(char)
        k += 1
    return phonemes
