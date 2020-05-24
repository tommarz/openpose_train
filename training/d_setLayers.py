# User configurable paths
## Path parameters
import os
from generateProtoTxt import generateProtoTxt
from math import floor, ceil

sCaffeFolder = '../../openpose_caffe_train/'
sDatasetFolder = '../dataset/'
# sLmdbFolders = ['lmdb_dome_bodyHand/']
sLmdbFolders = ['lmdb_coco/']
sProbabilities = "1.0"
sModelNames = []
# sLmdbFolders = ['lmdb_foot/']
# sLmdbFolders = ['lmdb_coco/', 'lmdb_dome/']
# sLmdbFolders = ['lmdb_foot/', 'lmdb_dome/']
# sLmdbFolders = ['lmdb_coco/', 'lmdb_dome_bodyHand/', 'lmdb_mpii_hand']
sLmdbBackground = 'lmdb_background/'
sTrainingFolder = '../training_results/pose/'
sPretrainedModelPath = sDatasetFolder + 'vgg/VGG_ILSVRC_19_layers.caffemodel'
sNormalization = 0
# # ResNet
# sPretrainedModelPath = sDatasetFolder + 'resnet/ResNet-50-model.caffemodel'
# sPretrainedModelPath = sDatasetFolder + 'resnet/ResNet-152-model.caffemodel'
# sPretrainedModelPath = sDatasetFolder + 'resnet/v2/resnet101-v2.caffemodel'
# sPretrainedModelPath = sDatasetFolder + 'resnet/v2/resnet152-v2.caffemodel'
# sNormalization = 1
# # DenseNet
# # sPretrainedModelPath = '/media/posefs3b/Users/gines/openpose_train/dataset/DenseNet-Caffe/DenseNet_161.caffemodel'
# sPretrainedModelPath = '/media/posefs3b/Users/gines/openpose_train/dataset/DenseNet-Caffe/DenseNet_121.caffemodel'
# sNormalization = 2

sAddFoot = 1
# sAddFoot = 0
sAddMpii = 1
# sAddMpii = 0
# sAddFace = 1
sAddFace = 0
# sAddHands = 1
sAddHands = 0
# sAddDome = 1
sAddDome = 0
sAddExtraPAFs = False # Extra PAFs? (BODY_25E, BODY_23)
# carVersion = 1
carVersion = 0
# sAddDistance = 1
sAddDistance = 0
# sProbabilityOnlyBackground = 0
# sProbabilityOnlyBackground = 0.01
sProbabilityOnlyBackground = 0.02
# sProbabilityOnlyBackground = 0.05
# sSuperModel = 2 # 2 is for SuperModel in 12 GB GPUs
# sSuperModel = 1 # 1 is for SuperModel for 32 GB GPUs
sSuperModel = 0

## Algorithm parameters
# Number heatmaps
sBodyParts = 17 + 6*sAddFoot + 2*sAddMpii + 70*sAddFace + 40*sAddHands # 19 (old), 18, 23, 25
sBodyPAFs = 2*(sBodyParts+1)
# Solver params
if sSuperModel:
    sLearningRateInit = 5e-5
    if sAddHands or sAddFace:
        sLearningRateInit = 3e-5
else:
    sLearningRateInit = 1e-4   # 4e-5, 2e-5
if sSuperModel == 2:
    sLearningRateInit //= 2.5
    sBatchSizes = [3]
else:
    sBatchSizes = [10] # [10], Gines: 21
# Data augmentation
if sSuperModel:
    sImageScale = 480
    sNumberStages = [1, 1, 0, 0, 0, 0]
else:
    sImageScale = 368
    sNumberStages = [5, 1, 0, 0, 0, 0]
