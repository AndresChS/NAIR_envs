# Sconegym notes
Paste init_v0.py and "nair_envs" folder in "/opt/scone/scone/scenarios/sconegym"

Running this command:
sudo cp init_v0.py /opt/scone/scone/scenarios/sconegym/sconegym/
sudo cp -r nair_envs /opt/scone/scone/scenarios/sconegym/sconegym/

pip install gym==0.13


# Scone_model(gym)

['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'actuator_input_array', 'actuators', 'adjust_state_for_load', 'advance_simulation_to', 'bodies', 'com_pos', 'com_vel', 'contact_force', 'contact_load', 'contact_power', 'control_step_size', 'current_measure', 'delayed_dof_position_array', 'delayed_dof_velocity_array', 'delayed_muscle_fiber_length_array', 'delayed_muscle_fiber_velocity_array', 'delayed_muscle_force_array', 'delayed_vestibular_array', 'dof_position_array', 'dof_velocity_array', 'dofs', 'final_measure', 'get_control_parameter', 'get_control_parameter_names', 'get_store_data', 'gravity', 'has_simulation_ended', 'init_muscle_activations', 'init_state_from_dofs', 'integration_step', 'joints', 'legs', 'log_measure_report', 'mass', 'measure', 'muscle_activation_array', 'muscle_excitation_array', 'muscle_fiber_length_array', 'muscle_fiber_velocity_array', 'muscle_force_array', 'muscles', 'name', 'reset', 'set_actuator_inputs', 'set_control_parameter', 'set_delayed_actuator_inputs', 'set_dof_positions', 'set_dof_velocities', 'set_simulation_end_time', 'set_state', 'set_store_data', 'state', 'time', 'write_results']