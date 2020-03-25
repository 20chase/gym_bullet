import gym
from gym.envs.registration import registry, make, spec


def register(id, *args, **kvargs):
    if id in registry.env_specs:
        return
    else:
        return gym.envs.registration.register(id, *args, **kvargs)

register(id='Walker2DBulletEnv-v0',
         entry_point='gym_bullet.gym_locomotion_envs:Walker2DBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)
register(id='HalfCheetahBulletEnv-v0',
         entry_point='gym_bullet.gym_locomotion_envs:HalfCheetahBulletEnv',
         max_episode_steps=1000,
         reward_threshold=3000.0)

register(id='AntBulletEnv-v0',
         entry_point='gym_bullet.gym_locomotion_envs:AntBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)

register(id='HopperBulletEnv-v0',
         entry_point='gym_bullet.gym_locomotion_envs:HopperBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)

register(id='HumanoidBulletEnv-v0',
         entry_point='gym_bullet.gym_locomotion_envs:HumanoidBulletEnv',
         max_episode_steps=1000)

register(id='HumanoidFlagrunBulletEnv-v0',
         entry_point='gym_bullet.gym_locomotion_envs:HumanoidFlagrunBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2000.0)

register(id='HumanoidFlagrunHarderBulletEnv-v0',
         entry_point='gym_bullet.gym_locomotion_envs:HumanoidFlagrunHarderBulletEnv',
         max_episode_steps=1000)

register(id='Walker2DBulletPositionControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_position_envs:Walker2DBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)

register(id='HalfCheetahBulletPositionControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_position_envs:HalfCheetahBulletEnv',
         max_episode_steps=1000,
         reward_threshold=3000.0)

register(id='AntBulletPositionControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_position_envs:AntBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)

register(id='HopperBulletPositionControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_position_envs:HopperBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)

register(id='HumanoidBulletPositionControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_position_envs:HumanoidBulletEnv',
         max_episode_steps=1000)

register(id='HumanoidFlagrunBulletPositionControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_position_envs:HumanoidFlagrunBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2000.0)

register(id='HumanoidFlagrunHarderBulletPositionControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_position_envs:HumanoidFlagrunHarderBulletEnv',
         max_episode_steps=1000)


register(id='Walker2DBulletVelocityControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_velocity_envs:Walker2DBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)
register(id='HalfCheetahBulletVelocityControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_velocity_envs:HalfCheetahBulletEnv',
         max_episode_steps=1000,
         reward_threshold=3000.0)

register(id='AntBulletVelocityControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_velocity_envs:AntBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)

register(id='HopperBulletVelocityControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_velocity_envs:HopperBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)

register(id='HumanoidBulletVelocityControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_velocity_envs:HumanoidBulletEnv',
         max_episode_steps=1000)

register(id='HumanoidFlagrunBulletVelocityControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_velocity_envs:HumanoidFlagrunBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2000.0)

register(id='HumanoidFlagrunHarderBulletVelocityControlEnv-v0',
         entry_point='gym_bullet.gym_locomotion_velocity_envs:HumanoidFlagrunHarderBulletEnv',
         max_episode_steps=1000)

def getList():
    btenvs = ['- ' + spec.id for spec in gym.envs.registry.all() if spec.id.find('Bullet') >= 0]
    return btenvs