sScaleMins = [1.0//3.0] # [1.0/3.0, 0.5, 0.25] # 0.5, 0.25 does harm it
sScaleMaxs = [1.5] # [1.5, 8.0, 2.5]
sCenterSwapProb = [0.0, 1.0, 0.0]
sMaxDegreeRotations = [45] # 40, 60 does harm it
sNumberMaxOcclusions = [2]
sKeypointSigmas = [7.0]
# Learning rate
sLearningRateMultDistro = [1.0, 1.0, 4.0, 1.0] # 'V', 'C(1-2)'('image'), 'C(1-2)', loss
# sLearningRateMultDistro = [1.0, 1.0, 1.0, 1.0] # 'V', 'C(1-2)'('image'), 'C(1-2)', loss
# sLearningRateMultDistro = [0.25, 1.0, 1.0, 1.0] # 'V', 'C(1-2)'('image'), 'C(1-2)', loss
# sLearningRateMultDistro = [1.0, 9.000018, 9.000018, 9.000018] # 'V', 'C(1-2)'('image'), 'C(1-2)', loss
# Ideally fixed
sNumberIterations = 1000000
sNumberIterationsMiddle = 50000
# sUsePReLU = 2 # 1 # 1 PReLU, 2 LReLU
sUsePReLU = 1 # 1 # 1 PReLU, 2 LReLU
sBatchNorm = 0
# sBatchNorm = 1
sBinaryConv = 0
# sBinaryConv = 1
if sBinaryConv:
    sPretrainedModelPath = '/media/posefs3b/Users/gines/openpose_train/training_results/2_19MoreScale2/pose/pose_iter_776000.caffemodel'
    sImageScale = 224
# Rescale training
rescaleLayer = sNumberStages[4] > 0
if rescaleLayer:
    sPretrainedModelPath = '/media/posefs3b/Users/gines/openpose_train/training_results/2_19_42/best_730k/pose_iter_730000.caffemodel'
    # sLmdbFolders = ['lmdb_coco2017_foot/']
    sLearningRateMultDistro = [0.0, 0.0, 0.0, 0.0, 1.0, 1.0] # 'V', 'C(1-2)'('image'), 'C(1-2)', loss
    sLearningRateInit = 1e-1   # 4e-5, 2e-5
    sBatchSizes = [16] # [10], Gines: 21

# Foot training
if sAddFoot:
    sBodyPAFs = 2*(sBodyParts+1)
    sLmdbFolders = ['lmdb_coco2017_foot/'] + sLmdbFolders
    sProbabilities = "0.05;" + str(0.95-sProbabilityOnlyBackground) + ""

# Hand training
# sNumberStages = [4, 2, 2, 1, 0, 0] # Enable hands
trainHand = sNumberStages[2] + sNumberStages[3] > 0
if trainHand:
    sBatchSizes = [11] # [10], Gines: 21
    sNumberMaxOcclusions = 0
    sKeypointSigmas = [6.0]
    sPretrainedModelPath = '/media/posefs3b/Users/gines/openpose_train/training_results/2_25YaserWholeBatch/pose/best_584k/pose_iter_584000.caffemodel'
    sHandParts = 40 # Without the 2 for wrist
    sHandPAFs = 2*sHandParts # Ideally -1, but hand-fingers PAF must be added here
    sLearningRateMultDistro = [0.0, 0.0, 0.0, 0.0, 4.0, 1.0] # 'V', 'C(1-2)'('image'), 'C(1-2)', loss
    sScaleMins = [0.8, 0.5, 0.25] # For hands
    sScaleMaxs = [3.0, 8.0, 2.5]
    sLmdbFolders = ['lmdb_hands_wrist_LR/']
    sSourceSecondary = os.path.abspath(sDatasetFolder + 'lmdb_hand143_panopticdb/')
    sModelNames = ['MPII_' + str(sBodyParts + sHandParts) + '_' + str(sHandParts+2)] * 2
else:
    sHandParts = 0
    sHandPAFs = 0
    sSourceSecondary = os.path.abspath(sDatasetFolder + 'lmdb_coco/')
    sModelNames = ['COCO_' + str(sBodyParts), 'COCO_' + str(sBodyParts) + '_17']
    # Extra PAFs
    if sAddExtraPAFs:
        if sAddFoot:
            sBodyPAFs = 2*(sBodyParts-1 + 14) # minimum spanning tree + extra ones
        else:
            sBodyPAFs = 2*(sBodyParts-1 + 12) # minimum spanning tree + extra ones
        sModelNames = ['COCO_' + str(sBodyParts) + 'E', 'COCO_' + str(sBodyParts) + '_17E']
        if sBodyParts == 23:
            sBodyPAFs = 2*(sBodyParts-1 + 14) # minimum spanning tree + extra ones
            sModelNames = ['COCO_' + str(sBodyParts), 'COCO_' + str(sBodyParts) + '_17']

# Car training
if carVersion > 0:
    sNumberMaxOcclusions = 0 # 0, 2
    if carVersion == 1:
        sBodyParts = 12
        sBodyPAFs = 2*(sBodyParts-1)
        sModelNames = ['CAR_' + str(sBodyParts)]
        sLmdbFolders = ['lmdb_car_v1/']
    elif carVersion == 2:
        sBodyParts = 22
        sBodyPAFs = 2*(sBodyParts-1+11)
        sModelNames = ['CAR_' + str(sBodyParts)] * 3 # Same than * 1
        sLmdbFolders = ['lmdb_car22_carfusion/', 'lmdb_car22_pascal3dplus/', 'lmdb_car22_veri776/']
        # Note that cars are horizontal, people are vertical. So scale is offseted.
        # sScaleMins = [0.5/3.0, 0.5/3.0, 0.5/3.0] # Too small for cars?
        sScaleMins = [1/3.0, 1/3.0, 1/3.0]
        sScaleMaxs = [0.5*1.5, 0.5*1.5, 0.5*1.5]
        sSourceSecondary = ''
    # sLmdbBackground = 'lmdb_car_background/' # Bug in there: many cars in there...
    sLmdbBackground = ''
    sProbabilities = "0.25;0.35;0.4"

partsStr = str(sBodyParts)
if sAddMpii:
    if len(sLmdbFolders) != 2:
        print('Not prepared for this case')
        assert(false)
    sLmdbFolders += ['lmdb_mpii/']
    sProbabilities = "0.05;" + str(0.9-sProbabilityOnlyBackground) + ";0.05"
    sModelNames = ['COCO_' + partsStr + 'B_23', 'COCO_' + partsStr + 'B_17', 'MPII_' + partsStr + 'B_16']
    sBodyPAFs = 2*(sBodyParts-1+12)
    sScaleMins = sScaleMins*2 + [sScaleMins[0]]
    sScaleMaxs = sScaleMaxs*2 + [2.5]

if sAddFace:
    if len(sLmdbFolders) != 3:
        print('Not prepared for this case')
        assert(false)
    sLmdbFolders += ['lmdb_face_frgc/', 'lmdb_face_multipie/', 'lmdb_face_mask_out/']
    sProbabilities = "0.05;" + str(0.85-sProbabilityOnlyBackground) + ";0.05;0.02;0.02;0.01"
    sModelNames = ['COCO_' + partsStr + '_23', 'COCO_' + partsStr + '_17', 'MPII_' + partsStr + '_16'] + ['FACE_' + partsStr + '_70']*3
    sBodyPAFs = 2*(sBodyParts-1+12+7*sAddFace)
    sScaleMins = sScaleMins*3 + [sScaleMins[0]]*3 # [0.2]*3
    sScaleMaxs = sScaleMaxs*3 + [sScaleMaxs[0]]*3
    # sScaleMaxs = sScaleMaxs*3 + [2*sScaleMaxs[0]]*3
    # sMaxDegreeRotations = sMaxDegreeRotations*3 + [66.7]*3
    sMaxDegreeRotations = sMaxDegreeRotations*3 + [sMaxDegreeRotations[0]]*3
    sNumberMaxOcclusions = 3*sNumberMaxOcclusions + [0]*3
    # sKeypointSigmas = 3*sKeypointSigmas + [6.0]*3
    sKeypointSigmas = 3*sKeypointSigmas + [7.0]*3

if sAddHands:
    if len(sLmdbFolders) != 6:
        print('Not prepared for this case')
        assert(false)
    # lmdb_hand_dome in openposedemo server is in /mnt/DataNVE/gines/lmdb_hand_dome/
    sLmdbFolders += ['lmdb_hand_dome/', 'lmdb_hand_mpii/']
    # sProbabilities = "0.05;" + str(0.82-sProbabilityOnlyBackground) + ";0.05;0.01;0.01;0.01;0.02;0.03"
    sProbabilities = "0.05;" + str(0.83-sProbabilityOnlyBackground-0.05) + ";0.05;0.0075;0.0075;0.005;0.06;0.04"
    sModelNames += ['HAND_' + partsStr + '_21'] + ['HAND_' + partsStr + '_42']
    sBodyPAFs = 2*(sBodyParts-1+11+7*sAddFace) # 2x shoulder-topHead --> neck-topHead
    sScaleMins += [2.0//3.0, 0.5]
    sScaleMaxs += [4.5, 4.0]
    sMaxDegreeRotations += [sMaxDegreeRotations[0]]*2
    # sMaxDegreeRotations += [90]*2
    sNumberMaxOcclusions += [0]*2
    # sKeypointSigmas += [6.0]*2
    sKeypointSigmas += [7.0]*2

if sAddDome:
    if not sAddHands or not sAddFace:
        print('Not prepared for this case (Dome135)')
        assert(false)
    # lmdb_hand_dome in openposedemo server is in /mnt/DataNVE/gines/lmdb_hand_dome/
    sLmdbFolders += ['lmdb_dome135/']
    # sProbabilities = "0.05;" + str(0.82-sProbabilityOnlyBackground) + ";0.05;0.01;0.01;0.01;0.02;0.03"
    # sProbabilities = "0.05;" + str(0.83-sProbabilityOnlyBackground-0.05-0.075) + ";0.05;0.0075;0.0075;0.005;0.06;0.04;0.075"
    #                 Foot                                      COCO                              MPII FRGC  MPIE FACE  HDome HMPII Dome135
    sProbabilities = "0.05;" + str(1.0-sProbabilityOnlyBackground-0.05-0.05-0.02-0.055-0.075) + ";0.05;0.005;0.01;0.005;0.005;0.05;0.075"
    sModelNames += ['DOME_' + partsStr]
    sScaleMins += [2.0/3.0]
    sScaleMaxs += [4.5]
    sMaxDegreeRotations += [sMaxDegreeRotations[0]]
    # sMaxDegreeRotations += [90]
    sNumberMaxOcclusions += [0]
    sKeypointSigmas += [7.0]
    sMediaDirectory = '/media/posefs0c/panopticdb/a4/hdImgs/'
else:
    sMediaDirectory = ''

# Distance
# sDistanceChannels = sAddDistance * 2 * (sBodyParts-1)
sDistanceChannels = sAddDistance * 2 * sBodyParts

# Relative paths to full paths
sCaffeFolder = os.path.abspath(sCaffeFolder)
for index, item in enumerate(sLmdbFolders):
    if sLmdbFolders[index][0] != '/':
        sLmdbFolders[index] = os.path.abspath(sDatasetFolder + sLmdbFolders[index])
if sLmdbBackground:
    sLmdbBackground = os.path.abspath(sDatasetFolder + sLmdbBackground)
sPretrainedModelPath = os.path.abspath(sPretrainedModelPath)
sTrainingFolder = os.path.abspath(sTrainingFolder)

sBodyPartsAndBkg = sBodyParts+1*(not sAddMpii)

## Things to try:
# 1. Different batch size --> 20
# 2. Different lr with the new clip size --> 1e-2, 1e-3, 1e-4

## Debugging - Check absolute paths
print('\n------------------------- Absolute paths: -------------------------')
print('sCaffeFolder absolute path:\t' + sCaffeFolder)
print('sLmdbFolder absolute paths:')
for lmdbFolder in sLmdbFolders:
    print('\t' + lmdbFolder)
print('sLmdbBackground absolute path:\t' + sLmdbBackground)
print('sPretrainedModelPath absolute path:\t' + sPretrainedModelPath)
print('sTrainingFolder absolute path:\t' + sTrainingFolder)
print('\n')

def concatStage(concatString, layerName, kernel, numberOutputChannels, stride):
    layerName               += [concatString]
    kernel                  += [ 0 ]
    numberOutputChannels    += [ 0 ]
    stride                  += [ 0 ]

def resetStage(layerName, kernel, numberOutputChannels, stride):
    layerName               += ['reset']
    kernel                  += [ 0 ]
    numberOutputChannels    += [ 0 ]
    stride                  += [ 0 ]

def getStringFromVector(vector):
    stringEquivalent = str(vector[0])
    for i in range(1, len(vector)):
        stringEquivalent += ';' + str(vector[i])
    return stringEquivalent

if __name__ == "__main__":
    # Model names (COCO, MPII, etc.)
    modelNames = getStringFromVector(sModelNames)
    print('modelNames: ' + modelNames)
    # LMDB paths
    lmdbFolders = getStringFromVector(sLmdbFolders)
    print('lmdbFolders: ' + lmdbFolders)
    # Min scales
    scaleMins = getStringFromVector(sScaleMins)
    print('scaleMins: ' + scaleMins)
    # Max scales
    scaleMaxs = getStringFromVector(sScaleMaxs)
    print('scaleMaxs: ' + scaleMaxs)
    # Max occlusions
    numberMaxOcclusions = getStringFromVector(sNumberMaxOcclusions)
    print('numberMaxOcclusions: ' + numberMaxOcclusions)
    # Sigmas
    sigmas = getStringFromVector(sKeypointSigmas)
    print('sigmas: ' + sigmas)
    # Max degree rotations
    maxDegreeRotations = getStringFromVector(sMaxDegreeRotations)
    print('maxDegreeRotations: ' + maxDegreeRotations)
    transformParams = [dict(stride=8, crop_size_x=sImageScale, crop_size_y=sImageScale,
                            target_dist=0.6, scale_prob=1, scale_mins=scaleMins, scale_maxs=scaleMaxs,
                            sources=lmdbFolders, models=modelNames, center_swap_prob=sCenterSwapProb[0],
                            center_perterb_max=40,
                            max_degree_rotations=maxDegreeRotations,
                            source_background=sLmdbBackground,
                            number_max_occlusions=numberMaxOcclusions,
                            sigmas=sigmas,
                            normalization=sNormalization,
                            # Distance
                            add_distance=(sDistanceChannels>0),
                            # # Hands
                            # # 1.5*2606 images (1.5 because it has 1 or 2 hands) vs. 14817 images (1 hand)
                            # # 3909 vs 14817 --> 1 to 3.7904835
                            # # 25-75 --> 1 to 3 (because MPI has much higher diversity)
                            probabilities=sProbabilities,
                            # Only-bkg imags
                            prob_only_background=sProbabilityOnlyBackground,
                            # do_clahe=False, visualize=False,
                            media_directory=sMediaDirectory
                        )]
    if len(sBatchSizes) > 1:
        print('Gines, you know that this was not the good way to go. Use instead sources with several entries.')
        assert(false)
    # # If COCO2017 foot
    # if len(sBatchSizes) > 1 and 'lmdb_coco2017_foot' in sLmdbFolders[1]:
    #     transformParamDome = eval(repr(transformParams[0]))
    #     transformParamDome['model'] = 'COCO_' + str(sBodyParts) + '_17'
    #     transformParamDome['scale_min'] = sScaleMins[1]
    #     transformParamDome['scale_max'] = sScaleMaxs[1]
    #     transformParamDome['center_swap_prob'] = sCenterSwapProb[1]
    #     transformParams = transformParams + [transformParamDome]
    # # If dome
    # if len(sBatchSizes) > 1 and 'dome' in sLmdbFolders[1]:
    #     transformParamDome = eval(repr(transformParams[0]))
    #     transformParamDome['model'] = 'DOME_' + str(sBodyParts)
    #     transformParamDome['scale_min'] = sScaleMins[1]
    #     transformParamDome['scale_max'] = sScaleMaxs[1]
    #     transformParamDome['center_swap_prob'] = sCenterSwapProb[1]
    #     transformParamDome['media_directory'] = '/media/posefs0c/panopticdb/a3/'
    #     transformParams = transformParams + [transformParamDome]
    # # If MPII hand
    # if len(sBatchSizes) == 3 and 'mpii_hand' in sLmdbFolders[2]:
    #     transformParamDome = eval(repr(transformParams[0]))
    #     transformParamDome['scale_min'] = sScaleMins[2]
    #     transformParamDome['scale_max'] = sScaleMaxs[2]
    #     transformParamDome['center_swap_prob'] = sCenterSwapProb[2]
    #     transformParamDome['model'] = 'MPII_' + str(sBodyParts)
    #     transformParams = transformParams + [transformParamDome]
    # # If first one is Dome
    # if 'dome' in sLmdbFolders[0]:
    #     transformParams[0]['model'] = 'DOME_' + str(sBodyParts)
    #     transformParams[0]['media_directory'] = '/media/posefs0c/panopticdb/a3/'
    # Create training folder
    if not os.path.exists(sTrainingFolder):
        os.makedirs(sTrainingFolder)

    # for maximumPafStage in range(1, sNumberStages[0]+2):
    for maximumPafStage in range(sNumberStages[0], sNumberStages[0]+1):
        trainingFolder = sTrainingFolder
        # if maximumPafStage <= sNumberStages[0]:
        #     trainingFolder = trainingFolder + '/' + str(maximumPafStage)
        #     isFinalModel = False
        #     numberIterations = sNumberIterationsMiddle
        # else:
        #     maximumPafStage = maximumPafStage - 1
        #     isFinalModel = True
        #     numberIterations = sNumberIterations
        isFinalModel = True
        numberIterations = sNumberIterations
        print(' ')
        print(trainingFolder)

        if sSuperModel:
            dcNumber=2
            # First stage             ----------------------- VGG 19 -----------------------   ---------- Body parts ----------
            layerName               = ['V','V','P'] * 2  +  ['V'] * 4 + ['P']  +  ['V'] * 4     + ['DC']*int(floor(dcNumber)) + ['DC']*1 + ['DC']*int(ceil(dcNumber)) + ['DC']*1 + ['C']*1 + ['$']
            kernel                  = [ 3,  3,  2 ] * 2  +  [ 3 ] * 4 + [ 2 ]  +  [ 3 ] * 4     + [ 3 ] *int(floor(dcNumber)) + [ 3 ] *1 + [ 3 ] *int(ceil(dcNumber)) + [ 3 ] *1 + [ 1 ]*1 + [ 0 ]
            numberOutputChannels    = [64]*3 + [128]* 3  +  [256] * 4 + [256]  +  [512] * 4     + [256] *int(floor(dcNumber)) + [224] *1 + [256] *int(ceil(dcNumber)) + [224] *1 + [512]*1 + [ 0 ]
            stride                  = [ 1 , 1,  2 ] * 2  +  [ 1 ] * 4 + [ 2 ]  +  [ 1 ] * 4     + [ 1 ] *int(floor(dcNumber)) + [ 1 ] *1 + [ 1 ] *int(ceil(dcNumber)) + [ 1 ] *1 + [ 1 ]*1 + [ 0 ]
            # # First stage             ----------------------- VGG 19 -----------------------   ---------- Body parts ----------
            # layerName               = ['V','V','P'] * 2  +  ['V'] * 4 + ['P']  +  ['V'] * 2     + ['DC']*3 + ['DC']*1 + ['$']
            # kernel                  = [ 3,  3,  2 ] * 2  +  [ 3 ] * 4 + [ 2 ]  +  [ 3 ] * 2     + [ 3 ] *3 + [ 3 ] *1 + [ 0 ]
            # numberOutputChannels    = [64]*3 + [128]* 3  +  [256] * 4 + [256]  +  [512] * 2     + [256] *3 + [224] *1 + [ 0 ]
            # stride                  = [ 1 , 1,  2 ] * 2  +  [ 1 ] * 4 + [ 2 ]  +  [ 1 ] * 2     + [ 1 ] *3 + [ 1 ] *1 + [ 0 ]
        else:
            # First stage             ----------------------- VGG 19 -----------------------   ---------- Body parts ----------
            layerName               = ['V','V','P'] * 2  +  ['V'] * 4 + ['P']  +  ['V'] * 2     + ['C'] * 2     + ['$']
            kernel                  = [ 3,  3,  2 ] * 2  +  [ 3 ] * 4 + [ 2 ]  +  [ 3 ] * 2     + [ 3 ] * 2     + [ 0 ]
            numberOutputChannels    = [64]*3 + [128]* 3  +  [256] * 4 + [256]  +  [512] * 2     + [256] + [128] + [ 0 ]
            stride                  = [ 1 , 1,  2 ] * 2  +  [ 1 ] * 4 + [ 2 ]  +  [ 1 ] * 2     + [ 1 ] * 2     + [ 0 ]
            # # First stage             -------- Body parts ----------
            # layerName               =  ['C'] * 2     + ['$']
            # kernel                  =  [ 3 ] * 2     + [ 0 ]
            # numberOutputChannels    =  [256] + [128] + [ 0 ]
            # stride                  =  [ 1 ] * 2     + [ 0 ]

        # Stages 2-sNumberStages   ------------------------------------ Body + PAF parts ------------------------------------
        if sSuperModel:
            nodesPerLayer = 9+2
        else:
            nodesPerLayer = 5+2
        # PAFs
        # for s in range(1, sNumberStages[0]+1):
        for s in range(1, maximumPafStage+1):
            if s == 1:
                resetStage(layerName, kernel, numberOutputChannels, stride)
            else:
                concatStage('@', layerName, kernel, numberOutputChannels, stride)

            np = sBodyPAFs
            if trainHand:
                layerName               += ['DC2'] * (nodesPerLayer-2) + ['C2'] * 2 +  ['L2d']
            else:
                # layerName               += ['SC2'] * (nodesPerLayer-2) + ['C2'] * 2 +  ['L2']
                # layerName               += ['DC2'] * (nodesPerLayer-2) + ['C2'] * 2 +  ['L2c']
                # layerName               += ['C2'] * (nodesPerLayer-2) + ['C2'] * 2  +  ['L2']
                layerName               += ['DC2'] * (nodesPerLayer-2) + ['C2'] * 2 +  ['L2']
            kernel                  += [ 3 ] * (nodesPerLayer-2) + [1]*2        +  [ 0 ]
            if s <= 1 and s != sNumberStages[0]:
                if sSuperModel:
                    numberOutputChannels    += [128] * (nodesPerLayer-2) + [256,np]  +  [ 0 ]
                else:
                    numberOutputChannels    += [64] * (nodesPerLayer-2) + [256,np]  +  [ 0 ]
            elif s <= 2 and s != sNumberStages[0]:
                # numberOutputChannels    += [96]*2 + [128] * (nodesPerLayer-4) + [256,np]  +  [ 0 ]
                # numberOutputChannels    += [96]*2 + [128] * (nodesPerLayer-4) + [512,np]  +  [ 0 ]
                numberOutputChannels    += [128] * (nodesPerLayer-2) + [256,np]  +  [ 0 ]
            elif s != sNumberStages[0]:
                numberOutputChannels    += [128] * (nodesPerLayer-2) + [512,np] +  [ 0 ]
            else:
                if sSuperModel:
                    numberOutputChannels    += [256] * (nodesPerLayer-2) + [512,np] +  [ 0 ]
                else:
                    numberOutputChannels    += [128] * (nodesPerLayer-2) + [512,np] +  [ 0 ]
            stride                  += [ 1 ] * nodesPerLayer                    +  [ 0 ]

        # Body parts
        if sSuperModel:
            nodesPerLayer = 9+2
        else:
            nodesPerLayer = 5+2
        for s in range(1, sNumberStages[1]+1):
            if s == 1:
                resetStage(layerName, kernel, numberOutputChannels, stride)
            concatStage('@', layerName, kernel, numberOutputChannels, stride)

            np = sBodyPartsAndBkg
            if trainHand:
                layerName               += ['DC1'] * (nodesPerLayer-2) + ['C1']*2   +  ['L1d']
            else:
                # layerName               += ['SC1'] * (nodesPerLayer-2) + ['C1'] * 2 +  ['L1']
                # layerName               += ['DC1'] * (nodesPerLayer-2) + ['C1'] * 2 +  ['L1c']
                layerName               += ['DC1'] * (nodesPerLayer-2) + ['C1']*2   +  ['L1']
            kernel                  += [ 3 ] * (nodesPerLayer-2) + [1]*2        +  [ 0 ]
            if s <= 1 and s != sNumberStages[1]:
                numberOutputChannels    += [64] * (nodesPerLayer-2) + [256,np]  +  [ 0 ]
            elif s <= 2 and s != sNumberStages[1]:
                numberOutputChannels    += [96] * (nodesPerLayer-2) + [256,np]  +  [ 0 ]
            elif s != sNumberStages[1]:
                numberOutputChannels    += [128] * (nodesPerLayer-2) + [512,np] +  [ 0 ]
            else:
                if sSuperModel:
                    numberOutputChannels    += [128+64] * (nodesPerLayer-2) + [512,np] +  [ 0 ]
                else:
                    numberOutputChannels    += [128] * (nodesPerLayer-2) + [512,np] +  [ 0 ]
            stride                  += [ 1 ] * nodesPerLayer                    +  [ 0 ]

        # Distance PAF
        if sAddDistance and sDistanceChannels > 0:
            for s in range(1, sNumberStages[1]+1):
                if s == 1:
                    resetStage(layerName, kernel, numberOutputChannels, stride)
                concatStage('@', layerName, kernel, numberOutputChannels, stride)

                np = sDistanceChannels
                if trainHand:
                    layerName               += ['DC3'] * (nodesPerLayer-2) + ['C3']*2   +  ['L3d']
                else:
                    # layerName               += ['SC3'] * (nodesPerLayer-2) + ['C3'] * 2 +  ['L3']
                    # layerName               += ['DC3'] * (nodesPerLayer-2) + ['C3'] * 2 +  ['L3c']
                    layerName               += ['DC3'] * (nodesPerLayer-2) + ['C3']*2   +  ['L3']
                kernel                  += [ 3 ] * (nodesPerLayer-2) + [1]*2        +  [ 0 ]
                if s <= 1 and s != sNumberStages[1]:
                    numberOutputChannels    += [96] * (nodesPerLayer-2) + [256,np]  +  [ 0 ]
                elif s != sNumberStages[1]:
                    numberOutputChannels    += [128] * (nodesPerLayer-2) + [512,np] +  [ 0 ]
                else:
                    numberOutputChannels    += [128] * (nodesPerLayer-2) + [512,np] +  [ 0 ]
                stride                  += [ 1 ] * nodesPerLayer                    +  [ 0 ]

        # Hand PAFs as extra layer (rather than inside same network)
        for s in range(1, sNumberStages[2]+1):
            if s == 1:
                resetStage(layerName, kernel, numberOutputChannels, stride)
            concatStage('@' + letter, layerName, kernel, numberOutputChannels, stride)

            if trainHand:
                letter = 'h'
                np = sHandPAFs
            elif trainFoot:
                letter = 'f'
                np = sHandPAFs
            layerName               += ['C2' + letter] + ['DC2' + letter] * (nodesPerLayer-2) + ['C2' + letter]*2 +  ['L2' + letter]
            kernel                  += [1]     + [ 3 ] * (nodesPerLayer-2) + [1]*2        +  [ 0 ]
            # Hands
            if s <= 1 and s != sNumberStages[3]:
                numberOutputChannels    += [128] + [128] * (nodesPerLayer-2) + [512,np]   +  [ 0 ]
            else:
                numberOutputChannels    += [128] + [128] * (nodesPerLayer-2) + [512,np]   +  [ 0 ]
            # # Foot
            # if s <= 1 and s != sNumberStages[3]:
            #     numberOutputChannels    += [128] + [64] * (nodesPerLayer-2) + [64,np]     +  [ 0 ]
            # else:
            #     numberOutputChannels    += [128] + [64] * (nodesPerLayer-2) + [128,np]    +  [ 0 ]
            stride                  += [ 1 ] * (nodesPerLayer+1)                          +  [ 0 ]

        # Foot/hand parts
        for s in range(1, sNumberStages[3]+1):
            if s == 1:
                resetStage(layerName, kernel, numberOutputChannels, stride)
            concatStage('@' + letter, layerName, kernel, numberOutputChannels, stride)

            if trainHand:
                letter = 'h'
                np = sHandParts
            elif trainFoot:
                letter = 'f'
                np = sHandParts
            layerName               += ['C1' + letter] + ['DC1' + letter] * (nodesPerLayer-2) + ['C1' + letter]*2 +  ['L1' + letter]
            kernel                  += [1]     + [ 3 ] * (nodesPerLayer-2) + [1]*2        +  [ 0 ]
            # Hands
            if s <= 1 and s != sNumberStages[3]:
                numberOutputChannels    += [128] + [128] * (nodesPerLayer-2) + [512,np]   +  [ 0 ]
            else:
                numberOutputChannels    += [128] + [128] * (nodesPerLayer-2) + [512,np]   +  [ 0 ]
            # # Foot
            # if s <= 1 and s != sNumberStages[3]:
            #     numberOutputChannels    += [128] + [64] * (nodesPerLayer-2) + [64,np]     +  [ 0 ]
            # else:
            #     numberOutputChannels    += [128] + [64] * (nodesPerLayer-2) + [128,np]    +  [ 0 ]
            stride                  += [ 1 ] * (nodesPerLayer+1)                          +  [ 0 ]

        # # Rescale / deconvolution layer
        # for s in range(1, sNumberStages[4]+1):
        #     if s == 1:
        #         resetStage(layerName, kernel, numberOutputChannels, stride)
        #     concatStage('@U', layerName, kernel, numberOutputChannels, stride)

        #     np = sBodyPartsAndBkg + sBodyPAFs + sHandParts + sHandPAFs
        #     layerName               += ['U'] + ['L']
        #     kernel                  += [ 0 ] + [ 0 ]
        #     numberOutputChannels    += [np]  + [ 0 ]
        #     stride                  += [ 0 ] + [ 0 ]

        extraGT = False
        # # Big PAF
        # for s in range(1, sNumberStages[4]+1):
        #     extraGT = True
        #     # Connection
        #     layerName               += ['@2']
        #     kernel                  += [ 0 ]
        #     numberOutputChannels    += [ 0 ]
        #     stride                  += [ 0 ]
        #     # Bilinear upsampling
        #     layerName               += ['U2']
        #     kernel                  += [ 0 ]
        #     numberOutputChannels    += [sBodyPAFs]
        #     stride                  += [ 2 ]
        #     # Concatenation
        #     layerName               += ['@V']
        #     kernel                  += [ 0 ]
        #     numberOutputChannels    += [ 0 ]
        #     stride                  += [ 0 ]
        #     # Conv
        #     nodesPerLayerC = 5+2
        #     layerName               += ['C2'] * nodesPerLayerC               +  ['L2_2']
        #     kernel                  += [ 7 ] * (nodesPerLayerC-2) + [1] * 2  +  [ 0 ]
        #     numberOutputChannels    += [128] * (nodesPerLayerC-1) + [0]      +  [ 0 ]
        #     stride                  += [ 1 ] * nodesPerLayerC                +  [ 0 ]
        #     # out of memory...
        #     # layerName               += ['DC2'] * (nodesPerLayerC-2) + ['C2'] * 2    +  ['L2_2']
        #     # kernel                  += [ 3 ] * (nodesPerLayerC-2) + [1] * 2         +  [ 0 ]
        #     # numberOutputChannels    += [128] * (nodesPerLayerC-1) + [0]             +  [ 0 ]
        #     # stride                  += [ 1 ] * nodesPerLayerC                       +  [ 0 ]
        # # Big body parts
        # for s in range(1, sNumberStages[5]+1):
        #     extraGT = True
        #     # Connection
        #     layerName               += ['@1']
        #     kernel                  += [ 0 ]
        #     numberOutputChannels    += [ 0 ]
        #     stride                  += [ 0 ]
        #     # Bilinear upsampling
        #     layerName               += ['U1']
        #     kernel                  += [ 0 ]
        #     numberOutputChannels    += [sBodyParts+1]
        #     stride                  += [ 2 ]
        #     # Concatenation
        #     layerName               += ['@V']
        #     kernel                  += [ 0 ]
        #     numberOutputChannels    += [ 0 ]
        #     stride                  += [ 0 ]
        #     # Conv
        #     nodesPerLayerC = 5+2
        #     layerName               += ['C1'] * nodesPerLayerC               +  ['L1_2']
        #     kernel                  += [ 7 ] * (nodesPerLayerC-2) + [1] * 2  +  [ 0 ]
        #     numberOutputChannels    += [128] * (nodesPerLayerC-1) + [0]      +  [ 0 ]
        #     stride                  += [ 1 ] * nodesPerLayerC                +  [ 0 ]
        # # # Bilinear upsampling
        # # layerName               += ['U1d', 'U2d']
        # # kernel                  += [ 0 ] * 2
        # # numberOutputChannels    += [sBodyParts+1, sBodyPAFs]
        # # stride                  += [ 2 ] * 2

        pretrainedModelPath = sPretrainedModelPath
        # if maximumPafStage == 1:
        #     pretrainedModelPath = sPretrainedModelPath
        # else:
        #     pretrainedModelPath = trainedModelsFolder + '/pose_iter_50000.caffemodel'
        print(pretrainedModelPath)

        # Create folders where saving
        if not os.path.exists(trainingFolder):
            os.makedirs(trainingFolder)
        trainedModelsFolder = os.path.join(trainingFolder, 'model')
        if not os.path.exists(trainedModelsFolder): # for storing Caffe models
            os.makedirs(trainedModelsFolder)

        generateProtoTxt(
            trainingFolder, sBatchSizes, layerName, kernel, stride, numberOutputChannels,
            transformParams, sLearningRateInit, trainedModelsFolder, sBodyParts, sBodyPAFs,
            sBatchNorm, sBinaryConv, sLearningRateMultDistro, sCaffeFolder, pretrainedModelPath,
            isFinalModel, numberIterations, maximumPafStage, sUsePReLU, extraGT, sHandParts, sHandPAFs,
            sDistanceChannels, not sAddMpii)
