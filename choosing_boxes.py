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

def get_token():
    '''Return your personal access token'''
    
    # TODO: Enter your token here
    return 'YOUR-TOKEN-HERE'

# TODO:  Add code here to define your QUBO dictionary
def get_qubo(S):
    """Returns a dictionary representing a QUBO.

    Args:
        S(list of integers): the value for each box
    """

    Q = {}

    # Add QUBO construction here
    
    return Q

# TODO:  Choose QPU parameters in the following function
def run_on_qpu(Q, sampler):
    """Runs the QUBO problem Q on the sampler provided.

    Args:
        Q(dict): a representation of a QUBO
        sampler(dimod.Sampler): a sampler that uses the QPU
    """

    numruns = 1 # update

    sample_set = sampler.sample_qubo(Q, num_reads=numruns, label='Training - Choosing Boxes')

    return sample_set

## ------- Main program -------
if __name__ == "__main__":

    S = [17, 21, 19]

    token = get_token()
    Q = get_qubo(S)

    #TODO:  Write code to define your sampler

    #TODO:  Write code to run your problem

    #TODO:  Write code to look at the solutions returned
