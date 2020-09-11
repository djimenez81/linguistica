#!/usr/bin/python
# module phonetics

# Copyright (c) 2020 Universidad de Costa Rica
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
# DISCLAIMED. IN NO EVENT SHALL UNIVERSIDAD DE COSTA RICA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Investigators:
#         David Jimenez <david.jimenezlopez@ucr.ac.cr>

# This module contains the methods, classes and variables necessary for the
# implementation of a phonetic system necessary for a research project.

###############
###############
##           ##
##  IMPORTS  ##
##           ##
###############
###############

#############
#############
##         ##
## CLASSES ##
##         ##
#############
#############

class Phone:
    ##############
    # ATTRIBUTES #
    ##############

    ##sets blank to strings considered attributes for phones.
    ##wouldn't it be better to have one class for vowels and another for consonants?
    ## Considering most traits will be void or 0 in most cases.

    place_of_articulation = ""
    manner_of_aritculation = ""
    phonation = ""
    voice_onset_type = ""
    airstream_mechanism = ""
    length = ""
    height = ""
    backness = ""
    roundedness = ""
    front_raised_retracted = ""
    nazalization = ""

    ################
    # CONSTRUCTORS #
    ################

    ##default constructor
    def __init__(self):
        pass

    ##parameratrized constructor
    def __init__(self, place_of_articulation,manner_of_articulation,phonation,voice_onset_type,airstream_mechanism,length,height,backness,roundedness,front_raised_retracted,nazalization):
        self.place_of_articulation = place_of_articulation
        self.manner_of_articulation = manner_of_articulation
        self.phonation = phonation
        self.voice_onset_type = voice_onset_type
        self.airstream_mechanism = airstream_mechanism
        self.length = length
        self.height = height
        self.backness = backness
        self.roundedness = roundedness
        self.front_raised_retracted = front_raised_retracted
        self.nazalization = nazalization
        pass


    ###########
    # GETTERS #
    ###########
        def get_place_of_articulation(self):
            return self._get_place_of_articulation
        def get_manner_of_articulation(self):
            return self._manner_of_aritculation
        def get_phonation(self):
            return self._phonation
        def get_voice_onset_type(self):
            return self._voice_onset_type
        def get_airstream_mechanism(self):
            return self._airstream_mechanism
        def get_length(self):
            return self._length
        def get_height(self):
            return self._height
        def get_backness(self):
            return self._backness
        def get_roundedness(self):
            return self._roundedness
        def get_front_raised_retracted(self):
            return self._front_raised_retracted
        def get_nazalization(self):
            return self._nazalization
    ###########
    # SETTERS #
    ###########
        def set_place_of_articulation(self, place_of_articulation):
            self._place_of_articulation = place_of_articulation

        def set_manner_of_articulation(self, manner_of_articulation):
            self._manner_of_aritculation = manner_of_articulation

        def set_phonation(self, phonation):
            self._phonation = phonation

        def set_voice_onset_type(self, voice_onset_type):
            self._voice_onset_type =voice_onset_type

        def set_airstream_mechanism(self, airstream_mechanism):
            self._airstream_mechanism = airstream_mechanism

        def set_length(self, length):
            self._length = length

        def set_height(self, height):
            self._height = height

        def set_backness(self, backness):
            self._backness = backness

        def set_roundedness(self, roundedness):
            self._roundedness = roundedness

        def set_front_raised_retracted(self, front_raised_retracted):
            self._front_raised_retracted = front_raised_retracted

        def set_nazalization(self, nazalization):
            self._nazalization = nazalization

    #############
    # FUNCTIONS #
    #############

    def to_display(self):
        print("Place of articulation: " + self.place_of_articulation)
        print("Manner of articulation: " + self.manner_of_articulation)
        print("Phonation: " + self.phonation)
        print("Voice onset type: " + self.voice_onset_type)
        print("Airstream mechinism: " + self.airstream_mechanism)
        print("Length: " + self.length)
        print("Height: " + self.height)
        print("Backness: " + self.backness)
        print("Roundedness: " + self.roundedness)
        print("Front raised retracted: " + self.front_raised_retracted)
        print("Nazalization: " + self.nazalization)

    pass

