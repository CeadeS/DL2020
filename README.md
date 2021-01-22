# DL2020
_This Repo is meant for collaboration during the DL2020 assignment_

## Folder Structure
- __architectures__ \
    Contains the models that were used to test different regularization techniques (-> see Models)
- __best__ \
    Contains the best restult that we have achieved with different regularization techniques
- __experiments__ \
    Contains experiments performed to achieve the restults in the form of ipynb-files
- __misc__ \
    Contains helpers for statistical analysis, plotting etc
- __results__ \
    Contains the generated CSV-Filed obtained by the experiments

## File Name Schema
All files are named after the following schema: `x_m_r-p[_r-p]_i` where __x__ is the number of epochs trained with this configuration, __m__ is the underlying model that was tested and __r__ the regularization technique/s that was/were used. Parameters are further separated by the __-__ Sign.

_Example:_ The `file 20_o_dropout-20_3.csv` would mean that _20 Epochs_ were trained on the _optimized base model_. The tested regularization was a _Dropout_ of _20 %_ and this is the _3_ rd iteration.

## Models
We used the following models to evaluate different regularization techniques:
1. (B)ase Model - _Basic XResNet50 implementation from fastai_
2. (O)ptimized Base Model - _XResnet50 with tuned parameters and regularizations_
4. (L)eaderboard Contestant - _State-of-the-art model [by Ayasyrev](https://github.com/ayasyrev/imagenette_experiments/blob/master/) for comparison from the [imagenette-leaderboard](https://github.com/fastai/imagenette)_

## Regularization Techniques

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

## Local Leaderboard
- The __leaderboard__ of the best results is updated on each push via a Github-Action. To see it, click the  :heavy_check_mark: - Symbol near the last commit description. Then "Details" and then "Get list of best results".
- For a graphical version, check out [this notebook for local recalculation](https://github.com/constantin-huetterer/DL2020/blob/main/misc/accuracy_check.ipynb) for [the latest results, rerun it in Colab](https://colab.research.google.com/github/constantin-huetterer/DL2020/blob/main/misc/accuracy_check.ipynb).

Open notebooks in Colab:
- [Current leader of the imagewoof-challenge](https://colab.research.google.com/github/constantin-huetterer/DL2020/blob/main/architectures/leader_Woof_128_twist.ipynb)
- [Our base model](https://colab.research.google.com/github/constantin-huetterer/DL2020/blob/main/optimized_base_model.ipynb)
