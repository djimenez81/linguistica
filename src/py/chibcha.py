#!/usr/bin/python
# module chibcha

# This module contains a set of functions that allows a series of computations
# based on the files prepared for a project to test a few numerical methods to
# automatically compute the phylogenetic tree of the Chibchan languages.
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
#         Ernesto García <luis.garciaestrada@ucr.ac.cr>
#         Viviana Solís <viviana.solissolis@ucr.ac.cr>

# This module contains the methods, classes and variables necessary for the
# implementation of a phonetic system necessary for a research project.


import pandas as pd
import numpy as np
import math


VOCALS = ['i', '1', 'u', 'I', 'U', 'e', '7', 'o', 'a', 'O','i~','1~','u~','I~',
          'e~','7~','o~','a~','0~']

CONSONANTS = ['p', 'b', 't', 'd', 'k', 'g', '?', 'F', 'B', 's', 'z', 'K', 'S',
              'Z', 'x', 'G', 'h', 'T', 'C', 'J', 'm', 'n', 'ñ', 'N', 'r', 'R',
              'l', 'L']


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
        chibchan_dict = prepareLanguageDictionary(spanish,chibchan_language)
        chibchan_lists[language_name] = chibchan_dict
        k += 1
    return chibchan_lists


def prepareLanguageDictionary(spanish,chibchan_language):
    # This function is done simply to simplify the logic of prepareLists. Needs
    # some renaming of variables to make it generalizable.
    chibchan_dict = {}
    for n in range(len(chibchan_language)):
        spanish_word = spanish[n]
        chibchan_word = chibchan_language[n]
        if type(chibchan_word) == str:
            chibchan_dict[spanish_word] = chibchan_word
    return chibchan_dict


def prepareFeatures():
    # This function reads the Feature List and converts it into two dictionary
    # objects, one for vowels and one for consonants.
    df_vow = pd.read_excel("../../res/rasgos.xlsx", sheet_name="vocales")
    df_con = pd.read_excel("../../res/rasgos.xlsx", sheet_name="consonantes")
    vowel_list = df_vow.to_dict()
    vowel_axes = list(df_vow.axes[1])
    consonant_list = df_con.to_dict()
    consonant_axes = list(df_con.axes[1])
    vowels = prepareFeatureType(vowel_axes, vowel_list)
    consonants = prepareFeatureType(consonant_axes, consonant_list)
    return vowels, consonants


def prepareFeatureType(type_axes, type_list):
    # This code repeated twice in the prepareFeatures function, so it seemed
    # appropriate to give it its own function.
    type_features = {}
    k = 1
    K = len(type_axes)
    while k < K:
        phoneme_name = type_axes[k]
        phoneme_features = type_list[phoneme_name]
        output_features = []
        for n in range(len(phoneme_features)):
            output_features.append(phoneme_features[n])
        if type(phoneme_name) == int:
            phoneme_name = str(phoneme_name)
        type_features[phoneme_name] = output_features
        k += 1
    return type_features


# New global variables.
# For some reason, if I add them at the beginning, it gives an error.
chibchan_swadesh_lists = prepareLists()
vowels, consonants = prepareFeatures()


def phonemeDistance(phoneme1,phoneme2):
    # This function returns the distance between two phonemes. It assumes that
    # the phonemes are in the lists, so, careful what you feed into it. The
    # distance is simple: if both phonemes are equal, returns 0, else, if both
    # are of the same type, returns the distance defined by the featureDistance
    # function. Else it returns 1.
    if phoneme1 == phoneme2:
        d = 0
    elif arePhonemesOfSameType(phoneme1,phoneme2):
        d = featureDistance(phoneme1,phoneme2)
    else:
        d = 1
    return d


def featureDistance(phoneme1,phoneme2):
    # This is a simple method that checks the type of phoneme represented by the
    # input (it assumes both are the same type, it does not verify this) and
    # computes the feature distance we defined: If both are vowels or both are
    # consonants, it returns the number of differing features divided by the
    # total number of features.
    if phoneme1 in CONSONANTS:
        feat1 = consonants[phoneme1]
        feat2 = consonants[phoneme2]
    else:
        feat1 = vowels[phoneme1]
        feat2 = vowels[phoneme2]
    return len([i for i in range(len(feat1)) if feat1[i]!=feat2[i]])/len(feat1)


