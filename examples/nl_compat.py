#!/usr/bin/env python
# Copyright (c) 2015, Ecole Polytechnique Federale de Lausanne, Blue Brain Project
# All rights reserved.
#
# This file is part of NeuroM <https://github.com/BlueBrain/NeuroM>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     1. Redistributions of source code must retain the above copyright
#        notice, this list of conditions and the following disclaimer.
#     2. Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.
#     3. Neither the name of the copyright holder nor the names of
#        its contributors may be used to endorse or promote products
#        derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''Compatibility between NL and H5 files'''
import numpy as np
from neurom import ezy

nrn_h5 = ezy.load_neuron('test_data/h5/v1/bio_neuron-000.h5')
nrn_asc = ezy.load_neuron('test_data/neurolucida/bio_neuron-000.asc')

print 'h5 number of sections: %s' % ezy.get('number_of_sections', nrn_h5)[0]
print 'nl number of sections: %s\n' % ezy.get('number_of_sections', nrn_asc)[0]
print 'h5 number of segments: %s' % ezy.get('number_of_segments', nrn_h5)[0]
print 'nl number of segments: %s\n' % ezy.get('number_of_segments', nrn_asc)[0]
print 'h5 total neurite surface area: %s' % np.sum(ezy.get('section_areas', nrn_h5))
print 'nl total neurite surface area: %s\n' % np.sum(ezy.get('section_areas', nrn_asc))
print 'h5 total neurite volume: %s' % np.sum(ezy.get('section_volumes', nrn_h5))
print 'nl total neurite volume: %s\n' % np.sum(ezy.get('section_volumes', nrn_asc))
print 'h5 total neurite length: %s' % np.sum(ezy.get('section_lengths', nrn_h5))
print 'nl total neurite length: %s\n' % np.sum(ezy.get('section_lengths', nrn_asc))
