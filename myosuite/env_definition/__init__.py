# =================================================
#	This model is generated with tacking the Myosuite conversion of [Rajagopal's full body gait model](https://github.com/opensim-org/opensim-models/tree/master/Models/RajagopalModel) as close
#reference.
#	Model	  :: Myo Leg 1 Dof Exo (MuJoCoV2.0)
#	Author	:: Andres Chavarrias (andreschavarriassanchez@gmail.com), David Rodriguez, Pablo Lanillos 
#	source	:: https://github.com/AndresChS/NAIR_Code
#	====================================================== -->
from myosuite.utils import gym; register=gym.register
import os
import numpy as np

register(id='ExoLeg40MuscFlexoExtEnv-v0',
    entry_point='myosuite.envs.nair.MyolegenvV0:Myoleg_env_v0', # where to find the new Environment Class
    max_episode_steps=512, # duration of the episode
    kwargs={
        'model_path': '/Users/achs/Documents/PHD/code/NAIR_Code/envs/myosuite/nair_envs/nair_envs/myoleg_1dof40muscexo/myoleg_1dof40muscexo_V0.xml', # where the xml file of the environment is located
        'target_jnt_range': {'knee_angle_r':(0, 1.57)},
        'target_qpos': 0.5,
        'sigma': .2,
        'target_type': 'generate',
        'normalize_act': True,
        'reset_type': 'fixed',
        'spasticity': 'passive'
    }
)

register(id='ExoLegPassiveFlexoExtEnv-v0',
    entry_point='myosuite.envs.nair.MyolegenvV0:Myoleg_env_v0', # where to find the new Environment Class
    max_episode_steps=512, # duration of the episode
    kwargs={
        'model_path': '/Users/achs/Documents/PHD/code/NAIR_Code/envs/myosuite/nair_envs/nair_envs/myoleg_passivemuscexo/myoleg_passivemuscexo_V0.xml', # where the xml file of the environment is located
        'target_jnt_range': {'knee_angle_r':(0, 1.57)},
        'target_qpos': 0.5,
        'sigma': .2,
        'target_type': 'fixed',
        'normalize_act': True,
        'reset_type': 'fixed',
        'spasticity': 'passive'
    }
)

register(id='ExoLegSpasticityFlexoExtEnv-v0',
    entry_point='myosuite.envs.nair.MyolegenvV0:Myoleg_env_v0', # where to find the new Environment Class
    max_episode_steps=512, # duration of the episode
    kwargs={
        'model_path': '/Users/achs/Documents/PHD/code/NAIR_Code/envs/myosuite/nair_envs/nair_envs/myoleg_spasticity_muscexo/myoleg_spasticity_muscexo_V0.xml', # where the xml file of the environment is located
        'target_jnt_range': {'knee_angle_r':(0, 1.57)},
        'target_qpos': 0.2,
        'sigma': .2,
        'target_type': 'fixed',
        'normalize_act': True,
        'reset_type': 'fixed',
        'spasticity': 'passive'
    }
)
# ***************************************************************
#                       Future works
# ***************************************************************

#register(id='ExoSuspendedLegFlexoExtEnv-v0',
#    entry_point='myosuite.envs.nair.MyolegenvV0:Myoleg_env_v0', # where to find the new Environment Class
#    max_episode_steps=200, # duration of the episode
#    kwargs={
#        'model_path': '/Users/achs/Documents/PHD/code/myosuite/envs/myoleg_suspendedexo/myoleg_suspendedexo_V0.xml', # where the xml file of the environment is located
#        'target_jnt_range': {'knee_angle_r':(0, 2.27),},
#        'normalize_act': True,
#        'pose_thd': .175,
#        'reset_type': 'random'
#    }
#)
