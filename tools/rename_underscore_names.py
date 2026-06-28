import json, re
from pathlib import Path

src_path = Path('d:/ME504Project/ME504Code.ipynb')
backup_path = src_path.with_suffix('.ipynb.bak')
new_path = Path('d:/ME504Project/ME504Code_humaly.ipynb')

shutil = __import__('shutil')
shutil.copy(src_path, backup_path)
print(f'Backup written to: {backup_path}')

nb = json.loads(src_path.read_text(encoding='utf-8'))

replacements = {
    'X_batch': 'Xbatch',
    'y_batch': 'ybatch',
    'X_s': 'Xs',
    'X_te': 'Xte',
    'X_tr': 'Xtr',
    'acc_cls_direct': 'accClsDirect',
    'acc_reg_converted': 'accRegConverted',
    'acc_scores': 'accScores',
    'batch_size': 'batchSize',
    'best_state': 'bestState',
    'best_val_loss': 'bestValLoss',
    'cl_te': 'clTe',
    'cl_tr': 'clTr',
    'cm_norm': 'cmNorm',
    'crit_c': 'critC',
    'crit_r': 'critR',
    'current_lr': 'currentLr',
    'dummy_2d': 'dummy2d',
    'dummy_logits': 'dummyLogits',
    'dummy_targets': 'dummyTargets',
    'eval_epoch': 'evalEpoch',
    'history_cls': 'historyCls',
    'history_reg': 'historyReg',
    'loss_fn': 'lossFn',
    'm_c': 'mC',
    'm_r': 'mR',
    'make_loader_2d': 'makeLoader2d',
    'mean_probs': 'meanProbs',
    'model_name': 'modelName',
    'n_epochs': 'nEpochs',
    'n_samples': 'nSamples',
    'n_test': 'nTest',
    'n_train': 'nTrain',
    'n_val': 'nVal',
    'new_lr': 'newLr',
    'num_classes': 'numClasses',
    'old_lr': 'oldLr',
    'opt_c': 'optC',
    'opt_r': 'optR',
    'ord_weight': 'ordWeight',
    'output_size': 'outputSize',
    'pad_width': 'padWidth',
    'patience_counter': 'patienceCounter',
    'per_class_acc': 'perClassAcc',
    'plot_history': 'plotHistory',
    'pred_class': 'predClass',
    'preds_reg_as_cls': 'predsRegAsCls',
    'quick_experiment': 'quickExperiment',
    'r2_scores': 'r2Scores',
    'rl_te': 'rlTe',
    'rl_tr': 'rlTr',
    'sample_sizes': 'sampleSizes',
    'scheduler_override': 'schedulerOverride',
    'stress_to_class': 'stressToClass',
    'stress_val': 'stressVal',
    'stress_vals': 'stressVals',
    'tc_': 'tc',
    'test_cls': 'testCls',
    'test_cls_2d': 'testCls2d',
    'test_ds': 'testDs',
    'test_loader': 'testLoader',
    'test_ratio': 'testRatio',
    'thickness_sample': 'thicknessSample',
    'top10_idx': 'top10Idx',
    'total_loss': 'totalLoss',
    'tr_': 'trExp',
    'train_cls': 'trainCls',
    'train_cls_2d': 'trainCls2d',
    'train_ds': 'trainDs',
    'train_epoch': 'trainEpoch',
    'train_loader': 'trainLoader',
    'train_loss': 'trainLoss',
    'train_model': 'trainModel',
    'true_c': 'trueC',
    'trues_as_cls': 'truesAsCls',
    'unique_x': 'uniqueX',
    'unique_y': 'uniqueY',
    'use_plateau': 'usePlateau',
    'val_cls': 'valCls',
    'val_cls_2d': 'valCls2d',
    'val_ds': 'valDs',
    'val_loader': 'valLoader',
    'val_loss': 'valLoss',
    'val_ratio': 'valRatio',
    'yc_s': 'ycS',
    'yc_te': 'ycTe',
    'yc_tr': 'ycTr',
    'yr_s': 'yrS',
    'yr_te': 'yrTe',
    'yr_tr': 'yrTr',
}

# Apply replacements token-wise to code cells only
patterns = [(re.compile(r'\b' + re.escape(k) + r'\b'), v) for k, v in replacements.items()]
changed = []
for cell in nb['cells']:
    if cell['cell_type'] != 'code':
        continue
    src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    new_src = src
    for pat, repl in patterns:
        new_src = pat.sub(repl, new_src)
    if new_src != src:
        changed.append(cell)
    cell['source'] = [line + '\n' for line in new_src.splitlines()]

new_path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
print(f'Wrote cleaned notebook to: {new_path}')
print(f'Updated code cells count: {len(changed)}')
