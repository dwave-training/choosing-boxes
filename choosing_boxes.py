# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

## ------- import packages -------
from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import BinaryQuadraticModel

# TODO:  Add code here to define your BQM
def get_bqm(S):
    """Returns a dictionary representing a QUBO.

    Args:
        S(list of integers): the value for each box
    """

    bqm = BinaryQuadraticModel('BINARY')

    # Add BQM construction here
    
    return bqm

# TODO:  Choose QPU parameters in the following function
def run_on_qpu(bqm, sampler):
    """Runs the BQM on the sampler provided.

    Args:
        bqm (BinaryQuadraticModel): a BQM for the problem;
            variable names should be 'box_17', 'box_21', and 'box_19'
        sampler (dimod.Sampler): a sampler that uses the QPU
    """

    numruns = 1 # update

    sample_set = sampler.sample(bqm, num_reads=numruns, label='Training - Choosing Boxes')

    return sample_set

## ------- Main program -------
if __name__ == "__main__":

    S = [17, 21, 19]

    bqm = get_bqm(S)

    #TODO:  Write code to define your sampler

    #TODO:  Write code to run your problem

    #TODO:  Write code to look at the solutions returned
