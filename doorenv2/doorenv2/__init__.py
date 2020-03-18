from gym.envs.registration import register

# register(
#     id='blue-doorenv-v1',
#     entry_point='doorenv.envs:DoorEnvBlueV1',
#     max_episode_steps=512,
# )

# register(
#     id='blue-doorenv-v2',
#     entry_point='doorenv.envs:DoorEnvBlueV2',
#     max_episode_steps=512,
# )

register(
    id='baxter-doorenv-v1',
    entry_point='doorenv2.envs:DoorEnvBaxter',
    max_episode_steps=512,
)