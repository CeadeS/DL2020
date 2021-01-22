# DL2020
_This Repo is meant for collaboration during the DL2020 assignment_

## Local Leaderboard
- The __leaderboard__ of the best results is updated on each push via a Github-Action. To see it, click the  :heavy_check_mark: - Symbol near the last commit description. Then "Details" and then "Get list of best results".
- For a graphical version, check out [this notebook for local recalculation](https://github.com/constantin-huetterer/DL2020/blob/main/accuracy_check.ipynb) for [the latest results, rerun it in Colab](https://colab.research.google.com/github/constantin-huetterer/DL2020/blob/main/accuracy_check.ipynb).

Open notebooks in Colab:
- [Current leader of the imagewoof-challenge](https://colab.research.google.com/github/constantin-huetterer/DL2020/blob/main/Current_leader_Woof_128_twist.ipynb)
- [Our base model](https://colab.research.google.com/github/constantin-huetterer/DL2020/blob/main/optimized_base_model.ipynb)

##Folders and experiments
### Optimizer and Early Stopping

### architectures

### blurpool and savemodelcallback
Model testing blurppol in unified code base together with savemodelcallback
### dropout

### epsilontest
Tests with the epsilon parameter
### final_imagenette
Results with the final notebook and imagenette dataset (for comparision)
### final_results
Results with the FINAL.ipynb
### item_transformation
experiemts with different transformation techniques, done before the unfied code base
### learning_rate

### lr_estimate
Experiments with LR exitmation from fastai
### results
Folder containing results of the optimized base model, our first unifed codebase
### savemodelcallback
Experiments with SaveModelCallback (restore weights, when results are worser then the spoch before)
### tested_params

### tests_before_unified_base_model

### variance 