def arePhonemesOfSameType(phoneme1,phoneme2):
    # This is simply a function that verify if the two phonemes are indeed both
    # VOCALS or both CONSONANTS,returnin TRUE in such a case and false in others.
    return (phoneme1 in VOCALS and phoneme2 in VOCALS) or \
           (phoneme1 in CONSONANTS and phoneme2 in CONSONANTS)


def alignWords(word1, word2):
    # This function takes two strings and alings them using the basic idea of
    # the Needleman Wunst algorithm.
    #
    # NOTE: This method should be improved by providing all the possible optimal
    #       alignments when there is more than one, to meassure later the
    #       distances of all the alignments and choose the minimal.
    word1 = splitWord(word1)
    word2 = splitWord(word2)
    directionMatrix = createDirectionMatrix(word1, word2)
    return finalWordAlignment(word1, word2, directionMatrix)
    # alignedWord1, alignedWord2 =  finalWordAlignment(word1, word2,
    # directionMatrix) return alignedWord1, alignedWord2.


def finalWordAlignment(word1,word2,directionMatrix):
    # This function returns the two words align according to the contents of
    # directionMatrix
    k = directionMatrix.shape[0]-1
    n = directionMatrix.shape[1]-1
    alignedWord1 = []
    alignedWord2 = []
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


def createDirectionMatrix(word1,word2):
    # This function returns the distance matrix from the alignment of the words
    # given using the basic idea of Needleman Wunst. The direction matrix has
    # the following standard to denote the direction of procedence:
    #   0: It comes from nowhere. Only the origin should have this.
    #   1: From above
    #   2: From left
    #   3: From diagonal
    K = len(word1)
    N = len(word2)
    alignmentMatrix = np.empty((K+1,N+1))
    directionMatrix = np.empty((K+1,N+1))
    alignmentMatrix[:] = np.nan
    alignmentMatrix[:,0] = 0
    alignmentMatrix[0,:] = 0
    directionMatrix[:] = np.nan
    directionMatrix[:,0] = 1
    directionMatrix[0,:] = 2
    directionMatrix[0,0] = 0
    for k in range(K):
        phoneme1 = word1[k]
        for n in range(N):
            phoneme2 = word2[n]
            phoneme_distance = phonemeDistance(phoneme1,phoneme2)
            upwards   = alignmentMatrix[k,n+1]
            leftwards = alignmentMatrix[k+1,n]
            diagwards = alignmentMatrix[k,n] + 1 - phoneme_distance
            alignmentMatrix[k+1,n+1] = max(upwards,leftwards,diagwards)
            directionMatrix[k+1, n+1] = \
                                defineDirection(upwards,leftwards,diagwards)
    return directionMatrix



def defineDirection(upwards,leftwards,diagwards):
    # This simple method defines the direction that is used by
    # createDirectionMatrix and alignWords functions.
    D = max(upwards,leftwards,diagwards)
    if D == diagwards:
        return 3
    elif D == leftwards:
        return 2
    else:
        return 1



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
        word1, word2 = alignWords2(word1,word2)
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
        elif char == ':' or char == '~':
            if phonemes[-1] in VOCALS:
                phonemes[-1] += char
        elif char in VOCALS or char in CONSONANTS:
            phonemes.append(char)
        k += 1
    return phonemes


def prepareGramMatrix(theMatrix):
    # This method is implemented as the reviewer wants a two dimentional spacial
    # representation of the points that represent the languages. We assume the
    # matrix given is square.
    N = theMatrix.shape[0]
    gramMatrix = np.zeros([N,N])
    for i in range(N):
        for j in range(N):
            gramMatrix[i,j] = \
                    (theMatrix[i,0]**2+theMatrix[0,j]**2-theMatrix[i,j]**2)/2
    return gramMatrix