class FeatureRule:
    # This class implements a small container of a Feature Rule. For example,
    # +CONSONANTAL implies -SYLLABIC could be one of the rules.
    # In this case, both the antecedent as the consequent are lists, as it might
    # be the case there are several arguments on each of these part,

    ##############n
    # ATTRIBUTES #
    ##############

    ###########
    # GETTERS #
    ###########

    ###########
    # SETTERS #
    ###########

    #############
    # FUNCTIONS #
    #############

    pass

class PhoneticSystem:
    ##############n
    # ATTRIBUTES #
    ##############

    ###########
    # GETTERS #
    ###########

    ###########
    # SETTERS #
    ###########

    #############
    # FUNCTIONS #
    #############

    pass

#############
#############
##         ##
## METHODS ##
##         ##
#############
#############



######################
######################
##                  ##
## GLOBAL VARIABLES ##
##                  ##
######################
######################

NAME_DICT = {
        "PLACE_OF_ARTICULATION":
            [
                "BILABIAL",
                "LABIO_DENTAL",
                "LINGUO_DENTAL",
                "DENTAL",
                "ALVEOLAR",
                "POST_ALVEOLAR",
                "RETROFLEX",
                "PALATAL",
                "VELAR",
                "UVULAR",
                "PHARYNGEAL",
                "GLOTTAL"
            ],
        "MANNER_OF_ARTICULATION":
            [
                "NASAL",
                "STOP",
                "AFFRICATE",
                "FRICATIVE",
                "TRILL",
                "FLAP",
                "FRICATIVE",
                "LATERAL_FRICATIVE",
                "APPROXIMANT",
                "LATERAL_APPROXIMANT"
            ],
        "PHONATION_SIMPLE":
            [
                "VOICED",
                "VOICELESS"
            ],
        "VOICE_ONSET_TYPE":
            [
                "STRONG_ASPIRATION",
                "MODERATE_ASPIRATION",
                "MILD_ASPIRATION",
                "TENUIS",
                "PARTIALLY_VOICED",
                "FULLY_VOICED"
            ],
        "AIRSTREAM_MECHANISM":
            [
                "PULMONIC_EGRESSIVE",
                "EJECTIVE",
                "CLICK",
                "IMPLOSSIVE"
            ],
        "LENGTH":
            [
                "SINGLE",
                "GEMINATED"
            ],
        "HEIGHT":
            [
                "HIGH",
                "NEAR_HIGH",
                "HIGH_MID",
                "MID",
                "LOW_MID",
                "NEAR_LOW",
                "LOW"
            ],
        "BACKNESS":
            [
                "FRONT",
                "NEAR_FRONT",
                "CENTRAL",
                "NEAR_BACK",
                "BACK"
            ],
        "ROUNDEDNESS":
            [
                "ROUNDED",
                "UNROUNDED"
            ],
        "FRONT_RAISED_RETRACTED":
            [
                "FRONT",
                "RAISED",
                "RETRACTED"
            ],
        "NAZALIZATION":
            [
                "NAZALIZED"
                "NOT_NAZALIZED"
            ],
        "PHONATION":
            [
                "MODAL_VOICE",
                "UNVOICED",
                "ASPIRATED",
                "BREATHY_VOICE",
                "SLACK_VOICE",
                "CREAKY_VOICE",
                "STIFF_VOICE"
            ]
    }


FEATURES = [
        "SYLLABIC",
        "SONORANT",
        "CONSONANTAL"
        "HIGH",
        "LOW",
        "BACK",
        "ROUND",
        "TENSE",
        "CORONAL",
        "ANTERIOR",
        "STRIDENT",
        "DISTRIBUTED",
        "CONTINUANT",
        "DELAYED_RELEASE",
        "NASAL",
        "LATERAL",
        "SPREAD_GLOTTIS",
        "CONSTRICTED_GLOTTIS",
        "VOICE",
        "LONG",
        "STRESS"
 ]
