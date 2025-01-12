import json

import torch

from gsamllavanav.parser import parse_args
from gsamllavanav.train_baseline_with_map import train
from gsamllavanav.evaluate import eval_goal_predictor
from gsamllavanav.evaluate_baseline_with_map import run_episodes_batch
from gsamllavanav.cityreferobject import get_city_refer_objects
from gsamllavanav.dataset.generate import generate_episodes_from_mturk_trajectories
from gsamllavanav.dataset.mturk_trajectory import load_mturk_trajectories
from gsamllavanav.models.seq2seq_with_map import Seq2SeqwithMap
from gsamllavanav.goal_selection import goal_selection_gdino

DEVICE = 'cuda'


args = parse_args()

if args.mode == 'train':

    train(args, DEVICE)

if args.mode == 'eval':

    model_trajectory = args.checkpoint.split('/')[-2]
    epoch = args.checkpoint.split('/')[-1].split('.')[0]

    objects = get_city_refer_objects()

    # load predictor
    seq2seqwithmap = Seq2SeqwithMap(args.map_size).to(DEVICE)
    if args.checkpoint:
        seq2seqwithmap.load_state_dict(torch.load(args.checkpoint)['predictor_state_dict'])

    for split in ('val_seen', 'val_unseen', 'test_unseen'):
        
        test_episodes = generate_episodes_from_mturk_trajectories(objects, load_mturk_trajectories(split, 'all', args.altitude))

        trajectory_logs, pred_goal_logs, pred_progress_logs = run_episodes_batch(args, seq2seqwithmap, test_episodes, DEVICE)

        predicted_positions = goal_selection_gdino(args, pred_goal_logs)
        for eps_id, pose in predicted_positions.items():
            trajectory_logs[eps_id].append(pose)
        
        metrics = eval_goal_predictor(args, test_episodes, trajectory_logs, pred_goal_logs, pred_progress_logs)

        print(f"{split} -- {metrics.mean_final_pos_to_goal_dist: .1f}, {metrics.success_rate_final_pos_to_goal*100: .2f}, {metrics.success_rate_oracle_pos_to_goal*100: .2f}")
        
        noise = f"noise_{args.gps_noise_scale}" if args.gps_noise_scale > 0 else ""
        alt_env = f"_{args.alt_env}" if args.alt_env else ""
        with open(f'logs_{model_trajectory}_{split}_{args.progress_stop_val}{noise}{alt_env}.json', 'w') as f:
            json.dump({
                'metrics': metrics.to_dict(),
                'trajectory_logs': {str(eps_id): [tuple(pose) for pose in trajectory] for eps_id, trajectory in trajectory_logs.items()},
                'pred_goal_logs': {str(eps_id): [tuple(pos) for pos in pred_goals] for eps_id, pred_goals in pred_goal_logs.items()},
                'pred_progress_logs': {str(eps_id): pred_progresses for eps_id, pred_progresses in pred_progress_logs.items()},
            }, f)

