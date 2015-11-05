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

'''Function that checks if tree is planar'''


import numpy as np
from neurom.core.tree import val_iter, ipreorder

def check_planar(tree, tol=0.1):

	# extract the x,y,z coordinates of all the points in the tree
	points = np.array([value[0:3] for value in val_iter(ipreorder(tree))])

	# center the points around 0.0
	points -= np.mean(points, axis=0)

	# calculate the covariance of the points
	cov = np.cov(points.transpose())

	# find the principal components
	eigs, eigv = np.linalg.eig(cov)

	# smallest component size
	min_eigv = eigs[np.argmin(eigs)]

	# projections onto the smallest component direction
	projections = np.dot(min_eigv, points)

	# sorting with respect to the distance from the center
	sorted(projections, key=np.linalg.norm)

	# the maximum extend on the line
	extend = np.linalg.norm(projections[0] - projections[-1])
	#sc = 2.*np.sqrt(6.251 * eigs) # 90%

	return  extend




