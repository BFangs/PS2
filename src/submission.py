#!/usr/bin/python
import numpy as np

def initialize_mdp_data(num_states):
    """
    Return a variable that contains all the parameters/state you need for your MDP.

    Assume that no transitions or rewards have been observed.
    Initialize the value function array to small random values (0 to 0.10, say).
    Initialize the transition probabilities uniformly (ie, probability of
        transitioning for state x to state y using action a is exactly
        1/num_states).
    Initialize all state rewards and counts to zero.

    Args:
        num_states: The number of states

    Returns: The initial MDP parameters.  It should be a Python dict with the
        following key/value structure.  You may add more key/value pairs to this
        to make things simpler, but the autograders will only consider the
        following:
        {
        'transition_probs': np.ndarray, dtype=np.float64,
            shape=(num_states, num_actions, num_states). The MDP transition
            probability for each transition.
        'transition_counts': np.ndarray, dtype=np.float64,
            shape=(num_states, num_actions, num_states). The count of the number
            of times each transition was taken (Used for tracking transitions to
            later calculate avg_reward and transition_probs)

        'avg_reward': np.ndarray, dtype=np.float64, shape=(num_states,). The
            average reward for entering each MDP state.
        'sum_reward': np.ndarray, dtype=np.float64, shape=(num_states,). The
            summed reward earned when entering each MDP state (used to track rewards for later calculating avg_reward).

        'value': np.ndarray, dtype=np.float64, shape=(num_states,). The
            state-value calculated for each MDP state (after value/policy
            iteration).
        'num_states': Int
        }
    """
    num_actions = 2 # RIGHT AND LEFT ACTIONS

    mdp_data = {
        'transition_probs': None,
        'transition_counts': None,

        'avg_reward': None,
        'sum_reward': None,

        'value': None,
        'num_states': None
    }

    # *** START CODE HERE ***
    # *** END CODE HERE ***
    return mdp_data


def choose_action(state, mdp_data):
    """
    Choose the next action (0 or 1) that is optimal according to your current
    mdp_data. When there is no optimal action, return a random action.

    Args:
        state: The current state in the MDP
        mdp_data: The parameters for your MDP. See initialize_mdp_data.

    Returns:
        int, 0 or 1.  The index of the optimal action according to your current MDP.
    """

    # BONUS LEARNING OPPORTUNITY: When you have finished the problem set, try
    # un-commenting the following two lines.  This will implement a strategy
    # called epsilon greedy, which drastically improves performance.  Why do you
    # think this works so well?
    #
    # if np.random.uniform() < 0.1: # 10% of the time, choose a random action
    #     return  0 if np.random.uniform() < 0.5 else 1

    action = None
    # *** START CODE HERE ***
    # *** END CODE HERE ***
    return action


def update_mdp_transition_counts_sum_reward(mdp_data, state, action, new_state, reward):
    """
    Update the transition count and reward sum information in your mdp_data. 
    Do not change the other MDP parameters (those get changed later).

    Record the number of times `state, action, new_state` occurs.
    Record the rewards for every `new_state`.
    Record the number of time `new_state` was reached.

    Args:
        mdp_data: The parameters of your MDP. See initialize_mdp_data.
        state: The state that was observed at the start.
        action: The action you performed.
        new_state: The state after your action.
        reward: The reward after your action (i.e. reward corresponding to new_state).

    Returns:
        Nothing
    """

    # *** START CODE HERE ***
    # *** END CODE HERE ***

    # This function does not return anything
    return


def update_mdp_transition_probs_avg_reward(mdp_data):
    """
    Update the estimated transition probabilities and average reward values in your MDP.

    Make sure you account for the case when a state-action pair has never
    been tried before, or the state has never been visited before. In that
    case, you must not change that component (and thus keep it at the
    initialized uniform distribution).
    
    Args:
        mdp_data: The data for your MDP. See initialize_mdp_data.

    Returns:
        Nothing

    """

    # *** START CODE HERE ***
    # *** END CODE HERE ***

    # This function does not return anything
    return



def update_mdp_value(mdp_data, tolerance, gamma):
    """
    Update the estimated values in your MDP.


    Perform value iteration using the new estimated model for the MDP.
    The convergence criterion should be based on `TOLERANCE` as described
    at the top of the file.
    
    Args:
        mdp_data: The data for your MDP. See initialize_mdp_data.
        tolerance: The tolerance to use for the convergence criterion.
        gamma: Your discount factor.

    Returns:
        Nothing

    """

    # *** START CODE HERE ***
    # *** END CODE HERE ***

    # This function does not return anything
    return
